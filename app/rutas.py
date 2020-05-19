from app import  app,db
from flask import  render_template, request, redirect, url_for
from app.calificacion import Calificacion,ListaDeCalificaciones
from app.jsonHelper import JSONHelper
from app.formas import FormaAlta
from app.modelos import TablaCalificacion

filename = "lista.json"

@app.route('/', methods=["POST","GET"])
def alta():
    if request.method == "POST":

        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        matricula = request.form["matricula"]
        materia = request.form["materia"]
        calificacion = request.form["calificacion"]
        c = Calificacion(nombre,apellido,matricula,materia,calificacion)
        listuca = JSONHelper.LeerJSON(filename)
        if len(listuca) == 0:
            listuca = ListaDeCalificaciones()
        listuca.append(c)
        JSONHelper.CreaJSON(listuca,filename)
    return render_template("alta.html")




@app.route('/lista')
def lista():
    listuca = TablaCalificacion.query.filter_by(isActive=True)
    return render_template("lista.html", calificaciones = listuca)


@app.route('/alta2', methods=["GET","POST"])
def alta2():
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
    return  render_template("alta2.html",forma = fa)


@app.route('/edit/<id>', methods=["GET","POST"])
def edit(id):
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
        return render_template('alta2.html',forma = fa)
    return redirect(url_for("alta2"))

@app.route('/delete/<int:id>', methods=["GET","POST"])
def delete(id):
    guardado = TablaCalificacion.query.get(id)
    if guardado:
        guardado.isActive = False
        db.session.commit()
    return redirect(url_for("lista"))

