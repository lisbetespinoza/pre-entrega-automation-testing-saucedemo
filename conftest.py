import pytest
from selenium import webdriver

import pathlib
import base64
import pytest_html

@pytest.fixture #decorador
def driver():
    driver = webdriver.Chrome()
    
    driver.implicitly_wait(10)
    
    
    yield driver
    
    driver.quit()
    
    
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return { "x-api-key": "pub_a82b2e0ce28b8533b5a7385383c24f9132332ea961bcfdc8889403f4323dc664"
    }
    
@pytest.hookimpl(hookwrapper=True)  
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    
    
    if report.when == "call" and report.failed: #para hacer la captura de pantalla en call
        driver = item.funcargs.get("driver") #devuelve un diccionario
        
        carpeta = pathlib.Path("reports/screenshots")
        carpeta.mkdir(parents=True,exist_ok=True) #crear carpetas desde python
        archivo = carpeta / f"{item.name}.png"
        
        
        driver.save_screenshot(str(archivo)) #definimos el nombre y formato del archivo
        
        imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8") #codifica la imagen a html
        report.extras = [
            pytest_html.extras.png(imagen,name="Screenshot")
        ]
        
        
        
    
    
    