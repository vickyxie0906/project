import datasource as ds  
import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import requests



class Window(tk.Tk):
    def __init__(self, lottery_name):  
        super().__init__()  
        
        bgImage = Image.open("lotto.png")
        self.tkImage = ImageTk.PhotoImage(bgImage)
        mainCanvas = tk.Canvas(self)
        mainCanvas.create_image(
            -30, -30, anchor=tk.NW, image=self.tkImage)  
        mainCanvas.pack(fill=tk.BOTH, expand=True)
        
        title_Label = tk.Label(mainCanvas, text="台灣彩卷最新開彩結果", fg="#f17432",bg="white", font=(
            "Arial", 20)).pack(padx=50, pady=50)   

        buttons_frame = tk.Frame(mainCanvas)
        buttons_frame.pack(padx=50, pady=(0, 40), )
        grid_row_nums = 5
       
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
            self,  text=cname, borderwidth=2, relief=tk.GROOVE)  
        self.displayFrame.pack(fill=tk.BOTH, padx=50, pady=(0, 30)) 
        tk.Label(self.displayFrame, text=data).pack(padx=10)


def main():
    window = Window(ds.lottery_name)
    window.title("台灣彩卷")
    window.resizable(0, 0)
    window.geometry("+450+10")
    window.mainloop()



if __name__ == "__main__":  
    main()
