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
    
    # تنظيف الجلسة
    clean_session = SESSION.strip() if SESSION else None
    if clean_session and len(clean_session) % 4 != 0:
        clean_session += '=' * (4 - len(clean_session) % 4)

    if not all([API_ID, API_HASH, clean_session]):
        print("خطأ: نقص في المتغيرات")
        return

    try:
        client = TelegramClient(
            StringSession(clean_session), 
            int(str(API_ID).strip()), 
            API_HASH.strip()
        )

        await client.start()
        print("--- تم الاتصال بنجاح! ---")

        @client.on(events.NewMessage(pattern=r'\.فحص', outgoing=True))
        async def check(event):
            await event.edit("**البوت شغال تمام يا أنس! ✅**")

        await client.run_until_disconnected()

    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
