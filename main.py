from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import telegram
import os
from flask import Flask

# Initialize Flask app for health checks
app = Flask(__name__)

@app.route('/')
def health_check():
    return "OK", 200

# Bot Token (replace with your actual token)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or "7750078176:AAFstaPP2l1-K3veM-RnFoSYIVq1iwK0KCA"

# Helper function to create back button
def back_button(target='start'):
    return [InlineKeyboardButton("🔙 Back", callback_data=target)]

# ======================
# COMMAND HANDLERS
# ======================

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Join our Community", callback_data='community')],
        [InlineKeyboardButton("I need help (Crisis & Reporting)", callback_data='help')],
        [InlineKeyboardButton("Support & Resources", callback_data='support')],
        [InlineKeyboardButton("Self Care & Healing", callback_data='care')],
        [InlineKeyboardButton("Learn & Volunteer", callback_data='learn')],
        [InlineKeyboardButton("Feedback", callback_data='feedback')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        intro_text = """
🤝 *About KOE & This Bot* 🤝

Hello! This bot was created by KOE, a project that strives to amplify voices of sexual assault survivors in Singapore. 

We are here to support sexual assault survivors by providing a one-stop centre for all types of resources required such as self care tips, resources for counselling or legal assistance, or helplines when in need. This bot can also support you (friends/families of survivors) in order to better support your loved ones when faced with such circumstances. 

This bot ensures privacy and confidentiality, thereby your user is kept completely anonymous. If you would like to reach out to KOE for any matters, do email us via gmail at koebusiness2022@gmail.com
"""
        await update.message.reply_text(intro_text, parse_mode='Markdown')
        await update.message.reply_text("Please choose an option below:", reply_markup=reply_markup)
    else:
        await update.callback_query.edit_message_text("Please choose an option below:", reply_markup=reply_markup)

# ======================
# MENU OPTION HANDLERS
# ======================

async def community(update: Update, context):
    text = """
🌟 *Join Our Community* 🌟  

Connect with survivors and allies in a safe, moderated space:  
- [KOE Support Group](https://t.me/koe_support) (Private, survivors-only)  
- [Public Awareness Channel](https://t.me/koe_public) (Updates/resources)  

Rules:  
1. Respect anonymity.  
2. No victim-blaming.  
3. Trigger warnings for sensitive content.  
"""
    keyboard = [back_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def help(update: Update, context):
    text = """
🚨 *Immediate Help* 🚨  

If you're in crisis, contact these Singapore-based resources:  
- **SOS Helpline**: 1767 (24/7)  
- **AWARE Helpline**: 1800 777 5555 (Mon–Fri, 10am–6pm)  
- **Police**: 999 (Emergency) / 1800 255 0000 (Non-emergency)  

For anonymous reporting:  
- [Submit to KOE](https://forms.gle/EXAMPLE) (We'll guide you).  
"""
    keyboard = [
        [InlineKeyboardButton("Legal Guidance", callback_data='legal')],
        [InlineKeyboardButton("Medical Support", callback_data='medical')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def support(update: Update, context):
    text = """
📚 *Support & Resources* 📚  

1. **Counseling**:  
   - [AWARE Counseling](https://aware.org.sg) (Low-cost)  
   - [RAINBOW Centre](https://rainbowcentre.sg) (For minors)  

2. **Legal Aid**:  
   - [Legal Aid Bureau](https://lab.mlaw.gov.sg) (Income-based)  

3. **Financial Assistance**:  
   - [MSF ComCare](https://www.msf.gov.sg)  
"""
    keyboard = [
        [InlineKeyboardButton("Download Resource Pack", callback_data='download')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def care(update: Update, context):
    text = """
💖 *Self-Care & Healing* 💖  

Try these exercises:  
- **Grounding Technique**: Name 5 things you see, 4 you hear, 3 you touch...  
- **Journal Prompt**: *"What's one small win today?"*  

Resources:  
- [Guided Meditations](https://youtube.com/playlist?list=EXAMPLE)  
- [Free Therapy Workbooks](https://example.com/workbooks)  
"""
    keyboard = [
        [InlineKeyboardButton("Daily Reminders", callback_data='reminders')],
        [InlineKeyboardButton("Coping Strategies", callback_data='coping')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def learn(update: Update, context):
    text = """
📢 *Learn & Volunteer* 📢  

**Educational Guides**:  
- [Understanding Consent](https://example.com/consent)  
- [How to Support Survivors](https://example.com/support-guide)  

**Volunteer Opportunities**:  
- Join KOE's outreach team (Email us!).  
- Help moderate our community chats.  
"""
    keyboard = [
        [InlineKeyboardButton("Upcoming Events", callback_data='events')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def feedback(update: Update, context):
    text = """
📝 *Feedback* 📝  

We'd love to hear from you!  
- **Bot suggestions**  
- **Resource requests**  
- **Anonymous testimonial**  

Email us: koebusiness2022@gmail.com  
"""
    keyboard = [back_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

# ======================
# SUB-MENU HANDLERS
# ======================

async def legal(update: Update, context):
    text = "⚖️ *Legal Guidance*\n\nContent coming soon..."
    reply_markup = InlineKeyboardMarkup([back_button('help')])
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def medical(update: Update, context):
    text = "🏥 *Medical Support*\n\nContent coming soon..."
    reply_markup = InlineKeyboardMarkup([back_button('help')])
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

# ======================
# GENERIC CALLBACK HANDLER
# ======================

async def handle_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    # Handle back button
    if query.data == 'start':
        await start(update, context)
    # Add other specific cases if needed

# ======================
# MAIN APPLICATION SETUP
# ======================

def main():
    # Create Application
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler('start', start))

    # Add main menu handlers
    application.add_handler(CallbackQueryHandler(community, pattern='^community$'))
    application.add_handler(CallbackQueryHandler(help, pattern='^help$'))
    application.add_handler(CallbackQueryHandler(support, pattern='^support$'))
    application.add_handler(CallbackQueryHandler(care, pattern='^care$'))
    application.add_handler(CallbackQueryHandler(learn, pattern='^learn$'))
    application.add_handler(CallbackQueryHandler(feedback, pattern='^feedback$'))

    # Add sub-menu handlers
    application.add_handler(CallbackQueryHandler(legal, pattern='^legal$'))
    application.add_handler(CallbackQueryHandler(medical, pattern='^medical$'))

    # Add generic callback handler for back button
    application.add_handler(CallbackQueryHandler(handle_callback))

    # Start Flask server for health checks (Render compatibility)
    if os.getenv('RENDER'):
        from threading import Thread
        Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()