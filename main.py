import os
from telethon import TelegramClient, events
import google.generativeai as genai
import asyncio

# سحب البيانات من إعدادات Railway
api_id = os.getenv('API_ID') 
api_hash = os.getenv('API_HASH')
gemini_key = os.getenv('GEMINI_KEY')
phone = os.getenv('PHONE')

# إعداد الذكاء الاصطناعي
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# استخدام اسم جلسة جديد تماماً لإجبار تليجرام على إرسال كود
client = TelegramClient('AnasFinalSession', int(api_id), api_hash)

async def main():
    print("جاري الاتصال بتليجرام...")
    await client.connect()
    if not await client.is_user_authorized():
        print(f"جاري طلب كود التحقق للرقم: {phone}")
        # إرسال طلب الكود يدوياً
        await client.send_code_request(phone)
        print("✅ تم إرسال الكود بنجاح! افحص تطبيق تليجرام الآن على هاتفك.")
    else:
        print("✅ الحساب مسجل دخول بالفعل وجاهز للعمل!")

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private and not event.out:
        try:
            prompt = f"أنت 'أنس الرقمي'، مساعد ذكي. رد بذكاء على: {event.text}"
            response = model.generate_content(prompt)
            await event.reply(response.text)
        except Exception as e:
            print(f"Error: {e}")

# تشغيل الجزء الخاص بطلب الكود أولاً
with client:
    client.loop.run_until_complete(main())
    print("🚀 البوت في وضع الانتظار...")
    client.run_until_disconnected()
    
