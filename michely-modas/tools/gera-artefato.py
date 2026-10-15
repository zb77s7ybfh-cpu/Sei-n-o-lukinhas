"""Gera a copia do site que vai no artefato do Claude.

O site de verdade (index.html) usa caminhos relativos: assets/pecas/x.jpg.
Isso funciona em qualquer hospedagem comum, e e o que vai no site.zip.

Dentro do Claude a pagina nao fica sempre no mesmo endereco, e o caminho
relativo quebra em alguns aparelhos (foi o que aconteceu no iPad). Para o
artefato, cada arquivo tem um endereco fixo, /_blob/<id>, que o proprio
Claude garante resolver em toda visualizacao.

Este script troca um pelo outro em um unico ponto: a funcao asset().
Rode assim, da pasta michely-modas:

    python3 tools/gera-artefato.py <pasta-de-saida>

e publique o index.html que ele escrever.
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

    mapa = json.load(io.open(os.path.join(AQUI, "blobs.json"), encoding="utf-8"))
    html = io.open(os.path.join(RAIZ, "index.html"), encoding="utf-8").read()

    for alvo, _ in TROCAS:
        if html.count(alvo) != 1:
            sys.exit("o trecho abaixo mudou de forma; ajuste TROCAS neste "
                     "script:\n" + alvo)

    # todo arquivo que a pagina pede tem que estar no mapa
    pedidos = set()
    for linha in html.splitlines():
        if 'data-src="assets/' in linha:
            for pedaco in linha.split('data-src="')[1:]:
                pedidos.add(pedaco.split('"')[0])
        if 'asset("assets/' in linha:
            for pedaco in linha.split('asset("')[1:]:
                pedidos.add(pedaco.split('"')[0])
    for nome in os.listdir(os.path.join(RAIZ, "assets", "pecas")):
        pedidos.add("assets/pecas/" + nome)

    faltam = sorted(p for p in pedidos if p not in mapa)
    if faltam:
        sys.exit("faltam no blobs.json: " + ", ".join(faltam))

    for alvo, troca in TROCAS:
        html = html.replace(
            alvo, troca.replace("__MAPA__", json.dumps(mapa, indent=2, sort_keys=True)))

    if not os.path.isdir(saida):
        os.makedirs(saida)
    destino = os.path.join(saida, "index.html")
    io.open(destino, "w", encoding="utf-8").write(html)
    print("escrevi %s (%d arquivos no mapa, %d pedidos conferidos)"
          % (destino, len(mapa), len(pedidos)))


if __name__ == "__main__":
    main()
