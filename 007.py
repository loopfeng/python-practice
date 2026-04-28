#Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. 
# A và B được nhập bất kỳ từ bàn phím.
# Hiển thị số A sau khi được làm tròn ra màn hình.
# Có xử lý ngoại lệ đầu vào
giatriA = input()
giatriB = input()

isParseDone = False
try:
    soA = float(giatriA)
    soB = int(giatriB)
    isParseDone = True
except:
    print('Định dạng đầu vào không hợp lệ!')
    # Format 

if isParseDone:
    print('Dùng format: {0:.{1}f}'.format(soA, soB))
        #Dùng hàm round
    formatedNum = round(soA, soB)
    print('Dùng round', formatedNum)