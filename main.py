from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8931599319:AAEJfTzlNeCE4brlO8cTEW9nogTrGVOrOjY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👻 Ghost Bot يعمل!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("👻 Ghost يعمل...")
    app.run_polling()

if __name__ == "__main__":
    main()