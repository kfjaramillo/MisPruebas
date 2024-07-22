#convertir a unittest
import unittest
#importar librerías: webdriver(librería principal para controlar el navegador) y by (localización de elementos en la web ID, nombre, clase,..)
from selenium import webdriver
from selenium.webdriver.common.by import By

#heredar de unittest clase
class FindbyIdName(unittest.TestCase):
    # crear 2 funciones Python inicio y fin de pruebas
    # metodo de inicio de prueba. Usar driver de Selenium en navegador 
    # self es una variable 
    def setUp(self):

    #crear una nueva instancia del navegador Microsoft Edge
        self.driver = webdriver.Edge() 

    #navegar a una web
        self.driver.get("https://kfjaramillo.github.io/MisPruebas/")

#Agregar un método las validaciones realizadas 
    def testId(self):
#busca un elemento en la página, en este caso ID cuyo atributo sea noImportante
        elemento = self.driver.find_element(By.ID, "Importante")

        #verifica si el elemento fue encontrado
        if elemento is not None:
            print ("El elemento by ID fue encontrado")

    def testName(self):
        #busca el elemento cuyo atributo NAME sea ultimo 
        elemento2 = self.driver.find_element(By.CLASS_NAME, "rojo")

        #verifica si el elemento fue encontrado
        if elemento2 is not None:
            print ("El elemento by CLASS NAME fue encontrado")

    # Metodo para cerrar el driver 
    def tearDown(self):
        #cierra el navegador  
        self.driver.quit()
        
