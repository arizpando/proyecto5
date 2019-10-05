print('calcular el volumen,la superficie de la base, la superficie lateral y la superficie total del cilindro')
diametroTotal = float(input('diametro Total = '))
diametroInterior = float(input('diametro interior = '))
altura = float(input('altura= '))
masa= float(input('masa= '))
radioTotal = diametroTotal/2
radioInterior =diametroInterior/2
volumenTotal = 3.14*(radioTotal**2)*altura
volumenInterior = 3.14*(radioInterior**2)*altura
volumen = volumenTotal-volumenInterior
densidad= masa*volumen
superficieTotalbase = 2*3.14*(radioTotal**2)
superficieInteriorbase = 2*3.14*(radioInterior**2)
superficieBase = superficieTotalbase-superficieInteriorbase
superficieExterior = 2*3.14*radioTotal*altura
superficieInterior = 2*3.14*radioInterior*altura
superficieLateral = superficieExterior+superficieInterior
superficieTotal = superficieLateral+superficieBase
print('volumen= ',round(volumen, 3))
print('superficie base= ',round(superficieBase, 3))
print('superficie lateral= ',round(superficieLateral, 3))
print('superficie total= ',round(superficieTotal, 3))
print('densidad = ',round(densidad, 3))
