from faker import Faker
import datetime
import csv
import random

fake = Faker()
start_date = datetime.date(year=2019, month=1, day=1)
end_date = datetime.date(year=2019, month=12, day=31)
start_birth = datetime.date(year=1930, month=1, day=1)
end_birth = datetime.date(year=2001, month=12, day=31)

with open('recorridos-realizados-2020.csv', newline='') as file:
    reader = csv.DictReader(file)
    miset = set()
    for row in reader:
        if row['id_usuario'] in miset:
            continue
        miset.add(row['id_usuario'])
    with open('usuarios.csv', 'w') as usuarios:
        usuarios.write('id,nombre,apellido,genero,nacimiento,tarjeta,alta\n')
        for id_usuario in miset:
            usuarios.write(
                f'{id_usuario},{fake.first_name()},{fake.last_name()},{random.choice(["M","F"])},'
                f'{fake.date_between(start_date=start_birth, end_date=end_birth)},'
                f'{random.choice(["Visa","American Express", "Mastercard"])},'
                f'{fake.date_between(start_date=start_date, end_date=end_date)}\n')
