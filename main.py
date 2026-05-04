import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# 1. جلب البيانات من متغيرات Railway (Variables)
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("STRING_SESSION")

async def start_bot():
    print("---")
    print("محاولة تشغيل البوت على سيرفر Railway...")
    print("---")
    
    # 2. تنظيف الجلسة من أي مسافات أو أسطر زائدة ناتجة عن النسخ
    clean_session = SESSION.strip() if SESSION else None
    
    # 3. إضافة الحشو (Padding) اللازم لضمان توافق الـ StringSession
    if clean_session and len(clean_session) % 4 != 0:
        clean_session += '=' * (4 - len(clean_session) % 4)

    # التحقق من وجود المتغيرات الأساسية
    if not all([API_ID, API_HASH, clean_session]):
        print("خطأ كاد يتسبب في انهيار البوت:")
        print("تأكد من إضافة API_ID و API_HASH و STRING_SESSION في إعدادات Railway")
        return

    try:
        # 4. إنشاء العميل وتنظيف المدخلات (تحويل ID لرقم)
        client = TelegramClient(
            StringSession(clean_session), 
            int(
