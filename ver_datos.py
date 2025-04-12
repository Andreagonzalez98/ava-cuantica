from app import app, db
from models import Usuario, Modulo

with app.app_context():
    usuarios = Usuario.query.all()
    modulos = Modulo.query.all()

    print("Usuarios:")
    for u in usuarios:
        print(f"{u.id} - {u.nombre} - {u.correo}")

    print("\nMódulos:")
    for m in modulos:
        print(f"{m.id} - {m.nombre} - {m.descripcion}")
