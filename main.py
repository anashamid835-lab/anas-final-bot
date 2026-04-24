import os
from telethon import TelegramClient, events
import google.generativeai as genai

# ضع بياناتك هنا مباشرة بين العلامات ' '
api_id = 26233486  # رقم الـ API ID الخاص بك
api_hash = '9768677c77c66432f4a56a6401666872' # الـ API HASH الخاص بك
phone = '+201125825797' # رقم هاتفك بالصيغة الدولية
gemini_key = 'AIzaSy...' # مفتاح جيميناي الخاص بك

# إعداد الجلسة والذكاء الاصطناعي
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel('gemini-1.5-flash')
client = TelegramClient('AnasFinalSession', api_id, api_hash)

async def main():
    print("جاري محاولة الاتصال...")
    await client.start(phone=lambda: phone)
    print("✅ تم تسجيل الدخول بنجاح! البوت يعمل الآن.")

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        try:
            response = model.generate_content(f"أنت مساعد أنس. رد على: {event.text}")
            await event.reply(response.text)
        except Exception as e:
            print(f"خطأ: {e}")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
    
