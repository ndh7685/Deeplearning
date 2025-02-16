import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("processed_dulieuxettuyendaihoc.csv")

# Phan6: Trực quan dữ liệu số lượng thí sinh đậu, rớt dựa trên từng nhóm dân tộc
df["KQ"] = df["KQXT"].apply(lambda x: "Đậu" if x > 0 else "Rớt")
cau36_plot = df.groupby(["DT", "KQ"]).size().reset_index(name="Số lượng")

plt.figure(figsize=(10, 6))
sns.barplot(data=cau36_plot, x="DT", y="Số lượng", hue="KQ", palette="Set2")
plt.xlabel("Dân tộc")
plt.ylabel("Số lượng thí sinh")
plt.title("Số lượng thí sinh đậu, rớt theo từng nhóm dân tộc")
plt.xticks(rotation=45)
plt.legend(title="Kết quả")
plt.show()