from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def gerar_keys():
    ask_keys = []
    msg = ['Ol� Samantha, sobre Joseph Weizenbaum, quem � ele?',
           'Sim! Estou fazendo um trabalho da faculdade sobre ele e preciso de informa��es do tipo, onde nasceu, '
           'onde estudou, fam�lia.', 'Ok! Essa parte eu anotei, agora sobre a Eliza, o que � um bot?',
           'E quando os bot�s surgiram?', 'O que a Eliza fazia?', 'O que � o Teste de Turing?',
           'Existem bot�s que passaram nesse teste?', 'E como os bot�s s�o utilizados na atualidade?',
           'E como essa tecnologia impacta na comunica��o das empresas?',
           'Fico agradecido pelas informa��es Samantha! Minha pesquisa est� conclu�da. Mas antes de terminar nossa '
           'conversa, voc� poderia me enviar suas fontes de pesquisa?',
           'Obrigado Samantha! At� mais.']

    for txt in msg:
        palavras = word_tokenize(txt.lower())
        stopw = set(stopwords.words('portuguese') + list(punctuation))
        palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopw]
        ask_keys.append(palavras_sem_stopwords)
    return ask_keys
