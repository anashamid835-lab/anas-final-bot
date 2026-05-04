import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# جلب البيانات من متغيرات Railway
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("STRING_SESSION")

# دالة لتصحيح نقص علامات التساوي في كود الجلسة تلقائياً
def fix_padding(session_str):
    if not session_str:
        return None
    session_str = session_str.strip()
    return session_str + '=' * (-len(session_str) % 4)

FIXED_SESSION = fix_padding(SESSION)

async def start_bot():
    print("... جاري تشغيل البوت على Railway")
    
    # التأكد من أن جميع البيانات موجودة
    if not all([API_ID, API_HASH, FIXED_SESSION]):
        print("خطأ: تأكد من إضافة API_ID و API_HASH و STRING_SESSION في Variables على Railway")
        return

    try:
        # إنشاء العميل باستخدام StringSession
        client = TelegramClient(
            StringSession(FIXED_SESSION), 
            int(API_ID), 
            API_HASH,
            connection_retries=10,
            retry_delay=5
        )

        await client.start()
        print("!تم الاتصال بنجاح")

        # أمر الفحص للتأكد من عمل البوت
        @client.on(events.NewMessage(pattern=r'\.فحص', outgoing=True))
        async def check(event):
            await event.edit("**!البوت شغال بنجاح يا أنس 🚀✅**")

        print("البوت الآن في وضع الاستماع...")
        await client.run_until_disconnected()

    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == '__main__':
    # تشغيل البوت باستخدام asyncio لضمان الاستقرار على السيرفر
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
