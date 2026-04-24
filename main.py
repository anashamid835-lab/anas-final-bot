import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# 1. جلب البيانات من متغيرات Railway التي أضفتها أنت
API_ID = int(os.getenv("API_ID", "31973818"))
API_HASH = os.getenv("API_HASH", "1f1a806752aa3139b6a3fb0824970223")
STRING_SESSION = os.getenv("STRING_SESSION")

# 2. إنشاء العميل باستخدام الجلسة النصية
client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

# 3. أمر الترحيب (/start)
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond('أهلاً بك يا أنس! البوت يعمل الآن بنجاح على Railway 🚀')

# 4. أمر الرد التلقائي على أي رسالة نصية
@client.on(events.NewMessage)
async def echo_handler(event):
    # يتجاهل الأوامر التي تبدأ بـ / لكي لا يتداخل مع الأوامر الأخرى
    if not event.text.startswith('/'):
        await event.reply(f'لقد استلمت رسالتك: {event.text}')

async def main():
    print("⏳ جاري تسجيل الدخول...")
    await client.start()
    print("✅ تم تشغيل البوت بنجاح يا أنس! اذهب لتجربته الآن.")
    await client.run_until_disconnected()

if __name__ == '__main__':
    # تشغيل البوت
    asyncio.run(main())
