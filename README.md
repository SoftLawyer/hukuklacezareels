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

1. **Konu Seçimi (Kusursuz Hukuki Netlik):** Yoruma açık, mantık hatası barındıran veya anlatım bozukluğu olan hiçbir vaka KULLANILAMAZ. Sadece **Yargıtay Ceza Genel Kurulu'nun (CGK)** veya yerleşik içtihatların %100 kesin çözdüğü vakalar seçilmelidir. Vaka metni hukuki bir dille, sıfır anlatım bozukluğuyla ve tek anlama gelecek şekilde yazılmalıdır.
2. **Şıkların Hazırlanması:** Çeldirici şıklar kesinlikle yanlış olmalı, doktrin veya istisnalar sebebiyle "iki şıkkın da doğru olabileceği" hiçbir mantık hatasına yer verilmemelidir. **Şıklarda kesinlikle parantez içi açıklamalara (örneğin "(Ceza almaz)", "(Gasp)" gibi) yer verilmez.** Sorular kesinlikle 4 şıklı (A, B, C, D) hazırlanır (E şıkkı KULLANILMAZ). D şıkkının hemen altında kırmızı renkle **"Cevap hikayede paylaşıldı"** ibaresi yer alır. Bu ibare ve şıklar, Instagram Reels'ın alt kısmındaki açıklama/profil/müzik arayüzünün arkasında kalmayacak şekilde (ekranın alt %35'lik güvenli boşluğunun üzerinde) konumlandırılır.
3. **JSON Üretimi:** Bu kusursuz olay için repodaki `example_data.json` yapısına uygun olarak yeni bir `vaka_adi.json` dosyası oluştur (Soru metnindeki önemli yerleri `<span class="text-[#2EE5D7] font-bold">` ile vurgula).
4. **Render (5 Saniye):** Terminalde `python generate.py vaka_adi.json Reel_Vaka_Adi.mp4` komutunu çalıştır (videolar 5 saniyelik statik döngü olarak üretilir).
5. **Kopya & Teslimat:** Olayın Yargıtay içtihatlarına dayanan ince detayını (neden sadece o şıkkın tartışmasız doğru olduğunu) anlatan kusursuz bir Türkçe ile Instagram Açıklama (Caption) metni yaz.
6. **Sunum:** Üretilen `.mp4` dosyasını `open -R` komutuyla kullanıcıya göster ve Caption metnini sohbete yaz.
