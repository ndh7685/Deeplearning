import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import torch
from torchvision import datasets, transforms


matplotlib.use('Agg')  # Bỏ dòng này nếu bạn đang chạy trên máy có giao diện đồ họa

# 🔹 Kiểm tra thiết bị
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Đang sử dụng thiết bị: {device}")


transform = transforms.Compose([transforms.ToTensor()])
data_folder = '~/data/FMNIST'  # Đường dẫn lưu dữ liệu
fmnist = datasets.FashionMNIST(data_folder, download=True, train=True, transform=transform)


tr_images = fmnist.data.numpy()  # Chuyển tensor về NumPy
tr_targets = fmnist.targets.numpy()  # Chuyển tensor về NumPy
print(f"Dữ liệu tải thành công! Số lượng ảnh: {len(tr_targets)}")


R, C = len(np.unique(tr_targets)), 10  
fig, ax = plt.subplots(R, C, figsize=(10, 10))


for label_class in range(R):
    label_x_rows = np.where(tr_targets == label_class)[0]  # Lấy index của ảnh có cùng nhãn
    for j in range(C):  # Duyệt qua từng ảnh trong hàng
        ix = np.random.choice(label_x_rows)  # Chọn ngẫu nhiên một ảnh từ lớp đó
        x = tr_images[ix]  # Lấy ảnh
        ax[label_class, j].imshow(x, cmap='gray')  # Hiển thị ảnh
        ax[label_class, j].axis('off')  # Ẩn trục


plt.tight_layout(pad=0.5)  # Điều chỉnh khoảng cách
plt.savefig("output.png")  # Luôn lưu ảnh ra file


if matplotlib.get_backend() != 'Agg':  # Kiểm tra nếu không phải chế độ server
    plt.show()

print("Hình ảnh đã được lưu vào 'output.png'")