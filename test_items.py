from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_presence_of_add_to_basket_button(browser):

    browser.get(link)

    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    except TimeoutException:
        assert False, "There's no add to basket button on the page"
