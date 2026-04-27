import os
import asyncio
from telethon import TelegramClient, events

# إحضار البيانات من متغيرات Railway
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("STRING_SESSION")

# دالة لتصحيح نقص علامات التساوي في كود الجلسة تلقائياً
def fix_padding(session_str):
    if not session_str:
        return None
    session_str = session_str.strip()
    return session_str + '=' * (-len(session_str) % 4)

# تطبيق التصحيح على الجلسة
FIXED_SESSION = fix_padding(SESSION)

client = TelegramClient(FIXED_SESSION, int(API_ID), API_HASH)

@client.on(events.NewMessage(pattern=r'\.فحص', outgoing=True))
async def check(event):
    await event.edit("**البوت شغال بنجاح يا أنس! ✅🚀**")

print("جاري تشغيل البوت...")
client.start()
client.run_until_disconnected()
