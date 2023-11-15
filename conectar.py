import psycopg2

# parametros de base de datos
conexion = {
    'host': 'localhost',
    'port':'5432',
    'database' : 'python',
    'user': 'openpg',
    'password': 'openpgpwd'
}

# probando conexion
conecta = psycopg2.connect(**conexion)