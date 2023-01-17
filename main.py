from flask import Flask, render_template, request, redirect, jsonify
from db import conn
from  psycopg2 import extras

# Modelo
class UserModel:
    def __init__(self):
        connection = conn()
        cur = connection.cursor()
        cur.execute('SELECT id, nombre, edad FROM usuario')
        connection.commit()
        users = cur.fetchall()
        
        usuarios = []
        for user in users:
            us = {'id':user[0], 'nombre':user[1], 'edad':user[2]}
            usuarios.append(us)
        
        cur.close()
        connection.close()

        self.users = usuarios

    def add_user(self, user_nombre, user_edad):
        connection = conn()
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO public.usuario(nombre, edad) VALUES (%s, %s);""", (user_nombre, user_edad))
            connection.commit()
        
        connection.close()
    def edit_user(self, index, user_nombre, user_edad):
        connection = conn()
        cur = connection.cursor()
        cur.execute("""UPDATE public.usuario SET nombre=%s, edad=%s WHERE id=%s""", (user_nombre, user_edad, index))
        
        connection.commit()
        cur.close()
        connection.close()

    def delete_user(self, index):
        connection = conn()
        cur = connection.cursor()  
        cur.execute("DELETE FROM public.usuario WHERE id=%s", str(index))
        connection.commit()
        connection.close()
        
        return jsonify({'message': 'User eliminado'})

    def promedio_edad(self):
        connection = conn()
        cur = connection.cursor()
        cur.execute('SELECT avg(edad) FROM public.usuario;')
        connection.commit()
        us = cur.fetchone()
        connection.commit()
        print(us)
        return jsonify({'promedio': str(us)}), 204

    def status(self):
        st = {
            'namesytem': 'app-users',
            'version': '0.1',
            'developer': 'Daniel M Villarte Caucota',
            'email': 'davic77cv@gmail.com'
        }
        print(st)
        # return st

# Controlador
class UserController:
    def __init__(self, model):
        self.model = model

    def add_user(self, user_nombre, user_edad):
        self.model.add_user(user_nombre, user_edad)

    def edit_user(self, index, user_nombre, user_edad):
        self.model.edit_user(index, user_nombre, user_edad)

    def delete_user(self, index):
        self.model.delete_user(index)

    def promedio_edad(self):
        self.model.promedio_edad()

    def status(self):
        self.model.status()

# Vistas
app = Flask(__name__)

app = Flask(__name__, template_folder="views")

@app.route('/usuarios')
def index():
    return render_template('index.html', users=user_controller.model.users)
    # return user_controller.model.users

@app.route('/usuarios', methods=['POST'])
def add_user():
    # print(request.form['user_nombre'])
    user_nombre = request.form['user_nombre']
    user_edad = int(request.form['user_edad'])
    user_controller.add_user(user_nombre, user_edad)
    return redirect('/usuarios')

@app.route('/usuarios/edit/<int:index>', methods=['PUT'])
def edit_user(index):
    user_nombre = request.json['user_nombre']
    user_edad = int(request.json['user_edad'])
    user_controller.edit_user(index, user_nombre, user_edad)
    return redirect('/usuarios')

@app.route('/usuarios/delete/<int:index>', methods=['DELETE'])
def delete_user(index):
    user_controller.delete_user(index)
    return redirect('/usuarios')
  
@app.route('/usuarios/promedio-edad', methods=['GET'])
def promedio():
    prom = user_controller.promedio_edad()
    # print(prom)
    return redirect('/usuarios')

@app.route('/status', methods=['GET'])
def status():
    st = user_controller.status()
    # print(prom)
    return redirect('/usuarios')

user_model = UserModel()
user_controller = UserController(user_model)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)

