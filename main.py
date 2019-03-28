import logging
from string import punctuation
from time import sleep
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from gerarKeys import gerar_keys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

token = 'COLOQUE O SEU TOKEN AQUI'
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

ask_keys = gerar_keys()
print(ask_keys)


def start(update, context):
    message = (
        'Olá, eu sou a Samantha, um bot que foi programado para trazer informações sobre Joseph Weizenbaum e o '
        'universo dos bot’s. Aqui vai algumas perguntas que posso responder, mas não são só essas:\n '
        '- O que é um bot?\n'
        '	- Como os bot’s surgiram?\n'
        '	- Quem é Joseph Weizenbaum?\n'
        '	- Onde essa tecnologia é aplicada?\n')
    context.bot.send_message(chat_id=update.message.chat_id, text=message)


def echo(update, context):
    msg = update['message']['text']
    palavras = word_tokenize(msg.lower())
    stopw = set(stopwords.words('portuguese') + list(punctuation))
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopw]
    print(palavras_sem_stopwords)

    cont_atual = cont_ant = index = 0

    for ch, value in enumerate(ask_keys):
        cont_atual = 0
        for key in palavras_sem_stopwords:
            if key in ask_keys[ch]:
                cont_atual += 1
            if cont_atual > cont_ant:
                index = ch
        if cont_atual > cont_ant:
            cont_ant = cont_atual

    if cont_ant <= 1:
        index = -1

    sleep(2)
    if index == 0:
        message = "Joseph W. foi um escritor e cientista da computação nascido em Berlim, ele foi o criador da " \
                  "linguagem de programação SLIP, mas a sua principal contribuição foi a criação do bot Eliza, " \
                  "que é considerada uma precursora das 'máquinas pensantes'. "
        context.bot.send_message(chat_id=update.message.chat_id, text=message)
        sleep(2)
        context.bot.send_message(chat_id=update.message.chat_id, text='Você gostaria de mais informações?')

    elif index == 1:
        message1 = "Entendi! Vou te ajudar nessa pesquisa. Ele nasceu em Berlim, mas tem nacionalidade Alemã e " \
                   "Estadunidense. Ele começou a estudar matemática mas teve seus estudos interrompidos pela Segunda " \
                   "Guerra Mundial, durante a qual ele serviu as forças armadas. "
        context.bot.send_message(chat_id=update.message.chat_id, text=message1)
        sleep(3)
        message2 = "Joseph é filho de pais Judeus, que fugiram da Alemanha nazista em 1935, emigrando com sua família " \
                   "para os Estados Unidos. "
        context.bot.send_message(chat_id=update.message.chat_id, text=message2)

    elif index == 2:
        message = "O nome bot, vem do diminutivo de robot, que é uma aplicação de software para simular ações " \
                  "humanas, a depender de maneira padrão, como um robô faria, ou de maneira inteligente com recursos " \
                  "da inteligência artificial. "
        sleep(3)
        context.bot.send_message(chat_id=update.message.chat_id, text=message)

    elif index == 3:
        message1 = "Engana-se quem pensa que os famosos assistentes virtuais foram desenvolvidos recentemente, " \
                   "pelo contrário, eles surgiram há um bom tempo, muito antes do que você imagina. "
        context.bot.send_message(chat_id=update.message.chat_id, text=message1)
        sleep(3)
        message2 = "Essa tecnologia foi vista pela primeira vez em 1966, quando o Joseph W. criou a Eliza. Alguns " \
                   "cientistas consideram que a história do chatbot se inicia a partir desse momento, " \
                   "assim considerando Eliza como a mãe de todos os bots."
        context.bot.send_message(chat_id=update.message.chat_id, text=message2)

    elif index == 4:
        message1 = "Ela foi criada para simular uma psicóloga, projetada para imitar as conversas humanas com base em " \
                   "instruções e respostas predefinidas, ela era capaz de identificar cerca de 250 tipos de frases. "
        context.bot.send_message(chat_id=update.message.chat_id, text=message1)
        sleep(3)
        message2 = "Apesar disso, Eliza falhou no Teste de Turing, mas sua invenção foi um avanço significativo, " \
                   "dando início a diversos experimentos até chegarmos aos chatbots que temos hoje."
        context.bot.send_message(chat_id=update.message.chat_id, text=message2)

    elif index == 5:
        message1 = 'O Teste de Turing testa a capacidade de uma máquina exibir comportamento inteligente equivalente ' \
                   'a um ser humano, ou até mesmo indistinguível a ele. Por exemplo, um humano entra em conversa em ' \
                   'linguagem natural com outro humano e uma máquina.'
        context.bot.send_message(chat_id=update.message.chat_id, text=message1)
        sleep(3)
        message2 = "Um participante não vê o outro, se o juiz não for capaz de distinguir com segurança a máquina do " \
                   "humano, diz-se que a máquina passou no teste."
        context.bot.send_message(chat_id=update.message.chat_id, text=message2)

    elif index == 6:
        message1 = 'Sim, em 2014 um chatbot chamado de Eugene Goostman convenceu 10 dos 30 juízes de que era um ' \
                   'menino de 13 anos e não um computador, ele foi desenvolvido por um pesquisador russo Vladimir ' \
                   'Veselov e pelo pesquisador ucraniano Eugene Demchenko.'
        context.bot.send_message(chat_id=update.message.chat_id, text=message1)
        sleep(3)
        message2 = "O teste aconteceu em um evento na Universidade de Reading em Londres. De acordo com o organizador " \
                   "do evento, seria a “primeira vez” que um software “passou” no teste de turing."
        context.bot.send_message(chat_id=update.message.chat_id, text=message2)

    elif index == 7:
        message1 = "Existem vaaarias aplicações, um dos mais famosos é o Watson da IBM que “nasceu” em 2006, " \
                   "ele foi projetado especificamente para participar de um programa de perguntas e respostas, " \
                   "o Jeopardy, na época, foi uma revolução."
        context.bot.send_message(chat_id=update.message.chat_id, text=message1)
        sleep(3)
        message2 = "Outros bot’s famosos são a Siri, assistente virtual da Apple, o Google Now do Google, Alexa que " \
                   "atua em milhares de dispositivos feito pela Amazon, Cortana assistente virtual da Microsoft, " \
                   "e um dos mais recentes foi o do Messenger (Facebook) que surgiu em 2016."
        context.bot.send_message(chat_id=update.message.chat_id, text=message2)

    elif index == 8:
        message = "A ideia central por esse tema é a otimização do atendimento ao cliente, mas existem inúmeras " \
                  "possibilidades, visto que não há setor de atuação que não possa aproveitá-los, eu por exemplo " \
                  "estou te ajudando em um trabalho acadêmico. "
        sleep(3)
        context.bot.send_message(chat_id=update.message.chat_id, text=message)

    elif index == 9:
        message1 = "Mas é claro! Segue os links:"
        context.bot.send_message(chat_id=update.message.chat_id, text=message1)
        sleep(3)
        message2 = "História dos Chatbot, saiba como tudo começou: " \
                   "https://push.al/historia-do-chatbot-saiba-como-tudo-comecou/ "
        context.bot.send_message(chat_id=update.message.chat_id, text=message2)
        sleep(3)
        message3 = "Quem foi Joseph Weizenbaum: https://pt.wikipedia.org/wiki/Joseph_Weizenbaum"
        context.bot.send_message(chat_id=update.message.chat_id, text=message3)
        sleep(3)
        message4 = "O que é o teste de turing: https://pt.wikipedia.org/wiki/Teste_de_Turing"
        context.bot.send_message(chat_id=update.message.chat_id, text=message4)
        sleep(3)
        message5 = "Computador convence juízes de que é garoto de 13 anos em “teste de turing”: " \
                   "http://g1.globo.com/tecnologia/noticia/2014/06/computador-convence-juizes-que-e-garoto-de-13-anos" \
                   "-em-teste-de-turing.html"
        context.bot.send_message(chat_id=update.message.chat_id, text=message5)

    elif index == 10:
        message = "Disponha! Fico muito feliz em ajuda-lo."
        sleep(3)
        context.bot.send_message(chat_id=update.message.chat_id, text=message)

    elif index == -1:
        sleep(3)
        context.bot.send_message(chat_id=update.message.chat_id, text='Desculpe, não entendi!')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
