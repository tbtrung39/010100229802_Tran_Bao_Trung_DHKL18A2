#In dãy số các số lẻ nhỏ hơn n
n = int(input("Nhap vao so nguyen duong n: "))
for i in range(n): #-> chuỗi chạy từ 0 đến n-1
    if i%2 == 1:
        print(i)    
#In n các số Fibonacci 
a = 0
b = 1
n = int(input("Nhap vao so nguyen duong n: "))
for i in range(n):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b

#Tính tổng các số hạng từ 1 đến n
tong_s = 0
n = int(input("Nhap vao gia tri nguyen duong n: "))
for i in range(n + 1):
    tong_s = tong_s + i 

print(f"Tong cac so tu 1 den n {tong_s}")
#Tính giai thừa của số n (n!)
tich_p = 1
n = int(input("Nhap vao gia tri nguyen duong n: "))
for i in range(n + 1):
    if i == 0:
        continue
    tich_p = tich_p*i 

print(f"Tich giai thừa của số n {tich_p}")




# # Nhập vào 2 số a,b Tìm ước chung lớn nhất của hai số này
a = int(input("Nhap vao so nguyen duong a: " ))
b = int(input("Nhap vao so nguyen duong b: " ))
so_nho_nhat = a
if b <= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print(f"{k} la uoc chung lon nhat")
        break
    k = k - 1
    
# Kiểm tra số n có phải số nguyên tố hay không
# số nguyên tố là số nguyên dương lớn hơn 1 và chỉ chia hết cho 1 và chính nó

n = int(input("Nhap vao so nguyen duong can kiem tra: "))
if n <= 1:
    print("So nay khong phai la so nguyen to")
else:
    k = n
    for i in range(n):
        if n % k == 0 and k != n and k != 1:
            print("So nay khong phai la so nguyen to")
            break
        k = k - 1
    else:
        print("So nay la so nguyen to")
            
