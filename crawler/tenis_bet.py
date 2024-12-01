
import threading
import queue
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
from time import sleep

class ThreadBet(threading.Thread):
    def __init__(self, cola1, cola2, username, password):
        threading.Thread.__init__(self)
        self.cola1 = cola1
        self.cola2 = cola2
        self.username = username
        self.password = password
        self.seguir = True

    def iniciar_sesion(self, driver):
        # Example login implementation
        driver.get("https://www.bet365.es")
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
                print("ThreadBet running...")
                sleep(5)
            except Exception as e:
                print(f"Error in ThreadBet: {e}")
                self.seguir = False
        driver.quit()
