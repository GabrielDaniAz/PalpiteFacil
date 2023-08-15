import pyodbc

class CriarDatabase:
    def __init__(self):
        self.driver = '{SQLite3 ODBC Driver}'
        self.server = 'localhost'
        self.database = 'brasileirao.sqlite'

        self.dados_conexao = f'Driver={self.driver};Server={self.server};Database={self.database}'

    
    def _criar_tabela_usuarios(self, cursor):
            criar_tabela_usuarios = """
            CREATE TABLE Usuarios (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Usuario VARCHAR(50) NOT NULL UNIQUE,
                Telefone VARCHAR(17) NOT NULL UNIQUE
            )
            """
            cursor.execute(criar_tabela_usuarios)


    def _criar_tabela_jogos(self, cursor):
        criar_tabela_jogos = """
        CREATE TABLE Jogos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Time_Casa VARCHAR(20) NOT NULL,
            Gols_Casa INT,
            Gols_Visitante INT,
            Time_Visitante VARCHAR(20) NOT NULL,
            Rodada INT NOT NULL,
            Dia_Semana VARCHAR(3) NOT NULL,
            Dia_Mes VARCHAR(10) NOT NULL,
            Estadio VARCHAR(30) NOT NULL,
            Horario VARCHAR(5) NOT NULL
        )
        """
        cursor.execute(criar_tabela_jogos)


    def _criar_tabela_palpites(self, cursor):
        criar_tabela_palpites = """
        CREATE TABLE Palpites (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Usuario VARCHAR(50) NOT NULL,
            Time_Casa VARCHAR(20) NOT NULL,
            Gols_Casa INT NOT NULL,
            Gols_Visitante INT NOT NULL,
            Time_Visitante VARCHAR(20) NOT NULL,
            Rodada INT NOT NULL,
            Acertos_Cheio BIT,
            Acertos_Parcial BIT,
            Erro BIT,
            Pontuacao INT
        )
        """
        cursor.execute(criar_tabela_palpites)


    def _tabelas_existem(self, tabelas, cursor):
        for tabela in tabelas:
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tabela,))
            resultado = cursor.fetchone()

            if resultado is None:
                return False # A tabela não existe
            
        return True
    

    def criar_todas_tabelas(self):
        conexao = pyodbc.connect(self.dados_conexao)
        cursor = conexao.cursor()

        if not self._tabelas_existem(["Usuarios", "Jogos", "Palpites"], cursor):
            self._criar_tabela_usuarios(cursor)
            self._criar_tabela_jogos(cursor)
            self._criar_tabela_palpites(cursor)

            cursor.commit()
        else:
            pass

        cursor.close()
        conexao.close()