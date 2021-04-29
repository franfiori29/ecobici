import csv

with open('recorridos-realizados-2020.csv', newline='') as file, open('recorridos.csv', 'w') as recorridos:
    reader = csv.DictReader(file, quotechar='"')
    recorridos.write(
        'duracion,id_estacion_origen,fecha_hora_salida,fecha_hora_llegada,id_estacion_destino,id_usuario,periodo\n')
    for row in reader:
        recorridos.write(
            f'{row["duracion_recorrido"]},{row["id_estacion_origen"]},'
            f'{row["fecha_origen_recorrido"]},{row["fecha_destino_recorrido"]},'
            f'{row["id_estacion_destino"].split(".")[0] if "." in row["id_estacion_destino"] else row["id_estacion_destino"]},'
            f'{row["id_usuario"]},{row["periodo"]}\n')

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
