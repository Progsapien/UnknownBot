
"""

Commands for Telegram Bot Unknown

"""
import BotMessages

def command_start(bot, message):
    bot.send_message(message.from_user.id, BotMessages.start_message())
