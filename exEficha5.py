magias_catalogo = ["Pergaminho dos Elementos", "Varinha da Água", "Grimório de 4 folhas"]
INVENTÁRIO = {
    "nível": 0,
    'magias': [],
    'itens': {
        "pás": ["Pá do herói"],
    },
    'troféus': {
        'Capacete do Espectro': 0,
        'Capacete Gélido': 0
    }
}

ITENS = {
    "F": {"secao": "magias", "nome": "Varinha de Chamas", "mensagem": "O que é isso? Sinto um fogo emanando do fundo da minha alma…"},
    "V": {"secao": "magias", "nome": "Varinha de Gelo", "mensagem": "Uma magia nova é sempre bom!"},
    "P": {"secao": "pás", "nome": "Pá Espectral", "mensagem": "Uma pá transparente, que loucura!"},
    "p": {"secao": "pás", "nome": "Pá comum", "mensagem": "Mais uma para minha coleção."},
}

CHEFES = {
    "Specter Knight": {"capacete": "Capacete do Espectro", "nivel_minimo": 2},
    "Polar Knight": {"capacete": "Capacete Gélido", "nivel_minimo": 5},
}

DIRECOES = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

def mover(posicao, direcao):

    linha = posicao[0] + DIRECOES[direcao][0]
    coluna = posicao[1] + DIRECOES[direcao][1]
    if 0 <= linha <= 4 and 0 <= coluna <= 4:
        return (linha, coluna)
    return posicao


def coletar(simbolo, inventario):
    """Guarda no inventário o item do símbolo e imprime sua mensagem."""
    item = ITENS[simbolo]
    if item["secao"] == "pás":
        inventario["itens"]["pás"].append(item["nome"])
    else:
        inventario[item["secao"]].append(item["nome"])
    print(item["mensagem"])


def explorar(mapa, inventario):
    """Lê direções até chegar ao 'X', coletando itens e níveis pelo caminho."""
    posicao = (0, 0)
    casa = mapa.get(posicao, 0)
    while casa != "X":
        direcao = input()
        posicao = mover(posicao, direcao)
        casa = mapa.get(posicao, 0)
        if casa in ITENS:
            coletar(casa, inventario)
            mapa.pop(posicao)
        elif casa == "N":
            inventario["nível"] += 1
            mapa.pop(posicao)


def enfrentar(chefe, inventario, nivel, tem_requisito):
    dados = CHEFES[chefe]
    if nivel >= dados["nivel_minimo"] and tem_requisito:
        inventario["troféus"][dados["capacete"]] = 1
        return True
    return False


def derrota():
    print("A jornada do herói chega a um triste fim…")
    print("Sua pá não foi capaz de cavar uma saída desse buraco de trevas em que estamos.")
    print("O que restou? Nada… brutal.")
    print()


def lista_ou_nenhum(lista):
    if len(lista) == 0:
        return "NENHUM"
    return ", ".join(lista)


def relatorio(inventario):
    print("======== RELATÓRIO FINAL ========")
    capacetes = []
    for capacete in inventario["troféus"]:
        if inventario["troféus"][capacete] == 1:
            capacetes.append(capacete)
    print(f"CAPACETES: {lista_ou_nenhum(capacetes)}")
    print(f"MAGIAS: {lista_ou_nenhum(inventario['magias'])}")
    print(f"PÁS: {lista_ou_nenhum(inventario['itens']['pás'])}")

entrada = input()
if entrada == 'sim':
    magia = input()
    if magia in magias_catalogo:
        INVENTÁRIO['magias'].append(magia)
print(INVENTÁRIO["magias"])
# O Cemitério dos Lichs
vivo = True
if INVENTÁRIO['magias'] == []:
    vivo = False
else:
    mapa_cemiterio = {
    (0, 2): "p",
    (1, 4): "P",
    (2, 1): "N",
    (2, 2): "N",
    (2, 3): "F",
    (3, 3): "N",
    (3, 4): "N",
    (4, 0): "p",
    (4, 1): "X",
}
    


