import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# جلب البيانات من المتغيرات التي أضفتها في Railway
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
string_session = os.getenv("STRING_SESSION")

# استخدام StringSession لضمان دخول فوري
client = TelegramClient(StringSession(string_session), api_id, api_hash)

async def main():
    await client.start()
    print("✅ تم تشغيل البوت بنجاح يا أنس!")
    
    # مثال لأمر بسيط يرد على كلمة /start
    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.respond('أهلاً بك يا أنس، البوت يعمل الآن بنجاح!')

    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
