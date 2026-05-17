import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ChatJoinRequestHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)

BOT_TOKEN = "8949333597:AAFm6fM1JFkWJzWhzONUF8U3GDqupejCQF8"

WELCOME_MESSAGE = """Qoutex Compounding series group click this link 🔗 👇

https://t.me/+bVcfKICihac0NTI1
https://t.me/+bVcfKICihac0NTI1

🔥 Just 2 Days Challenge! 🔥
Turn $10 → $500 💸
Limited slots — Join Fast & Start Earning Now! 🚀"""

async def handle_join_request(update, context):
    user = update.chat_join_request.from_user
    chat_id = user.id
    
    keyboard = [[InlineKeyboardButton("✅ Join Group Now", url="https://t.me/+38IXH_QUK6EyMWY1")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://i.imgur.com/REPLACE_THIS.jpg",
            caption=WELCOME_MESSAGE,
            reply_markup=reply_markup
        )
        logger.info(f"Welcome sent to {user.first_name}")
        await update.chat_join_request.approve()
        
    except Exception as e:
        logger.error(f"Error: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    logger.info("Bot started 24/7!")
    app.run_polling(drop_pending_updates=True)

if name == "main":
    main()
