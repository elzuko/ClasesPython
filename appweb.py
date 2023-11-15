from flask import Flask,jsonify, request, redirect, url_for, render_template
import json
import conectar as db

app = Flask(__name__)

@app.route("/")
def index():
  
   cursor = db.conecta.cursor()
   cursor.execute("select codigo,nombre,descripcion from producto")
   resultado = cursor.fetchall()

   ##### LISTA esto es una Lista ¡¡¡¡
   insertobject=[]
   colunm_names = [desc[0] for desc in cursor.description]

   for registro in resultado:
      insertobject.append(dict(zip(colunm_names,registro)))

   cursor.close()


   return render_template("index.html", data = insertobject)


app.run(host='0.0.0.0', port= 3200)