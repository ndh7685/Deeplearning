#Phan3.1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("processed_dulieuxettuyendaihoc.csv")
df_female = df[df["GT"] == "F"]
grade_order = ["Y", "TB", "K", "G", "XS"]
df_melted = df_female.melt(id_vars=["GT"], value_vars=["XL1", "XL2", "XL3"], 
                            var_name="Nhóm", value_name="Xếp loại")
plt.figure(figsize=(10, 6))
sns.countplot(data=df_melted, x="Nhóm", hue="Xếp loại", order=["XL1", "XL2", "XL3"], 
              hue_order=grade_order, palette="viridis")
plt.xlabel("Nhóm xếp loại")
plt.ylabel("Số lượng học sinh nữ")
plt.title("Phân bố học sinh nữ theo xếp loại")
plt.legend(title="Xếp loại")
plt.show()
#Phan3.2
# Lọc dữ liệu học sinh có khối thi A, A1, B thuộc khu vực 1, 2
cau32 = df[ ( (df["KT"]=='A')| (df["KT"]=='A1')| (df["KT"]=='B'))& ((df["KV"]=='1')| (df["KV"]=='2'))]
clum = ['KT','KV','KQXT']
print(cau32[clum])
#b2: dem du lieu: vd: KV1. Khoi A, KQXT =0 thì có bao nhiêu giá trị
cau32_plot = cau32.groupby(['KT','KV','KQXT'])[['KQXT']].count()
cau32_plot.plot.bar()
plt.show()
