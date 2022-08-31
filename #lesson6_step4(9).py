from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Посчитали значение
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    print(x)
    y = calc(x)
    print(y)

# Прокрутили до кнопки
    # browser.execute_script("window.scrollBy(0, 100);")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

# Подставить значение y
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    answer.send_keys(y)

# Чекбокс - поставить галочку
    che_button = browser.find_element(By.CSS_SELECTOR, "[type=checkbox]")
    che_button.click()
# Радиобатон - выбрать пункт "Роботырулят"
    rad_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rad_button.click()
# Нажать кнопку - "Выполнить"
    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    sub_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()