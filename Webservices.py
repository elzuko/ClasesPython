from flask import Flask, request
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


# Insertar registros a treves de webservices
# utilizando metodos POST GET DELete 
# con un JSON

@app.route("/api/insertar/", methods = ['POST'])
def insertar():
 

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
    
    data = request.get_json()
    

    print(data)
    #inombre = 
    #idescripcion =

    # Insertar el registro en la base de datos
   #cursor.execute("INSERT INTO producto (nombre, descripcion) VALUES (?,?)", (data.get('nombre'), data.get('descripcion')))

    for item in data:
            # Insertar cada objeto JSON en la base de datos utilizando marcadores de posición (%s)
            cursor.execute("INSERT INTO producto (nombre, descripcion) VALUES (%s, %s)",
                           (item.get('nombre'), item.get('descripcion')))

    #cursor.execute("INSERT INTO producto (nombre,descripcion) VALUES (%s,%s)",(inombre,idescripcion))
    conecta.commit()

      # Consultar un nombre desde la base de datos (ajusta la consulta según tu necesidad)
    cursor.execute("select codigo,nombre,descripcion from producto WHERE nombre = %s", (item.nombre,))
    resultado = cursor.fetchone()[0]

    #cursor.execute("select codigo,nombre,descripcion from producto")
                   #where nombre = %s",(nombre,))
    #resultado = cursor.fetchall()

    colunm_names = [desc[0] for desc in cursor.description]

    json_data = [dict(zip(colunm_names,row)) for row in resultado]

    return json.dumps(json_data, indent=2)



app.run(host='0.0.0.0', port= 3000)
