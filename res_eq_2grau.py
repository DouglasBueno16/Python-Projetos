"""
Programa que calcula as raízes de uma equação de 2 grau
ax^2 + bx + c = 0
Para 
delta > 0 -> duas raízes reais
delta = 0 -> uma raíz real
delta < 0 -> não existe raíz real
"""
print('Equação de 2 Grau no formato \n ax^2 + bx + c = 0')
a = int(input('Digite o valor de a: '))

if a != 0:
  b = int(input('Digite o valor de b: '))
  c = int(input('Digite o valor de c: '))
  delta = b**2 - (4*a*c)
  print(f'Delta: {delta}')
  if delta >= 0:
    x1 = (-b + delta **0.5)/(2*a)
    x2 = (-b - delta **0.5)/(2*a)
    print(f'Raíz 1: {x1}')
    print(f'Raíz 2: {x2}')
  
  elif delta == 0:
    x = (-b + delta **0.5)/(2*a)
    print(f'A raíz é: {x}')

  else:
    print(f'Não existe raíz real para o delta: {delta}')

else:  # if verificando o valor de a
  print('A sua equação não é de segundo grau!')
