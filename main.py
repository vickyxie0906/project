import datasource as ds  # 載入datasource 縮寫ds
import tkinter as tk  # 引入tkinter縮寫tk
from tkinter import ttk, messagebox
import requests


class Window(tk.Tk):
    def __init__(self, lottery_name):  # 建構子 (城市字典)
        super().__init__()  # 呼叫建構子父類別  # 建立視窗內容標題
        title_Label = tk.Label(self, text="台灣彩卷最新開彩結果", font=(
            "Arial", 20)).pack(padx=30, pady=30)  # 設定標籤文字的大小 字型 間距

        buttons_frame = tk.Frame(self)  # 建立框架
        buttons_frame.pack(padx=50, pady=(0, 30))

        # 建立存放按鈕的容器
        buttons_frame = tk.Frame(self)  # 建立框架
        buttons_frame.pack(padx=50, pady=(0, 30))  # 左右 上下 間距
        # 設定GRID的ROW數量
        grid_row_nums = 2
        # enumerate會回傳索引值 將數據組合為索引序列 一般用在迴圈 加上.items()回傳 key value
        for index, lname in enumerate(lottery_name.items()):
            # print(index,key)
            cname, ename = lname  # key value變數名 #command=self.button_click 註冊
            btn = tk.Button(buttons_frame, text=f"{cname}", font=(
                "Arial", 15), width=8, padx=20, pady=3)
            btn.grid(row=index % grid_row_nums, column=index //
                     grid_row_nums, padx=5, pady=5)
            btn.bind("<Button>", self.button_click)

    def button_click(self, event):
        # print(dir(event))查event方法
        # -->type=tkinter button  #說搞點擊後會抓該按鈕['text']字串的資料
        btn_text = event.widget['text']
        # widget抓按鈕文字 #屬性widget=button,抓資料["text"]取出文字
        # split分割 #說實體的方法要重新抓取按鈕文字 所以要用下一行來分割字串抓取
        name_list = btn_text.split("\n")
        cname = name_list[0]  # 抓分割後第0筆資料
        # ename = name_list[1]  # 抓分割後第1筆資料
        # print(f"{cname}-{ename}")

        # try:
        #  city_forcase = ds.get_forcast_data(ename, api_key)
        # # 去抓ds.get_forcast_data的函式
        # except Exception as e:
        #     # 出現錯誤訊息
        #     messagebox.showwarning("錯誤", "糟糕oops....").pack(
        #         side=tk.LEFT, padx=30, pady=30)
        #     return
        # 如果出錯就會跳出警告視窗
        # print(cname)

        # print(city_forcase)

        if hasattr(self, "displayFrame"):  # 檢查有沒有原框架
            self.displayFrame.destroy()  # 消滅原來顯示資料的框架 重新再建一個

        self.displayFrame = ttk.LabelFrame(
            self,  text=cname, borderwidth=2, relief=tk.GROOVE)  # 建立顯示資料的框架 relief按鈕邊框樣式
        self.displayFrame.pack(fill=tk.BOTH, padx=50, pady=(0, 30))  # 把寬高填滿


class DisplayFrame(ttk.LabelFrame):  # 繼承ttk.LabelFrame父類別

    def __init__(self, parent, data=None, **kwargs):  # **kwargs是打包上面DisplayFrame()裡text之後的內容
        super().__init__(parent, **kwargs)


def main():
    window = Window(ds.lottery_name)
    window.title("台灣彩卷")
    window.mainloop()


if __name__ == "__main__":
    # print("這裡是程式的執行點")#印出訊息
    main()
