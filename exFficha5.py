ARMAS = ['cajado', 'machado grande', 'adaga', 'adaga dupla']
UTILIDADES = ['grimorio', 'escudo de madeira', 'alaude', 'ferramentas de ladrao']
CONSUMIVEIS = ['pergaminho oculto', 'racao de viagem', 'pocao de cura', 'bomba de fumaca']

NOMES_CLASSES = {'B': 'Bardo', 'G': 'Guerreiro', 'L': 'Ladino', 'M': 'Mago'}

CLASSE_IDEAL = {'lira encantada': 'B','martelo do trovao': 'G','olho do abismo': 'L','orbe arcano': 'M',}

ALFABETO = 'abcdefghijklmnopqrstuvwxyz'


def descriptografar(texto, chave):
    resultado = ''
    for letra in texto:
        minuscula = letra.lower()
        if minuscula in ALFABETO:
            nova = ALFABETO[(ALFABETO.index(minuscula) - chave) % 26]
            resultado += nova.upper() if letra.isupper() else nova
        else:
            resultado += letra
    return resultado


def tipo_item(item):
    if item in ARMAS:
        return 'arma'
    if item in UTILIDADES:
        return 'utilidade'
    if item in CONSUMIVEIS:
        return 'consumivel'
    return 'desconhecido'


def primo(n):
    if n < 2:
        return False
    divisor = 2
    primo = True
    while divisor * divisor <= n and primo:
        if n % divisor == 0:
            primo = False
        divisor += 1
    return primo


def quadrado_perfeito(n):
    if n <= 0:
        return False
    raiz = 0
    while raiz * raiz < n:
        raiz += 1
    if raiz * raiz == n:
        return True
    return False


def tipo_sala(valor):
    if valor == 0:
        return 'Entrada'
    if valor == 99:
        return 'Saída'
    if primo(valor):
        return 'Armadilha'
    if quadrado_perfeito(valor):
        return 'Looting'
    return 'Sala Comum'


def tem_intem(grupo, classe, item):
    inventario = grupo.get(classe, {}).get('inventario', {})
    if inventario.get(item, 0) != 0:
        return True
    return False


def remover_aventureiro(grupo, ordem, classe):
    del grupo[classe]
    return [c for c in ordem if c != classe]


def proximo_passo(matriz, n, linha, coluna, visitadas):
    melhor_linha = -1
    melhor_coluna = -1
    melhor_valor = -1
    deslocamentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in deslocamentos:
        nl = linha + d[0]
        nc = coluna + d[1]
        if 0 <= nl < n and 0 <= nc < n and (nl, nc) not in visitadas:
            if matriz[nl][nc] > melhor_valor:
                melhor_valor = matriz[nl][nc]
                melhor_linha = nl
                melhor_coluna = nc
    return (melhor_linha, melhor_coluna)


def maior_arma(inventario):
    dano = 0
    for info in inventario.values():
        if info['tipo'] == 'arma' and info['poder'] > dano:
            dano = info['poder']
    return dano


def ordenar_iniciativa(ordem, iniciativas):
    return sorted(ordem, key=lambda c: -iniciativas[c])

print('Boa noite a todos!! Sejam bem vindos ao reino de Cinland. A aventura será longa, mas a gloria é eterna!!')
print('Vamos as apresentações.')

# Fase 1
print()

qnt_aventureiros = int(input())
while qnt_aventureiros < 1 or qnt_aventureiros > 4:
    print('Não tem toda essa gente pra jogar não.')
    qnt_aventureiros = int(input())

grupo = {}
ordem = []
for i in range(qnt_aventureiros):
    dados = input().split()
    nome = dados[0]
    classe = dados[1]

    aventureiro = {'nome': nome,'classe': NOMES_CLASSES[classe],'inventario': {},}

    entrada = input().strip()
    while entrada != 'pronto':
        partes = entrada.split(' - ')
        item = descriptografar(partes[0].strip(), int(partes[1]))
        poder = int(partes[2])
        aventureiro['inventario'][item] = {'tipo': tipo_item(item), 'poder': poder}
        entrada = input().strip()

    grupo[classe] = aventureiro
    ordem.append(classe)

    if len(aventureiro['inventario']) == 0:
        print(f"{nome} ({aventureiro['classe']}): sem itens")
    else:
        textos = []
        for item, info in aventureiro['inventario'].items():
            textos.append(f"{item} [{info['tipo']}, {info['poder']}]")
        lista_itens = ', '.join(textos)
        print(f"{nome} ({aventureiro['classe']}): {lista_itens}")

print('Grupo completamente apresentado, espero que todos estejam preparados para o que estar por vir.')

# fase 2
print()
print('Ao passa pelo arco de pedras, vocês encontram um lugar silencioso, com um odor nada agradável e um frio sem igual. Um calafrio na espinha os chama a recuar, mas a jornada começa aqui. Bem vindos a Dungeon do Grad5.')

tamanho = int(input())
matriz = []
for _ in range(tamanho):
    linha_texto = input().split()
    linha_numeros = []
    for valor in linha_texto:
        linha_numeros.append(int(valor))
    matriz.append(linha_numeros)

vivos = True
saiu = False
linha = 0
coluna = 0
visitadas = [(0, 0)]

while vivos and not saiu:
    valor = matriz[linha][coluna]
    sala = tipo_sala(valor)
    print(f'Casa visitada: {sala}')

    if sala == 'Saída':
        print('Vocês finalmente saem das cavernas escuras e frias. Mas não parece chegar em um lugar melhor.')
        saiu = True

    elif sala == 'Armadilha':
        tipo_armadilha = input().strip()

        if tipo_armadilha == 'flechas':
            if tem_intem(grupo, 'G', 'escudo de madeira'):
                print(f"O escudo de madeira de {grupo['G']['nome']} protegeu o grupo.")
                del grupo['G']['inventario']['escudo de madeira']
            else:
                sacrificado = ordem[len(ordem) - 1]
                nome_morto = grupo[sacrificado]['nome']
                print(f'{nome_morto} sacrificou-se pelo grupo.')
                if sacrificado != 'B' and tem_intem(grupo, 'B', 'pocao de cura'):
                    print(f"{grupo['B']['nome']} usou a pocao de cura e salvou {nome_morto}.")
                    del grupo['B']['inventario']['pocao de cura']
                else:
                    ordem = remover_aventureiro(grupo, ordem, sacrificado)
                    if len(ordem) == 0:
                        print('Os sonhos e objetivos de todos são deixados no chão do Grad5. Nenhum de vocês restou. A glória nunca será alcançada!')
                        vivos = False

        elif tipo_armadilha == 'beholder':
            if tem_intem(grupo, 'L', 'bomba de fumaca'):
                print(f"{grupo['L']['nome']} usou a bomba de fumaça e o escaparam do Beholder.")
                del grupo['L']['inventario']['bomba de fumaca']
            else:
                print('Entraram em uma sala que não deveriam. A ultima visão é tudo ficando vermelho e em um flash, tudo fica preto. Vocês tão mortos.')
                print('Os sonhos e objetivos de todos são deixados no chão do Grad5. Nenhum de vocês restou. A glória nunca será alcançada!')
                vivos = False

    elif sala == 'Looting':
        print('Finalmente um descanso! Aproveitam as maravilhas presentes na sala.')
        qnt_itens = 1
        if tem_intem(grupo, 'L', 'ferramentas de ladrao'):
            print(f"{grupo['L']['nome']} arrombou o baú trancado!")
            del grupo['L']['inventario']['ferramentas de ladrao']
            qnt_itens = 2

        for _ in range(qnt_itens):
            partes = input().split(' - ')
            item_especial = partes[0].strip()
            codigo = int(partes[1])

            #  Ordem (B, G, L, M)
            vivos_ordenados = sorted(grupo.keys())
            destino = vivos_ordenados[codigo % len(vivos_ordenados)]
            heroi = grupo[destino]
            print(f"{item_especial} foi para {heroi['nome']} ({heroi['classe']}).")

            if CLASSE_IDEAL.get(item_especial, '') == destino:
                for info in heroi['inventario'].values():
                    info['poder'] = info['poder'] * 2
                print('O poder que esta em suas mãos é grandioso e parece chamar-lhe a glória eterna.')
            else:
                for info in heroi['inventario'].values():
                    info['poder'] = info['poder'] * 5 // 4
                print('O poder é grande demais, você não consegue extrair o máximo dele.')

    # maior vizinho
    if vivos and not saiu:
        posicao = proximo_passo(matriz, tamanho, linha, coluna, visitadas)
        linha = posicao[0]
        coluna = posicao[1]
        visitadas.append(posicao)

# Fase 3
if vivos and saiu:
    print()
    print('O lugar é silencioso. Até que, de repente, um rugido é ouvido. Uma criatura surge das sombras: o temido TarraByte!')

    ficha = input().split()
    boss = {'hp': int(ficha[0]), 'ca': int(ficha[1])}

    iniciativas = {}
    ataques = {}
    for c in ordem:
        rolagens = input().split()
        iniciativas[c] = int(rolagens[0])
        ataques[c] = int(rolagens[1])

    ordem_acao = ordenar_iniciativa(ordem, iniciativas)
    nomes_ordem = []
    for c in ordem_acao:
        nomes_ordem.append(grupo[c]['nome'])
    texto_ordem = ', '.join(nomes_ordem)
    print(f'Ordem de iniciativa: {texto_ordem}')

    inspirado = False
    boss_vivo = True
    i = 0
    while i < len(ordem_acao) and boss_vivo:
        c = ordem_acao[i]
        heroi = grupo[c]
        inventario = heroi['inventario']

        if c == 'B' and tem_intem(grupo, 'B', 'alaude'):
            print(f"{heroi['nome']} inspirou o grupo.")
            inspirado = True
        else:
            rolagem = ataques[c]
            bonus = 0
            if inspirado and (c == 'G' or c == 'L'):
                bonus = 2

            consumivel = ''
            if c == 'M' and tem_intem(grupo, 'M', 'pergaminho oculto'):
                consumivel = 'pergaminho oculto'
            elif c == 'G' and tem_intem(grupo, 'G', 'racao de viagem'):
                consumivel = 'racao de viagem'

            critico = rolagem == 20
            acertou = critico or rolagem + bonus >= boss['ca']

            if acertou:
                dano = maior_arma(inventario)
                if consumivel != '':
                    dano += inventario[consumivel]['poder']
                    del inventario[consumivel]
                if critico:
                    dano = dano * 2
                    print(f"{heroi['nome']} acertou um critico e causou {dano} de dano.")
                else:
                    print(f"{heroi['nome']} acertou e causou {dano} de dano.")
                boss['hp'] -= dano
                if boss['hp'] <= 0:
                    print(f"O TarraByte foi derrotado por {heroi['nome']}!")
                    boss_vivo = False
            else:
                print(f"{heroi['nome']} errou o ataque.")
        i += 1

    if boss_vivo:
        print(f"O TarraByte sobreviveu com {boss['hp']} de HP e obliterou o grupo. Fim da aventura.")