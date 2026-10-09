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


## AI Otomasyon Akışı: "Sıradakini Ver"

Bu repository, yapay zeka (AI) asistanları ile tam otomatik içerik üretim bandı olarak çalışacak şekilde kodlanmıştır. Kullanıcı asistana sadece **"Sıradakini ver"** komutunu ilettiğinde, asistanın otonom olarak şu adımları uygulaması gerekir:

1. **Konu Seçimi:** Yargıtay kararları ve doktrin ışığında, hukukçuların çok sık karıştırdığı, "ikiye bölen" (gri alanda kalan) yeni ve çarpıcı bir vaka/olay bul.
2. **JSON Üretimi:** Bu olay için repodaki `example_data.json` yapısına uygun olarak yeni bir `vaka_adi.json` dosyası oluştur (Soru metnindeki önemli yerleri `<span class="text-[#2EE5D7] font-bold">` ile vurgula).
3. **Render:** Terminalde `python generate.py vaka_adi.json Reel_Vaka_Adi.mp4` komutunu arka planda çalıştır.
4. **Kopya & Teslimat:** Olayın Yargıtay içtihatlarına dayanan ince detayını (neden o şıkkın doğru olduğunu) anlatan bir Instagram Açıklama (Caption) metni yaz.
5. **Sunum:** Üretilen `.mp4` dosyasını `open -R` komutuyla kullanıcıya göster ve Caption metnini sohbete yaz.
