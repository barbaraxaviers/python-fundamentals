#Um programa para converter a temperatura digitada em °C e converter para °F
c = float(input('Informe a temperatura em °C:'))
f = ((9*c)/5)+32    #O mesmo principio da formula da porcentagem  / não esquecer da Precedência de Operadores
#9* a temperatura em celsius (esse valor que der) / 5 ( e o resultado dessa equação soma com 32)
print(f'A temperatura de {c} °C corresponde a {f} °F!')
print('A temperatura de {} °C corresponde a {} °F'.format(c,f))
print('A temperatura de',round(c),'°C corresponde a',round(f),'°F')  #esse em especial precisa ter cuidado pois ele gosta de arredondar os numeros
#dependendo do resultado, se for 6 é maior ou igual a 5, ele arredonda o número para cima
#Por isso, para trabalhar com moedas ou temperaturas exatas, o :.2f ou :.1f é bem mais seguro!
#1º	Parênteses (Tudo o que está dentro deles)	( )
#2º	Exponenciação (Potência / Elevado)	**
#3º	Multiplicação, Divisão, Divisão Inteira e Resto	*, /, //, %
#4º	Adição e Subtração (Soma e Menos)	+, -
#Se na mesma conta aparecerem operações com o mesmo peso (por exemplo, uma multiplicação * e uma divisão /)
#o Python resolve simplesmente da esquerda para a direita, na ordem em que elas aparecem.
#Nesse caso específico da fórmula, f = 9 * c / 5 + 32, o Python daria o mesmo resultado, pela regra, a multiplicação * e a divisão / já têm prioridade natural sobre a soma +