# Test para Intelimetrica, caso MELP  
## Api Python, Heroku deployment


Links:

Heroku App: https://im-test-baez.herokuapp.com/

API Documentation : 
 1. [ReDoc:](https://im-test-baez.herokuapp.com/redoc) 
 2. [Swagger:](https://im-test-baez.herokuapp.com/docs)

Postman Collection: 
  1. [Postman Collection](https://www.postman.com/science-astronaut-80467714/workspace/im-test-baez/collection/20549891-c8d89fe8-1138-4766-9c39-ce322cd4835d?action=share&creator=20549891)

##

## Funcionamiento en entorno Local:

1. Se requiere crear un entorno virtual de python: (linux) `python3 -m venv nombre-entorno`
2. Activar el entorno virtual : `source nombre-entorno/bin/activate`
3. Instalar los paquetes necesarios expresados en el archivo ***requirements.txt*** : 

  `pip3 install -r requirements.txt`
  
  4. Correr la app con el comando: `uvicorn src.main:app --reload`
