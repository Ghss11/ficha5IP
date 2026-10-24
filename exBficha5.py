armas = {'Vax': {}, 'Pike': {}, 'Grog': {}, 'Percy': {}, 'Scanlan': {}, 'Vex': {}, 'Keyleth': {} }

arma = input()
while arma != 'FIM':
    arma_certo = arma.split(' , ')

    nome_heroi = arma_certo[0]
    arma_heroi = arma_certo[1]
    poder_arma = int(arma_certo[2])

    armas[nome_heroi][arma_heroi] = poder_arma

    if nome_heroi == 'Vex' and arma_heroi == 'Fenthras':
        print('Um arco mágico, capaz de controlar todos os elementos? isso é perfeito para mim querido!')
    if nome_heroi == 'Grog' and arma_heroi == 'Manoplas de Titanstone':
        print('Estou maior agora, e pronto para entrar em fúria!')
    if nome_heroi == 'Vax' and arma_heroi == 'Adaga Mágica':
        print('Uma arma dada pela própria rainha dos corvos, agora apenas preciso saber se isso é uma dádiva ou uma maldição.')
    if nome_heroi == 'Scanlan' and arma_heroi == 'Caça Mitos':
        print('A espada lendária capaz de matar todos os Dragões... nas mãos do Scanlan?!')
    if nome_heroi == 'Keyleth' and arma_heroi == 'Pináculo da Confluência':
        print('Com isso e meu aramenté completo, a natureza inteira estará sobre meu controle.')
    if nome_heroi == 'Percy' and arma_heroi == 'The List':
        print('Não, ele novamente não, Orthax já me dominou uma vez, não posso deixar isso acontecer de novo.')
    if nome_heroi == 'Pike' and arma_heroi == 'Placa do Mártir':
        print('Everlight, espero que um dia você me perdoe, mas não vou mais depender de você.')
    
    arma = input()


for nome_heroi in armas:
    arma_forte = ''
    maior_poder = 0
    for arma,poder in armas[nome_heroi].items():
        if poder > maior_poder:
            maior_poder = poder
            arma_forte = arma
    if arma_forte == '':
        print(f'{nome_heroi} não possui nenhuma arma.')
    else:
        print(f'A arma mais forte de {nome_heroi} é a {arma_forte} com {maior_poder} Pontos de Poder.')
        