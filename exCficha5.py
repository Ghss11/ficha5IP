dicionario = {}

print('As sombras avançam sobre o Reino Celeste... É chegada a hora de reunir os heróis dispostos a enfrentar o Rei Demônio!')

nome_heroi = input()
while nome_heroi != 'FIM':

    atributo = input()
    atributos = atributo.split(' - ')

    vida_heroi = int(atributos[0].split(' ')[1])
    agilidade_heroi = int(atributos[1].split(' ')[1])
    arma = atributos[2].split(' ', 1)[1]
    dicionario[nome_heroi] = [vida_heroi, agilidade_heroi, arma]

    nome_heroi = input()

vida_rei = 100
agilidade_rei = 32
dano_rei = 25

if len(dicionario) > 2:
    print('Os portões do castelo se abrem e os heróis marcham rumo ao campo de batalha. O confronto contra o Rei Demônio começa agora!')
    herois_caidos = []
    while vida_rei > 0 and len(dicionario) > 0:
        heroi_escolhido = input()
        if heroi_escolhido not in dicionario:
            print('Nenhum herói com esse nome está no campo de batalha. O Rei Demônio aguarda impacientemente por seu próximo adversário!')
        else:

            vida_heroi = dicionario[heroi_escolhido][0]
            agilidade_heroi = dicionario[heroi_escolhido][1]
            arma = dicionario[heroi_escolhido][2]

            if arma == 'Espada Sagrada':
                dano_heroi = 15
            elif arma == 'Arco Lendário':
                dano_heroi = 20
            elif arma == 'Cajado Magistral':
                dano_heroi = 25
            else:
                dano_heroi = 0


            if agilidade_heroi > agilidade_rei:
                if dano_heroi == 0:
                    print('A arma do herói não possui poder suficiente para atravessar a aura sombria do Rei Demônio!')
                else:
                    print(f'{heroi_escolhido} brandiu {arma} contra o Rei Demônio e causou {dano_heroi} pontos de dano!')
                    vida_rei -= dano_heroi
                if vida_rei > 0:
                    print(f'O Rei Demônio avançou com suas garras infernais e atingiu {heroi_escolhido}, causando 25 pontos de dano!')
                    vida_heroi -= dano_rei

            else:
                print(f'O Rei Demônio avançou com suas garras infernais e atingiu {heroi_escolhido}, causando 25 pontos de dano!')
                vida_heroi -= dano_rei
                if vida_heroi > 0:
                    if dano_heroi == 0:
                        print('A arma do herói não possui poder suficiente para atravessar a aura sombria do Rei Demônio!')
                    else:
                        print(f'{heroi_escolhido} brandiu {arma} contra o Rei Demônio e causou {dano_heroi} pontos de dano!')
                        vida_rei -= dano_heroi

            if vida_heroi <= 0:
                del dicionario[heroi_escolhido]
                herois_caidos.append(heroi_escolhido)
                print(f'{heroi_escolhido} tombou diante do poder do Rei Demônio!')
            else:
                dicionario[heroi_escolhido][0] = vida_heroi

    if vida_rei > 0:
        print('O último herói tombou. Vitorioso, o Rei Demônio retoma sua marcha sombria em direção ao Reino Celeste!')
    else:
        print(f'Com um golpe decisivo, {heroi_escolhido} derrota o Rei Demônio! Após uma longa batalha, o Reino Celeste está finalmente livre de sua ameaça!')
        if len(herois_caidos) == 0:
            print('Contra todas as expectativas, todos os heróis retornaram vivos ao Reino Celeste. Naquela noite, nenhuma nova inscrição precisou ser feita no Memorial dos Heróis.')
        else:
            print('A vitória foi conquistada, mas teve seu preço. Alguns heróis não retornaram do campo de batalha e seus nomes serão eternizados no Memorial dos Heróis.')

    if len(herois_caidos) > 0:
        print('--- Memorial dos Heróis Caídos ---')
        for heroi in herois_caidos:
            print(heroi)
else:
    print('Poucos atenderam ao chamado do reino... Sem ao menos três heróis para formar a resistência, o Reino Celeste parece condenado à ruína!')