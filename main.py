import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# جلب البيانات من Railway
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("STRING_SESSION")

async def start_bot():
    print("... جاري تشغيل البوت")
    
    # تنظيف الجلسة من أي مسافات أو أسطر زائدة
    clean_session = SESSION.strip() if SESSION else None
    
    # إضافة الحشو (Padding) اللازم إذا كان ناقصاً لضمان عمل الـ StringSession
    if clean_session and len(clean_session) % 4 != 0:
        clean_session += '=' * (4 - len(clean_session) % 4)

    if not all([API_ID, API_HASH, clean_session]):
        print("خطأ: تأكد من إضافة المتغيرات API_ID و API_HASH و STRING_SESSION في Railway")
        return

    try:
        # استخدام البيانات المنظفة لبدء الاتصال
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
        print(f"حدث خطأ أثناء الاتصال: {e}")

if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except Exception as e:
        # حل بديل في حال وجود Loop مفتوح مسبقاً على السيرفر
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
