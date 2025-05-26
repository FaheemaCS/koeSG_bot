from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def feedback(update: Update, context):
    text = (
        "📝 *Feedback* 📝\n\n"
        "We'd love to hear from you!\n"
        "- **Bot suggestions**\n"
        "- **Resource requests**\n"
        "- **Anonymous testimonial**\n\n"
        "Email us: koebusiness2022@gmail.com"
    )
    keyboard = [back_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)