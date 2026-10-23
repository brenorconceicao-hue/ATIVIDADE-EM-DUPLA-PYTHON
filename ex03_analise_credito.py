
import os
os.system('cls')

print('=== PRE ANALISE DE EMPRESTIMO ===')

desconto = 0
valor = float(input('Digite o valor do produto: R$ '))

print('1 - A vista')
print('2 - A prazo')

forma_pagamento = int(input('Escolha a forma de pagamento: '))

if forma_pagamento == 1:
    desconto = valor * 0.10
    total = valor - desconto

    print('\n=== RESUMO DO PAGAMENTO ===')
    print(f'Valor do produto: R$ {valor:.2f}')
    print('Forma de pagamento: A vista')
    print(f'Desconto: R$ {desconto:.2f}')
    print(f'Total a pagar: R$ {total:.2f}')

else:
    if forma_pagamento == 2:
        parcelas = int(input('Digite o numero de parcelas de 1 a 6: '))

        if parcelas < 1 or parcelas > 6:
            print('Numero de parcelas invalido!')
        else:
            total = valor
            valor_parcela = total / parcelas

            print('\n=== RESUMO DO PAGAMENTO ===')
            print(f'Valor do produto: R$ {valor:.2f}')
            print('Forma de pagamento: A prazo')
            print('Desconto: R$ 0.00')
            print(f'Quantidade de parcelas: {parcelas}')
            print(f'Valor da parcela: R$ {valor_parcela:.2f}')
            print(f'Total a pagar: R$ {total:.2f}')

    else:
        print('Forma de pagamento invalida!')
