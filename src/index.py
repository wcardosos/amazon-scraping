from classes.AmazonScraping.AmazonScraping import AmazonScraping

scrap = AmazonScraping()

results = scrap.getProducts("iphone")

for product in results:
    print(product)