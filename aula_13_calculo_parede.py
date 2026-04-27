larg = float(input('Qual a largura da parede?'))
alt = float(input('Qual a altura da parede?'))
area = larg * alt 
print(f'Sua parede tem uma dimensão de {larg} x {alt} e uma área de {area:.2f} m². ')
print('Sua parede tem uma dimensão de {} x {} e uma área de {:.2f} m².'.format(larg, alt, area))
tinta = area / 2
#porque nesse caso hipotético - Cada litro de tinta pinta uma área de 2m².
print(f'Para pintar essa parede você precisará de {tinta:.2f} litros de tinta.')
print('Para pintar essa parede você precisará de {:.2f} litros de tinta.'.format(tinta))