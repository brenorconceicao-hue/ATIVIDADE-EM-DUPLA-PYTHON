import os 
os.system('cls')

print('===CALCULADORA===')

numero1 = int(input('digite um numero:  '))
numero2 = int(input('digite um numero novamente: '))

operacoes = input('escolha uma operaçao (+ , - , * ou / )')

match operacoes :
    case '+':
        numero1 += numero2
        print(f'Resultado {numero1}')
    case '-':
        numero1 -= numero2
        print(f'Resultado {numero1}')
    case '*':
        numero1 *= numero2
        print(f'Resultado {numero1}')
    case '/':
        if  operacoes != 0:
            print('operaçao invalida')
    
            numero1 /= numero2
        print(f'Resultado {numero1}')
    case _:
        print('opcao invalida')