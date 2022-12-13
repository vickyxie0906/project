import datasource as ds  # 載入datasource 縮寫ds
import tkinter as tk  # 引入tkinter縮寫tk
from tkinter import ttk, messagebox
import requests


class Window(tk.Tk):
    def __init__(self, lottery_name):  
        super().__init__()  
        title_Label = tk.Label(self, text="台灣彩卷最新開彩結果", fg="#f17432", font=(
            "Arial", 20)).pack(padx=30, pady=30)  # 設定標籤文字的大小 字型 間距

        buttons_frame = tk.Frame(self) 
        buttons_frame.pack(padx=50, pady=(0, 30))

        # 建立存放按鈕的容器
        buttons_frame = tk.Frame(self) 
        buttons_frame.pack(padx=50, pady=(0, 30)) 
        grid_row_nums = 2
       
        for index, lname in enumerate(lottery_name.items()):
         
            cname, ename = lname 
            btn = tk.Button(buttons_frame, text=f"{cname}", bg="#f1e767", bd=4, font=(
                "Arial", 15, "bold"), width=8, padx=20, pady=3, activeforeground="#f1e767")
            
            btn.grid(row=index % grid_row_nums, column=index //
                     grid_row_nums, padx=4, pady=4)
            btn.bind("<Button>", self.button_click)

    def button_click(self, event):
 
        btn_text = event.widget['text']
        name_list = btn_text.split("\n")
        cname = name_list[0] 
       
     
        try:
         data = ds.get_data(cname)
  
        except Exception as e:
          
            messagebox.showwarning("錯誤", "糟糕oops....").pack(
                side=tk.LEFT, padx=30, pady=30)
            return
      

        if hasattr(self, "displayFrame"):  
            self.displayFrame.destroy()  

        self.displayFrame = ttk.LabelFrame(
            self,  text=cname, borderwidth=2, relief=tk.GROOVE)  # 建立顯示資料的框架 relief按鈕邊框樣式
        self.displayFrame.pack(fill=tk.BOTH, padx=50, pady=(0, 30)) 
        tk.Label(self.displayFrame, text=data).pack(padx=10)


def main():
    window = Window(ds.lottery_name)
    window.title("台灣彩卷")
    window.mainloop()


if __name__ == "__main__":  
    main()
