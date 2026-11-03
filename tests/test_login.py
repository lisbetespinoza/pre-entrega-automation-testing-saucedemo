from pages.login_page import LoginPage
import pytest
from utils.reader import read_users_csv
from utils.logger import logger


@pytest.mark.parametrize(
    "data", read_users_csv())
    
    #"usuario, password",
    #[
    #    ("standard_user", "secret_sauce"),
    #    ("admin", "1234"),
    #   ("jose", "123")
    #])

def test_login(driver,data): #iniciamos la prueba del login
    try:
        logger.info("Iniciando prueba de login") #texto
        login_page = LoginPage(driver)
        
        driver.get("https://www.saucedemo.com/")
        logger.info("Pagina abierta correctamente")
        
        login_page.login(data["usuario"],data["password"])
        logger.info("Ingreso de credenciales")
        
        if data["tipo_usuario"] == "True":
            assert "/inventory.html" in driver.current_url
            logger.info("Login exitoso")
        elif data["tipo_usuario"] == "False":
            error = login_page.obtener_mensaje_error()
            print(error)
            assert "Epic sadface" in error
            logger.info("Prueba de mensaje de error valida")
    except Exception: #captura una excepcion 
        logger.exception("Error durante la prueba de login")
        raise
        