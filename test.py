from helpers import *

site_data = [
        "JMA", "https://www.data.jma.go.jp/multi/quake/index.html?lang=en", 
        "quakeindex_table"
    ]

driver = get_page(site_data[1])
header = get_table_header(driver, site_data[2])
table = get_table_body(driver, site_data[2])
table.pop(0)

print(header)
for row in table: 
    print(get_data_from_row(row))