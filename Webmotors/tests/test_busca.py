# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"appium:automationName": "UIAutomator2",
	"appium:platformName": "Android",
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
	"appium:appPackage": "hands.android.webmotors",  # Exemplo: Calculadora
	"appium:appActivity": ".Webmotors",
	"appium:udid": "RQCT302JFED",
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


def test_busca_carro():
	el3 = driver.find_element(by=AppiumBy.ID, value="hands.android.webmotors:id/et_search_view")
	el3.send_keys("honda fit")
	el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Honda Fit\")")
	el4.click()
	el5 = driver.find_element(by=AppiumBy.ID, value="hands.android.webmotors:id/tvTitle")
	el5.click()

	assert True


