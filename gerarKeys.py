from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def gerar_keys():
    ask_keys = []
    msg = ['Olá Samantha, sobre Joseph Weizenbaum, quem é ele?',
           'Sim! Estou fazendo um trabalho da faculdade sobre ele e preciso de informações do tipo, onde nasceu, '
           'onde estudou, família.', 'Ok! Essa parte eu anotei, agora sobre a Eliza, o que é um bot?',
           'E quando os bot’s surgiram?', 'O que a Eliza fazia?', 'O que é o Teste de Turing?',
           'Existem bot’s que passaram nesse teste?', 'E como os bot’s são utilizados na atualidade?',
           'E como essa tecnologia impacta na comunicação das empresas?',
           'Fico agradecido pelas informações Samantha! Minha pesquisa está concluída. Mas antes de terminar nossa '
           'conversa, você poderia me enviar suas fontes de pesquisa?',
           'Obrigado Samantha! Até mais.']

    for txt in msg:
        palavras = word_tokenize(txt.lower())
        stopw = set(stopwords.words('portuguese') + list(punctuation))
        palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopw]
        ask_keys.append(palavras_sem_stopwords)
    return ask_keys
