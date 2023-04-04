# Generated by Selenium IDE
import pytest
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import date
from Constants import globalConstants
from pathlib import Path
from datetime import date

class TestAddtocart():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.maximize_window()
    self.driver.get(globalConstants.URL)
    self.folderPath = str(date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_offer(self):
    username = self.driver.find_element(By.CSS_SELECTOR, globalConstants.userName)
    username.click()
    username.send_keys("standard_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, globalConstants.password)))
    password = self.driver.find_element(By.CSS_SELECTOR, globalConstants.password)
    password.send_keys("secret_sauce")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, globalConstants.loginButton)))
    self.driver.find_element(By.CSS_SELECTOR, globalConstants.loginButton).click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "1")))
    self.driver.find_element(By.LINK_TEXT, "1").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"checkout\"]")))
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_item_name")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"firstName\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("asd")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("asd")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("123")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"continue\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"finish\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
    self.driver.save_screenshot(self.folderPath + "/offer.png")
    assert self.driver.find_element(By.CSS_SELECTOR, ".complete-header").text == "Thank you for your order!"
  