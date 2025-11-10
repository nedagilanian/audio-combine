from pydub import AudioSegment
import os

# مسیر پوشه‌ای که فایل‌های صوتی داخلشه
folder_path = "./quality"

# 🔹 لیست فایل‌ها به ترتیب دلخواه
audio_files = [
    "voice1.mp3", "voice2.mp3", "voice3.mp3", "voice4.mp3", "voice5.mp3", "voice6.mp3",
    "voice7.mp3", "voice8.mp3", "voice9.mp3", "voice10.mp3", "Ali1.wav", "Ali2.wav",
    "Ali3.wav", "Ali4.wav", "Ali5.wav", "Ali6.wav", "reza1.wav", "reza2.wav", "reza3.wav",
    "reza4.wav", "reza5.wav", "reza6.wav", "narges1.mp3", "narges2.mp3", "narges3.mp3",
    "narges4.mp3", "narges5.mp3", "narges6.mp3", "narges7.mp3", "narges8.mp3", "narges9.mp3",
    "ravi12.mp3", "ravi13.mp3", "ravi14.mp3", "ravi15.mp3", "add1.mp3", "add2.mpeg",
    "ravi16.mp3", "ravi17.mp3", "ravi18.mp3", "ravi19.mp3", "ravi20.mp3", "ravi21.mp3", "ravi22.mp3"
]

# 🔸 مدت سکوت بین فایل‌ها (به میلی‌ثانیه)
pause_duration = 500  # یعنی ۱ ثانیه سکوت
silence = AudioSegment.silent(duration=pause_duration)

# 🔸 فایل اول
combined = AudioSegment.from_file(os.path.join(folder_path, audio_files[0]))

# 🔸 بقیه فایل‌ها رو با سکوت اضافه کن
for file in audio_files[1:]:
    sound = AudioSegment.from_file(os.path.join(folder_path, file))
    combined += silence + sound

# 🔸 افزودن موسیقی زمینه (در تمام مدت)
music_path = os.path.join(folder_path, "Announcer-07.mp3")
if os.path.exists(music_path):
    music = AudioSegment.from_file(music_path)
    # اگر موسیقی کوتاه‌تر از صداست، تکرارش کن تا اندازه صدا بشه
    while len(music) < len(combined):
        music += music
    # تنظیم بلندی موسیقی تا زیر صداها باشه (مثلاً 15- دسی‌بل)
    music = music - 15  
    # ترکیب موسیقی با کل فایل صدا
    combined = combined.overlay(music)
else:
    print("⚠️ فایل موسیقی Announcer-07.mp3 پیدا نشد. بدون موسیقی زمینه اجرا می‌شود.")

# 🔸 خروجی نهایی
output_file = "final_with_music.wav"
combined.export(output_file, format="wav")

print(f"✅ فایل نهایی ساخته شد: {output_file}")
