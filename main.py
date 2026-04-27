import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# إحضار البيانات من متغيرات Railway
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_STR = os.getenv("STRING_SESSION")

# التأكد من صحة البيانات قبل التشغيل
if not API_ID or not API_HASH or not SESSION_STR:
    print("خطأ: تأكد من إضافة API_ID و API_HASH و STRING_SESSION في Variables")
else:
    # إنشاء العميل باستخدام StringSession مباشرة
    client = TelegramClient(StringSession(SESSION_STR.strip()), int(API_ID), API_HASH)

    @client.on(events.NewMessage(pattern=r'\.فحص', outgoing=True))
    async def check(event):
        await event.edit("**تم بنجاح! البوت الآن قيد التشغيل يا أنس ✅🚀**")

    print("جاري الاتصال بتليجرام...")
    client.start()
    print("البوت يعمل الآن! جرب .فحص في تليجرام.")
    client.run_until_disconnected()
