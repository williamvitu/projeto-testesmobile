import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
import time
import logging



class TestBuscaWebmotors():

	capabilities = {
		"appium:automationName": "UIAutomator2",
		"appium:platformName": "Android",
		"appium:newCommandTimeout": 3600,
	}

	url = "http://127.0.0.1:4723"
	options = AppiumOptions()
	options.load_capabilities(capabilities)

	driver = webdriver.Remote(url, options=options)
	driver.implicitly_wait(10)

	button_filter = "hands.android.webmotors:id/iv_filter"
	button_filters = "hands.android.webmotors:id/btn_filter"
	button_tab_search= "hands.android.webmotors:id/navigation_search"
	button_accept_location_app = "hands.android.webmotors:id/btOkPermission"
	button_accept_location_permission = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"

	input_search_car = "hands.android.webmotors:id/et_search_view"


	def test_buscar_por_carro_no_campo_de_texto(self):

		# Seleciona o botão 'Buscar'
		self.driver.find_element(by=AppiumBy.ID, value=self.button_tab_search).click()
		time.sleep(5)
		# Digita o nome/modelo do carro no campo de busca
		self.driver.find_element(by=AppiumBy.ID, value=self.input_search_car).send_keys("honda fit")
		time.sleep(5)
		# Clica no elemento de destaque de Busca
		self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Honda Fit\")").click()
		time.sleep(2)

		try :
			# Verifica se aparece pop-up de localizacao
			if self.driver.find_element(by=AppiumBy.ID, value=self.button_accept_location_app).is_displayed():
				# Clica para permitir a localizacao
				self.driver.find_element(by=AppiumBy.ID, value=self.button_accept_location_app).click()

				# Verifica se aparece o pop-up de permissao de localizacao do android
				if self.driver.find_element(by=AppiumBy.ID, value=self.button_accept_location_permission).is_displayed():
					# Clica para permitir que o aplicativo utilize a localizacao
					self.driver.find_element(by=AppiumBy.ID,value=self.button_accept_location_permission).click()
		except NoSuchElementException as e:
			logging.info(e)
		# Clica no botao de filtros
		self.driver.find_element(by=AppiumBy.ID, value=self.button_filter).click()
		time.sleep(2)

		# Valida se os valores dos campos de Marca/Modelo batem com o que foi pesquisado pelo campo de busca
		assert self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"HONDA\")").is_displayed() and self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"FIT\")").is_displayed()

	# @pytest.mark.parametrize("")
	def test_busca_rapida(self):
		# Seleciona o botão 'Buscar'
		self.driver.find_element(by=AppiumBy.ID, value=self.button_tab_search).click()
		time.sleep(2)
		# Seleciona uma busca de marca rapida
		self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"CHEVROLET\")").click()
		time.sleep(5)
		# Clica no botao de filtro
		self.driver.find_element(by=AppiumBy.ID, value=self.button_filter).click()

		# Valida se a marca selecionada nos filtros é a mesma que foi selecionada na busca rapida
		assert self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"CHEVROLET\")").is_displayed()