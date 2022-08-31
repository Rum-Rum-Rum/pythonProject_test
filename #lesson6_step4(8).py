#lesson6_step4.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Выбор 1-го числа
    x_1 = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap")
    x = x_1.text
    print(x)

# Выбор 2-го числа
    y_1 = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap")
    y = y_1.text
    print(y)

# Сумма xbctk
    xy = str(int(x) + int(y))
    print(xy)

# Отбор - подставка значения xy
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(xy) # ищем элемент с текстом "Python"

# Нажать кнопку - "Выполнить"
    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default ")
    sub_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

