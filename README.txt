# 💻 AVA - Computación Cuántica

Este es un prototipo funcional de un **Ambiente Virtual de Aprendizaje (AVA)** desarrollado con **Flask** sobre **computación cuántica**. Permite el registro e inicio de sesión de usuarios, muestra un catálogo de módulos educativos y permite agregar módulos a un carrito.

---

## 🚀 Funcionalidades

- Registro e inicio de sesión de usuarios  
- Catálogo de módulos sobre computación cuántica  
- Visualización de detalles de cada módulo  
- Agregar y eliminar módulos desde el carrito  
- Carga automática de módulos demo y usuario demo  
- Base de datos SQLite lista para usarse  
- Código modular con Blueprints

---

## 👨‍🏫 Usuario demo

Puedes iniciar sesión con el siguiente usuario para probar el sistema:

- 📧 Correo: `admin@correo.com`  
- 🔐 Contraseña: `admin123`

---

## 🧪 Tecnologías utilizadas

- Python 3  
- Flask  
- Flask-Login  
- Flask-WTF  
- SQLAlchemy  
- SQLite  
- HTML + Jinja2

---

## 📁 Estructura del proyecto

. ├── run.py ├── app.py ├── create_db.py ├── requirements.txt ├── router/ │ └── catalogo.py ├── forms/ │ └── init.py ├── models/ │ └── init.py ├── templates/ │ ├── base.html │ ├── login.html │ ├── register.html │ ├── dashboard.html │ ├── modulo.html │ ├── carrito.html │ └── catalogo.html ├── static/ │ └── estilos, imágenes, etc. └── instance/ └── ava.db
---

## 📦 Cómo clonar y ejecutar el proyecto localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

2. Crear entorno virtual (opcional pero recomendado)

python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

 Instalar dependencias

pip install -r requirements.txt

Ejecutar la aplicación

python run.py
