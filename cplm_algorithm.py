import secrets

def generate_cplm_key(bit_length=512):

    # Başlangıç Durumları (1024-bit CSPRNG Seed)
    state_a = secrets.randbits(1024)
    state_b = secrets.randbits(1024)
    
    generated_bits = []
    iteration = 0
    
    while len(generated_bits) < bit_length:
        raw_pair = []
        while len(raw_pair) < 2:
            iteration += 1
            
            # Motor A: Collatz İterasyonu
            if state_a <= 4: 
                state_a += (secrets.randbits(512) | 1)
            
            if state_a % 2 == 0:
                state_a //= 2
            else:
                state_a = (3 * state_a + 1) // 2
                
            # Motor B: Collatz İterasyonu
            if state_b <= 4: 
                state_b += (secrets.randbits(512) | 1)
                
            if state_b % 2 == 0:
                state_b //= 2
            else:
                state_b = (3 * state_b + 1) // 2
                
            # Cross-Link: Motorlar arası veri etkileşimi (Her 8 adımda)
            if iteration % 8 == 0:
                state_a ^= (state_b & 0xFF)
                state_b ^= (state_a & 0xFF)

            # Bit Çıkarımı (Parity XOR)
            raw_pair.append((state_a % 2) ^ (state_b % 2))
            
        # Von Neumann Deskewing (İstatistiksel Filtreleme)
        b1, b2 = raw_pair[0], raw_pair[1]
        if b1 == 0 and b2 == 1:
            generated_bits.append(0)
        elif b1 == 1 and b2 == 0:
            generated_bits.append(1)
            
    return "".join(map(str, generated_bits))

if __name__ == "__main__":
    # Yapılandırma
    KEY_SIZE = 512
    print(f"--- CPLM Anahtar Üretici Başlatıldı ---")
    print(f"Hedef: {KEY_SIZE} bit\n")
    
    # Anahtar Üretimi
    final_key = generate_cplm_key(KEY_SIZE)
    
    print(f"Üretilen Nihai Anahtar:")
    print(final_key)
    
    # Analiz
    c0 = final_key.count('0')
    c1 = final_key.count('1')
    denge = (min(c0, c1) / max(c0, c1)) * 100
    
    print(f"\n[Analiz]")
    print(f"0 Sayısı: {c0} | 1 Sayısı: {c1}")
    print(f"İstatistiksel Başarı: %{denge:.2f}")
