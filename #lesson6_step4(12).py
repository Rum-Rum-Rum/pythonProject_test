from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from math import log, sin

def calc(x):
    return str(log(abs(12 * sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать кнопку - "trollface"
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    button.click()

    windows = browser.window_handles
    current_window = browser.current_window_handle

    # Переходим на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Посчитали значение
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    print(x)
    y = calc(x)
    print(y)

    # Подставить значение y
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    answer.send_keys(y)

    # Нажать кнопку - "Выполнить"
    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    sub_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()