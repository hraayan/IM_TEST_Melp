# Test para Intelimetrica, caso MELP  . Api Python, Heroku deployment

--update HerokuApp Out of Deploying Service

#
Links:

API Documentation : https://melp-hbaez.herokuapp.com/docs

Postman Collection: 

##

## Funcionamiento en entorno Local:

1. Se requiere crear un entorno virtual de python: (linux) `python3 -m venv nombre-entorno`
2. Activar el entorno virtual : `source nombre-entorno/bin/activate`
3. Instalar los paquetes necesarios expresados en el archivo ***requirements.txt*** : 

  `pip3 install -r requirements.txt`
  
  4. Correr la app con el comando: `uvicorn main:app --reload`
