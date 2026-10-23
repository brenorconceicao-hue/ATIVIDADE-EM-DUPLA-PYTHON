import os
os.system

print ("<<< ESCOLHA O PRODUTO E A QUANTIDADE >>> ")


nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade : "))
preco_unitario = float(input("Digite o preço unitário: "))


total = quantidade * preco_unitario


if quantidade <= 5:
    percentual_desconto = 0.02
elif quantidade <= 10:
    percentual_desconto = 0.03
else:
    percentual_desconto = 0.05


desconto = total * percentual_desconto
total_a_pagar = total - desconto


print("\n" + "="*30)
print(f"Produto: {nome_produto}")
print(f"Total bruto: R$ {total:.2f}")
print(f"Desconto ({percentual_desconto * 100:.0f}%): R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
print("="*30)


