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
        self.driver.get("https://kfjaramillo.github.io/PaginaPruebas/")

#Agregar un método las validaciones realizadas 
    def testClase(self):
#busca un elemento en la página, en este caso la clase rojo
        elemento = self.driver.find_element(By.CLASS_NAME, "rojo")

    #verifica si el elemento fue encontrado
        if elemento is not None:
            print ("El elemento by CLASS NAME rojo fue encontrado")
    
    def testCeldas(self):
#busca elementos en la página, en este caso todas las celdas
        elementos = self.driver.find_elements(By.TAG_NAME, "td")

    #verifica si los elementos fueron encontrados
        if elementos is not None:
            print ("Las celdas fueron encontradas")
            # escribir cada celda
            for celdas in elementos:
                print (celdas.text)
            
    def testFilas(self):
        #busca el elemento cuyo atributo link parcial sea parte del link que buscas 
        elementos2 = self.driver.find_elements(By.XPATH, "//tr")

        #verifica si el elemento fue encontrado
        if elementos2 is not None:
            print ("Las filas fueron contabilizadas")
            # numero de elementos
            print (len(elementos2))
    # Metodo para cerrar el driver 
    def tearDown(self):
        #cierra el navegador  
        self.driver.quit()
        
