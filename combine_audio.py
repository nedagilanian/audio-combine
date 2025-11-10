from pydub import AudioSegment
import os


folder_path = "./quality"

# 🔹 لیست فایل‌ها به ترتیب دلخواه
audio_files = [
    "1.mp3", "2.wav", "3.wav", "44.wav", "tavakoli (2).mp3",
    "ravi12.mp3", "ravi13.mp3", "ravi14.mp3", "ravi15.mp3", "add1.mp3", "add2.mpeg",
    "akhar1.mp3", "akhare2.mp3", "akhar3.mp3", "akhar4.mp3"
]

# 🔸 ساخت سکوت‌ها
silence_default = AudioSegment.silent(duration=500)   # سکوت معمولی
silence_3s = AudioSegment.silent(duration=3000)       # ۳ ثانیه سکوت
silence_5s = AudioSegment.silent(duration=5000)       # ۵ ثانیه سکوت

# 🔸 فایل اول
combined = AudioSegment.from_file(os.path.join(folder_path, audio_files[0]))

# 🔸 اضافه کردن بقیه فایل‌ها با سکوت بین‌شان
for file in audio_files[1:]:
    sound = AudioSegment.from_file(os.path.join(folder_path, file))
    combined += silence_default + sound

    # ✳️ بررسی برای اضافه کردن سکوت‌های خاص بعد از فایل‌های مشخص:
    if file == "akhar1.mp3":
        combined += silence_5s  # بعد از akhar1 → ۵ ثانیه سکوت
    elif file == "akhare2.mp3":
        combined += silence_3s  # بعد از akhar2 → ۳ ثانیه سکوت
    elif file == "akhar3.mp3":
        combined += silence_5s  # بعد از akhar3 → ۵ ثانیه سکوت

# 🔸 افزودن موسیقی زمینه (در تمام مدت)
music_path = os.path.join(folder_path, "Announcer-07.mp3")
if os.path.exists(music_path):
    music = AudioSegment.from_file(music_path)
    while len(music) < len(combined):
        music += music
    music = music - 15  
    combined = combined.overlay(music)
else:
    print("⚠️ فایل موسیقی Announcer-07.mp3 پیدا نشد. بدون موسیقی زمینه اجرا می‌شود.")

# 🔸 خروجی نهایی
output_file = "final_snowa.wav"
combined.export(output_file, format="wav")

print(f"✅ فایل نهایی ساخته شد: {output_file}")
