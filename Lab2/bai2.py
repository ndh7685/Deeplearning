import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file
file_du_lieu = 'processed_dulieuxettuyendaihoc.csv'
du_lieu = pd.read_csv(file_du_lieu)

# 1. Trình bày dữ liệu biến Giới Tính (GT)
tan_so_GT = du_lieu['GT'].value_counts()
tan_suat_GT = du_lieu['GT'].value_counts(normalize=True) * 100

# Vẽ biểu đồ tần số, tần suất và tần suất tích lũy
plt.figure(figsize=(12, 5))

# Biểu đồ tần số (cột)
plt.subplot(1, 3, 1)
tan_so_GT.plot(kind='bar', color='lightblue')
plt.title('Biểu đồ Tần số của Giới Tính')
plt.xlabel('Giới Tính')
plt.ylabel('Tần số')

# Biểu đồ tần suất (tròn)
plt.subplot(1, 3, 2)
tan_suat_GT.plot(kind='pie', autopct='%1.1f%%')
plt.title('Biểu đồ Tần suất của Giới Tính')
plt.title('Biểu đồ Tích lũy Tần suất của Giới Tính')
plt.xlabel('Giới Tính')
plt.tight_layout()
plt.show()

# 2. Trình bày dữ liệu cho các biến US_TBM1, US_TBM2, US_TBM3
for bien in ['US_TBM1', 'US_TBM2', 'US_TBM3']:
    sns.histplot(du_lieu[bien], kde=True, color='green')
    plt.title(f'Phân phối điểm của {bien}')
    plt.xlabel(bien)
    plt.ylabel('Tần số')
    plt.show()

# 3. Trình bày dữ liệu biến Dân Tộc (DT) với các học sinh nam
hoc_sinh_nam = du_lieu[du_lieu['GT'] == 'Nam']
sns.countplot(x='DT', data=hoc_sinh_nam, palette='Set2')
plt.title('Phân phối Dân Tộc của học sinh Nam')
plt.xlabel('Dân Tộc')
plt.ylabel('Tần số')
plt.show()

# 4. Trình bày dữ liệu biến Khu Vực (KV) với học sinh nam dân tộc Kinh và thỏa điều kiện điểm số
hoc_sinh_kinh = hoc_sinh_nam[(hoc_sinh_nam['DT'] == 'Kinh') & 
                             (hoc_sinh_nam['DH1'] >= 5.0) & 
                             (hoc_sinh_nam['DH2'] >= 4.0) & 
                             (hoc_sinh_nam['DH3'] >= 4.0)]

plt.figure(figsize=(8, 6))
sns.barplot(x=hoc_sinh_kinh['KV'].value_counts().index, 
            y=hoc_sinh_kinh['KV'].value_counts().values, palette='coolwarm')
plt.title('Phân phối Khu Vực của học sinh Nam dân tộc Kinh (đủ điểm)')
plt.xlabel('Khu Vực')
plt.ylabel('Tần số')
plt.show()

# 5. Trình bày dữ liệu các biến DH1, DH2, DH3 lớn hơn hoặc bằng 5.0 và thuộc khu vực 2NT
hoc_sinh_2nt = du_lieu[(du_lieu['DH1'] >= 5.0) & 
                        (du_lieu['DH2'] >= 5.0) & 
                        (du_lieu['DH3'] >= 5.0) & 
                        (du_lieu['KV'] == '2NT')]

plt.figure(figsize=(15, 5))
for i, diem in enumerate(['DH1', 'DH2', 'DH3'], 1):
    plt.subplot(1, 3, i)
    sns.boxplot(y=hoc_sinh_2nt[diem], color='orange')
    plt.title(f'Phân phối điểm {diem} (>=5.0) trong khu vực 2NT')
    plt.ylabel('Điểm')

plt.tight_layout()
plt.show()
