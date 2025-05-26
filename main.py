from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
from handlers.start_handler import start
from handlers.community_handler import community
from handlers.help_handler import help
from handlers.support_handler import support
from handlers.care_handler import (
    care, care_story, care_support_groups, care_tips, care_journaling,
    care_journaling_prompts, care_grounding, care_letters, care_younger_self
)
from handlers.learn_handler import learn
from handlers.feedback_handler import feedback

async def handle_story(update: Update, context):
    if context.user_data.get('expecting_story'):
        # TODO: Implement story handling logic (e.g., send to admin)
        await update.message.reply_text("Thank you for sharing your story. It has been received anonymously.")
        context.user_data['expecting_story'] = False

def main():
    application = Application.builder().token(TOKEN).build()
    
    # Main menu handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(start, pattern='^start$'))
    application.add_handler(CallbackQueryHandler(community, pattern='^community$'))
    application.add_handler(CallbackQueryHandler(help, pattern='^help$'))
    application.add_handler(CallbackQueryHandler(support, pattern='^support$'))
    application.add_handler(CallbackQueryHandler(care, pattern='^care$'))
    application.add_handler(CallbackQueryHandler(learn, pattern='^learn$'))
    application.add_handler(CallbackQueryHandler(feedback, pattern='^feedback$'))
    
    # Care menu handlers
    application.add_handler(CallbackQueryHandler(care_story, pattern='^care_story$'))
    application.add_handler(CallbackQueryHandler(care_support_groups, pattern='^care_support_groups$'))
    application.add_handler(CallbackQueryHandler(care_tips, pattern='^care_tips$'))
    application.add_handler(CallbackQueryHandler(care_journaling, pattern='^care_journaling$'))
    application.add_handler(CallbackQueryHandler(care_journaling_prompts, pattern='^care_journaling_prompts$'))
    application.add_handler(CallbackQueryHandler(care_grounding, pattern='^care_grounding$'))
    application.add_handler(CallbackQueryHandler(care_letters, pattern='^care_letters$'))
    application.add_handler(CallbackQueryHandler(care_younger_self, pattern='^care_younger_self$'))
    
    # Story submission handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_story))
    
    print('Bot is running...')
    application.run_polling()

if __name__ == '__main__':
    main()