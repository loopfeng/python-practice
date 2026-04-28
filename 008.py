#Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, dãy số nằm trên 1 dòng, các sô cách nhau bởi khoảng trắng. TÍnh tổng của dãy số và hiển thị ra màn hình.
dayGiaTri = input('Nhập vào dãy các số cách nhau bởi khoảng trắng: ')
danhSachGiaTri = dayGiaTri.split()
print(danhSachGiaTri)
danhSachSo = map(int, danhSachGiaTri)
tongDaySo = sum(danhSachSo)
print("Tổng của dãy số: ", tongDaySo)