# ===== DESCONTO FIXO =====

produto = (float(input('Qual o preço do produto? R$:')))
desconto = 0.05 * produto
final = produto - desconto
print(f'O valor original é R$ {produto}, e aplicando o desconto fica {final}')

# ===== AUMENTO FIXO =====


produto2 = (float(input('Qual o preço do produto? R$:')))
aumento = produto2 * 0.10
final2 = produto2 + aumento
print(f'O valor original é de R${produto2} e com juros do cartão R$ {final2}')

# ===== VERSÃO DINÂMICA =====


produto3 = (float(input('Qual o preço do produto? R$')))
porcentagem = (float(input('Digite a porcentagem que você quer dar:')))
conta = porcentagem/100
final3 = produto3 +(produto3*conta)
final4 = produto3 - (produto3*conta)
print(f' O valor original é de R$ {produto3} e com ajuste fica {final3}')
print(f'O valor original é de R$ {produto3} e com ajuste fica {final4}')
# porcentagem sozinha é só o tipo 0.10, não é dinheiro. Sempre precisa fazer: produto * porcentagem e isso sim dá o valor em reais 
#aumento produto + (produto * porcentagem) ordem de precedencia
#desconto produto - (produto * porcentagem)

#875 ( de imposto) *15 (porcentagem)/100 (875 é o valor 100%) = 131.25 de imposto.  que é exatamente 15% de 875
