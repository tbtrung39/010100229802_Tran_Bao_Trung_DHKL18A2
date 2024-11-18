#Bài 3: Nhập vào một chuỗi bất kỳ. Xóa tất cả các khoảng trống thừa trong chuỗi
#Ví dụ: "     chuoi     nhap   vao         "
nhap_chuoi_vao = input("Nhập chuỗi của bạn vào :")
bien_luu_tam = []
bien_hien_tai = ""
for chu in nhap_chuoi_vao :
    if chu != " ":
        bien_hien_tai += chu
    else :
        if bien_hien_tai != "":
            bien_luu_tam += [bien_hien_tai]
            bien_hien_tai =""
if bien_hien_tai != "" :
    bien_luu_tam += bien_hien_tai 
chuoi_ket_qua = " ".join(bien_luu_tam)
print(f"Chuỗi của bạn là {chuoi_ket_qua}")