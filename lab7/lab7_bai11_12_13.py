# LAB 7 - FILE 5: BÀI 11, 12, 13 (XỬ LÝ KHO NGỮ LIỆU TÊN NAMES CORPUS)
import nltk
import random

def run():
    print("--- CÂU 11: ĐẾM SỐ LƯỢNG VÀ IN 10 TÊN NAM/NỮ ĐẦU TIÊN ---")
    nltk.download('names', quiet=True)
    
    names_corpus = nltk.corpus.names
    nam_tuyen_tap = names_corpus.words('male.txt')
    nu_tuyen_tap = names_corpus.words('female.txt')
    
    print(f"Tổng số lượng tên Nam: {len(nam_tuyen_tap)}")
    print(f"Tổng số lượng tên Nữ: {len(nu_tuyen_tap)}")
    print("10 tên Nam đầu tiên:", nam_tuyen_tap[:10])
    print("10 tên Nữ đầu tiên:", nu_tuyen_tap[:10])

    print("\n--- CÂU 12: IN 15 KẾT HỢP NGẪU NHIÊN ĐƯỢC GẮN NHÃN NAM VÀ NỮ ---")
    # Gắn nhãn
    labeled_names = ([(name, 'male') for name in nam_tuyen_tap] + 
                     [(name, 'female') for name in nu_tuyen_tap])
    
    # Trộn ngẫu nhiên bằng seed để cố định kết quả
    random.seed(42)
    random.shuffle(labeled_names)
    
    print("15 kết hợp ngẫu nhiên đầu tiên (Tên, Nhãn):")
    for i, item in enumerate(labeled_names[:15], 1):
        print(f" {i}. {item[0]} -> Nhãn: {item[1]}")

    print("\n--- CÂU 13: TRÍCH XUẤT KÝ TỰ CUỐI CÙNG CỦA TÊN VÀ TẠO MẢNG MỚI ---")
    # Tạo mảng mới chứa chữ cái cuối và nhãn liên kết
    last_letter_features = [(name[-1].lower(), gender) for (name, gender) in labeled_names]
    print("Trích xuất 10 dòng đầu tiên của mảng đặc trưng chữ cái cuối cùng:")
    for i, item in enumerate(last_letter_features[:10], 1):
        print(f" Dòng {i}: Chữ cái cuối: '{item[0]}' | Nhãn giới tính: '{item[1]}'")

if __name__ == '__main__':
    run()