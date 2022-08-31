from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    print(y)

# Подставить значение y
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer.send_keys(y)

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