while True:
    try:
        name=input("請輸入姓名")
        height=float(input('請輸入身高(cm):'))
        weight=float(input('請輸入體重(kg):'))
        bmi=round(weight/((height*0.01)**2),ndigits=2)
        if bmi<18.5:
            grade="體重過輕"
        elif bmi<24:
            grade="正常範圍"
        elif bmi<27:
            grade="過重"
        elif bmi<30:
            grade="輕度肥胖"
        elif bmi<35:
            grade="中度肥胖"
        else:
            grade="重度肥胖"
        print(f"{name}的bmi為{bmi},為{grade}")
            
    except ValueError:
        print("格式錯誤")
        continue
    decide=input("還要繼續嗎?('q':離開,enter:繼續)")
    if decide=='q':
                break
print("應用程式結束")