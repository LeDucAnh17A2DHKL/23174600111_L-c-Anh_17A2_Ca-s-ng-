def draw_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' + ' *' * i)

    for i in range(n-2, -1, -1):
        print(' ' * (n - i - 1) + '*' + ' *' * i)

# Thay đổi giá trị của n để thay đổi kích thước của hình
n = 5  
draw_pattern(n)
