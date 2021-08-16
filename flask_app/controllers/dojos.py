from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def dojos_home():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos = dojos)

@app.route('/dojos/create', methods =['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('ninjas.html', dojos = dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")

@app.route('/dojos/<int:dojo_id>')
def view_dojo(dojo_id):
    data = {
        'dojo_id': dojo_id
    }
    ninjas = Ninja.get_all_ninjas(data)
    return render_template('view_dojo.html', ninjas = ninjas)