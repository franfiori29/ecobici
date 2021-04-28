from random import randint

numero_bicicletas = 2000

with open('bicicletas.csv', 'w') as bicicletas:
    bicicletas.write('id,estado\n')
    for num in range(1, numero_bicicletas + 1):
        random_numero = randint(1, 100)
        bicicletas.write(
            f'{num},{"perdida" if random_numero < 2 else "en reparación" if random_numero > 98 else "funcionando"}\n')
