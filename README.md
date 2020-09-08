# Amazon Scraping

Web crawler que raspa dados do site da Amazon e salva em uma planilha Excel.

## Atributos

* **term**: nome do produto que deve ser pesquisado

* **url**: endereço do site da Amazon Brasil

* **products**: lista de dicionários que contêm o nome e o preço de cada produto retornado pela pesquisa

## Métodos

### **init(term)**

Método constrututor que recebe como parâmetro o termo que servirá como base para a busca no site

### **search()**

Método que pesquisa o termo dado no site e retorna uma lista com os elementos da seção de resultados do site

### **extract_data(products_elements)**

Método que recebe como parâmetro a lista de elementos HTML retornados do método **search** e extrai os dados de nome e preço de cada produto para o atributo **products**

### **save()**

Método que salva os resultados da pesquisa em um arquivo **.xlsx**

## Funcionamento

Seu funcionamento é simples: execute como um arquivo Python normalmente, com a adição do termo de pesquisa após o script principal.

```bash
python index.py term
```

Após a execução do script, será salvo um arquivo **.xlsx** no diretório atual


### Script criado para fins educativos por Wagner Cardoso