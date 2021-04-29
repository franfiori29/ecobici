import zipfile
with zipfile.ZipFile("recorridos-realizados-2020.zip", "r") as zip_ref:
    zip_ref.extractall("./")

exec(open('generate_bicicletas.py').read())
exec(open('generate_estaciones.py').read())
exec(open('generate_usuarios.py').read())
exec(open('clean_recorridos.py').read())
