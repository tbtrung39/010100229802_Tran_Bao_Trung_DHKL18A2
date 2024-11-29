#Bài 1: Nhập vào số nguyên dương n. 
#In ra màn hình dãy số các số nguyên tố nhỏ hơn n theo thứ tự từ nhỏ đến lớn
#Bài làm
ds_nguyen_to = []
while True:
    n = input("Nhap vao so nguyen duong n: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(1, n):
    if i == 1:
        ds_nguyen_to.append(i)
        continue
    for j in range(1,i):
        if i%j == 0 and j != 1 and i != j:
            break
    else:
        ds_nguyen_to.append(i)

ds_nguyen_to.sort()
print(ds_nguyen_to)
# #Tính tổng các giá trị trong danh sách
# tong = sum(ds_nguyen_to)
# print(tong)



#Bài 2: Nhập vào dãy A gồm n phần tử từ bàn phím. 
#Tính tổng các phần tử trong dãy A
ds_so = []
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu {i + 1}: ")
        if so.isdigit() == False:
            print("Yeu cau nhap vao so!!")
        else:
            so = float(so)
            break
    ds_so.append(so)

tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")

#Bài 3: Nhập vào số nguyên dương n.
#In ra màn hình: 
# - Danh sách A gồm các số lẻ nhỏ hơn n
# - Danh sách B gồm các số chẵn nhỏ hơn n
#Sắp xếp dãy số theo thứ tự giảm dần


#Bài 4: Viết chương trình sinh ra ma trận K kích cỡ m*n chỉ chứa số 0
#Bài làm
m = int(input("Nhap vao so cot cua ma tran m = "))
n = int(input("Nhap vao so hang cua ma tran n = "))
#0 ... m
#.     .
#.     .
#.     .
#n ... 0
ma_tran_a = [[0,0,0],
             [0,0,0],
             [0,0,0]]
ma_tran_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
print(ma_tran_a)

ma_tran_a = [[0]*m]*n 
print(ma_tran_a)

#Bài 5: Viết chương trình nhập vào n. Sinh ra ma trận đơn vị I kích cỡ n*n
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
n = int(input("Nhap vao n = "))
ma_tran_don_vi = []
for i in range(n):
    phan_tu_trong_hang = [0]*i + [1] + [0]*(n-1-i)
    ma_tran_don_vi.append(phan_tu_trong_hang)
print(ma_tran_don_vi)

#Bài 6: Viết chương trình nhập vào ma trận A kích cỡ m*n và in ra màn hình

#Bài 7: Viết chương trình đảo vị trí hai hàng i, j của ma trận A kích cỡ m*n
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
i = int(input("Nhap vao hang i: "))
j = int(input("Nhap vao hang J: "))
[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
temp = ma_tran_don_vi[i]
ma_tran_don_vi[i] = ma_tran_don_vi[j]
ma_tran_don_vi[j] = temp
print(ma_tran_don_vi)

#Bài 8: Viết chương trình đảo vị trí hai cột i, j của ma trận A kích cỡ m*n

#Bài 9: Viết chương trình nhập vào hai ma trận A, B có cùng kích thước.
#Tính:
# - Tổng hai ma trận A, B
# - Hiệu hai ma trận A, B
# - Tích của ma trận A với số k nhập từ bàn phím
# - Tích hai ma trận A, B
# - Ma trận đối xứng của ma trận A

#Bài 10: Lập một danh sách với n sinh viên bao gồm thông tin tên và điểm tổng kết cuối năm của các sinh viên đó
# thong_tin_sinh_vien = {"Hung": 4.0}
# ds_sinh_vien = [{"Hung": 4.0},{"Hung": 4.0},{"Hung": 4.0},{"Hung": 4.0}]
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {ten: diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)

#Bài 11: Viết lệnh in danh sách sinh viên ở bài 10. Có dạng:
#Ten    Diem
#Dung   10.0
#Quang  5.3
#Trang  7.5

#Bài 12: Viết lệnh xóa thông tin của sinh viên trong danh sách sinh viên ở bài 10 ứng với tên được nhập vào bàn phím

#Bài 13: Viết lệnh thêm một sinh viên vào danh sách sinh viên ở bài 10. Với điều kiện:
# - Nếu tên sinh viên đã tồn tại, thông báo: "Thông tin sinh viên đã tồn tại"
# - Nếu chưa có sinh viên này, thông báo: "Đã thêm sinh viên"

#Bài 14: Viết lệnh sửa thông tin của một sinh viên ở bài 10 ứng với tên được nhập vào bàn phím

#Bài 15: Viết một chương trình quản lý một danh sách sinh viên.
# Danh sách sinh viên chứa các thông tin:
# - "Mã sinh viên"
# - "Họ đệm"
# - "Tên"
# - "Điểm toán"
# - "Điểm lý"
# - "Điểm hóa"
# - "Điểm trung bình" được tính từ 3 điểm toán, lý, hóa
# Thiết kế chương trình quản lý có menu như sau:
# 1. Xem danh sách sinh viên
# 2. Nhập thông tin sinh viên mới vào danh sách
# 3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên
# 4. Xóa thông tin sinh viên ứng với mã sinh viên
# 5. Thoát chương trình