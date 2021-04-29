import csv

quote = "\""

with open('recorridos-realizados-2020.csv') as file:
    reader = csv.reader(file, quotechar='"')
    next(file)
    dictionary = {}
    for row in reader:
        if row[1] in dictionary:
            continue
        dictionary[row[1]
                   ] = (f'{row[1]},{quote+row[3]+quote if "," in row[3] else row[3]},'
                        f'{quote+row[8]+quote if "," in row[8] else row[8]},{row[9]},{row[10]}')
    with open('estaciones.csv', 'w') as estaciones:
        estaciones.write('id,nombre,direccion,long,lat\n')
        for estacion in dictionary.values():
            estaciones.write(estacion + '\n')

# 0 duracion_recorrido
# 1 id_estacion_origen
# 2 fecha_origen_recorrido
# 3 nombre_estacion_origen
# 4 fecha_destino_recorrido
# 5 id_estacion_destino
# 6 nombre_estacion_destino
# 7 id_usuario
# 8 direccion_estacion_origen
# 9 long_estacion_origen
# 10 lat_estacion_origen
# 11 direccion_estacion_destino
# 12 long_estacion_destino
# 13 lat_estacion_destino
# 14 periodo
