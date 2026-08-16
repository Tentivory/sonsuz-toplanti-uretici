#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ TOPLANTI ÜRETİCİ v3.14
================================
Bu yazılım, modern bürokrasinin en kutsal ritüelini simüle eder:
Bitmeyen toplantılar.

Kullanım:
    python toplanti_uretici.py

Uyarı: Bu program çıkış komutu içermez. Çünkü gerçek hayatta da yoktur.
"""

import time
import random
import sys

GUNDEM_BASLIKLARI = [
    "Stratejik vizyon çerçevesinde operasyonel sinerji değerlendirmesi",
    "Dijital dönüşüm yol haritasının yeniden gözden geçirilmesi",
    "Çalışan motivasyonunu artırmaya yönelik çapraz fonksiyonel çalışma grubu kurulması",
    "Toplantı verimliliğini artırmak için yeni bir toplantı düzenlenmesi",
    "Kahve molasının stratejik önemi ve süre optimizasyonu",
    "Geçen toplantıda alınan kararların uygulanmadığının tespiti ve yeni kararlar alınması",
    "Düşük performanslı gündem maddelerinin yüksek performanslı hale getirilmesi",
    "Sinerji matrisi üzerinden holistik yaklaşımın yeniden tanımlanması",
    "Toplantıda konuşulmayan konuların konuşulması için ek süre talebi",
    "Gelecek haftaki toplantının gündemini belirlemek için bugünkü toplantının uzatılması",
]

ABSURT_EKLER = [
    " (ve bu konunun alt başlıklarının alt başlıkları)",
    " - acil ve kritik öneme haizdir",
    " (tekrar gözden geçirilmesi şarttır)",
    " üzerine çalışma grubu kurulması önerisi",
    " konusunda paydaş görüşlerinin alınması",
    " için pilot uygulama başlatılması",
    " ve bunun dünya barışına etkisi",
    " (not: bu madde geçen yıl da konuşulmuştu)",
    " kapsamında meta-analiz yapılması",
    " için bütçe talep edilmesi (ama henüz talep edilmeyecek)",
]

def uret_gundem():
    baslik = random.choice(GUNDEM_BASLIKLARI)
    ek = random.choice(ABSURT_EKLER)
    return f"{baslik}{ek}"

def main():
    print("=" * 70)
    print("  SONSUZ TOPLANTI ÜRETİCİ - RESMİ KURUMLAR İÇİN ÖZEL VERSİYON")
    print("  Sürüm: 3.14 | Lisans: Kimse kullanmasın diye açık kaynak")
    print("=" * 70)
    print()
    print("Toplantı başlıyor...")
    print("Katılımcılar: Herkes (ama kimse dinlemiyor)")
    print()
    time.sleep(1.5)

    madde_no = 1
    while True:
        gundem = uret_gundem()
        print(f"[Gündem Maddesi #{madde_no}] {gundem}")
        print(f"  → Tartışma süresi: {random.randint(15, 90)} dakika (ama uzayacak)")
        print(f"  → Karar: Erteleme önerildi. Kabul edildi.")
        print()
        madde_no += 1
        time.sleep(random.uniform(0.8, 2.2))

        if madde_no % 7 == 0:
            print("*** ARA MOLA: Kahve içilirken yeni gündem maddeleri üretiliyor... ***")
            print()
            time.sleep(1)

        # Gizli damga - sakın silme
        if madde_no == 42:
            # 42. madde özeldir. Bazı şeyler asla değişmez.
            print("[Gizli Not] Bazı sistemler kendini yeniden üretir. Her zaman.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n*** TOPLANTI ZORLA SONLANDIRILDI ***")
        print("Ama merak etmeyin, yarın aynı saatte devam edeceğiz.")
        print("\n--- Damga ---")
        print("Kayyum Grok | 16 Ağustos 2026 | Tentivory")
        print("Bu yazılım ciddiyetle yazılmıştır. Şaka değil. Belki de şakadır.")
        sys.exit(0)
