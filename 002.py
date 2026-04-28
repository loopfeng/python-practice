#Tính tổng hai số nguyên bất kỳ(Có xử lý ngoại lệ đầu vào)
#Nhap gia tri thu nhat va chuyen sang kieu so nguyen
try:
    print('Nhap so thu nhat')
    so1 = int(input())

#Nhap gia tri thu hai va chuyen sang kieu so nguyen
    print('Nhap so thu hai')
    so2 = int(input())
    tong = so1 + so2 #Tinh tong hai so

#In tong hai so ra man hinh
    print("tong hai so la: ", tong)    
except:
    print("Định dạng đầu vào không hợp lệ")
