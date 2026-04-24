import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# جلب البيانات من المتغيرات التي أضفتها أنت في Railway
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")

# استخدام StringSession لضمان تسجيل دخول فوري
client = TelegramClient(StringSession(string_session), api_id, api_hash)

async def main():
    # لا حاجة لطلب الكود هنا لأننا نستخدم الـ StringSession
    await client.start()
    print("✅ تم تشغيل البوت بنجاح يا أنس!")
    
    # هنا تضع أوامر البوت الخاصة بك (مثال بسيط للرد)
    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.respond('أهلاً بك يا أنس، البوت يعمل الآن بنجاح!')

    await client.run_until_disconnected()

if __name__ == '__main__':
    import telethon.events as events
    client.loop.run_until_complete(main())
    
