import BotMessages, Markups

def command_callback_handle(bot, call):
    print(call.data)
    if(call.message):
        if(call.data == "btn1"):
            callback_btn1(bot, call)
        elif(call.data == "btn1_4"):
            callback_btn1_4(bot, call)
        elif(call.data == "btn2"):
            callback_btn2(bot, call)



def callback_btn1(bot, call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=BotMessages.on_btn1(), reply_markup=Markups.btn1_markup())

def callback_btn1_4(bot, call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=BotMessages.start_message(),
                          reply_markup=Markups.start_markup())

def callback_btn2(bot, call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=BotMessages.on_btn2(), reply_markup=Markups.btn2_markup())

