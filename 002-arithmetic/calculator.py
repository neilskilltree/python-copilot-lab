def main():
    """
    簡單的計算機程式，接受使用者輸入並計算結果
    """
    # 顯示歡迎訊息，告訴使用者如何結束程式
    print("簡單計算機 (輸入 'exit' 結束程式)")

    # 無限迴圈，持續接受使用者輸入
    while True:
        # 取得使用者輸入的算式
        user_input = input("\n請輸入算式: ")

        # 檢查使用者是否想要結束程式
        if user_input.lower() == "exit":
            print("再見！")
            break  # 跳出迴圈，結束程式

        # 將 ^ 符號轉換成 Python 的次方運算符號 **
        user_input = user_input.replace("^", "**")

        # 嘗試計算使用者輸入的算式
        try:
            # 使用 eval() 計算算式的結果
            result = eval(user_input)
            # 顯示計算結果
            print(f"結果: {result}")
        except Exception as e:
            # 如果輸入的格式錯誤，顯示友善的錯誤訊息
            print("❌ 輸入格式錯誤，請輸入有效的算式 (例如: 1+2, 5*3, 10/2, 2^3)")


if __name__ == "__main__":
    main()
