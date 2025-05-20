from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import telegram
import os

token = os.getenv("8097068704:AAHq7aMU7AtedTpG1Ynjfa3RS7BTM4CPSMs")
from flask import Flask  # Required for Render health checks

# Initialize Flask app for health checks
app = Flask(__name__)

@app.route('/')
def health_check():
    return "OK", 200

# Helper function to create back button
def back_button(target='main'):
    return [InlineKeyboardButton("🔙 Back", callback_data=target)]

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("🆘 Immediate Help Needed", callback_data='emergency')],
        [InlineKeyboardButton("❓ Understand My Options", callback_data='options')],
        [InlineKeyboardButton("⚖️ Learn About Rights", callback_data='rights')],
        [InlineKeyboardButton("💬 Emotional Support", callback_data='support')],
        [InlineKeyboardButton("ℹ️ About This Bot", callback_data='about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Only show intro text if this is a /start command (update.message exists)
    if update.message:
        intro_text = """
🤝 *About KOE & This Bot* 🤝

KOE is a Singapore-based initiative committed to supporting survivors of sexual assault with empathy, care, and confidentiality.

This bot, *Koe_SG*, was developed in collaboration with students from the Singapore Institute of Technology (SIT). It provides immediate information, emotional support contacts, and guides on legal and medical options for survivors in Singapore.

You are not alone — help is available. 💙
"""
        await update.message.reply_text(intro_text, parse_mode='Markdown')
        await update.message.reply_text("Please choose an option below:", reply_markup=reply_markup)
    else:
        # For callback queries (back button), just show the menu
        await update.callback_query.edit_message_text("Please choose an option below:", reply_markup=reply_markup)


async def button_handler(update: Update, context):
    query = update.callback_query
    try:
        await query.answer()
    except telegram.error.BadRequest as e:
        if "Query is too old" in str(e):
            # Ignore old queries
            return
        raise e
    
    # Main menu options
    if query.data == 'emergency':
        response = """
🆘 *Immediate Help Needed* 🆘

*24/7 Emergency Contacts:*
- Police: 999
- Sexual Assault Care Centre: 6779 0282
- AWARE Helpline: 1800 777 5555
"""
        reply_markup = InlineKeyboardMarkup([back_button()])
        await query.edit_message_text(response, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif query.data == 'options':
        keyboard = [
            [InlineKeyboardButton("🏥 Medical Attention", callback_data='medical')],
            [InlineKeyboardButton("👮 Reporting Options", callback_data='reporting')],
            [InlineKeyboardButton("⚖️ Legal Advice", callback_data='legal')],
            back_button()
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("❓ *Understand My Options*\nSelect a category:", reply_markup=reply_markup, parse_mode='Markdown')
    
    # Sub-options under "Understand My Options"
    elif query.data == 'medical':
        response = """
🏥 *Medical Attention Guide* 🏥

*Where to go:*
- KK Women's and Children's Hospital (24/7)
- Singapore General Hospital (24/7)
"""
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back to Options", callback_data='options')],
            back_button()
        ])
        await query.edit_message_text(response, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif query.data == 'reporting':
        response = """
👮 *Reporting Options* 👮

1. Police report: 999 or any station
2. University reporting (if applicable)
3. Anonymous options available
"""
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back to Options", callback_data='options')],
            back_button()
        ])
        await query.edit_message_text(response, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif query.data == 'legal':
        response = """
⚖️ *Legal Advice* ⚖️

- Free legal clinics available
- Protection orders
- Court accompaniment services
"""
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back to Options", callback_data='options')],
            back_button()
        ])
        await query.edit_message_text(response, reply_markup=reply_markup, parse_mode='Markdown')
    
    # Other main menu options
    elif query.data == 'rights':
        response = """
⚖️ *Your Legal Rights* ⚖️

- Right to be treated with dignity
- Right to have a support person
- Right to request female officers
"""
        reply_markup = InlineKeyboardMarkup([back_button()])
        await query.edit_message_text(response, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif query.data == 'support':
        response = """
💬 *Emotional Support* 💬

- AWARE Counseling: 1800 777 5555
- SOS Helpline: 1767
- Online chat support available
"""
        reply_markup = InlineKeyboardMarkup([back_button()])
        await query.edit_message_text(response, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif query.data == 'about':
        response = """
ℹ️ *About This Bot* ℹ️

Created by KOE and SIT students
to provide confidential guidance.
"""
        reply_markup = InlineKeyboardMarkup([back_button()])
        await query.edit_message_text(response, reply_markup=reply_markup, parse_mode='Markdown')
    
    # Navigation handlers
    elif query.data == 'main':
        await start(update, context)

def main():
    token = os.getenv("BOT_TOKEN", "7975694771:AAGgljJg2hQudGNpfL73Vb9qc2tFlimUElI")
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Render-specific setup
    if os.getenv('RENDER'):  # Detect if running on Render
        port = int(os.environ.get("PORT", 8443))
        webhook_url = f"https://your-service-name.onrender.com/{token}"
        
        # Start webhook
        application.run_webhook(
            listen="0.0.0.0",
            port=port,
            webhook_url=webhook_url,
            drop_pending_updates=True
        )
    else:
        # Local development with polling
        application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    # Start Flask server for health checks
    from threading import Thread
    Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 3000}).start()
    
    # Start Telegram bot
    main()


