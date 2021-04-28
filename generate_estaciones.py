import csv

with open('recorridos-realizados-2020.csv') as file:
    reader = csv.DictReader(file)
    dictionary = {}
    for row in reader:
        if row['id_estacion_origen'] in dictionary:
            continue
        dictionary[row['id_estacion_origen']
                   ] = (f'{row["id_estacion_origen"]},{row["nombre_estacion_origen"]},'
                        f'{row["direccion_estacion_origen"]},{row["long_estacion_origen"]},{row["lat_estacion_origen"]}')
    with open('estaciones.csv', 'w') as estaciones:
        estaciones.write('id,nombre,direccion,long,lat\n')
        for estacion in dictionary.values():
            estaciones.write(estacion + '\n')


# duracion_recorrido
# id_estacion_origen
# fecha_origen_recorrido
# nombre_estacion_origen
# fecha_destino_recorrido
# id_estacion_destino
# nombre_estacion_destino
# id_usuario
# direccion_estacion_origen
# long_estacion_origen
# lat_estacion_origen
# direccion_estacion_destino
# long_estacion_destino
# lat_estacion_destino
# periodo
