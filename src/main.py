from database.database_manager import DatabaseManager
from webscraper.webscraper import WebScraper
from whatsapp.whatsapp import Whatsapp

if __name__ == "__main__":
    """
    Ideia:
    - Ao abrir o aplicativo:
        - Já possuir o banco de dados (retornar uma mensagem caso não haja banco de dados)
        - Talvez implementar isso, não sei se é a melhor ideia: Verificar qual é a rodada atual no site 
            e comparar no banco de dados se já possui os jogos da rodada
        - Ler os dados da rodada anterior (com placares), e dados da próxima rodada
            Armazenar os valores em:
            lista_dicionarios_jogos_proximo/anterior contendo todas as informações necessárias)
    
    - Interface
        - Login
        - Cadastro
        - Principal

    - Botões Principal:
        - Botão para enviar texto_proxima_rodada por whatsapp para todos os usuários
        - Botão para enviar palpites_banco_dados

    """

    """
    1 - Criar banco de dados e manter o código comentado para ser utilizado apenas quando for apagado (OK)
    2 - Continuar implementando a ideia. Parei por aqui
    """
    w = Whatsapp()
    x = WebScraper()
    lista = x.pegar_jogos_rodada()
    print(lista)
