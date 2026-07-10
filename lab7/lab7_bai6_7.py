# LAB 7 - FILE 3: BÀI 6, 7 (WORDNET: ĐỊNH NGHĨA, ĐỒNG NGHĨA & TRÁI NGHĨA)
import nltk
from nltk.corpus import wordnet

def run():
    print("--- CÂU 6: TÌM ĐỊNH NGHĨA VÀ VÍ DỤ CỦA MỘT TỪ QUA WORDNET ---")
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
    
    tu_can_tim = "stage"
    syns = wordnet.synsets(tu_can_tim)
    
    if syns:
        print(f"Từ cần tìm: '{tu_can_tim}'")
        print("Định nghĩa (Definition):", syns[0].definition())
        print("Ví dụ (Examples):", syns[0].examples())
    else:
        print(f"Không tìm thấy dữ liệu cho từ '{tu_can_tim}'")

    print("\n--- CÂU 7: TÌM TẬP HỢP TỪ ĐỒNG NGHĨA VÀ TRÁI NGHĨA ---")
    dong_nghia = set()
    trai_nghia = set()
    
    # Khảo sát từ 'good'
    for syn in wordnet.synsets("good"):
        for l in syn.lemmas():
            dong_nghia.add(l.name())
            if l.antonyms():
                trai_nghia.add(l.antonyms()[0].name())
                
    print("Từ đồng nghĩa (Synonyms) của 'good':", list(dong_nghia)[:10])
    print("Từ trái nghĩa (Antonyms) của 'good':", list(trai_nghia))

if __name__ == '__main__':
    run()