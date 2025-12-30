import math
from cplm_algorithm import generate_cplm_key

def chi_square_test(bit_string):
    """Ki-Kare (Chi-Square) Frekans Testi"""
    n = len(bit_string)
    n0 = bit_string.count('0')
    n1 = bit_string.count('1')
    
    # Beklenen değer: n/2
    expected = n / 2.0
    
    # Ki-kare istatistiği: sum((gözlenen - beklenen)^2 / beklenen)
    chi_stat = ((n0 - expected)**2 / expected) + ((n1 - expected)**2 / expected)
    
    # p-değeri hesaplama (1 serbestlik derecesi için basitleştirilmiş)
    # n=1 serbestlik derecesi için p_value = erfc(sqrt(chi_stat)/sqrt(2))
    p_value = math.erfc(math.sqrt(chi_stat) / math.sqrt(2))
    
    return chi_stat, p_value

def runs_test(bit_string):
    """Runs (Dizi) Testi"""
    n = len(bit_string)
    n0 = bit_string.count('0')
    n1 = bit_string.count('1')
    
    # Oran kontrolü (Eğer oran çok bozuksa test anlamsızdır)
    proportion = n1 / n
    if abs(proportion - 0.5) >= (2 / math.sqrt(n)):
        return 0, 0.0 # Başarısız
    
    # Toplam dizi (run) sayısını bul
    runs = 1
    for i in range(1, n):
        if bit_string[i] != bit_string[i-1]:
            runs += 1
            
    # Beklenen dizi sayısı ve varyans
    expected_runs = (2 * n0 * n1 / n) + 1
    variance = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (n**2 * (n - 1))
    
    # Z-skoru
    z_score = (runs - expected_runs) / math.sqrt(variance)
    
    # p-değeri
    p_value = math.erfc(abs(z_score) / math.sqrt(2))
    
    return runs, p_value

def serial_test(bit_string):
    """Seri Test (İkili Grupların Dağılımı)"""
    n = len(bit_string)
    pairs = [bit_string[i:i+2] for i in range(n-1)]
    counts = {
        '00': pairs.count('00'),
        '01': pairs.count('01'),
        '10': pairs.count('10'),
        '11': pairs.count('11')
    }
    
    expected = (n - 1) / 4.0
    chi_stat = sum([(counts[p] - expected)**2 / expected for p in counts])
    
    # 2 serbestlik derecesi (yaklaşık)
    p_value = math.exp(-chi_stat / 2.0)
    
    return counts, p_value

if __name__ == "__main__":
    # Test için büyük bir örneklem üretelim (10,000 bit)
    SAMPLE_SIZE = 10000
    print(f"--- CPLM Algoritması İstatistiksel Analiz Raporu ---")
    print(f"Örneklem Boyutu: {SAMPLE_SIZE} bit\n")
    
    bits = generate_cplm_key(SAMPLE_SIZE)
    
    # 1. Ki-Kare Testi
    chi_stat, p_chi = chi_square_test(bits)
    print(f"[1] Ki-Kare (Frekans) Testi:")
    print(f"    - Ki-Kare İstatistiği: {chi_stat:.4f}")
    print(f"    - P-Değeri: {p_chi:.6f}")
    print(f"    - Sonuç: {'BAŞARILI' if p_chi > 0.01 else 'BAŞARISIZ'}")
    
    # 2. Runs Testi
    runs, p_runs = runs_test(bits)
    print(f"\n[2] Runs (Dizi) Testi:")
    print(f"    - Toplam Dizi Sayısı: {runs}")
    print(f"    - P-Değeri: {p_runs:.6f}")
    print(f"    - Sonuç: {'BAŞARILI' if p_runs > 0.01 else 'BAŞARISIZ'}")
    
    # 3. Seri Test
    counts, p_seri = serial_test(bits)
    print(f"\n[3] Seri Test (Çift Bit Dağılımı):")
    print(f"    - Dağılım: {counts}")
    print(f"    - P-Değeri: {p_seri:.6f}")
    print(f"    - Sonuç: {'BAŞARILI' if p_seri > 0.01 else 'BAŞARISIZ'}")
    
    print("\n* Not: P-Değeri > 0.01 ise dizi istatistiksel olarak rastgele kabul edilir.")
