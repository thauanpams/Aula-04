valor = float(input('Insira o valor da compra'))

forma_de_pagamento = input('Forma de Pagamento: ').lower()
desconto = valor * 0.16 
valor_total = valor - desconto


if valor > 250 and forma_de_pagamento  == "a vista":
    print(f'Desconto igual a {valor_total}')
    

else:
    print(f'O valor é {valor}')