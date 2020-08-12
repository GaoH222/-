import tkinter as tk
import pyautogui as gui
import time
window = tk.Tk()
window.title('微中刷屏1.0.0')
window.geometry('800x600')
mima = [123456]
mima_2 = [654321]

photo = tk.PhotoImage(file="mn.png")
ph_now = tk.Label(window, image=photo, compound=tk.CENTER)
ph_now.pack()

var_1 = tk.StringVar()
var_2 = tk.StringVar()

e1 = tk.Entry(window, textvariable=var_1, show=None, font=('Arial', 13))
e2 = tk.Entry(window, textvariable=var_2, show="*", font=("Arial", 13))
e1.place(x=310,y=300)
e2.place(x=310,y=325)



var = tk.StringVar()
lv = tk.Label(window, textvariable=var, width=40, height=3,bg="lightblue")
lv.place(x= 500,y = 300)

l = tk.Label(window, text="请输入账号", width=15, height=1,font=("宋体",10))
l.place(x= 170,y = 305)

ll = tk.Label(window, text="请输入密码", width=15, height=1,font=("宋体",10))
ll.place(x= 170,y = 326)

def jk_li():
        nam = int(var_1.get())
        nam2 = int(var_2.get())

        if nam == mima[0]:
            if nam2 == mima_2[0]:
                var.set("成功登录")
                window.destroy()
                window_1 = tk.Tk()
                window_1.title("工作台")
                window_1.geometry("800x600")

                var_3 = tk.StringVar()
                var_4 = tk.StringVar()
                var_5 = tk.StringVar()

                lv2 = tk.Entry(window_1,textvariable=var_3, show=None, font=('Arial', 13))
                lv3 = tk.Entry(window_1,textvariable=var_4, show=None, font=('Arial', 13))
                lv2.place(x=270, y=170)
                lv3.place(x=270, y=200)

                lv4 = tk.Entry(window_1, textvariable=var_5, show=None, font=('Arial', 13))
                lv4.place(x=270,y=230)


                def att():
                    nam3 = str(var_3.get())
                    nam4 = str(var_4.get())
                    nam5 = int(var_5.get())
                    gui.hotkey('ctrl', 'alt', 'z')
                    for i in range(0, nam5):
                        gui.typewrite(message=nam3)
                        gui.hotkey(' ')
                        gui.hotkey('Enter')
                        time.sleep(0.05)
                        gui.typewrite(message=nam4)
                        gui.hotkey(' ')
                        gui.hotkey('Enter')
                b2 = tk.Button(window_1, text="开始工作", width=20, height=2, command=att)
                b2.place(x=270, y=450)

                def attf():
                    window_2 = tk.Toplevel()
                    window_2.title("注意事项")
                    window_2.geometry("600x400")
                    lt = tk.Label(window_2, text="①请打开需要发送qq消息的聊天框并最小化\n②注意您可以输入内容-1和内容-2\n③内容-1和-2需要都是英文：例如：写\"失败\"需要输入\"shibai\""
                                                 "\n④举例：内容-1：nihao\n\t内容-2：dage\n\t请输入重复次数：2\n\t打到聊天框为：你好\n\t\t大哥\n\t\t你好\n\t\t大哥", width=600, height=400, font=("宋体", 10))
                    lt.pack()

                b3 = tk.Button(window_1, text="查看注意事项", width=20, height=2, command=attf)
                b3.place(x=270, y=500)

                l1 = tk.Label(window_1, text="刷屏的内容-1", width=15, height=1, font=("宋体", 10))
                l2 = tk.Label(window_1, text="刷屏的内容-2", width=15, height=1, font=("宋体", 10))
                l3 = tk.Label(window_1, text="请输入重复次数", width=15, height=1, font=("宋体", 10))

                l1.place(x=120, y=175)
                l2.place(x=120, y=205)
                l3.place(x=120, y=235)

                window_1.mainloop()
            else:
                var.set("密码错误请联系qq群1065166032")

        elif nam != mima[0]:
            var.set("密码错误请联系qq群1065166032")

b = tk.Button(window, text="登录", width=20, height=2, command=jk_li)
b.place(x=310,y=348)

window.mainloop()