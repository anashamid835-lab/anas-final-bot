import os, asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r'\.فحص'))
async def test(event):
    await event.edit('**أهلاً أنس، اليوزر بوت يعمل الآن بنجاح! ✅🚀**')

async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
