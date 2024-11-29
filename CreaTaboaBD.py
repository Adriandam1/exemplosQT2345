
from conexionBD import ConexionBD


class CreaTaboaBD():
    def __init__(self):

        # conexion con la base de datos conexionDB
        # en este caso crea usuarios.bd con la tabla usuarios y los parametros de abajo
        # si lo ejecutamos varias veces nos dice que la tabla ya existe

        bDatos = ConexionBD("usuarios.bd")
        bDatos.conectaBD()
        bDatos.creaCursor()
        datos = bDatos.consultaSenParametros("""Create Table usuarios
        ('nome' text,
        'dni' text,
        'xenero' text,
        'falecido' int)""")

        bDatos.pechaBD()

if __name__ == "__main__":
    creaTaboa = CreaTaboaBD()














