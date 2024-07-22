#convertir a unittest
import unittest
#importar librerías: webdriver(librería principal para controlar el navegador) y by (localización de elementos en la web ID, nombre, clase,..)
from selenium import webdriver
from selenium.webdriver.common.by import By
# verificar la prueba en tiempo
import time
#heredar de unittest clase
class ClickAndSendKeys(unittest.TestCase):
    # crear 2 funciones Python inicio y fin de pruebas
    # metodo de inicio de prueba. Usar driver de Selenium en navegador 
    # self es una variable 
    def setUp(self):

    #crear una nueva instancia del navegador Microsoft Edge
        self.driver = webdriver.Edge() 

    #navegar a una web
        self.driver.get("https://kfjaramillo.github.io/PaginaPruebas/")

    #Agregar un método las validaciones realizadas 
    def testId(self):
        #busca un elemento en la página, en este caso la clase rojo
        liga = self.driver.find_element(By.XPATH , "//a[contains(text(),'Pagina 2')]")

        #verifica si el elemento fue encontrado y al dar click se va a la 2da pagina
        if liga is not None:
            liga.click()
        # encontrar por ID   
            nombre = self.driver.find_element(By.ID,"segundo")
   
        # validr si fue encontrado y escribir utilizando la funcion send_keys
        if nombre is not None:
            nombre.send_keys("Karina")
        #tiempo de espera
        time.sleep(5)  
    # Metodo para cerrar el driver 
    def tearDown(self):
        #cierra el navegador  
        self.driver.quit()
        
