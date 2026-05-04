import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# جلب البيانات من Railway وتنظيفها من أي مسافات زائدة
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("STRING_SESSION")

async def start_bot():
    print("... جاري تشغيل البوت")
    
    # تنظيف الجلسة والبيانات برمجياً لضمان عدم حدوث خطأ Invalid Session
    clean_session = SESSION.strip() if SESSION else None
    
    if not all([API_ID, API_HASH, clean_session]):
        print("خطأ: تأكد من إضافة المتغيرات بشكل صحيح في Railway")
        return

    try:
        # تحويل API_ID لرقم وتنظيف الـ API_HASH
        client = TelegramClient(
            StringSession(clean_session), 
            int(str(API_ID).strip()), 
            API_HASH.strip()
        )

        await client.start()
        print("---")
        print("تم الاتصال بنجاح! البوت الآن يعمل")
        print("---")

        @client.on(events.NewMessage(pattern=r'\.فحص', outgoing=True))
        async def check(event):
            await event.edit("**البوت شغال تمام يا أنس! ✅**")

        await client.run_until_disconnected()

    except Exception as e:
        # هذا السطر سيطبع لنا نوع الخطأ بالضبط إذا فشل
        print(f"حدث خطأ أثناء الاتصال: {e}")

if __name__ == '__main__':
    # طريقة التشغيل المتوافقة مع Railway و asyncio
    try:
        asyncio.run(start_bot())
    except Exception as e:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
