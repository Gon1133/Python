try:
    ts = int(input('Nhập tử số: '))
    ms = int(input('Nhập mẫu số: '))
    kq = ts/ms
    print('Kết quả của phép chia là:',kq)
except ValueError:
    print('Giá trị không hợp lệ.')
except ZeroDivisionError:
    print('Mẫu số không thể là 0.')

try:
    ts = int(input('Nhập tử số: '))
    ms = int(input('Nhập mẫu số: '))
    kq = ts/ms
    print('Kết quả của phép chia là:',kq)
except (ValueError, ZeroDivisionError):
        print('Giá trị không hợp lệ.')
        print('Mẫu số không thể là 0.')
