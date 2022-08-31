from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from math import log, sin

def calc(x):
    return str(log(abs(12 * sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button_1 = browser.find_element(By.ID, "book")
    button_1.click()

    # Посчитали значение
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    print(x)
    y = calc(x)
    print(y)

    # Подставить значение y
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    answer.send_keys(y)

    # Нажать кнопку - "Выполнить"
    sub_button = browser.find_element(By.CSS_SELECTOR, "button#solve.btn.btn-primary")
    sub_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

