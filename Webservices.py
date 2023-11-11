from flask import Flask, request,jsonify
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

# Decorador que permite ingresar datos manuales en la BD
# a traves de una url

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


# Insertar registros a traves de webservices
# utilizando metodos POST GET DELete 
# con un JSON

@app.route("/api/insertar_masivo/", methods = ['POST'])
def insertar_masivo():
 

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
    
    # Insertar el registro en la base de datos

    for item in data:
            # Insertar cada objeto JSON en la base de datos utilizando marcadores de posición (%s)
            cursor.execute("INSERT INTO producto (nombre, descripcion) VALUES (%s, %s)",
                           (item.get('nombre'), item.get('descripcion')))
            conecta.commit()
            
    cursor.execute("select codigo,nombre,descripcion from producto")
                   #where nombre = %s",(nombre,))
    resultado = cursor.fetchall()

    colunm_names = [desc[0] for desc in cursor.description]

    json_data = [dict(zip(colunm_names,row)) for row in resultado]

    return json.dumps(json_data, indent=2)

# Modificar registros a traves de webservices
# utilizando metodos POST GET DELete 
# con un JSON

@app.route("/api/MOdificar_registro/", methods = ['POST'])
def MOdificar_registro():
 

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
        
    for item in data:
         # Actualizar el registro en la base de datos utilizando marcadores de posición (%s)
         cursor.execute("UPDATE producto SET descripcion = %s WHERE nombre = %s",
                       (item.get('descripcion'), item.get('nombre')))
         conecta.commit()

    return jsonify({'mensaje': 'Registros actualizados exitosamente'})
  
  
app.run(host='0.0.0.0', port= 3200)
