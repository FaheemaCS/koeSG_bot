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
🚨 *I need help (Crisis & Reporting)* 🚨  

Hello, thank you for reaching out! Please share if you are currently in an emergency.

Examples of emergencies: 
- Police: a sexual assault/harassment case is currently/has just happened and you would like to report it immediately
- SOS: if you have thoughts of hurting yourself or those around you.
"""
    keyboard = [
        [InlineKeyboardButton("Yes, I need to call the police now", callback_data='emergency_police')],
        [InlineKeyboardButton("Yes, I need to call SOS now", callback_data='emergency_sos')],
        [InlineKeyboardButton("No, I'm not in emergency - show helplines", callback_data='helplines')],
        back_button()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def emergency_police(update: Update, context):
    text = """
🚔 *Emergency Police Assistance* 🚔

Please call **999** immediately if you're in danger.

For non-emergency police assistance, call **1800 255 0000**.

Would you like me to:
1. Provide the number to copy?
2. Open your phone app with the number ready to call?
"""
    keyboard = [
        [InlineKeyboardButton("Copy Police Number", callback_data='copy_police')],
        [InlineKeyboardButton("Open Phone App", callback_data='call_police')],
        back_button('help')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def emergency_sos(update: Update, context):
    text = """
🆘 *Emergency SOS Assistance* 🆘

Please call **1767** immediately for SOS (Samaritans of Singapore).

They provide 24/7 emotional support for those in distress.

Would you like me to:
1. Provide the number to copy?
2. Open your phone app with the number ready to call?
"""
    keyboard = [
        [InlineKeyboardButton("Copy SOS Number", callback_data='copy_sos')],
        [InlineKeyboardButton("Open Phone App", callback_data='call_sos')],
        back_button('help')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

async def helplines(update: Update, context):
    text = """
📞 *Helplines* 📞

Thank you for reaching out! Below are specialized helplines:

🔹 *Sexual Assault Support (All Genders)*:
- AWARE: Call 6779 0282 (Mon-Fri, 10am-6pm)
- Care Corner: 6476 1482 or projectstart@carecorner.org.sg

🔹 *Workplace Harassment*:
- AWARE: 6950 9191 (Mon-Fri, 10am-6pm)

🔹 *For Sex Workers*:
- Project X: 9060 9906 (3pm-11:30pm)

🔹 *For Primary School Children*:
- Tinkle Friend: 1800 274 4788

🔹 *LGBTQ+ Support*:
- Oogachaga: WhatsApp 8592 0609 (Tue/Thu 7pm-10pm, Sat 2pm-5pm)

🔹 *Online Harassment*:
- SCWO: 8001 01 4616 or WhatsApp 6571 4400 (9am-9pm)
"""
    keyboard = [
        [InlineKeyboardButton("Legal Guidance", callback_data='legal')],
        [InlineKeyboardButton("Medical Support", callback_data='medical')],
        back_button('help')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)

# Add these new handlers to your main application setup:
def main():
    application = Application.builder().token(TOKEN).build()
    
    # Existing handlers...
    application.add_handler(CallbackQueryHandler(help, pattern='^help$'))
    application.add_handler(CallbackQueryHandler(emergency_police, pattern='^emergency_police$'))
    application.add_handler(CallbackQueryHandler(emergency_sos, pattern='^emergency_sos$'))
    application.add_handler(CallbackQueryHandler(helplines, pattern='^helplines$'))
    application.add_handler(CallbackQueryHandler(legal, pattern='^legal$'))
    application.add_handler(CallbackQueryHandler(medical, pattern='^medical$'))
    
    # New utility handlers
    application.add_handler(CallbackQueryHandler(copy_number, pattern='^copy_.*$'))
    application.add_handler(CallbackQueryHandler(call_number, pattern='^call_.*$'))
    
    # ... rest of your setup

async def copy_number(update: Update, context):
    query = update.callback_query
    number_type = query.data.replace('copy_', '')
    
    numbers = {
        'police': '999',
        'sos': '1767'
    }
    
    await query.answer(f"Number copied: {numbers.get(number_type, '')}", show_alert=True)
    await query.edit_message_reply_markup()  # Keep same message but update buttons

async def call_number(update: Update, context):
    query = update.callback_query
    number_type = query.data.replace('call_', '')
    
    numbers = {
        'police': 'tel:999',
        'sos': 'tel:1767'
    }
    
    keyboard = [
        [InlineKeyboardButton("↗️ Open Phone App", url=numbers.get(number_type))],
        back_button('help')
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_reply_markup(reply_markup)
    await query.answer("Please check your phone dialer app")

    
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