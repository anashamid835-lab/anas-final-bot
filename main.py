import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# التوكن من متغير البيئة
TOKEN = os.environ.get("8931599319:AAEJfTzlNeCE4brlO8cTEW9nogTrGVOrOjY")

# تفعيل السجلات
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# معالج أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً! 👻 Ghost Bot يعمل بنجاح!")

# معالج أمر /status
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ البوت يعمل بشكل طبيعي")

def main():
    # بناء التطبيق (الطريقة الصحيحة في v20+)
    application = Application.builder().token(TOKEN).build()
    
    # إضافة المعالجات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    
    # تشغيل البوت
    application.run_polling()

if __name__ == "__main__":
    main()