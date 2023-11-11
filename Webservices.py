from flask import Flask
import psycopg2
import json

app = Flask(__name__)

# crear metodo para realizar un crud
# cundo la sintaxis comineza con arroba se denomina DECORADORES
# permite modificar la caracteristica de un metodo, en este caso vamos a modificar la URL


@app.route("/api/consulta/<nombre>")
def consulta(nombre):
    #return "llamado de consulta"


# parametros de base de datos
    conexion = {
        'host': 'localhost',
        'port':'5432',
        'database' : 'python',
        'user': 'openpg',
        'password': 'openpgpwd'}

# probando conexion
    try:
        conecta = psycopg2.connect(**conexion)
        cursor = conecta.cursor()
        print ('conexion exitosa')
    except (Exception,psycopg2.Error ) as error:
         print('Ocurrio un error', error)

    cursor.execute("select codigo,nombre,descripcion from producto where nombre = %s",(nombre,))
    resultado = cursor.fetchall()

    colunm_names = [desc[0] for desc in cursor.description]

    json_data = [dict(zip(colunm_names,row)) for row in resultado]

    return json.dumps(json_data, indent=2)

@app.route("/api/agregar/<inombre>,<idescripcion>")
def agregar(inombre,idescripcion):
   

    # parametros de base de datos
    conexion = {
        'host': 'localhost',
        'port':'5432',
        'database' : 'python',
        'user': 'openpg',
        'password': 'openpgpwd'}

# probando conexion
    try:
        conecta = psycopg2.connect(**conexion)
        cursor = conecta.cursor()
        print ('conexion exitosa')
    except (Exception,psycopg2.Error ) as error:
         print('Ocurrio un error', error)


    cursor.execute("INSERT INTO producto (nombre,descripcion) VALUES (%s,%s)",(inombre,idescripcion))
    conecta.commit()

     
    cursor.execute("select codigo,nombre,descripcion from producto where nombre = %s",(inombre,))
    resultado = cursor.fetchall()

    colunm_names = [desc[0] for desc in cursor.description]

    json_data = [dict(zip(colunm_names,row)) for row in resultado]

    return json.dumps(json_data, indent=2)





app.run(host='0.0.0.0', port= 3000)
