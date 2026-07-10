# LAB 7 - FILE 1: BÀI 1, 2, 3 (DANH SÁCH CORPUS & STOPWORDS)
import nltk

def run():
    print("--- CÂU 1: LIỆT KÊ CÁC TÊN CỦA CORPUS ---")
    # Tải danh sách danh mục corpus nếu chưa có
    nltk.download('punkt', quiet=True)
    
    # Cách lấy một số corpus phổ biến có sẵn trong nltk.corpus
    print("Một số thuộc tính/kho ngữ liệu chính có sẵn trong nltk.corpus:")
    corpus_list = ['gutenberg', 'stopwords', 'names', 'movie_reviews', 'wordnet']
    for cp in corpus_list:
        print(f" - {cp}")

    print("\n--- CÂU 2 & 3: LIỆT KÊ VÀ KIỂM TRA STOPWORDS CỦA CÁC NGÔN NGỮ ---")
    nltk.download('stopwords', quiet=True)
    
    # Lấy danh sách các ngôn ngữ được hỗ trợ stopword
    languages = nltk.corpus.stopwords.fileids()
    print(f"Số lượng ngôn ngữ hỗ trợ stopword trong NLTK: {len(languages)}")
    print("Danh sách các ngôn ngữ:", languages)
    
    # In thử 5 từ stopword đầu tiên của một số tiếng phổ biến
    sample_langs = ['english', 'french', 'german', 'spanish']
    for lang in sample_langs:
        if lang in languages:
            sw_list = nltk.corpus.stopwords.words(lang)
            print(f" -> 5 stopword đầu tiên của [{lang}]: {sw_list[:5]}")

if __name__ == '__main__':
    run()