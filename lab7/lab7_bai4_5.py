# LAB 7 - FILE 2: BÀI 4, 5 (LOẠI BỎ VÀ BỎ QUA STOPWORDS)
import nltk

def run():
    print("--- CÂU 4: LOẠI BỎ STOPWORD TỪ MỘT VĂN BẢN CHO TRƯỚC ---")
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)
    
    van_ban = "Hello bro, this is a sample sentence showing how to filter out stopwords easily from text."
    print("Văn bản gốc:", van_ban)
    
    # Tách từ (Tokenize)
    words = nltk.word_tokenize(van_ban)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    
    # Lọc bỏ
    filtered_words = [w for w in words if w.lower() not in stop_words]
    print("Văn bản sau khi lọc bỏ stopword:", filtered_words)

    print("\n--- CÂU 5: BỎ QUA STOPWORDS TỪ DANH SÁCH STOPWORDS GỐC ---")
    # Ví dụ: Ta có một danh sách từ tự tạo, muốn bỏ qua (loại trừ) các từ nếu chúng nằm trong tập stopwords
    danh_sach_tu = ['apple', 'the', 'computer', 'is', 'running', 'and', 'good', 'to']
    print("Danh sách từ ban đầu:", danh_sach_tu)
    
    # Loại bỏ các từ trùng với stopword tiếng Anh
    ket_qua = [w for w in danh_sach_tu if w.lower() not in stop_words]
    print("Danh sách sau khi bỏ qua các từ là stopword:", ket_qua)

if __name__ == '__main__':
    run()