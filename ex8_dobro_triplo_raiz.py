n = int(input("Digite um numero:"))
d = n * 2
t = n * 3
terca_parte = n/3
r = n **(1/2)
print(f'O dobro de {n} vale {d}.')
print(' - O dobro de {} vale {}'.format(n,d))
print(f'O triplo de {n} vale {t}.')
print('- O triplo de {} vale {}'.format(n,t))
print(f'A terça parte de {n} vale {terca_parte:.2f}.')
print('- A terça parte de {} vale {:.2f}'.format(n,terca_parte))
print(f'A raiz quadrada de {n} vale {r:.2f}')
print('- A raiz quadrada de {} \n vale {:.2f}'.format(n,r))  # se eu quiser a mensagem para a linha debaixo sem fazer outro print, uso \n

#{ : Começa o buraco. Abre chaves
#: : "Agora vou te dizer como quero que o número apareça". Dois pontos - O separador. É o sinal de "Atenção, lá vem regra!".
#. : "Vou falar das casas decimais". É o sinal de "Corte as casas decimais".
#2 : "Quero duas". É o "Quanto e de qual tipo".
#f : "É um número com vírgula F (float(flutuantes))". - e antes que eu me esqueça, python usa . e não , 
#} : Fecha o buraco. Fecha chaves

n1 = int(input('Digite um numero:'))
print('O dobro de {} vale {}.'.format(n1, n1*2))
print(f'O dobro de {n1} vale {n1*2}')
print('O triplo de {} vale {}. \nA raiz quadrada de {} é {:.2f}.'.format(n1, (n1*3), n1, (n1**(1/2))))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é {:.2f}.'.format (n1,(n1*3), n1, pow(n1,(1/2))))
print(f'O triplo de {n1} vale {n1*3}. \nA raiz quadrada de {n1} vale {n1**(1/2):.2f}')
print(f'O triplo de {n1} vale {n1*3}. \nA raiz quadrada de {n1} vale {pow (n1,1/2):.2f}')