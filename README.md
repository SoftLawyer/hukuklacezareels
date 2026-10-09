# HukukLA Ceza Reels Generator

Bu repository, HukukLA'nın "ÇOĞU HUKUKÇU BUNU ÇÖZEMİYOR" tarzındaki eğitici/tartışmalı Ceza Hukuku vakalarını (Reels videoları formatında) otomatik üretmek için tasarlanmıştır.

Tasarım tamamen kilitlenmiş, Instagram'ın %10 güvenli alan kurallarına (Safe Area) uygun hale getirilmiş ve TailwindCSS/Playwright/FFmpeg kullanılarak matematiksel kesinlikle standartlaştırılmıştır.

## Kurulum

```bash
pip install -r requirements.txt
playwright install chromium
# FFmpeg bilgisayarınızda kurulu olmalıdır (brew install ffmpeg).
```

## Kullanım

Bir JSON dosyası hazırlayın (örn. `example_data.json`) ve aşağıdaki komutu çalıştırın:

```bash
python generate.py example_data.json output_reel.mp4
```

JSON yapısı şu şekildedir:
```json
{
    "hook_line1": "ÇOĞU",
    "hook_line2": "HUKUKÇU",
    "hook_line3": "BUNU",
    "hook_line4": "ÇÖZEMİYOR:",
    "question_text": "Vaka metni buraya yazılır...",
    "option_a": "A şıkkı",
    "option_b": "B şıkkı",
    "option_c": "C şıkkı",
    "option_d": "D şıkkı"
}
```
