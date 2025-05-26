from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.utils import back_button

async def support(update: Update, context):
    text = (
        "📚 *Support & Resources* 📚\n\n"
        "1. **Counseling**:\n"
        "   - [AWARE Counseling](https://aware.org.sg) (Low-cost)\n"
        "   - [RAINBOW Centre](https://rainbowcentre.sg) (For minors)\n\n"
        "2. **Legal Aid**:\n"
        "   - [Legal Aid Bureau](https://lab.mlaw.gov.sg) (Income-based)\n\n"
        "3. **Financial Assistance**:\n"
        "   - [MSF ComCare](https://www.msf.gov.sg)"
    )
    keyboard = [back_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, parse_mode='Markdown', reply_markup=reply_markup)