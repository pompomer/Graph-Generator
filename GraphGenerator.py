import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk as ttk
import matplotlib as mpl


font = {"family":"Noto Sans CJK JP"}
mpl.rc('font', **font)


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    # widgetの作成
    def create_widgets(self):
        self.create_frame()
        self.create_frame_left()
        self.create_frame_center()
        self.create_frame_right()

    # Frame作成
    def create_frame(self):
        self.frame_left = tk.Frame(self)
        self.frame_left.grid(row=0, column=0, sticky=tk.NW)
        self.frame_center = tk.Frame(self)
        self.frame_center.grid(row=0, column=1, sticky=tk.NW)
        self.frame_right = tk.Frame(self)
        self.frame_right.grid(row=0, column=2, sticky=tk.NW)

    # 左Frame作成
    def create_frame_left(self):
        label_X = tk.Label(self.frame_left, text="X-axis name")
        label_X.grid(row=1, column=0)
        self.entry_X = tk.Entry(self.frame_left, justify=tk.CENTER)
        self.entry_X.grid(row=1, column=1)

        label_Y1 = tk.Label(self.frame_left, text="Y1-axis name")
        label_Y1.grid(row=2, column=0)
        self.entry_Y1 = tk.Entry(self.frame_left, justify=tk.CENTER)
        self.entry_Y1.grid(row=2, column=1)
    
        label_Y2 = tk.Label(self.frame_left, text="Y2-axis name")
        label_Y2.grid(row=3, column=0)
        self.entry_Y2 = tk.Entry(self.frame_left, justify=tk.CENTER)
        self.entry_Y2.grid(row=3, column=1)

        self.button_apply = tk.Button(self.frame_left, text="Output", command=self.create_graph)
        self.button_apply.grid(row=4, column=1)

        self.button_import = tk.Button(self.frame_left, text="Import file", command=self.import_file)
        self.button_import.grid(row=5, column=1)

    # 中央Frame作成
    def create_frame_center(self):

        # ウィンドウサイズに合わせて中央線を延長
        root.update_idletasks()
        wy = self.frame_left.winfo_height()
        self.canvas = tk.Canvas(self.frame_center, width=1, height=wy, bg="black")
        self.canvas.pack()

    # 右Frame作成
    def create_frame_right(self):
        self.label_X = tk.Label(self.frame_right, text="X", justify=tk.CENTER)
        self.label_X.grid(row=0, column=0)

        self.label_Y1 = tk.Label(self.frame_right, text="Y1", justify=tk.CENTER)
        self.label_Y1.grid(row=0, column=1)

        self.label_Y2 = tk.Label(self.frame_right, text="Y2", justify=tk.CENTER)
        self.label_Y2.grid(row=0, column=2)

        self.label_Label = tk.Label(self.frame_right, text="Label", justify=tk.CENTER)
        self.label_Label.grid(row=0, column=3)

        self.label_Marker = tk.Label(self.frame_right, text="Marker", justify=tk.CENTER)
        self.label_Marker.grid(row=0, column =4)

        self.label_Line = tk.Label(self.frame_right, text="Line", justify=tk.CENTER)
        self.label_Line.grid(row=0, column=5)

        self.label_Approx = tk.Label(self.frame_right, text="Approx",justify=tk.CENTER)
        self.label_Approx.grid(row=0, column=6)

        self.label_Degree = tk.Label(self.frame_right, text="Degree", justify=tk.CENTER)
        self.label_Degree.grid(row=0, column=7)

        self.label_ApproxLabel = tk.Label(self.frame_right, text="ApproxLabel", justify=tk.CENTER)
        self.label_ApproxLabel.grid(row=0, column=8)

    # センターライン作成
    def centerline(self):
        root.update_idletasks()
        x = self.frame_left.winfo_height()
        y = self.frame_right.winfo_height()

        if (x > y):
            self.canvas["height"] = x
        else:
            self.canvas["height"] = y
        

    # ファイルのインポート
    def import_file(self):
        filename = tk.filedialog.askopenfilename()

        if filename!="":

            with open(filename, "r") as f:
                #ヘッダ判定
                while True:

                    try:
                        self.data = np.loadtxt(f, dtype="float", skiprows=0, delimiter=",")                  
                    except ValueError:                   
                        pass
                    else:
                        break

            self.create_graph_status()
           
        self.centerline()


    # チェックボックス生成
    def create_graph_status(self):

        def func():
            self.row = len(self.data)
            self.column = max([len(v) for v in self.data])
            print(self.row)
            
            # widget初期化
            self.frame_right.destroy()
            self.frame_right = tk.Frame(self)
            self.frame_right.grid(row=0, column=2, sticky=tk.NW)
            self.create_frame_right()

            # X軸ラジオボタン
            self.var_X = tk.IntVar()
            for i in range(self.column):
                self.radio = tk.Radiobutton(self.frame_right, value=i, variable=self.var_X)
                self.radio.grid(row=i+2, column=0)

            # Y1軸チェックボタン
            self.var_Y1 = []
            self.checkbutton_Y1 = []
            for i in range(self.column):
                self.var_Y1.append(tk.BooleanVar())
                self.checkbutton_Y1.append(tk.Checkbutton(self.frame_right, variable=self.var_Y1[i]))
                self.checkbutton_Y1[i].grid(row=i+2, column=1)

            # Y2軸チェックボタン
            self.var_Y2 = []
            self.checkbutton_Y2 = []
            for i in range(self.column):
                self.var_Y2.append(tk.BooleanVar())
                self.checkbutton_Y2.append(tk.Checkbutton(self.frame_right, variable=self.var_Y2[i]))
                self.checkbutton_Y2[i].grid(row=i+2, column=2)
      
            # Label入力ボックス
            self.entry_Label = []
            for i in range(self.column):
                self.entry_Label.append(tk.Entry(self.frame_right, justify=tk.RIGHT, width=10))
                self.entry_Label[i].grid(row=i+2, column=3)

            # Markerコンボボックス
            self.combobox_Marker = []
            Marker_values = ["None", "〇", "△", "▽", "□", "◇", "×", "＋"]
            for i in range(self.column):
                self.combobox_Marker.append(ttk.Combobox(self.frame_right, state="readonly", width=5, values=Marker_values, justify=tk.CENTER))
                self.combobox_Marker[i].current(i)
                self.combobox_Marker[i].grid(row=i+2, column=4, padx=2)

            # Lineコンボボックス
            self.combobox_Line = []
            Line_values = ["None","Solid", "Dotted", "Broken", "Dot-dash"]
            for i in range(self.column):
                self.combobox_Line.append(ttk.Combobox(self.frame_right, state="readonly", width=10, values=Line_values, justify=tk.CENTER))
                self.combobox_Line[i].current(1)
                self.combobox_Line[i].grid(row=i+2, column=5, padx=2)

            # 近似曲線コンボボックス
            self.combobox_Approx = []
            Approx_values = ["None", "Polyfit"]
            for i in range(self.column):
                self.combobox_Approx.append(ttk.Combobox(self.frame_right, state="readonly", width=10, values=Approx_values, justify=tk.CENTER))
                self.combobox_Approx[i].current(0)
                self.combobox_Approx[i].grid(row=i+2, column=6, padx=2)

            # 次数エントリーボックス
            self.entry_Degree = []
            for i in range(self.column):
                self.entry_Degree.append(tk.Entry(self.frame_right, justify=tk.CENTER, width=5))
                self.entry_Degree[i].grid(row=i+2, column=7, padx=2)

            # 近似曲線Labelエントリーボックス
            self.entry_ApproxLabel = []
            for i in range(self.column):
                self.entry_ApproxLabel.append(tk.Entry(self.frame_right, justify=tk.CENTER, width=10))
                self.entry_ApproxLabel[i].grid(row=i+2, column=8, padx=2)

            # 対数軸設定
            label_Log = tk.Label(self.frame_right, text="Log axis")
            label_Log.grid(row=self.row+1, column=3)

            label_LogX = tk.Label(self.frame_right, text="X")
            label_LogX.grid(row=self.row+1, column=4)

            label_LogY1 = tk.Label(self.frame_right, text="Y1")
            label_LogY1.grid(row=self.row+1, column=5)

            label_LogY2 = tk.Label(self.frame_right, text="Y2")
            label_LogY2.grid(row=self.row+1, column=6)

            self.var_LogX = []
            self.var_LogX.append(tk.BooleanVar())
            self.checkbutton_LogX = tk.Checkbutton(self.frame_right, variable=self.var_LogX)
            self.checkbutton_LogX.grid(row=self.row+2, column=4)

            self.var_LogY1 = []
            self.var_LogY1.append(tk.BooleanVar())
            self.checkbutton_LogY1 = tk.Checkbutton(self.frame_right, variable=self.var_LogY1)
            self.checkbutton_LogY1.grid(row=self.row+2, column=5)

            self.var_LogY2 = []
            self.var_LogY2.append(tk.BooleanVar())
            self.checkbutton_LogY2 = tk.Checkbutton(self.frame_right, variable=self.var_LogY2)
            self.checkbutton_LogY2.grid(row=self.row+2, column=6)

        return func()

    # グラフ出力
    def create_graph(self):

        def func():
            x = self.var_X.get()
            judge = 0
            fig, self.ax1 = plt.subplots()
            
            for i in range(self.column):

                if self.var_Y2[i].get()==True:
                    self.ax2 = self.ax1.twinx()
                    break

            # グラフ描画
            for i in range(self.column):

                if (self.var_Y1[i].get()==True)&(self.combobox_Approx[i].get()=="None"):
                    self.ax1.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_Label[i].get(), color="black", markerfacecolor="None")

                if (self.var_Y2[i].get()==True)&(self.combobox_Approx[i].get()=="None"):
                    self.ax2.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_Label[i].get(), color="black", markerfacecolor="None")
                    self.ax2.set_ylabel(self.entry_Y2.get())
                    judge = 1

            # 近似曲線描画
            for i in range(self.column):

                if self.combobox_Approx[i].get()!="None":
                    
                    if self.var_Y1[i].get()==True:
                        self.ax1.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls="None", label=self.entry_Label[i].get(), color="black", markerfacecolor="None")
                        self.ax1.plot(self.data[:,x], self.ApproxLine(i), marker="None", ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_ApproxLabel[i].get(), color="black")
                        
                    if self.var_Y2[i].get()==True:
                        self.ax2.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls="None", label=self.entry_Label[i].get(), color="black", markerfacecolor="None")
                        self.ax2.plot(self.data[:,x], self.ApproxLine(i), marker="None", ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_ApproxLabel[i].get(), color="black")
                        self.ax2.set_ylabel(self.entry_Y2.get())
                        judge = 1

            # ラベル生成
            if judge==0:
                self.ax1.legend(frameon=False, loc='best').set_draggable(state=True)
                self.ax1.set_xlabel(self.entry_X.get())
                self.ax1.set_ylabel(self.entry_Y1.get())
            else:
                lines, labels = self.ax1.get_legend_handles_labels()
                lines2, labels2 = self.ax2.get_legend_handles_labels()
                self.ax2.legend(lines + lines2, labels + labels2, frameon=False, loc='best').set_draggable(state=True)
                self.ax1.set_xlabel(self.entry_X.get())
                self.ax1.set_ylabel(self.entry_Y1.get())
                self.ax2.set_ylabel(self.entry_Y2.get())

            self.LogAxis()

            plt.show()

        return func()

    # マーカーのスタイルをmatplotlibの表記に変換
    def trans_marker(self, marker):
        if marker=="〇":
            return "o"
        elif marker=="△":
            return "^"
        elif marker=="▽":
            return "v"
        elif marker=="□":
            return "s"
        elif marker=="◇":
            return "D"
        elif marker=="×":
            return "x"
        elif marker=="＋":
            return "+"
        else:
            return "None"

    # 線のスタイルをmatplotlibの表記に変換
    def trans_line(self, line):
        if line=="Solid":
            return "-"
        elif line=="Dotted":
            return ":"
        elif line=="Broken":
            return "--"
        elif line=="Dot-dash":
            return "-."
        else:
            return "None"

    # 対数軸生成
    def LogAxis(self):
        if self.var_LogX[0].get()==True:
            self.ax1.set_xscale("log")
        
        if self.var_LogY1[0].get()==True:
            self.ax1.set_yscale("log")

        if self.var_LogY2[0].get()==True:
            self.ax2.set_yscale("log")
            
    
    # 近似曲線の計算
    def ApproxLine(self, i):

        # x軸が対数スケールのとき補正　有効か検証必要あり
        if self.var_LogX[0].get()==True:
            x = np.log10(self.data[:,self.var_X.get()])
        else:
            x = self.data[:,self.var_X.get()]
        
        y = self.data[:,i]
        approxstyle = self.combobox_Approx[i].get()
        deg = int(self.entry_Degree[i].get())

        return np.poly1d(np.polyfit(x, y, deg))(x)
        



root = tk.Tk()
root.title(u"Graph Generator")
root.resizable(0, 0)
app = App(master=root)
app.mainloop()