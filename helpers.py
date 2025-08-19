from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Quake:
    """Data structure for each earthquake occurrence. Includes the date of
    the earthquake, location, and magnitude."""

    def __init__(
        self, date=None, location=None, magnitude=None, longitude=None, latitude=None
    ):
        self.date = date
        self.location = location
        self.magnitude = magnitude
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return f"""Magnitude {self.magnitude} Earthquake at {self.location}, {self.date}, longitude {self.longitude}, latitude {self.latitude}"""


def get_page(url):
    """Returns a Selenium Chrome webdriver object given an url."""
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
    except WebDriverException:
        return None

    return driver


def get_table(driver, table_class, wait_rows):
    """Returns a list of rows or <tr> tags that contain the earthquake data.
    The first element of that list is the row of <th> headings of the table.
    Please also specify how many total table rows, header row included,
    you would like the driver to wait for loading using wait_rows."""
    wait = WebDriverWait(driver, 20)

    wait.until(
        lambda d: len(
            d.find_elements(By.XPATH, f"//table[@id='{table_class}']/tbody/tr")
        )
        >= wait_rows
        and len(d.find_elements(By.XPATH, f"//table[@id='{table_class}']/tbody/tr/th"))
        >= 5
    )

    rows = driver.find_elements(By.XPATH, f"//table[@id='{table_class}']/tbody/tr")
    return rows


def get_data_from_row(row):
    """Returns a list of headers or earthquake data, given one <tr> table row."""
    if row:
        cells = row.find_elements(By.XPATH, ".//td | .//th")
        if cells:
            for i in range(len(cells)):
                cells[i] = cells[i].text
        return cells


def get_link_from_row(row):
    """Returns the link in a row, given the row has one."""
    # TODO: What if a row doesn't have a link? Add defensive features.
    a = row.find_element(By.TAG_NAME, "a")
    return a.get_attribute("href")


def parser(site_data):
    """Parse the earthquake site given its site data."""
    driver = get_page(site_data[1])
    table = get_table(driver, site_data[2], 20)

    quakes = []

    for row in table[1:]:
        quake = Quake()
        basic_data = get_data_from_row(row)
        quake.date = basic_data[0]
        quake.location = basic_data[1]
        quake.magnitude = basic_data[2]

        link = get_link_from_row(row)
        detailed_page = get_page(link)
        detailed_table = get_table(detailed_page, site_data[2], 2)
        detailed_data = get_data_from_row(detailed_table[1])
        quake.latitude = detailed_data[1]
        quake.longitude = detailed_data[2]
        quakes.append(quake)
        print(quake)

    return quakes
