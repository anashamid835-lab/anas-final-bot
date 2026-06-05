import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# ──────────────────────────────────────────
#  قراءة التوكن
# ──────────────────────────────────────────
# للسحابة: يقرأ من متغير البيئة
# للمحلي: يمكنك تعديل السطر التالي مؤقتاً
TOKEN = os.environ.get("8931599319:AAGB46erA5f7eku01Kob_k95iK7jJO9LGnU")

# ──────────────────────────────────────────
#  إعداد السجلات (Logs)
# ──────────────────────────────────────────
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ──────────────────────────────────────────
#  معالجات الأوامر
# ──────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """أمر /start"""
    await update.message.reply_text(
        "👻 مرحباً بك في Ghost Bot!\n\n"
        "✅ البوت يعمل بنجاح\n"
        "📡 الحالة: متصل بالسيرفر\n\n"
        "الأوامر المتاحة:\n"
        "/start - بدء البوت\n"
        "/status - حالة النظام\n"
        "/help - المساعدة"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """أمر /status"""
    await update.message.reply_text("✅ Ghost Bot يعمل بشكل طبيعي")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """أمر /help"""
    await update.message.reply_text(
        "🤖 Ghost Bot - المساعدة\n\n"
        "الأوامر:\n"
        "/start - بدء البوت\n"
        "/status - فحص الحالة\n"
        "/help - هذه الرسالة\n\n"
        "أرسل أي رسالة وسأرد عليك!"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """رد على أي رسالة نصية"""
    await update.message.reply_text(f"📨 لقد قلت: {update.message.text}")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """معالج الأخطاء"""
    logger.error(f"خطأ: {context.error}")

# ──────────────────────────────────────────
#  الدالة الرئيسية
# ──────────────────────────────────────────
def main():
    # بناء التطبيق
    application = Application.builder().token(TOKEN).build()

    # إضافة المعالجات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # معالج الأخطاء
    application.add_error_handler(error_handler)

    # تشغيل البوت
    logger.info("🚀 Ghost Bot يبدأ العمل...")
    application.run_polling()

if __name__ == "__main__":
    main()