acao = input().upper()
itens = {}
while acao != 'FIM':
    if acao =='ADICIONAR': 
        nome_intem = input()
        qnt_intem = int(input())
        if not itens or nome_intem not in itens:
            itens[nome_intem] = qnt_intem
        elif nome_intem in itens:
            itens[nome_intem] += qnt_intem

    elif acao == 'REMOVER':
        nome_intem = input()
        qnt_intem = int(input())
        if nome_intem in itens and qnt_intem <= itens[nome_intem]:
            itens[nome_intem] -= qnt_intem
            if itens[nome_intem] == 0:
                del itens[nome_intem]
        elif nome_intem in itens:
            if qnt_intem > itens[nome_intem]:
                print('ERRO! Quantidade insuficiente no Inventário!')
        else:
            print('ERRO! Item não está no Inventário!')
    acao = input().upper()

if not itens:
    print('Inventário Vazio!')     
else:   
    for nome_intem, qnt_intem in itens.items():
        print(f'{nome_intem} - {qnt_intem}')
