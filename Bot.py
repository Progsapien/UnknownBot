import telebot
import BotCommands

class Bot:

    def __init__(self, token):

        self.token = token
        self.__bot = self.__initBot()

    def __initBot(self):

        return telebot.TeleBot(self.token)

    def startHandleCommands(self):

        @self.__bot.message_handler(commands=['start'])

        def handle(message):
            BotCommands.command_start(self.__bot, message)
            # ...

        self.__bot.polling(none_stop=True)


    # Properties

    @property
    def token(self):
        return self.__bot_token

    @token.setter
    def token(self, value):
        if(type(value) == str):
            self.__bot_token = value