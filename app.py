contador = 0  # muito importante
contadorNome = ""  # passa o nome ao .format
print('Seja bem-vindo a Lanchonete do Ralfe Antunes')
while True:
    print('****************Cardápio****************')
    print('| Codigo | Descrição | Valor |')
    print('| 100 | Cachorro-Quente | 9,00 |')
    print('| 101 | Cachorro-Quente-Duplo | 11,00 |')
    print('| 102 | X-EGG | 12,00 |')
    print('| 103 | X-Salada | 13.00 |')
    print('| 104 | X-Bacon | 14,00 |')
    print('| 105 | X-Tudo | 17,00 |')
    print('| 200 | Refrigerante Lata | 5,00 |')
    print('| 201 | Chá Gelado | 4,00 |')
    codigo = input('Entre com o código do produto Desejado: ')
    if codigo == "100":
        contadorNome = contadorNome + "\n| Cachorro-quente: 9,00 |"
        contador = contador + 9
    elif codigo == "101":
        contadorNome = contadorNome + "\n| Cachorro-Quente-Duplo: 11,00 |"
        contador = contador + 11
    elif codigo == "102":
        contadorNome = contadorNome + "\n| X-EGG: 12,00 |"
        contador = contador + 12
    elif codigo == "103":
        contadorNome = contadorNome + "\n| X-Salada: 13,00 |"
        contador = contador + 13
    elif codigo == "104":
        contadorNome = contadorNome + "\n| X-Bacon: 14,00 |"
        contador = contador + 14
    elif codigo == "105":
        contadorNome = contadorNome + "\n| X-Tudo: 17,00 |"
        contador = contador + 17
    elif codigo == "200":
        contadorNome = contadorNome + "\n| Refrigerante Lata: 5,00 |"
        contador = contador + 5
    elif codigo == "201":
        contadorNome = contadorNome + "\n| Chá Gelado: 4,00 |"
        contador = contador + 4
    else:
        print('Opção Inválida')
        continue
    resposta = input('Deseja pedir mais alguma coisa ?(s/n) ')
    if resposta == "s":
        continue
    else:
        print('Você pediu {}'.format(contadorNome))
        print('o Total a ser pago é: {:.2f}'.format(contador))
    break
