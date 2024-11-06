#Vòng lặp trong Python
#Vòng lặp có giới hạn (vòng lặp for)

#các kiểu dữ liệu tuần tự: string, list, tuple, set, dictionary
# range()
# for abc in range(10):
#     print(abc)
#range(10) -> 0,1,2,3,4,5,6,7,8,9
#range khi truyền giá trị mặc định yêu cầu phải là giá trị nguyên dương
#các giá trị trong range sẽ chạy từ 0 đến n - 1

#Khi sử dụng vong lặp nên kết hợp sử dụng với các câu lệnh điều kiện
#(Khi sử dụng vòng lặp nên có mục đích rõ ràng)

#Trong python vòng lặp cung cấp cho người dùng 3 công cụ: break, continue, else
#break: Dừng vòng lặp ngay lập tức thoát tại lần lặp gặp break
for i in range(10):
    if i == 4:
        break
    print(i)

#continue: Vòng lặp sẽ bỏ qua lần lặp mà ở đấy xuất hiện continue
for i in range(10):
    if i == 4:
        continue
    print(i)

#else: Vòng lặp sẽ chạy các câu lệnh xử lý của else trong trường hợp 
#      vòng lặp không gặp break
for i in range(10):
    if i == 4:
        break
    print(i)
else:
    print("Chay cau lenh else")
    
for i in range(10):
    if i == 4:
        continue
    print(i)
else:
    print("Chay cau lenh else")
#Vòng lặp không giới hạn (vòng lặp while)