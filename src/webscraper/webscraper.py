from selenium import webdriver
from selenium.webdriver.common.by import By
import re

class WebScraper:
    def __init__(self):
        self.url = 'https://ge.globo.com/futebol/brasileirao-serie-a/'
        self.xpath = '//*[@id="classificacao__wrapper"]/section' # XPATH das informações necessárias


    """
    Este método acessa o site da ge.globo e retorna uma lista de dicionários
    com informações referente aos jogos
    """
    def pegar_jogos_rodada(self):
        driver = webdriver.Chrome() # Abrindo o Google Chrome
        driver.get(self.url) # Acessando a URL

        # Pegando o texto do elemento
        texto_jogos = driver.find_element(By.XPATH, self.xpath).text

        driver.quit() # Fechar o Chrome

        lista_jogos = texto_jogos.split('\n') # Passando o texto para lista

        # Retorna a lista de dicionários dos jogos
        return self._tratar_lista_jogos(lista_jogos) # Se retornar vazio é porque os jogos estão em andamento


    """
    Exemplo de como a lista pode vim:
    ['SÁB 12/08/2023 NILTON SANTOS (ENGENHÃO) 21:00','Botafogo','3','1','Internacional','VEJA COMO FOI','DOM 13/08/2023 MINEIRÃO 11:00','Atlético-MG','1',
    '0','Bahia','VEJA COMO FOI','DOM 13/08/2023 NEO QUÍMICA ARENA 16:00','Corinthians','Coritiba','DOM 13/08/2023 ARENA DO GRÊMIO 16:00','Grêmio','Fluminense',
    'DOM 13/08/2023 INDEPENDÊNCIA 16:00','América-MG','Goiás','DOM 13/08/2023 MARACANÃ 18:30','Flamengo','São Paulo','DOM 13/08/2023 CASTELÃO (CE) 18:30',
    'Fortaleza','Santos','SEG 14/08/2023 ALLIANZ PARQUE 19:00','Palmeiras','Cruzeiro','SEG 14/08/2023 NABI ABI CHEDID 21:00','Bragantino','Vasco',
    'TER 15/08/2023 LIGGA ARENA 20:00','Athletico-PR','Cuiabá']
    
    Como deve ficar:
    [{'Time_Casa': valor, 'Gols_Casa': valor, 'Gols_Visitante': valor,'Time_Visitante': valor, 'Rodada': valor, 'Dia_Semana': valor,'Dia_Mes': valor, 'Estadio': valor, 'Horario': valor}]
    """  
    def _tratar_lista_jogos(self, lista):
        self.rodada = lista[1][:2] # Identificar a rodada
        lista = lista[2:] # Ignorar os dois primeiros itens ('JOGOS' e a Rodada)

        # Ignorar informações que aparecem durante os jogos
        lista_ignorar = ['ACOMPANHE EM TEMPO REAL', 'VEJA COMO FOI']
        lista = [info for info in lista if info not in lista_ignorar]

        # Formatar a lista em uma lista de dicionários
        lista = self._formatar_lista_dic(lista)
        return lista
    

    """
    As listas podem vir da seguinte forma:
    ['SÁB 12/08/2023 NILTON SANTOS (ENGENHÃO) 21:00','Botafogo','3','1','Internacional','DOM 13/08/2023 MINEIRÃO 11:00','Atlético-MG','1',
    '0','Bahia','DOM 13/08/2023 NEO QUÍMICA ARENA 16:00','Corinthians','Coritiba','DOM 13/08/2023 ARENA DO GRÊMIO 16:00','Grêmio','Fluminense','DOM 13/08/2023 INDEPENDÊNCIA 16:00',
    'América-MG','Goiás','DOM 13/08/2023 MARACANÃ 18:30','Flamengo','São Paulo','DOM 13/08/2023 CASTELÃO (CE) 18:30','Fortaleza','Santos','SEG 14/08/2023 ALLIANZ PARQUE 19:00',
    'Palmeiras','Cruzeiro','SEG 14/08/2023 NABI ABI CHEDID 21:00','Bragantino','Vasco','TER 15/08/2023 LIGGA ARENA 20:00','Athletico-PR','Cuiabá']
    """
    def _formatar_lista_dic(self, lista):
        lista_dic_jogos = []

        # Loop para percorrer a lista e pular passos personalizados
        i = 0
        while i < len(lista):
            info_jogo = lista[i] # As informações do jogo sempre serão o primeiro item
            dia_sem, dia_mes, estadio, horario = self._tratar_info_jogo(info_jogo)
            
            time_casa = lista[i+1] # Time da casa sempre será o segundo item

            # Se entrar na condição, possui placar
            if i+4 < len(lista) and lista[i+2].isdigit() and lista[i+3].isdigit():
                gols_casa = lista[i+2]
                gols_visitante = lista[i+3]
                time_visitante = lista[i+4]
                i += 5 # Possui 5 informações, então pula 5 itens

            elif i+2<len(lista):
                gols_casa = None
                gols_visitante = None
                time_visitante = lista[i+2]
                i += 3 # Possui 3 informações, então pula 3 itens

            # Adicionar as informações no dicionário
            dic_jogo = {
                'Time_Casa': time_casa,
                'Gols_Casa': gols_casa,
                'Gols_Visitante': gols_visitante,
                'Time_Visitante': time_visitante,
                'Rodada': self.rodada,
                'Dia_Semana': dia_sem,
                'Dia_Mes': dia_mes,
                'Estadio': estadio,
                'Horario': horario
            }
            lista_dic_jogos.append(dic_jogo) # Adicionar o dicionário do jogo na lista

        return lista_dic_jogos
    
    
    def _tratar_info_jogo(self, info_jogo):
        # Padrão dos textos das informações dos jogos
        # (DOM 13/08/2023 NEO QUÍMICA ARENA 16:00)
        padrao = '(\w{3}) (\d{2}/\d{2}/\d{4}) ([\w\s()]+) (\d{2}:\d{2})'

        info_jogo = re.findall(padrao, info_jogo)
        dia_sem = info_jogo[0][0]
        dia_mes = info_jogo[0][1]
        estadio = info_jogo[0][2]
        horario = info_jogo[0][3]

        return dia_sem, dia_mes, estadio, horario
    
        
    


    