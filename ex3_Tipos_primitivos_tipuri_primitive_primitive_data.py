#Tipos primitivos e saidas de dados
#Tipuri Primitive si Iesirea Datelor 
#Primitive Data Types and Data Output
n1 = input ('digite um numero:')
n2 = input ('Digite outro numero:')
soma = (n1+n2)
print(soma)
print(type(n1)) # aqui dá str porque não disse que era numero
# aqui apenas concatena ( juntar uma string na outra)

#aqui realmente faz a soma
n3 = float(input ("Digite mais um numero:"))
n4 = float(input ("Digite mais outro numero:"))
soma1 = n3+n4
print("O resultado é:",soma1)
print('A soma vale: {}'.format(soma1))
print(f'O valor é: {soma1}')
print (f"A soma entre {n3} e {n4} é: {soma1} ")
print ('O valor somado de ',n3,'e',n4, 'é:',soma1)
print ("A soma de {} e de {} é: {}.".format(n3,n4,soma1))
print(type(n3)) #(saber  o tipo, aqui dá float porque falo que é num)

n = float(input('Digite um valor:'))
print(n) 
n0 = bool(input("Digite outro valor:"))
print(n0) # aqui vamos ler o valor que for colocado no terminal, se não por valor fica falso.( porque nao tem valor dentro) Se tiver valor dentro é verdadeiro.
print(n1.isalnum) #só podemos chamar a função is quando a variavel for string. se chamar is em n por exemplo que é float não vai aparecer = serve para mostrar seu tipo primitivo


#Os principais numeros primitivos do python: 
#Int = inteiros - 7, -4, 0, 9875
#Float = reais ou ponto flutuante - 4.5, 0.076, -15.233, 7.0
#Bool = Lógicos -  True or False ( Letra maiuscula no inicio SEMPRE)
# Str = Caracteres ou string - 'Olá' Sempre em aspas. '7,5' Numero em aspas é texto. '' (string vazia)