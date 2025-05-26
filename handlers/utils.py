from telegram import InlineKeyboardButton

def back_button(target='start'):
    return [InlineKeyboardButton("🔙 Back", callback_data=target)]