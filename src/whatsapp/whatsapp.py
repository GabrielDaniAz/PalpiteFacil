from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib
import time

class Whatsapp:
    def __init__(self):
        self.url = 'https://web.whatsapp.com'
        self.id_elemento = 'side' # Id fixo do web Whatsapp para verificar se a tela carregou
        self.xpath_botao_enviar = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'


    """
    Parâmetro lista de dicionários dos jogos:
    Exemplo:
    [{'Time_Casa': 'Botafogo', 'Gols_Casa': '3', 'Gols_Visitante': '1', 'Time_Visitante': 'Internacional', 
    'Rodada': '19', 'Dia_Semana': 'SÁB', 'Dia_Mes': '12/08/2023', 
    'Estadio': 'NILTON SANTOS (ENGENHÃO)', 'Horario': '21:00'}, 

    {'Time_Casa': 'Atlético-MG', 'Gols_Casa': '1', 'Gols_Visitante': '0', 'Time_Visitante': 'Bahia', 
    'Rodada': '19', 'Dia_Semana': 'DOM', 'Dia_Mes': '13/08/2023', 
    'Estadio': 'MINEIRÃO', 'Horario': '11:00'}, 

    {'Time_Casa': 'Corinthians', 'Gols_Casa': None, 'Gols_Visitante': None, 'Time_Visitante': 'Coritiba', 
    'Rodada': '19', 'Dia_Semana': 'DOM', 'Dia_Mes': '13/08/2023', 
    'Estadio': 'NEO QUÍMICA ARENA', 'Horario': '16:00'}, ...]

    Método para enviar mensagem no Whatsapp para os usuários
    """
    def enviar_mensagem(self, lista_dicionarios_jogos):
        texto = urllib.parse.quote(self._formatar_mensagem(lista_dicionarios_jogos))
        telefone = '+5532991544543'
        # telefone = '+5532988637204'
        link = f'{self.url}/send?phone={telefone}&text={texto}'

        driver = webdriver.Chrome()
        driver.get(link)

        # Espera carregar o botão de enviar
        while len(driver.find_elements(By.XPATH, self.xpath_botao_enviar)) < 1:
            time.sleep(1) 
        time.sleep(2) # Apenas uma garantia
            
        driver.find_element(By.XPATH, self.xpath_botao_enviar).click() # Enviar mensagem
        time.sleep(2) # Esperar um tempo para enviar a mensagem (estava dando problema de não enviar a mensagem caso não esperasse um pouco)

        driver.quit()

    
    def _formatar_mensagem(self, mensagem):
        texto = f"Nome: \nRodada: {mensagem[0]['Rodada']}\n"
        for dic in mensagem:
            time_casa = self._converter_sigla(dic['Time_Casa'])
            gols_casa = dic['Gols_Casa']
            gols_visitante = dic['Gols_Visitante']
            time_visitante = self._converter_sigla(dic['Time_Visitante'])
            if gols_casa:
                texto += f"{time_casa} \t{gols_casa} x {gols_visitante} \t{time_visitante}\n"
            else:
                texto += f"{time_casa} \t  x \t{time_visitante}\n"
        
        print(texto)
        return texto
    

    def _converter_sigla(self, time):
        conversoes = {
            'América-MG': 'AME', 
            'Athletico-PR': 'CAP', 
            'Atlético-MG': 'CAM', 
            'Bahia': 'BAH', 
            'Botafogo': 'BOT', 
            'Corinthians': 'COR', 
            'Coritiba': 'CFC', 
            'Cruzeiro': 'CRU', 
            'Cuiabá': 'CUI', 
            'Flamengo': 'FLA', 
            'Fluminense': 'FLU', 
            'Fortaleza': 'FOR', 
            'Goiás': 'GOI', 
            'Grêmio': 'GRE', 
            'Internacional': 'INT', 
            'Palmeiras': 'PAL', 
            'Bragantino': 'RBB', 
            'Santos': 'SAN', 
            'São Paulo': 'SAO', 
            'Vasco': 'VAS'
        }

        return conversoes.get(time)

        