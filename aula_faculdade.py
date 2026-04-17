print('Ola mundo!')
# para declarar variaveis, sempre coloca o 'nome' da coisa e o = 
idade = 29
nome = 'Barbara Bianca'
valor = 39.50
resposta = True

print(f'Olá {nome},idade: {idade}')
#
nome = input ('Informe seu nome:')
input('Coloque sua idade:')


# aula 3 

print("Olá, mundo!")
#Variaveis são onde eu armazeno informações no programa.
#Variaveis são valores que ficam armazenadas na memoria e que variam com o tempo - ficam na RAM
endereço = 'Rua tremembé , 151' # tipo texto, string - str
valor = 188.50 #segue padrao americano, por isso o ponto ao inves da virgula separando casas decimais
idade = 29 # tipo numerico /quantidade/inteiro
print(idade)
print(valor)
print(endereço)

#Tipos de variaveis ( tipos de dados)

#tipos numericos
qtde_filhos: int = 1
peso: float = 55.00

#tipos literais
nome: str = input("Informe seu nome:")
print(nome)

#QUero um fiat uno, vendedor passa o preço
#qual pergunta devo fazer? - Será que posso pagar?
#Resposas possiveis: 
#Será que posso pagar?
#Sim e Não
#Qtde Parcelas

#Eu posso comprar?
# Sim e Não
#isso é uma tomada de decisão.

valor_carro = 90000.00
# Se eu posso comprar, eu vou comprar, se eu não posso, eu não compro ( if)
dinheiro = float (input("Informe o valor da conta:"))
#precisa avisar quando colocar valor se é float
#if é um bloco de desvio condicional
#o codigo esta tomando uma decisão no meio do projeto, no meio do codigo fonte
#ele esta fazendo alguma coisa, imprimindo uma mensagem == é comparando os dois um de um lado e o outro do outro. 

if dinheiro >= valor_carro:
    #colocando o operador de maior estamos excluindo se a pessa tiver exatamente o valor do carro para comprar, diz que nao da 
    #colocar os dois operadores juntos >= 
    print(f'Posso comprar o carro de {valor_carro} reais')
    print("posso comprar o carro" +str (valor_carro)+ "reais")
elif dinheiro >= 35000.00:
    print("Pode comprar o carro parcelado")
elif dinheiro >= 30000.00:
    print("Pode comprar mais notas promissórias ou valor parcelado")
    
    if dinheiro >= 32000.00:
        print("Dar desconto de 3000,00 reais")
else:
    print("Deixar para a proxima")

