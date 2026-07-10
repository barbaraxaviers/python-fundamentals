#Funcionario ganhava R$4319.43  -  Terá um aumento salarialde 15%
#passa a receber R$4967,34
print("Desafio 15: Faça o reajuste salarial com porcentagem\ne mostre o resultado.") #testando o \n de novo
salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100) #salario é 100% e o x corresponde a 15%

#-----------------------------------------------------------------------------------------------------

print(f"Um funcionário que ganhava R${salario:.2f}, com 15% de aumento\npassa a receber R${novo:.2f} ")
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento\npassa a receber R${:.2f}'.format(salario,novo))
print('Um funcionário que ganhava R$ ',round (salario),'com 15% de aumento\npassa a receber',round(novo), '')
