#Escreva um programa que pergunte a quantidade de KM percorridos por um carro
#alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado
#__________________________________________________________________________________________
#Eu vou acrescentar aqui também um custo de seguro viagem por dia, no valor de R$30,00
#vou acrescentar também multa por hora de atraso na devolução do carro no valor de R$20,00/h
#__________________________________________________________________________________________

#fazer por partes 
dias = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados?:'))
seguro = int(input('Coloque os dias alugados: '))
multa = float(input('Quantas horas adicionais de atraso?:'))

#Aqui calcula o preço base do aluguel + km + seguro
pago = (dias * 60)+(km*0.15)+(seguro*30)

#Aqui calcula o valor da multa pelas horas que o usuário atrasou
pagmulta = (multa*20)

#Aqui temos o total final que é a soma do preço base COM a multa.
total_geral = pago + pagmulta
print(f'O Valor da multa por hora adicional é: R${pagmulta:.2f}')
print(f'O total a pagar (Aluguel + Seguro + Multa) é de R${total_geral:.2f}')

#pagmulta = multa * 20: Agora o Python pega o número de horas que você digitou (na variável multa) 
#e multiplica por R$ 20,00. Se a pessoa atrasou 2 horas, vai dar 40 dinheiros.

#total_geral = preco_base + pagmulta: o valor total juntando o preço do 
#aluguel com o valor da multa que foi calculada.