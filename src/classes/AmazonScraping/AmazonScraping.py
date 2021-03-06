import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook


class AmazonScraping:
    def __init__(self, term):
        self.term = term
        self.url = "https://www.amazon.com.br/"
        self.products = []

    def search(self):
        option = Options()
        #option.headless = True
        driver = webdriver.Chrome(options=option)

        driver.get(self.url)
        driver.implicitly_wait(5)

        search_input = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')

        search_input.send_keys(self.term)
        search_input.send_keys(Keys.ENTER)

        driver.implicitly_wait(10)

        search_results_div = driver.find_element_by_xpath('//*[@class="s-main-slot s-result-list s-search-results sg-row"]')


        html_content = search_results_div.get_attribute('outerHTML')

        soup = BeautifulSoup(html_content, 'html.parser')
        productsElements = soup.findAll('div', {
            "class": "sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item s-asin sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"
        })

        return productsElements

    def extract_data(self, products_elements):
        for product in products_elements:
            name = product.find('span', { "class": "a-size-base-plus a-color-base a-text-normal" })
            price = product.find('span', { "class": "a-offscreen" })

            if(type(name) != Tag):
                name = Tag(name=str(name))

            if(type(price) != Tag):
                price = Tag(name=str(price))

            self.products.append({
                "name": name.getText(),
                "price": price.getText()
            })

    def save(self):
        excel_file = Workbook()
        spreadsheet = excel_file.active

        spreadsheet.title = "Amazon results"

        spreadsheet["A1"] = "Nome do Produto"
        spreadsheet["B1"] = "Preço"

        for product in self.products:
            data = (product["name"], product["price"])
            spreadsheet.append(data)

        excel_file.save(f"{self.term}_results.xlsx")

    def run(self):
        print(f"Searching {self.term } on amazon's site ...")
        results = self.search()

        print("Extracting data from search results ...")
        self.extract_data(results)

        print("Saving extracted information on Excel file ...")
        self.save()

        print("File saved")