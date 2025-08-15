from helpers import *

def main(): 

    # Relevant information about JMA earthquake site
    site_data = [
        "JMA", "https://www.data.jma.go.jp/multi/quake/index.html?lang=en", 
        "quakeindex_table"
    ]

    # Get page from site data
    driver = get_page(site_data[1])

    # Parse information from site into readable format, and print them
    table = get_quake_table(driver, site_data[2])

    parser(table)

if __name__ == "__main__": 
    main() 