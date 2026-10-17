"""Gera a copia do site que vai no artefato do Claude.

O site de verdade (index.html) usa caminhos relativos: assets/pecas/x.jpg.
Isso funciona em qualquer hospedagem comum, e e o que vai no site.zip.

Dentro do Claude a pagina nao fica sempre no mesmo endereco, e o caminho
relativo quebra em alguns aparelhos (foi o que aconteceu no iPad). Para o
artefato, cada arquivo tem um endereco fixo, /_blob/<id>, que o proprio
Claude garante resolver em toda visualizacao.

Este script troca um pelo outro em um unico ponto: a funcao asset().
Sao duas paginas: index.html (a loja) e carrito.html (o pedido).
As duas usam a mesma funcao asset(), entao a troca e a mesma nas duas.

Rode assim, da pasta michely-modas:

    python3 tools/gera-artefato.py <pasta-de-saida>

e publique os dois arquivos que ele escrever.
"""
import io, json, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)

TROCAS = [
    (
        "function asset(rel){ return BASES[baseIdx] + rel; }",
        """var BLOB = __MAPA__;
/* Vira true se /_blob/ nao responder aqui: ai a pagina volta aos caminhos
   relativos sozinha. E o que salva esta copia se ela for parar numa
   hospedagem de verdade, onde /_blob/ nao existe. */
var semBlob = false;
function asset(rel){
  return (!semBlob && BLOB[rel]) ? BLOB[rel] : (BASES[baseIdx] + rel);
}""",
    ),
    (
        """function healAssets(){
  if (healed || BASES.length < 2) return false;
  healed = true; baseIdx = 1;""",
        """function healAssets(){
  if (!semBlob) { semBlob = true; }                  /* 1o: larga o /_blob/ */
  else if (healed || BASES.length < 2) return false; /* ja tentou tudo */
  else { healed = true; baseIdx = 1; }               /* 2o: troca a base */""",
    ),
]


def main():
    if len(sys.argv) != 2:
        sys.exit("uso: python3 tools/gera-artefato.py <pasta-de-saida>")
    saida = sys.argv[1]
    if not os.path.isdir(saida):
        os.makedirs(saida)

    mapa = json.load(io.open(os.path.join(AQUI, "blobs.json"), encoding="utf-8"))

    # tudo que as paginas podem pedir
    pedidos = set()
    for nome in os.listdir(os.path.join(RAIZ, "assets", "pecas")):
        pedidos.add("assets/pecas/" + nome)

    paginas = ["index.html", "carrito.html"]
    for pagina in paginas:
        html = io.open(os.path.join(RAIZ, pagina), encoding="utf-8").read()

        achou = False
        for alvo, _ in TROCAS:
            n = html.count(alvo)
            if n > 1:
                sys.exit("%s: o trecho abaixo aparece %d vezes:\n%s" % (pagina, n, alvo))
            if n == 1:
                achou = True
        if not achou:
            sys.exit("%s: nao achei nenhum trecho conhecido; "
                     "a funcao asset() mudou de forma?" % pagina)

        for linha in html.splitlines():
            if 'data-src="assets/' in linha:
                for pedaco in linha.split('data-src="')[1:]:
                    pedidos.add(pedaco.split('"')[0])
            for marca in ('asset("assets/', 'wireImg($("#selo"), "'):
                if marca in linha:
                    for pedaco in linha.split(marca)[1:]:
                        alvo = pedaco.split('"')[0]
                        if alvo.startswith("assets/"):
                            pedidos.add(alvo)
            if 'var QR = "assets/' in linha:
                pedidos.add(linha.split('"')[1])

        for alvo, troca in TROCAS:
            html = html.replace(
                alvo, troca.replace("__MAPA__", json.dumps(mapa, indent=2, sort_keys=True)))

        io.open(os.path.join(saida, pagina), "w", encoding="utf-8").write(html)

    faltam = sorted(p for p in pedidos if p not in mapa)
    if faltam:
        sys.exit("faltam no blobs.json: " + ", ".join(faltam))

    print("escrevi %s (%d arquivos no mapa, %d pedidos conferidos)"
          % (", ".join(paginas), len(mapa), len(pedidos)))


if __name__ == "__main__":
    main()
