def hollow_triangle(n):
    # 檢查輸入的數字是否有效
    if n <= 0:
        return "請輸入大於0的數字"

    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        
        for k in range(2 * i - 1):
            if i == n or k == 0 or k == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        
        print()  # 每行結束後換行

# 測試輸入
hollow_triangle(3)