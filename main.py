import os
from telethon import TelegramClient, events
import google.generativeai as genai

# بياناتك الشخصية
api_id = '1234567' # الـ API ID الخاص بك
api_hash = 'your_api_hash_here' # الـ API Hash الخاص بك
gemini_key = 'AIzaSy...' # مفتاح Gemini الخاص بك
my_user_id = 'me' # كلمة 'me' تعني أن البوت سيرسل الرسالة لك أنت

genai.configure(api_key=gemini_key)
model = genai.GenerativeModel('gemini-1.5-flash')

client = TelegramClient('AnasCloudSession', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # الرد فقط في الخاص وعلى غيرك (عشان ميردش على نفسه)
    if event.is_private and not event.out:
        try:
            # توليد الرد من الذكاء الاصطناعي
            prompt = f"أنت 'أنس الرقمي'، وكيل ذكي. رد بذكاء على: {event.text}"
            response = model.generate_content(prompt)
            bot_reply = response.text
            
            # 1. الرد على الشخص
            await event.reply(bot_reply)
            
            # 2. إرسال إشعار لك (التعديل الجديد)
            sender = await event.get_sender()
            notification = f"🔔 **إشعار من أنس الرقمي:**\n\n👤 **المرسل:** {sender.first_name} (@{sender.username})\n💬 **رسالته:** {event.text}\n🤖 **ردي عليه:** {bot_reply}"
            await client.send_message(my_user_id, notification)
            
        except Exception as e:
            print(f"Error: {e}")

print("أنس الرقمي يعمل مع ميزة الإشعارات...")
client.start()
client.run_until_disconnected()




