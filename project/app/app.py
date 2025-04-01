from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host='db',      # Nombre del servicio en docker-compose
        user='root',
        password='rootpassword',
        database='users_db'
    )
    return connection

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar las credenciales en la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return render_template('welcome.html', name=user[1])  # user[1] es el nombre
        else:
            return render_template('index.html', error="Credenciales incorrectas.")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
