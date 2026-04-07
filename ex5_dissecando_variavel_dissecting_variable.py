#Dissecando uma variável


a = input('Digite algo:')
print("O tipo primitivo desse valor é:", type(a))
print("Só tem espaços?", a.isspace())
print("É um numero?", a.isnumeric())
print("É alfabético?", a.isalpha())
print("É alfanumérico?", a.isalnum())
print("Está em maiuscula?:", a.isupper())
print("Está em minuscula?:", a.islower())
print("Está capitalizada?", a.istitle()) # COmeça com a letra maiuscula = Python.
# o a. é sempre objeto - ele tem caracteristicas e realiza função - atributos e metodos
# Parentesis após eles são os metodos -  todo objeto string tem esses métodos



#Don't forget the ()! Without them, Python shows the memory location of the function instead of the result.

#Não esqueça os ()! Sem eles, o Python mostra o local da função na memória em vez do resultado.

#Nu uita parantezele ()! Fără ele, Python arată locația funcției în memorie în loc de rezultat.