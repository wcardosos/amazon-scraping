from classes.AmazonScraping.AmazonScraping import AmazonScraping

scrap = AmazonScraping()

results = scrap.getProducts("iphone")

scrap.save()