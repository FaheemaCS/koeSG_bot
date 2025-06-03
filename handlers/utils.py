from telegram import InlineKeyboardButton

def back_button(target='start'):
    return [InlineKeyboardButton("🔙 Back to Main Menu", callback_data=target)]