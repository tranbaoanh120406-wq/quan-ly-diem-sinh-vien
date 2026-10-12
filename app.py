
import streamlit as st

# YEU CAU 1: TAO DATAFRAME
data = {
    "Ho va ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Hoang Nam",
        "Pham Thi Lan",
        "Nguyen Minh Anh",
        "Tran Quoc Bao",
        "Le Thi Hoa",
        "Pham Minh Tuan",
        "Hoang Ngoc Mai",
        "Do Thanh Dat"
    ],
    "Chuyen_can": [9, 8, 10, 7, 9, 8, 10, 6, 9, 8],
    "Giua_ky":    [8, 7, 9, 6, 8, 7, 9, 5, 8, 7],
    "Cuoi_ky":    [9, 8, 8, 7, 9, 8, 10, 6, 9, 8]
}

# Chuyen du lieu thanh DataFrame
df = pd.DataFrame(data)

# YEU CAU 2: TINH DIEM TONG KET
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

# Lam tron diem den 2 chu so thap phan
df["Tong_ket"] = df["Tong_ket"].round(2)

# HIEN THI BANG DU LIEU
print("BANG DIEM SINH VIEN")
st.dataframe(df).


# YEU CAU 3: XEP LOAI SINH VIEN

def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

# Them cot Xep_loai vao DataFrame
df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Hien thi bang diem va xep loai
print("BANG DIEM VA XEP LOAI SINH VIEN")
display(df)


# YEU CAU 4: THONG KE

# 1. Diem tong ket trung binh cua lop
diem_tb = df["Tong_ket"].mean()
print("Diem tong ket trung binh cua lop:", round(diem_tb, 2))

# 2. Sinh vien co diem tong ket cao nhat
diem_cao_nhat = df["Tong_ket"].max()
print("Diem cao nhat:", diem_cao_nhat)
print("Sinh vien co diem cao nhat:")
display(df.loc[df["Tong_ket"] == diem_cao_nhat,
               ["Ho va ten", "Tong_ket"]])

# 3. Sinh vien co diem tong ket thap nhat
diem_thap_nhat = df["Tong_ket"].min()
print("Diem thap nhat:", diem_thap_nhat)
print("Sinh vien co diem thap nhat:")
display(df.loc[df["Tong_ket"] == diem_thap_nhat,
               ["Ho va ten", "Tong_ket"]])

# 4. Dem so sinh vien dat (diem >= 5)
so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()
print("So sinh vien dat:", so_sinh_vien_dat)


# YEU CAU 5: TRUC QUAN HOA DU LIEU

import matplotlib.pyplot as plt

# Lay ten sinh vien va diem tong ket
ten = df["Ho va ten"]
diem = df["Tong_ket"]

# Tao bieu do cot
plt.figure(figsize=(10, 6))
plt.bar(ten, diem)

# Dat tieu de va ten truc
plt.title("DIEM TONG KET CUA 10 SINH VIEN")
plt.xlabel("Ho va ten sinh vien")
plt.ylabel("Diem tong ket")

# Gioi han truc diem tu 0 den 10
plt.ylim(0, 10)

# Hien thi ten sinh vien nghieng de de doc
plt.xticks(rotation=45, ha="right")

# Hien thi gia tri diem tren dau moi cot
for i, d in enumerate(diem):
    plt.text(i, d + 0.1, str(d), ha="center")

# Dieu chinh khoang cach va hien thi bieu do
plt.tight_layout()
plt.show()

 
