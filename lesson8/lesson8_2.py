from widget import tools  # from 後面可放 package(資料夾) 或 module

#主程式
while True:
    try:
        name=input("請輸入姓名:")
        height=float(input('請輸入身高(cm):'))
        weight=float(input('請輸入體重(kg):'))
        bmi=weight/((height*0.01)**2)
        grade=tools.get_status_message(bmi)
        print(f"{name} 的 BMI 為 {bmi:.2f},為{grade}")
    except ValueError:
        print("格式錯誤")
        continue
    stuff=input("請問是否繼續輸入資料 ('q':離開,任意鍵:繼續)?")
    if stuff=='q':
        break
print("應用程式結束\n")