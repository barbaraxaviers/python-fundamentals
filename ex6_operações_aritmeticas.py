
#Operadores aritméticos - precisa de operandos - pode ser numero, string e até variaveis
#nesse caso aqui são aritméticos = numeros ou variaveis que contem numeros
#operadores binarios - operador que precisa de 2 operandos
#Se eu quero testar se algo é igual a outro no Python, eu uso == e UM SIMBOLO DE IGUAL é para atribuição = recebe
#C, JAVA,PHP == igualdade ou operador relacional de igualdade
#+ adição ( ou concatenação - 5+2==7
#- subtração -  5-2==3
#* multiplicação - 5*2==10
#/ divisão - 5/2==2.5
#** potência  - 5**2==25
##// divisão inteira -  5//2==2
#% resto da divisão - 5%2==1
#======================================================
#ordem de precedencia: 1(), 2**, 3 * / // %, 4 + -. 
#======================================================
# ex: 5+3*2== 11 - 2x3 = 6 e 6+5 = 11
# ex: 3*5+4**2== 31  -  4**2(4x4) = 16 e 3*5 =15 =31
# ex: 3*(5+4)**2 = - 5+4 = 9 e 9**2(9x9) = 81 e 81x3 = 243  (mesmo que seja +, esta dentro dos parenteses)
#para fazer os calculos no termina, digite python e enter. - entrar no ''modo tradutor''
# raiz quadrada - dá pra fazer 81**(1/2) = 9.0 é a potencia dele por meio. |Raiz quadrada (Square root)
# raiz cúbica - 127**(1/3) |Raiz cúbica (Cube root)
#>>> 18%2
#0
#>>> 122%3
#2
#>>> 4**3
#64
#>>> pow(4,3)
#64
#>>> 81**(1/2)
#9.0
#>>> 25**(1/2)
#5.0
#>>> 127**(1/3)
#5.026525695313479
#Tambem funciona com string
#>>> 'oi'*5
#'oioioioioi'

nome = input('Qual seu nome?')
print('Prazer em te conhecer{:20}!!'.format(nome))
print(f"Prazer em te conhecer{nome:20}!!!!")
print(f"Prazer em te conhecer{nome:>20}!!!!")
print(f"Prazer em te conhecer{nome:<20}!!!!")
print(f"Prazer em te conhecer{nome:^20}!!!!")
print(f"Prazer em te conhecer{nome:=^20}!!!!")
n1 = float(input('Um valor:'))
n2 = float(input("Outro valor:"))
s = n1+n2 #ou
print(f'A soma vale {s}')
print(f'A soma vale {n1+n2}')
m= n1*n2
d = n1/n2
di = n1//n2
e = n1** n2
print(f'A multiplicação dá:{n1*n2}')
print(f'A multiplicação dá:{m}')
print(f'A divisão dá:{n1/n2}')
print(f'A divisão dá:{d}')
print(f'A divisão inteira dá: {n1//n2}')
print(f'A divisão inteira dá: {di}')
print(f'A potencia dá: {n1**n2}')
print(f'A potência dá: {e}')
print(f'A soma é {s}, \n o produto é {m} e a divisão é {d:.3f}',end="  ")  #ex: para ter apenas 3 casas, ao inves de 0.6666666666, fica 0.666
#o end é para manter na mesma linha ao inves de quebrar para a de baixo. e a \n faz ela quebrar a linha sem precisas criar um novo print. é tipo um 'enter'
#a string fica vazia ou pode colocar  <<< dentro também
print(f'A soma é {n1+n2}, o produto é {n1*n2} e a divisão é {n1/n2}')
#exercicios:
num1 = 2
num2 = 1
num3 = 3
print (f'o numero é o {num1} seu antecessor é {num2} e o sucessor {num3}')
#ou
nume1 = int(input('Digite um numero:'))
nume2 = nume1 - 1
nume3 = nume1 + 1
print(f'O numero é o {nume1} seu antecessor é {nume2} e o sucessor é {nume3}')
#####
numer1 = int(input('Digite um numero:'))
numer2 = numer1 * 2
print(f'O dobro do {numer1} é {numer2} ')
######
numero1 = int(input('Digite um numero'))
numero2 = numero1 * 2
numero3 = numero1 * 3
numero4 = numero1 **(1/2)
print(f'O numero é {numero1}, seu dobro é {numero2}, seu triplo é {numero3} e sua raiz quadrada é {numero4:.2f}')
#ordem de precedencia
nome1 = input ('Digite seu nome:')
nota1 = int(input('Insira sua nota:'))
nota2 = int(input('Insira sua outra nota:'))
nf = (nota1 + nota2) / 2
print(f'Olá, {nome1} sua média é {nf}')
#pra não esquecer: primeiro ou resultado de vai um parentese. - eu preciso do resultado da soma para depois dividir - se precisa desse resultado 
#par ausar em outra conta, esse algo vira um pacote fechado com ()
#imagine que os operadores de multiplicação e divisão são imas, se deixar o /2 encostado na nota2 ele vai puxar para a conta antes da nota 1 chegar perto
#para proteger a soma e garanir que as duas notas se unam antes de serem atacadas pela divisão, você cria um escudo, os ()
metro1 = float(input('Quantos metros?:'))
cm = metro1 *100
mm = metro1 *1000
print(f'a medida de {metro1}m corresponde a {cm}cm e {mm}mm.')
# Passo 1: Receber o valor (o float permite números com vírgula)
#m = float(input('Digite a metragem: '))

# Passo 2: Aplicar a regra que a gente descobriu (o cálculo)
#centimetros = m * 100   # Multiplica por 100
#milimetros = m * 1000   # Multiplica por 1000

# Passo 3: Exibir pro usuário
#print(f'{m} metros equivalem a {centimetros}cm e {milimetros}mm')

##########################################################
#O input sempre recebe o que você digita como texto (string)
##########################################################
km =  float(input('Quantos km?:'))
m = km *1000
print(f'{km}km em metros é {m}')

m = float(input('Quantos m?:'))
km = m / 1000
print(f'{m}m é igual a {km}km.')

dolar = float(input('Quantos dolares?'))
reais = dolar*5
print('Hoje o dolar esta valendo {} reais.'.format(reais))

reais = float(input('Quantos reais você tem?:'))
dolar = reais / 5
print('Hoje o real esta valendo {} dolares.'.format(dolar))

tabuada = float(input('Digite um numero:'))
tabuada1 = tabuada*1, tabuada*2, tabuada*3, tabuada*4, tabuada*5
print('A tabuada completa do {}, é {}'.format(tabuada,tabuada1))

tabuada = int(input('Digite um numero para ver sua tabuada:'))
print('-'*12) #isso cria uma linha decorativa, é uma "malandragem" do Python para criar uma linha divisória. Ele repete o caractere de hífen 12 vezes.
print(f'{tabuada} x {1:2} = {tabuada * 1}')  #O f' antes das aspas indica que é uma f-string. - forma de formatar
print(f'{tabuada} x {2:2} = {tabuada * 2}') #Tudo que está entre {} é código Python sendo executado ali dentro.
print(f'{tabuada} x {3:2} = {tabuada * 3}') #O :2 dentro de {1:2} serve apenas para o alinhamento. Ele diz ao Python para reservar o espaço de 2 caracteres, assim a tabuada fica com as unidades e dezenas retinhas.
print(f'{tabuada} x {4:2} = {tabuada * 4}')
print(f'{tabuada} x {5:2} = {tabuada * 5}')
print(f'{tabuada} x {6:2} = {tabuada * 6}')
print(f'{tabuada} x {7:2} = {tabuada * 7}')
print(f'{tabuada} x {8:2} = {tabuada * 8}')
print(f'{tabuada} x {9:2} = {tabuada * 9}')
print(f'{tabuada} x {10:} = {tabuada * 10}')
print('-'*12) # aqui ele vai repetir a 'string' de dentro só pra ficar bonitinho. Mas pode ser qualquer coisa, _ - = <3.

real = float(input('Quantos reais você tem na carteira R$?')) # Lê o valor em reais que a pessoa tem na carteira
cotacao = 5.06 # Define a cotação do dólar hoje
dolar = real / cotacao # Faz o cálculo da conversão
print(f'Com R$ {real:.2f} você pode comprar US$ {dolar:.2f}') # Exibe o resultado com duas casas decimais

# Lê as dimensões da parede
larg = float(input('largura em metros:'))
alt = float(input('altura em metros:'))
area = larg * alt # Calcula a área (Base x Altura)
tinta = area / 2 # Calcula a tinta (Sabe-se que 1L pinta 2m²)
print(f'sua parede tem dimentão de {larg} x {alt} e a sua area tem {area:.2f}m².')
print(f'A quantidade de tinta necessária é de {tinta:.2f} litros.')
#Cálculo da Área: Em geometria, a área de um retângulo (sua parede) 
#é calculada multiplicando a largura pela altura ($A = L \times H$).
#A Regra de Três: Se $1$ litro de tinta pinta $2m^2$, para descobrir o total de litros basta dividir a área total por $2$.

produto = float(input('Digite o valor do produto R$:'))
result = produto - (produto *0.05) # A forma detalhada: preco - (preco * 5 / 100). Primeiro você descobre quanto é 5% e depois subtrai do valor cheio.
print(f' O valor do produto é {produto} e com o desconto ficaria R$:{result:.2f}')

salario = float(input('Seu salário é R$:'))
novo_salario = salario + (salario*0.15)
print(f' Seu salário era de R${salario:.2f}, e com o reajuste foi para R$ {novo_salario:.2f}, use com moderação.')
