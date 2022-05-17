def calculadora(*args, **kwargs):
  suma = 0
  if 'operacion' in kwargs:
    if kwargs['operacion'] == 'suma':
      for arg in args:
        suma += arg
    elif kwargs['operacion'] == 'resta':
      for arg in args:
        suma -= arg
  return suma


operacion = input('Ingrese la operacion a realizar (suma/resta): ')
print(calculadora(30, 100, 80, 30, 22, 5, operacion = operacion))
