import tensorflow as tf
from tensorflow.keras import layers, models

print("================ CÂU 11: XÂY DỰNG & HUẤN LUYỆN MÔ HÌNH CNN ================")

# 1. Tải và Tiền xử lý dữ liệu Fashion MNIST
print("--> Đang tải dữ liệu Fashion MNIST...")
fashion_mnist = tf.keras.datasets.fashion_mnist
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

# Chuẩn hóa pixel về [0, 1]
X_train = X_train / 255.0
X_test = X_test / 255.0

# Reshape dữ liệu thêm kênh màu đơn (1)
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

print(f"Kích thước tập Train: {X_train.shape}")
print(f"Kích thước tập Test: {X_test.shape}")

# 2. Xây dựng kiến trúc CNN
print("\n--> Đang thiết lập kiến trúc CNN...")
model = models.Sequential([
    # Lớp Tích chập (Conv2D): 32 filters, kích thước 3x3, activation ReLU
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    
    # Lớp Pooling (MaxPooling2D)
    layers.MaxPooling2D((2, 2)),
    
    # Lớp Flatten để duỗi dữ liệu phẳng ra
    layers.Flatten(),
    
    # Lớp ẩn Dense 64 units, activation ReLU
    layers.Dense(64, activation='relu'),
    
    # Lớp đầu ra Dense 10 units (10 nhóm quần áo), activation Softmax
    layers.Dense(10, activation='softmax')
])

model.summary()

# 3. Biên dịch và Huấn luyện mô hình
print("\n--> Đang compile và fit mô hình trong 5 epochs...")
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Fit mô hình
history = model.fit(
    X_train, 
    y_train, 
    epochs=5, 
    validation_data=(X_test, y_test),
    batch_size=64
)

# 4. Đánh giá mô hình trên tập kiểm thử
print("\n--> Đang đánh giá mô hình trên tập Test...")
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=1)
print(f"\nĐộ chính xác (Accuracy) trên tập kiểm thử: {test_acc * 100:.2f}%")