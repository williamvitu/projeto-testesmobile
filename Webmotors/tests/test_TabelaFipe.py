import time
import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

class TestTabelaFip(unittest.TestCase):


   def setUp(self):
       options = AppiumOptions()
       options.load_capabilities({
           "platformName": "Android",
           "appium:automationName": "uiautomator2"
       })
       self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
       btn_menu = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Menu")
       btn_menu.click()

       btn_tabelaFip = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tabela Fipe e Webmotors")
       btn_tabelaFip.click()

   def test_pesquisa_tabela_fip(self):
       driver = self.driver

       btn_marca = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="hands.android.webmotors:id/txtLineMain" and @text="Marca"]')
       btn_marca.click()

       time.sleep(1)
       btn_ecolher_marca = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                 value='new UiSelector().className("android.view.ViewGroup").instance(0)')
       btn_ecolher_marca.click()

       time.sleep(1)
       btn_ecolher_modelo = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("AGILE")')
       btn_ecolher_modelo.click()

       time.sleep(1)
       btn_ecolher_ano = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("2014")')
       btn_ecolher_ano.click()

       time.sleep(1)
       btn_ecolher_versao = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                 value='new UiSelector().text("1.4 MPFI EFFECT 8V FLEX 4P MANUAL")')
       btn_ecolher_versao.click()

       time.sleep(1)
       btn_ecolher_estado = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Alagoas (AL)")')
       btn_ecolher_estado.click()

       time.sleep(1)
       btn_avaliar = driver.find_element(by=AppiumBy.ID, value="hands.android.webmotors:id/btnEvaluate")
       btn_avaliar.click()

       time.sleep(1)
       btn_mostrar_ofertas = driver.find_element(by=AppiumBy.ID, value='hands.android.webmotors:id/btnShowOffers')
       self.assertTrue(btn_mostrar_ofertas.is_displayed())

   def test_limpar_pesquisa_tabela_fip(self):
       driver = self.driver

       time.sleep(1)
       btn_limpar = driver.find_element(by=AppiumBy.ID, value="hands.android.webmotors:id/btnClear")
       btn_limpar.click()

       time.sleep(1)
       btn_confirmar_limpeza = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
       btn_confirmar_limpeza.click()

       time.sleep(1)
       btn_avaliar = driver.find_element(by=AppiumBy.ID, value="hands.android.webmotors:id/btnEvaluate")
       self.assertTrue(btn_avaliar.is_displayed())

   def tearDown(self):
       self.driver.quit()


if __name__ == '__main__':
   unittest.main()