from helpers import *


def main():

    # Relevant information about JMA earthquake site
    site_data = [
        "JMA",
        "https://www.data.jma.go.jp/multi/quake/index.html?lang=en",
        "quakeindex_table",
    ]

    parser(site_data)


if __name__ == "__main__":
    main()
