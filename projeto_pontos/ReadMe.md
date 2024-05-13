# Sistema de Pontos da Twitch

Em nossa live temos um sistema de pontos para aumentar o engajamento de nossos usuários.

Chamamos esses pontos de cubos.

Até o momento há três maneiras de ganhar cubos:

1. Interagir no chat da Twitch.
2. Assinar a lista de presença digitando `!presente`.
3. Resgatar pôneis.

Com os cubos, os usuários realizam trocas por `datapoints`, moeda do StreamElements utilizado em nossa lojinha.

## Objetivo

Desejamos identificar quais usuário são mais propensos à continuarem engajados em nosso projeto, realizando assim comunicação direcionada agradecendo a parceria, mantendo-os ainda mais engajados.

Outro ponto importante é mapear aqueles que tem altas chances de abandonarem o projeto.

Ter uma ideia de quais são as variáveis (comportamentos históricos) que ajudam a explicar esse nível de engajamento, seria bem útil para definir novas mecânicas e estratégias de retenção.

## Dados

Com base no histórico de transações (eventos), construimos uma base com algumas estatísticas de nossos usuários, bem como a sinalização se ele continuou acompanhando as nossas lives pelos 15 dias adiante.

Essa ABT (*Analytical Base Table*) foi criada a partir dos códigos em `projeto_pontos/dataprep/`. Por se tratar de alguns dados pessoais, não disponibilizamos os dados brutos para que você possa reconstruir esses passos, embora o código possa server de aprendizado.

A tabela final estará disponível junto aos demais arquivos de dados em [nosso drive](https://drive.google.com/drive/folders/1N3U_U_8QqbkN4FMMLYg-_iRSEDDYWMGI?usp=sharing).