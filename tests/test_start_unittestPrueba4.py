import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndSendKeys(unittest.TestCase):

    def setUp(self):
    
        self.driver = webdriver.Edge() 

        self.driver.get("https://kfjaramillo.github.io/MisPruebas")

    def testId(self):
        liga = self.driver.find_element(By.XPATH , "//a[contains(text(),'Pagina 2')]")

        if liga is not None:
            liga.click()


        nombre = self.driver.find_element(By.ID, "Segundo")

        if nombre is not None:
            nombre.send_keys("Karina")

        time.sleep(5)



            
    def tearDown(self):    
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
