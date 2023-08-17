# Projeto FMF ChatBot (Voicebot)
Este é um projeto da disciplina de Pensamento Analítico de Dados ministrada por Fernando Henrique Federson.

# Equipe 
  - Enzo Rodrigues Novais Dias
  - Gustavo Coimbra Cavalcante
  - Maria Eduarda Silva Borba
  - Mariana Nogueira Carvalho da Silveira

# Descrição do projeto
## Projeto FMF:
O projeto de referência utilizado para desenvolvimento do original: 
["How To Create A Chatbot with Python & Deep Learning In Less Than An Hour"](https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44)

## Projeto ORIGINAL:
O projeto original é uma versão do Projeto FMF com alguma originalidade. Como originalidade: a resposta do Chatbot (ou Voicebot) será por voz.

# Ask
  1.  Será que podemos responder as perguntas dos usuários de maneira eficiente e clara com o chatbot?
  2. Podemos responder de maneira eficiente e clara às perguntas dos usuários quando perguntados sobre músicas?

# Get the data 

## Eliminando os dados??
Inicialmente, como uma abordagem original para o nosso projeto, consideramos a viabilidade de incorporar um dos modelos de linguagem desenvolvidos pela OpenAI. Essencialmente, quando o usuário inserisse um texto, a API forneceria uma conclusão correspondente às instruções ou contexto fornecidos, eliminando assim a necessidade de utilizar os dados do projeto FMF.

## Novos dados?
Optamos por  dar continuidade a ideia inicial e comparar com o que faríamos usando o modelo original. Todavia, trocamos o dataset para um outro contexto. Utilizando a API do Vagalume, extraímos músicas do cantor Bruno Mars e a ideia é o modelo responder a partir disso. Imaginamos que utilizar dados específicos gere melhores resultados. Portanto, optamos por explorar outras maneiras de aprimorar a funcionalidade e eficácia do projeto, mantendo sua abrangência e propósito originais.


# Explore the data
## OPENAI
Os modelos GPT, incluindo o GPT-3.5, são treinados em grandes conjuntos de dados que incluem textos de uma variedade de fontes. A exploraração de  dados de treinamento foi feita de modo a entender as tendências linguísticas, a diversidade de tópicos abordados e como o modelo aprendeu a gerar respostas. 
## VAGALUME
Fizemos o Scrapping das músicas do cantor Bruno Mars, já que avaliamos que seria mais fácil treinar um modelo com menos dados. Como as músicas compartilham muitas palvras, é mais fácil confundida se estiver um dataset muito grande. Por isso a restrição.


# Model
## OPENAI
O modelo escolhido para trabalhar das disponíveis pela OPENAI, foi o GPT-3.5 . A escolha levou em consideração alguns fatores: preço, performance descrita pela própria OPENAI e performance observada ao utilizar cada modelo. O Whisper para a transcrição de áudio também foi usado.
## VAGALUME + keras + tensorflow + NLTK
Foi utilizado o Whisper para transcrição de áudio. Para o treinamento do modelo foi o deep Learning do Keras.

# Comunication and Vizualation
Em ambos os modelos criados, foi utilizado a biblioteca GRADIO para verificar os resultados e ter uma interface. 


Os resultados podem ser vistos e reproduzidos por meio dos documentos CHACAL e CHACAL_KERAS. O CHACAL é o apelido do Voicebot. O arquivo v.01 contém a versão do modelo sem o tratamento de voz, somente um Chatbot.

