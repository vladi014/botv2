
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ThreadCodere(threading.Thread):
    def __init__(self, cola1, cola2, cola5, cola6, username, password):
        threading.Thread.__init__(self)
        self.cola1 = cola1
        self.cola2 = cola2
        self.cola5 = cola5
        self.cola6 = cola6
        self.username = username
        self.password = password
        self.seguir = True

    def iniciar_sesion(self, driver):
        driver.get("https://www.codere.es/inicio")
        sleep(2)
        # Replace with the actual login procedure

    def run(self):
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        self.iniciar_sesion(driver)
        while self.seguir:
            try:
                # Add your logic here
                print("ThreadCodere running...")
                sleep(5)
            except Exception as e:
                print(f"Error in ThreadCodere: {e}")
                self.seguir = False
        driver.quit()
