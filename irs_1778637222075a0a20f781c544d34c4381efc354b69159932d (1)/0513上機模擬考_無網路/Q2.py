'''
請為三角形面積計算公式設計一個名為HeronFormula類別，並撰寫一測試程式驗證此類別程式碼的正確性。
'''
import math

class HeronFormula:
    def __init__(self, a=0, b=0, c=0):
        """建構元方法：設定邊長a, b, c的初始值"""
        self.__a = a
        self.__b = b
        self.__c = c
    
    def inputSide(self):
        """公有方法：讓使用者輸入三邊長a,b,c，確認皆大於0"""
        while True:
            try:
                sides = input("請輸入大於0的三邊長：")
                values = sides.split(',')
                if len(values) != 3:
                    raise ValueError
                a, b, c = float(values[0]), float(values[1]), float(values[2])
                
                if a > 0 and b > 0 and c > 0:
                    self.__a = a
                    self.__b = b
                    self.__c = c
                    break
                else:
                    print("輸入錯誤，請重新輸入大於0的三邊長：", end="")
            except:
                print("輸入錯誤，請重新輸入大於0的三邊長：", end="")
    
    def getAssessResult(self):
        """公有方法：判斷三邊長是否可以構成三角形"""
    # 請寫上您的程式碼
    
    def getPerimeter(self):
        """公有方法：回傳三角形的週長，若無法構成三角形則回傳-1"""
        if self.getAssessResult():
            return self.__a + self.__b + self.__c
        else:
            return -1
    
    def getArea(self):
        """公有方法：回傳三角形的面積(Heron公式)，若無法構成三角形則回傳-1"""
    # 請寫上您的程式碼   


def main():
    print("HeronFormula 測試程式啟動")
    while True:
        triangle = HeronFormula()
        triangle.inputSide()
        
        if triangle.getAssessResult():
            perimeter = triangle.getPerimeter()
            area = triangle.getArea()
            print(f"您所輸入的三角形週長為{int(perimeter)}，面積為{area}。")
        else:
            print("所輸入的三個整數無法構成三角形")
        
        while True:
            response = input("繼續玩嗎？若想繼續玩，請按'y'或'Y': ")
            if response in ['y', 'Y']:
                break
            elif response in ['n', 'N']:
                return
            else:
                print("輸入錯誤，請重新輸入：")


# 測試程式
if __name__ == "__main__":
    main()
