import pyodbc
import pandas as pd

class DatabaseManager:
    def __init__(self):
        self.driver = '{SQLite3 ODBC Driver}'
        self.server = 'localhost'
        self.database = 'brasileirao.sqlite'

        self.dados_conexao = f'Driver={self.driver};Server={self.server};Database={self.database}'


    def _conectar_database(self):
        self.conexao = pyodbc.connect(self.dados_conexao)
        self.cursor = self.conexao.cursor()


    def _fechar_database(self):
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()


    def inserir_jogos(self, lista_jogos):
        self._conectar_database()
        query_inserir = """
            INSERT INTO Jogos (Time_Casa, Gols_Casa, Gols_Visitante, Time_Visitante, Rodada, Dia_Semana, Dia_Mes, Estadio, Horario)
            VALUES (?,?,?,?,?,?,?,?,?)
            """
        
        for jogo in lista_jogos:
            if not self._dados_existentes(jogo):
                self.cursor.execute(query_inserir, jogo['Time_Casa'], jogo['Gols_Casa'], jogo['Gols_Visitante'], 
                            jogo['Time_Visitante'], jogo['Rodada'], jogo['Dia_Semana'],
                            jogo['Dia_Mes'], jogo['Estadio'], jogo['Horario'])
        
            else:
                pass

        self._fechar_database()


    def _dados_existentes(self,jogo):
        df = self._sql_pandas_jogos()
        time_casa, time_visitante, dia_mes = jogo['Time_Casa'], jogo['Time_Visitante'], jogo['Dia_Mes']

        if not df[(df['Time_Casa'] == time_casa) & (df['Time_Visitante'] == time_visitante) & (df['Dia_Mes'] == dia_mes)].empty:
            return True
        return False

    
    def _sql_pandas_jogos(self):
        self.cursor.execute("""
        SELECT * FROM Jogos
        """)

        valores = self.cursor.fetchall()
        colunas = self.cursor.description
        colunas = [tupla[0] for tupla in colunas]

        df = pd.DataFrame.from_records(valores, columns=colunas)
        df = df.set_index('ID')

        return df
    

    def _ordenar_database(self):
        query = """
        SELECT * FROM Jogos
        ORDER BY STR_TO_DATE(Dia_Mes, '%d/%m/%Y')
        """
        self.cursor.execute(query)