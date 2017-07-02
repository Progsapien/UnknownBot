
"""

Commands for Telegram Bot Unknown

"""


import BotMessages, Markups

def command_start(bot, message):
    bot.send_chat_action(message.from_user.id, "typing")
    bot.send_message(message.from_user.id, BotMessages.start_message(), reply_markup=Markups.start_markup())

