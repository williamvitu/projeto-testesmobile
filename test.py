from appium import webdriver
from appium.options.common import AppiumOptions

desired_caps = {
    "platformName": "Android",
    "deviceName": "device",
    "udid": "RQCT302JFED",  # Opcional se houver apenas 1 dispositivo
    "appPackage":  "com.sec.android.app.popupcalculator",  # Exemplo: Calculadora
    "appActivity": ".Calculator",
    "automationName": "UiAutomator2"
}

url =  "http://192.168.1.71:4723"
driver = webdriver.Remote(url,
    options=AppiumOptions().load_capabilities(desired_caps), keep_alive=True)


print("Aplicativo iniciado!")
