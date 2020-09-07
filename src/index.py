import sys
from classes.AmazonScraping.AmazonScraping import AmazonScraping


try:
    search_term = sys.argv[1]
except IndexError:
    print("Search term was not provided")
    sys.exit()


scrap = AmazonScraping(search_term)

scrap.run()