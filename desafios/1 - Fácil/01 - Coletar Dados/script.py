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

    def iniciar(self) -> None:
        # Seu script aqui.
        WebDriverWait(self.navegador, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "category-link"))
        )

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

        for produto in produtos:
                # Coleta os dados do produto
                nome = produto.find_element(By.XPATH, ".//a[@title]").get_attribute("title").strip()
                preco = produto.find_element(By.CLASS_NAME, "price").text
                descricao = produto.find_element(By.CLASS_NAME, "description").text
                estrelas = produto.find_element(By.XPATH, ".//div[@class='ratings']//p[@data-rating]").get_attribute("data-rating")
                reviews = produto.find_element(By.XPATH, ".//p[@class='review-count float-end']").text.strip()

                # Adiciona o produto com seus dados na lista
                dados_laptops.append({
                    "Nome": nome,
                    "Preco": preco,
                    "Descricao": descricao,
                    "Estrelas": estrelas,
                    "Reviews": reviews
                })

        # Converte para um DataFrame
        df_laptops = pd.DataFrame(dados_laptops)

        # Converte as colunas para os dados apropriados
        df_laptops['Preco'] = df_laptops['Preco'].replace(r'[\$,]', '', regex=True).astype(float)
        df_laptops['Reviews'] = df_laptops['Reviews'].replace(' reviews', '', regex=True).astype(int)
        df_laptops['Estrelas'] = df_laptops['Estrelas'].astype(int)

        # Ordena por preço
        laptops_por_preco = df_laptops.sort_values(by='Preco', ascending=True)

        # Ordena por quantidade de reviews
        laptops_por_reviews = df_laptops.sort_values(by='Reviews', ascending=False)

        # Ordena por quantidade de estrelas
        laptops_por_estrelas = df_laptops.sort_values(by='Estrelas', ascending=False)

        # Ordena por menor preço, maior quantidade de reviews e maior quantidade de estrelas
        laptops_bonus = df_laptops.sort_values(by=['Preco', 'Reviews', 'Estrelas'], ascending=[True, False, False])

        # Cria um ExcelWriter para salvar um Excel com 4 abas
        with pd.ExcelWriter('laptops.xlsx') as writer:
            laptops_por_preco.to_excel(writer, sheet_name='Por Preço', index=False)
            laptops_por_reviews.to_excel(writer, sheet_name='Por Reviews', index=False)
            laptops_por_estrelas.to_excel(writer, sheet_name='Por Estrelas', index=False)
            laptops_bonus.to_excel(writer, sheet_name='Bonus', index=False)

        # Tablets
        aba_tablets = self.navegador.find_element(By.XPATH, "//a[@href='/test-sites/e-commerce/allinone/computers/tablets']")
        aba_tablets.click()

        # Aguarde os produtos da categoria carregarem
        WebDriverWait(self.navegador, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "thumbnail")))

        # Encontre todos os produtos na página
        produtos = self.navegador.find_elements(By.CLASS_NAME, "thumbnail")

        # Lista para tablets
        dados_tablets = []

        for produto in produtos:
            # Coleta os dados do produto
            nome = produto.find_element(By.XPATH, ".//a[@title]").get_attribute("title").strip()
            preco = produto.find_element(By.CLASS_NAME, "price").text
            descricao = produto.find_element(By.CLASS_NAME, "description").text
            estrelas = produto.find_element(By.XPATH, ".//div[@class='ratings']//p[@data-rating]").get_attribute("data-rating")
            reviews = produto.find_element(By.XPATH, ".//p[@class='review-count float-end']").text.strip()

            # Adiciona o produto com seus dados na lista
            dados_tablets.append({
                "Nome": nome,
                "Preco": preco,
                "Descricao": descricao,
                "Estrelas": estrelas,
                "Reviews": reviews
            })

        # Converte para um DataFrame
        df_tablets = pd.DataFrame(dados_tablets)

        # Converte as colunas para os dados apropriados
        df_tablets['Preco'] = df_tablets['Preco'].replace(r'[\$,]', '', regex=True).astype(float)
        df_tablets['Reviews'] = df_tablets['Reviews'].replace(' reviews', '', regex=True).astype(int)
        df_tablets['Estrelas'] = df_tablets['Estrelas'].astype(int)

        # Ordena por preço
        tablets_por_preco = df_tablets.sort_values(by='Preco', ascending=True)

        # Ordena por quantidade de reviews
        tablets_por_reviews = df_tablets.sort_values(by='Reviews', ascending=False)

        # Ordena por quantidade de estrelas
        tablets_por_estrelas = df_tablets.sort_values(by='Estrelas', ascending=False)

        # Ordena por menor preço, maior quantidade de reviews e maior quantidade de estrelas
        tablets_bonus = df_tablets.sort_values(by=['Preco', 'Reviews', 'Estrelas'], ascending=[True, False, False])

        # Cria um ExcelWriter para salvar um Excel com 4 abas
        with pd.ExcelWriter('tablets.xlsx') as writer:
            tablets_por_preco.to_excel(writer, sheet_name='Por Preço', index=False)
            tablets_por_reviews.to_excel(writer, sheet_name='Por Reviews', index=False)
            tablets_por_estrelas.to_excel(writer, sheet_name='Por Estrelas', index=False)
            tablets_bonus.to_excel(writer, sheet_name='Bonus', index=False)


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

        for produto in produtos:
            # Coleta os dados do produto
            nome = produto.find_element(By.XPATH, ".//a[@title]").get_attribute("title").strip()
            preco = produto.find_element(By.CLASS_NAME, "price").text
            descricao = produto.find_element(By.CLASS_NAME, "description").text
            estrelas = produto.find_element(By.XPATH, ".//div[@class='ratings']//p[@data-rating]").get_attribute("data-rating")
            reviews = produto.find_element(By.XPATH, ".//p[@class='review-count float-end']").text.strip()

            # Adiciona o produto com seus dados na lista
            dados_phones.append({
                "Nome": nome,
                "Preco": preco,
                "Descricao": descricao,
                "Estrelas": estrelas,
                "Reviews": reviews
            })

        # Converte para um DataFrame
        df_phones = pd.DataFrame(dados_phones)

        # Converte as colunas para os dados apropriados
        df_phones['Preco'] = df_phones['Preco'].replace(r'[\$,]', '', regex=True).astype(float)
        df_phones['Reviews'] = df_phones['Reviews'].replace(' reviews', '', regex=True).astype(int)
        df_phones['Estrelas'] = df_phones['Estrelas'].astype(int)

        # Ordena por preço
        phones_por_preco = df_phones.sort_values(by='Preco', ascending=True)

        # Ordena por quantidade de reviews
        phones_por_reviews = df_phones.sort_values(by='Reviews', ascending=False)

        # Ordena por quantidade de estrelas
        phones_por_estrelas = df_phones.sort_values(by='Estrelas', ascending=False)

        # Ordena por menor preço, maior quantidade de reviews e maior quantidade de estrelas
        phones_bonus = df_phones.sort_values(by=['Preco', 'Reviews', 'Estrelas'], ascending=[True, False, False])

        # Cria um ExcelWriter para salvar um Excel com 4 abas
        with pd.ExcelWriter('phones.xlsx') as writer:
            phones_por_preco.to_excel(writer, sheet_name='Por Preço', index=False)
            phones_por_reviews.to_excel(writer, sheet_name='Por Reviews', index=False)
            phones_por_estrelas.to_excel(writer, sheet_name='Por Estrelas', index=False)
            phones_bonus.to_excel(writer, sheet_name='Bonus', index=False)

        # Fecha o navegador
        self.navegador.close()
        input()


if __name__ == '__main__':
    Desafio01().iniciar()

