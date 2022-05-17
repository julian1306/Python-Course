nombre = input('ingrese nombre').lower()

while nombre[0] < 'a' or nombre[0] > 'z':
    nombre = input('Ingrese nombre valido A-Z :')

fan = input('prefiere marvel o capcom ?').lower()

while fan != 'marvel' and fan != 'capcom':
    fan = input('Solo se puede ingresar marvel o capcom :')


if (fan == 'marvel' and nombre[0] < 'm' and nombre[0] >= 'a') or (fan == 'capcom' and nombre[0] > 'n' and nombre[0] <= 'z'):
    print('grupoa A')

else:
    print('grupo B')
