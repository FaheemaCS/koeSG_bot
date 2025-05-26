from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def help(update: Update, context):
    text = (
        "🚨 *I Need Help (Crisis & Reporting)* 🚨\n\n"
        "Hello, thank you for reaching out! Please share if you are currently in an emergency.\n\n"
        "Examples of emergencies:\n"
        "- Police: a sexual assault/harassment case is currently/has just happened and you would like to report it immediately\n"
        "- SOS: if you have thoughts of hurting yourself or those around you."
    )
    keyboard = [
        [InlineKeyboardButton("Yes, I need to call the police now", callback_data='emergency_police')],
        [InlineKeyboardButton("Yes, I need to call SOS now", callback_data='emergency_sos')],
        [InlineKeyboardButton("No, I'm not in emergency - show helplines", callback_data='helplines')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)