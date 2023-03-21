from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test:

    def test1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(f"Test result: {errorMessage.text}")
        sleep(1000)

    def test2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(f"Test result: {errorMessage.text}")
        sleep(1000)

    def test3(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(f"Test result: {errorMessage.text}")
        sleep(1000)

    def test4(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(4)
        closeButton = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        closeButton.click()
        sleep(1000)

    def test5(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        listings = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"There are {len(listings)} items in list.")
        sleep(1000)



