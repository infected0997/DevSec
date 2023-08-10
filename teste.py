from selenium import webdriver

def teste_main():
    driver = webdriver.Chrome()

    driver.get("0.0.0.0")

    title = driver.title
    assert title == "OlaGabriel"

    driver.quit()
