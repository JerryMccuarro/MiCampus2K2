from app import app, db
from flask import render_template, request, redirect, url_for
from app.calificacion import Calificacion, ListaDeCalificaciones
from app.jsonHelper import JSONHelper
from app.formas import FormaAlta, FormaLogin, FormaCreaUsuario
from app.modelos import TablaCalificacion, TablaUsuario
from flask_login import login_required, login_user, logout_user, current_user

filename = "lista.json"


@app.route('/', methods=["POST", "GET"])
@login_required
def alta():
    if not current_user.esAdmin:
        return redirect(url_for("lista"))
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        matricula = request.form["matricula"]
        materia = request.form["materia"]
        calificacion = request.form["calificacion"]
        c = Calificacion(nombre, apellido, matricula, materia, calificacion)
        listuca = JSONHelper.LeerJSON(filename)
        if len(listuca) == 0:
            listuca = ListaDeCalificaciones()
        listuca.append(c)
        JSONHelper.CreaJSON(listuca, filename)
    return render_template("alta.html", user=current_user)


@app.route('/lista')
@login_required
def lista():
    listuca = TablaCalificacion.query.filter_by(isActive=True)
    return render_template("lista.html", calificaciones=listuca, user=current_user)


@app.route('/alta2', methods=["GET", "POST"])
@login_required
def alta2():
    if not current_user.esAdmin:
        return redirect(url_for("lista"))
    fa = FormaAlta()
    nc = TablaCalificacion()
    if fa.validate_on_submit():
        nc.nombre = fa.nombre.data
        nc.apellido = fa.apellido.data
        nc.matricula = fa.matricula.data
        nc.materia = fa.materia.data
        nc.calificacion = fa.calificacion.data
        db.session.add(nc)
        db.session.commit()
        return redirect(url_for("lista"))
    return render_template("multiusos.html", forma=fa, user=current_user)


@app.route('/edit/<id>', methods=["GET", "POST"])
@login_required
def edit(id):
    if not current_user.esAdmin:
        return redirect(url_for("lista"))
    guardado = TablaCalificacion.query.get(id)
    fa = FormaAlta()
    if fa.validate_on_submit():
        guardado.nombre = fa.nombre.data
        guardado.apellido = fa.apellido.data
        guardado.matricula = fa.matricula.data
        guardado.materia = fa.materia.data
        guardado.calificacion = fa.calificacion.data
        db.session.commit()
        return redirect(url_for("lista"))
    if guardado:
        fa.nombre.data = guardado.nombre
        fa.apellido.data = guardado.apellido
        fa.matricula.data = guardado.matricula
        fa.materia.data = guardado.materia
        fa.calificacion.data = guardado.calificacion
        return render_template('multiusos.html', forma=fa, user=current_user)
    return redirect(url_for("alta2"))


@app.route('/delete/<int:id>', methods=["GET", "POST"])
@login_required
def delete(id):
    if not current_user.esAdmin:
        return redirect(url_for("lista"))
    guardado = TablaCalificacion.query.get(id)
    if guardado:
        guardado.isActive = False
        db.session.commit()
    return redirect(url_for("lista"))


@app.route('/login', methods=["GET", "POST"])
def login():
    fl = FormaLogin()
    if current_user.is_authenticated:
        return redirect(url_for("lista"))
    if fl.validate_on_submit():
        correo = fl.email.data
        usuario = TablaUsuario.query.filter_by(email=correo).first()
        if usuario and usuario.isActive:
            if usuario.check_password(fl.password.data):
                login_user(usuario, True)
                if usuario.esAdmin:
                    return redirect(url_for("alta2"))
                return redirect(url_for("lista"))
    return render_template("multiusos.html", forma=fl, user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/registro', methods=["GET", "POST"])
def registro():
    fcu = FormaCreaUsuario()
    if fcu.validate_on_submit():
        email = fcu.email.data
        usuario = TablaUsuario.query.filter_by(email=email).first()
        if usuario is not None:
            return redirect(url_for("registro"))
        nuevo = TablaUsuario()
        nuevo.email = email
        nuevo.set_password(fcu.password.data)
        db.session.add(nuevo)
        db.session.commit()
        login_user(nuevo,True)
        return  redirect(url_for("lista"))
    return render_template("multiusos.html", forma=fcu, user=current_user)
