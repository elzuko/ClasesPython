# Las principales librerias para hacer scrapear
import requests
from bs4 import BeautifulSoup

# URL del sitio web a scrapear
url = 'http://192.168.1.116:3000/'

url = 'https://www.bcv.org.ve/'

# Realizar la solicitud HTTP
#response = requests.get(url,verify=True)
response = requests.get(url, verify=False)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Obtener el título de la página
    #titulo = soup.title.text 
    precio = soup.find("H2")
    # Imprimir el título
    print(f'Título de la página: {precio}')

else:
    print(f'Error en la solicitud: {response.status_code}')