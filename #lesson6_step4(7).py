from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    print(x_element)
    y_element = x_element.get_attribute("valuex")
    print(y_element)
    z = calc(y_element)
    print(z)

# Подставить значение y
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer.send_keys(z)

# Чекбокс - поставить галочку
    che_button = browser.find_element(By.CSS_SELECTOR, "[type=checkbox]")
    che_button.click()
# Радиобатон - выбрать пункт "Роботырулят"
    rad_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rad_button.click()
# Нажать кнопку - "Выполнить"
    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default ")
    sub_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()