# Esta é a minha resolução do exercício proposto sobre o uso de condicionais em Python, seguindo as regras estabelecidas.
from csv import excel

print('Olá, Alonso Viana')
while True:
    try:
        valor_unitario = float(input('Insira o valor unitário do produto: '))
        quantidade_produtos = int(input('Insira a quantidade do produto: '))
        break
    except ValueError:
        print('insira um valor valido !')

valor_total = valor_unitario * quantidade_produtos

if valor_total  >= 2500 and valor_total < 6000:
    desconto = 4/100
    valor_total_descontado = valor_total - (valor_total * desconto)
elif valor_total >= 6000 and valor_total < 10000:
    desconto = 7/100
    valor_total_descontado = valor_total - (valor_total * desconto)
elif valor_total >= 10000:
    desconto = 11/100
    valor_total_descontado = valor_total - (valor_total * desconto)
else:
    valor_total_descontado = valor_total

print(f'O valor SEM desconto: R$ {valor_total}')
print(f'O valor COM desconto: R$ {valor_total_descontado}')




