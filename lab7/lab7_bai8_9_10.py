# LAB 7 - FILE 4: BÀI 8, 9, 10 (POS TAGSETS VÀ ĐỘ TƯƠNG ĐỒNG TỪ VỰNG)
import nltk
from nltk.corpus import wordnet

def run():
    print("--- CÂU 8: TỔNG QUAN VỀ BỘ TAG (PART-OF-SPEECH TAGSETS) ---")
    nltk.download('tagsets', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    
    print("Chi tiết của một tag cụ thể (Ví dụ tag 'NN' - Danh từ):")
    nltk.help.upenn_tagset('NN')

    print("\n--- CÂU 9: SO SÁNH SỰ GIỐNG NHAU GIỮA HAI DANH TỪ ---")
    # Lấy tập ngữ nghĩa (synset) của 2 danh từ
    danh_tu_1 = wordnet.synset('dog.n.01')
    danh_tu_2 = wordnet.synset('cat.n.01')
    
    # Tính toán độ tương đồng Wu-Palmer Similarity
    do_tuong_dong_n = danh_tu_1.wup_similarity(danh_tu_2)
    print(f"Độ giống nhau giữa danh từ '{danh_tu_1.name()}' và '{danh_tu_2.name()}': {do_tuong_dong_n:.4f}")

    print("\n--- CÂU 10: SO SÁNH SỰ GIỐNG NHAU GIỮA HAI ĐỘNG TỪ ---")
    dong_tu_1 = wordnet.synset('run.v.01')
    dong_tu_2 = wordnet.synset('walk.v.01')
    
    do_tuong_dong_v = dong_tu_1.wup_similarity(dong_tu_2)
    print(f"Độ giống nhau giữa động từ '{dong_tu_1.name()}' và '{dong_tu_2.name()}': {do_tuong_dong_v:.4f}")

if __name__ == '__main__':
    run()