from config.config import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class Desafio01:

    def __init__(self) -> None:
        self.navegador = Driver().driver
        self.navegador.get('https://webscraper.io/test-sites/e-commerce/allinone')
        self.navegador.maximize_window()

    # Função para salvar os produtos em uma lista
    def salva_produtos(self, dados_produtos):
        # Encontre todos os produtos na página
        produtos = self.navegador.find_elements(By.CLASS_NAME, "thumbnail")

        for produto in produtos:
            # Coleta os dados do produto
            nome = produto.find_element(By.XPATH, ".//a[@title]").get_attribute("title").strip()
            preco = produto.find_element(By.CLASS_NAME, "price").text
            descricao = produto.find_element(By.CLASS_NAME, "description").text
            estrelas = produto.find_element(By.XPATH, ".//div[@class='ratings']//p[@data-rating]").get_attribute(
                "data-rating")
            reviews = produto.find_element(By.XPATH, ".//p[@class='review-count float-end']").text.strip()

            # Adiciona o produto com seus dados na lista
            dados_produtos.append({
                "Nome": nome,
                "Preco": preco,
                "Descricao": descricao,
                "Estrelas": estrelas,
                "Reviews": reviews
            })

        return dados_produtos

    # Função para converter colunas para os dados apropriados
    def converte_colunas(self, df):
        # Converte as colunas para os dados apropriados
        df['Preco'] = df['Preco'].replace(r'[\$,]', '', regex=True).astype(float)
        df['Reviews'] = df['Reviews'].replace(' reviews', '', regex=True).astype(int)
        df['Estrelas'] = df['Estrelas'].astype(int)

        return df

    # Função para ordenar os produtos
    def ordena_produtos(self, df):
        # Ordena por preço (Menor - Maior)
        por_preco = df.sort_values(by='Preco', ascending=True)

        # Ordena por quantidade de reviews (Maior - Menor)
        por_reviews = df.sort_values(by='Reviews', ascending=False)

        # Ordena por quantidade de estrelas (Maior - Menor)
        por_estrelas = df.sort_values(by='Estrelas', ascending=False)

        # Ordena por menor preço, maior quantidade de reviews e maior quantidade de estrelas
        bonus = df.sort_values(by=['Preco', 'Reviews', 'Estrelas'], ascending=[True, False, False])

        return por_preco, por_reviews, por_estrelas, bonus

    # Função para salvar o DataFrame em Excel com 4 planilhas
    def salva_para_excel(self, produtos_ordenados, nome_arquivo='produtos.xlsx'):
        # Cria um ExcelWriter para salvar um Excel com 4 planilhas
        with pd.ExcelWriter(nome_arquivo) as writer:
            produtos_ordenados[0].to_excel(writer, sheet_name='Por Preço', index=False)
            produtos_ordenados[1].to_excel(writer, sheet_name='Por Reviews', index=False)
            produtos_ordenados[2].to_excel(writer, sheet_name='Por Estrelas', index=False)
            produtos_ordenados[3].to_excel(writer, sheet_name='Bonus', index=False)

    def iniciar(self) -> None:
        # Seu script aqui.
        # Aguarda 10 segundos
        WebDriverWait(self.navegador, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "category-link")))

        # Clique no link da categoria
        # Computers
        aba_computers = self.navegador.find_element(By.XPATH, "//a[@href='/test-sites/e-commerce/allinone/computers']")
        aba_computers.click()

        # Laptops
        aba_laptops = self.navegador.find_element(By.XPATH, "//a[@href='/test-sites/e-commerce/allinone/computers/laptops']")
        aba_laptops.click()

        # Aguarde os produtos da categoria carregarem
        WebDriverWait(self.navegador, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "thumbnail")))

        # Encontre todos os produtos na página
        produtos = self.navegador.find_elements(By.CLASS_NAME, "thumbnail")

        # Lista para laptops
        dados_laptops = []

        # Chama a função salva_produtos para salvar os dados na lista
        self.salva_produtos(dados_laptops)

        # Converte para um DataFrame
        df_laptops = pd.DataFrame(dados_laptops)

        # Chama as funções para converter as colunas, ordenar e salvar em Excel
        df_laptops = self.converte_colunas(df_laptops)
        laptops_ordenados = self.ordena_produtos(df_laptops)
        self.salva_para_excel(laptops_ordenados, nome_arquivo='laptops.xlsx')

        # Tablets
        aba_tablets = self.navegador.find_element(By.XPATH, "//a[@href='/test-sites/e-commerce/allinone/computers/tablets']")
        aba_tablets.click()

        # Aguarde os produtos da categoria carregarem
        WebDriverWait(self.navegador, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "thumbnail")))

        # Encontre todos os produtos na página
        produtos = self.navegador.find_elements(By.CLASS_NAME, "thumbnail")

        # Lista para tablets
        dados_tablets = []

        # Chama a função salva_produtos para salvar os dados na lista
        self.salva_produtos(dados_tablets)

        # Converte para um DataFrame
        df_tablets = pd.DataFrame(dados_tablets)

        # Chama as funções para converter as colunas, ordenar e salvar em Excel
        df_tablets = self.converte_colunas(df_tablets)
        tablets_ordenados = self.ordena_produtos(df_tablets)
        self.salva_para_excel(tablets_ordenados, nome_arquivo='tablets.xlsx')


        # Clique no link da categoria
        # Phones
        aba_phones = self.navegador.find_element(By.XPATH, "//a[@href='/test-sites/e-commerce/allinone/phones']")
        aba_phones.click()

        # Touch
        aba_touch = self.navegador.find_element(By.XPATH, "//a[@href='/test-sites/e-commerce/allinone/phones/touch']")
        aba_touch.click()

        # Aguarde os produtos da categoria carregarem
        WebDriverWait(self.navegador, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "thumbnail")))

        # Encontre todos os produtos na página
        produtos = self.navegador.find_elements(By.CLASS_NAME, "thumbnail")

        # Lista para phones
        dados_phones = []

        # Chama a função salva_produtos para salvar os dados na lista
        self.salva_produtos(dados_phones)

        # Converte para um DataFrame
        df_phones = pd.DataFrame(dados_phones)

        # Chama as funções para converter as colunas, ordenar e salvar em Excel
        df_phones = self.converte_colunas(df_phones)
        phones_ordenados = self.ordena_produtos(df_phones)
        self.salva_para_excel(phones_ordenados, nome_arquivo='phones.xlsx')

        # Fecha o navegador
        self.navegador.quit()
        input()


if __name__ == '__main__':
    Desafio01().iniciar()

