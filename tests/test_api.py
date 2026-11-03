# x-api-key: pub_a82b2e0ce28b8533b5a7385383c24f9132332ea961bcfdc8889403f4323dc664

import requests

# GET
def test_obtener_usuario(base_url,headers):
    url = f"{base_url}/users/2"
    
    response = requests.get(url,headers=headers)
    
    # Validaciones
    # NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 200
    #print(codigo)
    
    # NIVEL 2: HEADERS
    #data = response.json()
    #print(data)
    assert "application/json" in response.headers["Content-Type"]
    
    # NIVEL 3: ESTRUCTURA
    data = response.json()
    
    assert isinstance(data,dict)  # Validar que el contenido sea un diccionario
    assert "data" in data
    assert isinstance(data["data"],dict)
    
    assert "id" in data ["data"]
    assert "email" in data ["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]
    
    
    # NIVEL 4: CONTENIDO
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    
    
    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2
    
    # POST
def test_crear_usuario(base_url,headers):
    url = f"{base_url}/users/"
         
    usuario = {
        "email": "jose.motezuma@bue.edu.ar",
        "first_name": "Jose",
        "last_name": "Motezuma",
        "job": "Instructor"
    }
    
    
    response = requests.post(url,headers=headers,json=usuario)
    
    #print(response.json())
    
    # NIVEL 1
    assert response.status_code == 201
    
    # NIVEL 2
    assert "application/json" in response.headers["Content-Type"]
    
    # NIVEL 3
    data = response.json()
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "id" in data
    
    # NIVEL 4
    assert data["email"] == usuario["email"]
    assert data["first_name"] == usuario["first_name"]
    
    # NIVEL 5
    assert response.elapsed.total_seconds() < 2
    
    
    # DELETE

def test_eliminar_usuario(base_url,headers):
    url = f"{base_url}/users/2"
        
    response = requests.delete(url,headers=headers)
        
        
    # NIVEL 1: STATUS CODE
    assert response.status_code == 204
        
    # NIVEL 2: HEADERS
    assert "Content-Type" not in response.headers
        
        
    # NIVEL 3: ESTRUCTURA Y CONTENIDO
    assert response.content == b""
    assert len (response.content) == 0  #otra forma de validar la cantidad de bytes
    
    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2
       
        
#test_obtener_usuario()


    