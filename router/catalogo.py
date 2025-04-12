from flask import Blueprint, render_template, session, redirect, url_for, flash
from flask_login import current_user, login_required
from models import Modulo, Carrito, db

catalogo_bp = Blueprint('catalogo', __name__)

# Ruta para mostrar los módulos del catálogo
@catalogo_bp.route('/catalogo')
def catalogo():
    modulos = Modulo.query.all()
    return render_template('catalogo.html', modulos=modulos)

# Ruta para agregar un módulo al carrito del usuario logueado
@catalogo_bp.route('/agregar_carrito/<int:modulo_id>')
@login_required
def agregar_carrito(modulo_id):
    try:
        # Verifica si el módulo ya está en el carrito del usuario
        existe = Carrito.query.filter_by(usuario_id=current_user.id, modulo_id=modulo_id).first()
        if existe:
            flash('Este módulo ya está en tu carrito.', 'warning')
        else:
            nuevo_item = Carrito(usuario_id=current_user.id, modulo_id=modulo_id)
            db.session.add(nuevo_item)
            db.session.commit()
            flash('Módulo agregado al carrito.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Ocurrió un error al agregar al carrito: ' + str(e), 'danger')
    
    return redirect(url_for('catalogo.catalogo'))
