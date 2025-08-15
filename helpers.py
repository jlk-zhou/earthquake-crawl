from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Quake: 
    '''Data structure for each earthquake occurrence. Includes the date of
    the earthquake, location, and magnitude. '''
    def __init__(self, date, location, magnitude):
        self.date = date
        self.location = location
        self.magnitude = magnitude

    def __str__(self): 
        return f"Magnitude {self.magnitude} Earthquake at {self.location}, {self.date}"


def get_page(url): 
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    try: 
        driver.get(url)
    except WebDriverException: 
        return None
    
    return driver


def get_quake_table(driver, table_class): 
    wait = WebDriverWait(driver, 20)
    wait.until(lambda driver: 
               len(driver.find_elements(
                   By.XPATH, f"//table[@id='{table_class}']/tbody/tr")) >= 10)
    rows = driver.find_elements(By.XPATH, f"//table[@id='{table_class}']/tbody/tr")
    return rows


def add_coordinates(rows, table_class): 
    for row in rows: 
        cells = row.find_elements(By.TAG_NAME, "td")
        if cells: 
            detail_url = cells[0].find_element(By.TAG_NAME, "a").get_attribute("href")
            detail_page = get_page(detail_url)
            detail_table = get_quake_table(detail_page, table_class)
            if detail_table: 
                latitude = detail_table[1]
    

def parser(rows): 
    quakes = []
    for row in rows: 
        cells = row.find_elements(By.TAG_NAME, "td")
        if cells: 
            quake = Quake(
                cells[0].find_element(By.TAG_NAME, "a").text, 
                cells[1].text, 
                cells[2].text
            )
            quakes.append(quake)

    for quake in quakes: 
        print(quake)

