real = float(input('Quanto você tem na carteira? R$'))
dolar = real / 5.03

print(f'Com R${real:.2f} você pode comprar US$ {dolar:.2f}')
print('Com R${:.2f} você pode comprar US$ {:.2f}'.format(real,dolar))
print('Com R$',round (real,2),'você pode comprar US$',round(dolar,2))
#aprendendo a função do round para formatação se por acaso aparecer virgula.

euro = real/ 5.88
ron = real/ 1.15
print(f'Com R$ {real:.2f} você pode comprar € {euro:.2f} ')
print('Com R$ {:.2f} você pode comprar € {:.2f}'.format(real,euro))
print('Com R$',round (real,2), 'você pode comprar €',round (euro,2))

print(f'Com R$ {real:.2f} você pode comprar L {ron:.2f} ')
print('Com R$ {:.2f} você pode comprar L {:.2f}'.format(real,ron))
print('Com R$',round (real,2),'você pode comprar L',round (ron,2))
#aqui usando as 3 formas de escrita para print

dol = float(input('Digite quanto você tem na carteira: US$'))
rea = dol * 5.03
#Fazendo a conta ao contrário
print(f'Com US${dol:.2f} você pode comprar R$ {rea:.2f}')
print('Com US${:.2f} você pode comprar R${:.2f}'.format(dol, rea))
print('Com US$',round (dol,2),'você pode comprar R$',round (rea,2))

