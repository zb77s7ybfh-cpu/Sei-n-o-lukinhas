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

ANTES = 'function asset(rel){ return BASES[baseIdx] + rel; }'

DEPOIS = """var BLOB = __MAPA__;
function asset(rel){ return BLOB[rel] || (BASES[baseIdx] + rel); }"""


def main():
    if len(sys.argv) != 2:
        sys.exit("uso: python3 tools/gera-artefato.py <pasta-de-saida>")
    saida = sys.argv[1]

    mapa = json.load(io.open(os.path.join(AQUI, "blobs.json"), encoding="utf-8"))
    html = io.open(os.path.join(RAIZ, "index.html"), encoding="utf-8").read()

    if html.count(ANTES) != 1:
        sys.exit("a funcao asset() mudou de forma; ajuste ANTES neste script")

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

    corpo = DEPOIS.replace("__MAPA__", json.dumps(mapa, indent=2, sort_keys=True))
    html = html.replace(ANTES, corpo)

    if not os.path.isdir(saida):
        os.makedirs(saida)
    destino = os.path.join(saida, "index.html")
    io.open(destino, "w", encoding="utf-8").write(html)
    print("escrevi %s (%d arquivos no mapa, %d pedidos conferidos)"
          % (destino, len(mapa), len(pedidos)))


if __name__ == "__main__":
    main()
