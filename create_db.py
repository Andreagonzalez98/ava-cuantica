from app import app
from models import db, Usuario, Modulo

with app.app_context():
    db.drop_all()
    db.create_all()

    # Crear usuario demo
    usuario_demo = Usuario(nombre="Demo", correo="admin@correo.com")
    usuario_demo.set_password("admin123")
    db.session.add(usuario_demo)

    # Crear módulos demo
    modulo1 = Modulo(
        nombre="Introducción a la computación cuántica",
        descripcion="Conceptos básicos de la computación cuántica.",
        precio=100.000
    )

    modulo2 = Modulo(
        nombre="Qubits y puertas lógicas cuánticas",
        descripcion="Explora los estados cuánticos y las puertas lógicas fundamentales.",
        precio=200.000
    )

    modulo3 = Modulo(
        nombre="Computación clásica vs cuántica",
        descripcion="Comparación de ventajas, desventajas y desafíos entre ambos paradigmas.",
        precio=400.000
    )

    modulo4 = Modulo(
        nombre="Superposición y entrelazamiento cuántico",
        descripcion="Aprende sobre los fenómenos clave de la computación cuántica y sus aplicaciones.",
        precio=600.000
    )

    db.session.add_all([modulo1, modulo2, modulo3, modulo4])
    db.session.commit()
