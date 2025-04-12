from flask import Blueprint, render_template, session, redirect, url_for
from models import Modulo

catalogo_bp = Blueprint('catalogo', __name__)

@catalogo_bp.route('/catalogo')
def catalogo():
    modulos = Modulo.query.all()
    return render_template('catalogo.html', modulos=modulos)
