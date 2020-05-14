from app import  app
from flask import  render_template, request, redirect, url_for
from app.calificacion import Calificacion,ListaDeCalificaciones
from app.jsonHelper import JSONHelper
from app.formas import FormaAlta

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
    listuca = JSONHelper.LeerJSON(filename)
    return render_template("lista.html", calificaciones = listuca)


@app.route('/alta2', methods=["GET","POST"])
def alta2():
    fa = FormaAlta()
    if fa.validate_on_submit():
        nombre = fa.nombre.data
        apellido = fa.apellido.data
        matricula = fa.matricula.data
        materia = fa.materia.data
        calificacion = fa.calificacion.data
        c = Calificacion(nombre, apellido, matricula, materia, calificacion)
        listuca = JSONHelper.LeerJSON(filename)
        if listuca is None or len(listuca) == 0:
            listuca = ListaDeCalificaciones()
        listuca.append(c)
        JSONHelper.CreaJSON(listuca, filename)
        return redirect(url_for("lista"))
    return  render_template("alta2.html",forma = fa)