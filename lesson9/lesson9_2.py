class BMI():
    def __init__(self,name:str,height:float,weight:float):
        self.__name=name
        self.height=height
        self.weight=weight
    
    @property  ##只能讀出，不能寫入
    def name(self)->str:
        return self.__name

    def getBMI(self)->float:
        return round(self.weight/((self.height*0.01)**2),ndigits=2);

    def get_status_message(self)->str:
        self.bmi=self.getBMI()

        if self.bmi<18.5:
            return "體重過輕"
        elif self.bmi<24:
            return "正常範圍"
        elif self.bmi<27:
            return "過重"
        elif self.bmi<30:
            return "輕度肥胖"
        elif self.bmi<35:
            return "中度肥胖" 
        elif self.bmi>=35:
            return "重度肥胖"

while True:
    try:
        name=input("請輸入姓名:")
        height=float(input('請輸入身高(cm):'))
        weight=float(input('請輸入體重(kg):'))

        #建立一個BMI的實體
        myBMI=BMI(name=name,height=height,weight=weight)

        #myBMI.name='xxxx'
        print(f"{myBMI.name} 的 BMI 為 {myBMI.getBMI()},為{myBMI.get_status_message()}")
    
    except ValueError:
        print("格式錯誤")
        continue
    stuff=input("請問是否繼續輸入資料 ('q':離開,任意鍵:繼續)?")
    if stuff=='q':
        break

print("應用程式結束")