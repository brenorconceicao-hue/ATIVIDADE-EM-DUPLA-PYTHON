import os
os.system ("cls")



valor_produto = float(input("Digite o valor do produto (R$): "))

print("\nFormas de pagamento:")
print("1 - À vista")
print("2 - A prazo")
forma_pagamento = int(input("Escolha a forma de pagamento (1 ou 2): "))


match forma_pagamento:
    case 1:
        
        desconto = valor_produto * 0.10
        total = valor_produto - desconto
        
        
        print("\n--- RESUMO DO PEDIDO ---")
        print(f"Valor original: R$ {valor_produto:.2f}")
        print("Forma de pagamento: À vista")
        print(f"Desconto (10%): R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

    case 2:
        parcelas = int(input("Digite a quantidade de parcelas (no máximo 6): "))
        
        
        if 1 <= parcelas <= 6:
            valor_parcela = valor_produto / parcelas
            
            
            print("\n--- RESUMO DO PEDIDO ---")
            print(f"Valor original: R$ {valor_produto:.2f}")
            print("Forma de pagamento: A prazo")
            print(f"Quantidade de parcelas: {parcelas}x")
            print(f"Valor por parcela: R$ {valor_parcela:.2f}")
            print(f"Total a pagar: R$ {valor_produto:.2f} (Sem desconto)")
        else:
            print("\n[ERRO] Quantidade de parcelas inválida! Permitido apenas de 1 até 6 parcelas.")

    case _:
        print("\n[ERRO] Forma de pagamento inválida! Escolha 1 ou 2.")
