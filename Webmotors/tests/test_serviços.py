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
       btn_menu = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Serviços")
       btn_menu.click()

       btn_lavagem = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Lavagem")
       btn_lavagem.click()

       time.sleep(1)
       btn_higienizacao = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                              value='Higienização Interna\nLimpeza de estofado, carpete e piso.\nR$ 369,99\nR$ 199,99\n-46%')
       btn_higienizacao.click()

       time.sleep(1)
       btn_carro_pequeno = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                               value='Carro pequeno\nCarros categoria Compacto e Hatch popular\nR$ 199,99\nR$ 369,99')
       btn_carro_pequeno.click()

       time.sleep(1)
       btn_escolher_veiculo = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Escolher serviço")
       btn_escolher_veiculo.click()

   def test_adicionar_carro(self):
       driver = self.driver

       time.sleep(3)
       btn_adicionar_veiculo = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Adicionar veículo')
       btn_adicionar_veiculo.click()

       time.sleep(1)
       numero_placa = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
       numero_placa.click()
       numero_placa.send_keys("tes1234")

       time.sleep(1)
       btn_marca = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.view.View\").instance(8)")
       btn_marca.click()

       time.sleep(2)
       escolher_chevrolet = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="CHEVROLET")
       escolher_chevrolet.click()

       time.sleep(1)
       btn_modelo = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.view.View\").instance(9)")
       btn_modelo.click()

       time.sleep(1)
       escolher_modelo = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="A20")
       escolher_modelo.click()

       time.sleep(1)
       btn_ano = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.view.View\").instance(10)")
       btn_ano.click()

       time.sleep(1)
       btn_selecionar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Selecionar")
       btn_selecionar.click()

       time.sleep(1)
       btn_versao = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.view.View\").instance(11)")
       btn_versao.click()

       time.sleep(1)
       escolher_versao = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="4.1 CUSTOM DE LUXE CD 12V ÁLCOOL 4P MANUAL")
       escolher_versao.click()

       time.sleep(1)
       btn_salvar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Salvar")
       btn_salvar.click()

       time.sleep(2)
       resultado = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="1996 Chevrolet A20\nTES1234")
       self.assertTrue(resultado.is_displayed())

   def tearDown(self):
       self.driver.quit()


if __name__ == '__main__':
   unittest.main()