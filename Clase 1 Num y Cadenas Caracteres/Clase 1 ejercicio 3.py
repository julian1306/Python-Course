cadena = "acitametaM ,5.8 ,otipeP ordeP"


cadena_volteada = cadena[::-1]

#print (cadena_volteada)


nombre_alumno = cadena_volteada[0:12 ]

#print(nombre_alumno)

nota = cadena_volteada[14:17]

#print(nota)


materia = cadena_volteada [19:]

#print(materia)


print(nombre_alumno, "ha sacado un", nota , "en", materia)