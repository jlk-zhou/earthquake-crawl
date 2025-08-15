from helpers import *

site_data = [
        "JMA", "https://www.data.jma.go.jp/multi/quake/index.html?lang=en", 
        "quakeindex_table"
    ]

driver = get_page(site_data[1])
table = get_quake_table(driver, site_data[2])
add_coordinates(table)