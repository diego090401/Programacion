from  selenium import webdriver
from pyunitreport import HTMLTestRunner
import unittest
from selenium import webdriver

class Prueba(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r"C:/Users/User/Desktop/chromedriver_win32/chromedriver.exe")
        driver =cls.driver
        driver.get("https://blerning.colegiosaintjohn.com/index.php")
       
        
    
    def test_find_field (self):
        driver = self.driver
        search_field = self.driver.find_element_by_id("login")
    
    @classmethod
    def tearDown(cls):
        driver =cls.driver
        driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))