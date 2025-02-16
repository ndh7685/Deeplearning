import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv("processed_dulieuxettuyendaihoc.csv")

# Phan7: Trực quan dữ liệu số lượng thí sinh đậu, rớt dựa trên từng nhóm giới tính
df["KQ"] = df["KQXT"].apply(lambda x: "Đậu" if x > 0 else "Rớt")
cau37_plot = df.groupby(["GT", "KQ"]).size().reset_index(name="Số lượng")

plt.figure(figsize=(10, 6))
sns.barplot(data=cau37_plot, x="GT", y="Số lượng", hue="KQ", palette="Set2")
plt.xlabel("Giới tính")
plt.ylabel("Số lượng thí sinh")
plt.title("Số lượng thí sinh đậu, rớt theo từng nhóm giới tính")
plt.legend(title="Kết quả")
plt.show()
