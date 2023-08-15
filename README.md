# PalpiteFacil

## Sobre o Projeto

O PalpiteFácil é um aplicativo desktop desenvolvido em Python, projetado para proporcionar uma experiência interativa e envolvente em palpites de jogos esportivos. 
O objetivo principal do aplicativo é permitir que os usuários participem de competições de palpites, onde eles podem tentar prever os resultados de jogos esportivos e 
acumular pontos com base na precisão de suas previsões.

Ao acertar o placar do jogo, o usuário recebe 3 pontos.

Se errar o placar do jogo mas acertar o time que ganhou ou se empatou, o usuário recebe 1 ponto.

O aplicativo haverá uma tabela de pontuação dos usuários.


## Funcionalidades

- WebScraping do site da ge.globo utilizando Selenium.
- Automação do WhatsApp com Selenium.
- Interface gráfica com Tkinter (em desenvolvimento).
- Análise de dados com Pandas.
- Lógica de pontuação para palpites dos usuários.
- Tabela de classificação dos usuários na interface gráfica.


## Banco de Dados

O projeto utiliza um banco de dados SQLite, com as seguintes tabelas:

- Tabela `Usuarios`: ID, Usuario e telefone apenas.
- Tabela `Palpites`: ID, Usuario, Time_Casa, Gols_Casa, Gols_Visitante, Time_Visitante, Rodada, Acertos_Cheio, Acertos_Parcial, Erro, Pontuacao.
- Tabela `Jogos`: ID, Time_Casa, Gols_Casa, Gols_Visitante, Time_Visitante, Rodada, Dia_Sem, Dia_Mes, Estadio, Horario.
  

## Lógica de Pontuação

- Acertar o placar em cheio: +3 pontos.
- Acertar o time vencedor ou empate: +1 ponto.
- Errar o palpite: 0 pontos.


## Próximos Passos

No futuro, está planejado incluir as seguintes funcionalidades:

- Integração com Django.
- Integração com Flask.
