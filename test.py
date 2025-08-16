from helpers import *

site_data = [
        "JMA", "https://www.data.jma.go.jp/multi/quake/index.html?lang=en", 
        "quakeindex_table"
    ]

driver = get_page(site_data[1])
table = get_table(driver, site_data[2], 30)
for row in table: 
    print(get_data_from_row(row))

for row in table[1:]: 
    link = get_link_from_row(row)
    detail_page = get_page(link)
    detail_table = get_table(detail_page, site_data[2], 2)

    for data in detail_table: 
        print(get_data_from_row(data))