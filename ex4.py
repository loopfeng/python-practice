#Nhập số bất kỳ ở hệ thập phân và hiển thị ra ở hệ bát phân
"""Kiến thức cần có:
Hàm input() và hàm print()
Định dạng đầu ra trong Python
Biến và kiểu dữ liệu
"""
#Code tự gõ
a = float(input())
b = float(a/8)
print("So thap phan ", float(a), "trong he bat phan la ", float(b))
#Code mẫu
#Nhap gia tri tu ban phim va chuyen sang kieu so nguyen
soThapPhan = int(input())

#Xuat cau voi dinh dang theo yeu cau de bai
# %d dong vai tro giu cho cho 1 gia tri so thap phan
# %o dong vai tro giu cho cho 1 gia tri so bat phan
print('So thap phan %d trong he bat phan la %o' % (soThapPhan, soThapPhan))
#Làm lại
sothapphan = int(input())
print("Số thập phân %d trong hệ bát phân là %o ----- %o" % (sothapphan, sothapphan, 9))