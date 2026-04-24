import os, asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# جلب البيانات من المتغيرات التي أضفتها في Railway
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(session), api_id, api_hash)

async def main():
    await client.start()
    print("✅ BOT IS ALIVE!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
    
