import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk as ttk
import matplotlib as mpl
from matplotlib.ticker import ScalarFormatter
import japanize_matplotlib
import pandas as pd
import os.path


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.frame_gen()
        self.createframeL(self.frameL)
        self.createframeC(self.frameC)
        self.createframeR(self.frameR)


    #左、中心、右にframeを定義（左はグラフ基本構造、中心は中央線、右はプロットデータ情報）
    def frame_gen(self):
        self.frameL = tk.Frame(self)
        self.frameL.grid(row=0, column=0, sticky=tk.NW)
        self.frameC = tk.Frame(self)
        self.frameC.grid(row=0, column=1, sticky=tk.NW)
        self.frameR = tk.Frame(self)
        self.frameR.grid(row=0, column=2, sticky=tk.NW)


    #左frame生成
    def createframeL(self, frame):
        #-----ここから各軸のラベル設定ボックス-----
        label_Xname = tk.Label(frame, text="X-axis name")
        label_Xname.grid(row=0, column=0)
        self.entry_Xname = tk.Entry(frame, justify=tk.CENTER)
        self.entry_Xname.grid(row=0, column=1, columnspan=3)
        label_Y1name = tk.Label(frame, text="Y1-axis name")
        label_Y1name.grid(row=1, column=0)
        self.entry_Y1name = tk.Entry(frame, justify=tk.CENTER)
        self.entry_Y1name.grid(row=1, column=1, columnspan=3)
        label_Y2name = tk.Label(frame, text="Y2-axis name")
        label_Y2name.grid(row=2, column=0)
        self.entry_Y2name = tk.Entry(frame, justify=tk.CENTER)
        self.entry_Y2name.grid(row=2, column=1, columnspan=3)

        #-----ここから各軸の範囲設定ボックス-----
        label_begin = tk.Label(frame, text="begin")
        label_begin.grid(row=3, column=1)
        label_end = tk.Label(frame, text="end")
        label_end.grid(row=3, column=2)
        label_tick = tk.Label(frame, text="tick")
        label_tick.grid(row=3, column=3)
        label_Xrange = tk.Label(frame, text="X-range")
        label_Xrange.grid(row=4, column=0)
        self.entry_Xrange_min = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Xrange_min.grid(row=4, column=1)
        self.entry_Xrange_max = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Xrange_max.grid(row=4, column=2)
        self.entry_Xtick = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Xtick.grid(row=4,column=3)
        label_Y1range = tk.Label(frame, text="Y1-range")
        label_Y1range.grid(row=5, column=0)
        self.entry_Y1range_min = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Y1range_min.grid(row=5, column=1)
        self.entry_Y1range_max = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Y1range_max.grid(row=5, column=2)
        self.entry_Y1tick = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Y1tick.grid(row=5,column=3)
        label_Y2range = tk.Label(frame, text="Y2-range")
        label_Y2range.grid(row=6, column=0)
        self.entry_Y2range_min = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Y2range_min.grid(row=6, column=1)
        self.entry_Y2range_max = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Y2range_max.grid(row=6, column=2)
        self.entry_Y2tick = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Y2tick.grid(row=6,column=3)

        #encoding指定
        encode = ["utf-8","shift-jis"]
        self.encoding_label = tk.Label(frame, text="encoding")
        self.encoding_label.grid(row=7, column=0)
        self.combobox_encoding = ttk.Combobox(frame, state="readonly", width=5, values=encode, justify=tk.CENTER)
        self.combobox_encoding.current(0)
        self.combobox_encoding.grid(row=8,column=0)

        #グラフ設定更新ボタン
        self.button_apply = tk.Button(frame, text="Output", command=self.graph)
        self.button_apply.grid(row=7, column=2, columnspan=2)

        #ファイル取り込みボタン
        self.button_import = tk.Button(frame, text="Import file", command=self.importfile)
        self.button_import.grid(row=8, column=2, columnspan=2)


    #中央frame作成
    def createframeC(self, frame):
        # ウィンドウサイズに合わせて中央線を延長
        root.update_idletasks()
        wy = self.frameL.winfo_height()
        self.canvas = tk.Canvas(frame, width=1, height=wy, bg="black")
        self.canvas.pack()


    #右frame作成
    def createframeR(self, frame):
        self.label_Dataname = tk.Label(frame, text="Dataname", justify=tk.CENTER)
        self.label_Dataname.grid(row=0, column=0)
        self.label_X = tk.Label(frame, text="X", justify=tk.CENTER)
        self.label_X.grid(row=0, column=1)
        self.label_Y1 = tk.Label(frame, text="Y1", justify=tk.CENTER)
        self.label_Y1.grid(row=0, column=2)
        self.label_Y2 = tk.Label(frame, text="Y2", justify=tk.CENTER)
        self.label_Y2.grid(row=0, column=3)
        self.label_Label = tk.Label(frame, text="Label", justify=tk.CENTER)
        self.label_Label.grid(row=0, column=4)
        self.label_Marker = tk.Label(frame, text="Marker", justify=tk.CENTER)
        self.label_Marker.grid(row=0, column=5)
        self.label_Line = tk.Label(frame, text="Line", justify=tk.CENTER)
        self.label_Line.grid(row=0, column=6)
        self.label_Approx = tk.Label(frame, text="Approx",justify=tk.CENTER)
        self.label_Approx.grid(row=0, column=7)
        self.label_Degree = tk.Label(frame, text="Degree", justify=tk.CENTER)
        self.label_Degree.grid(row=0, column=8)
        self.label_ApproxLabel = tk.Label(frame, text="ApproxLabel", justify=tk.CENTER)
        self.label_ApproxLabel.grid(row=0, column=9)


    #ファイル取り込み
    def importfile(self):
        self.filepath = tk.filedialog.askopenfilename()
        if self.filepath!="":
            self.df = pd.read_csv(self.filepath,encoding=self.combobox_encoding.get())
            self.data = self.df.values
            self.graphconfig(self.frameR)
            self.centerline()
            self.load()

    def graphconfig(self, frame):
        self.row = len(self.data)
        self.column = max([len(v) for v in self.data])
            
        # widget初期化
        frame.destroy()
        self.frameR = tk.Frame(self)
        self.frameR.grid(row=0, column=2, sticky=tk.NW)
        frame = self.frameR
        self.createframeR(frame)

        # データ名ラベル
        self.Dataname = []
        for i in range(self.column):
            self.Dataname.append(tk.Label(frame, text=self.df.columns[i], justify=tk.CENTER))
            self.Dataname[i].grid(row=i+1,column=0)

        # X軸コンボボックス
        X_values = []
        self.combobox_X = []
        for i in range(self.column):
            X_values.append(i+1)
        for i in range(self.column):
            self.combobox_X.append(ttk.Combobox(frame, state="readonly", width=5, values=X_values, justify=tk.CENTER))
            self.combobox_X[i].current(0)
            self.combobox_X[i].grid(row=i+1, column=1)

        # Y1軸チェックボタン
        self.var_Y1 = []
        self.checkbutton_Y1 = []
        for i in range(self.column):
            self.var_Y1.append(tk.BooleanVar())
            self.checkbutton_Y1.append(tk.Checkbutton(frame, variable=self.var_Y1[i]))
            self.checkbutton_Y1[i].grid(row=i+1, column=2)

        # Y2軸チェックボタン
        self.var_Y2 = []
        self.checkbutton_Y2 = []
        for i in range(self.column):
            self.var_Y2.append(tk.BooleanVar())
            self.checkbutton_Y2.append(tk.Checkbutton(frame, variable=self.var_Y2[i]))
            self.checkbutton_Y2[i].grid(row=i+1, column=3)
      
        # Label入力ボックス
        self.entry_Label = []
        for i in range(self.column):
            self.entry_Label.append(tk.Entry(frame, justify=tk.RIGHT, width=10))
            self.entry_Label[i].grid(row=i+1, column=4)

        # Markerコンボボックス
        self.combobox_Marker = []
        Marker_values = ["None", "〇", "△", "▽", "□", "◇", "×", "＋"]
        for i in range(self.column):
            self.combobox_Marker.append(ttk.Combobox(frame, state="readonly", width=5, values=Marker_values, justify=tk.CENTER))
            self.combobox_Marker[i].current(1)
            self.combobox_Marker[i].grid(row=i+1, column=5, padx=2)

        # Lineコンボボックス
        self.combobox_Line = []
        Line_values = ["None","Solid", "Dotted", "Broken", "Dot-dash"]
        for i in range(self.column):
            self.combobox_Line.append(ttk.Combobox(frame, state="readonly", width=10, values=Line_values, justify=tk.CENTER))
            self.combobox_Line[i].current(1)
            self.combobox_Line[i].grid(row=i+1, column=6, padx=2)

        # 近似曲線コンボボックス
        self.combobox_Approx = []
        Approx_values = ["None", "Polyfit"]
        for i in range(self.column):
            self.combobox_Approx.append(ttk.Combobox(frame, state="readonly", width=10, values=Approx_values, justify=tk.CENTER))
            self.combobox_Approx[i].current(0)
            self.combobox_Approx[i].grid(row=i+1, column=7, padx=2)

        # 次数エントリーボックス
        self.entry_Degree = []
        for i in range(self.column):
            self.entry_Degree.append(tk.Entry(frame, justify=tk.CENTER, width=5))
            self.entry_Degree[i].grid(row=i+1, column=8, padx=2)

        # 近似曲線Labelエントリーボックス
        self.entry_ApproxLabel = []
        for i in range(self.column):
            self.entry_ApproxLabel.append(tk.Entry(frame, justify=tk.CENTER, width=10))
            self.entry_ApproxLabel[i].grid(row=i+1, column=9, padx=2)

        # 対数軸設定
        label_Log = tk.Label(frame, text="Log axis")
        label_Log.grid(row=self.column+1, column=3)
        label_LogX = tk.Label(frame, text="X")
        label_LogX.grid(row=self.column+1, column=4)
        label_LogY1 = tk.Label(frame, text="Y1")
        label_LogY1.grid(row=self.column+1, column=5)
        label_LogY2 = tk.Label(frame, text="Y2")
        label_LogY2.grid(row=self.column+1, column=6)
        self.var_LogX = []
        self.var_LogX.append(tk.BooleanVar())
        self.checkbutton_LogX = tk.Checkbutton(frame, variable=self.var_LogX)
        self.checkbutton_LogX.grid(row=self.column+2, column=4)
        self.var_LogY1 = []
        self.var_LogY1.append(tk.BooleanVar())
        self.checkbutton_LogY1 = tk.Checkbutton(frame, variable=self.var_LogY1)
        self.checkbutton_LogY1.grid(row=self.column+2, column=5)
        self.var_LogY2 = []
        self.var_LogY2.append(tk.BooleanVar())
        self.checkbutton_LogY2 = tk.Checkbutton(frame, variable=self.var_LogY2)
        self.checkbutton_LogY2.grid(row=self.column+2, column=6)

    def graph(self):

        def func():
            judge = 0

            fig = plt.figure(figsize=(8,6))
            self.ax1 = fig.add_subplot(1,1,1)

            for i in range(self.column):

                if self.var_Y2[i].get()==True:
                    self.ax2 = self.ax1.twinx()
                    break

            # グラフ描画
            for i in range(self.column):
                x = int(self.combobox_X[i].get())-1
              
                if (self.var_Y1[i].get()==True)&(self.combobox_Approx[i].get()=="None"):
                    self.ax1.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_Label[i].get(), color="black", markerfacecolor="None")
     
                if (self.var_Y2[i].get()==True)&(self.combobox_Approx[i].get()=="None"):
                    self.ax2.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_Label[i].get(), color="black", markerfacecolor="None")
                    judge = 1

            # 近似曲線描画
            for i in range(self.column):
                x = int(self.combobox_X[i].get())-1
                if self.combobox_Approx[i].get()!="None":
                    
                    if self.var_Y1[i].get()==True:
                        self.ax1.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls="None", label=self.entry_Label[i].get(), color="black", markerfacecolor="None")
                        self.ax1.plot(self.data[:,x], self.ApproxLine(i), marker="None", ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_ApproxLabel[i].get(), color="black")
                        
                    if self.var_Y2[i].get()==True:
                        self.ax2.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls="None", label=self.entry_Label[i].get(), color="black", markerfacecolor="None")
                        self.ax2.plot(self.data[:,x], self.ApproxLine(i), marker="None", ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_ApproxLabel[i].get(), color="black")
                        judge = 1
            a=3
            # ラベル生成
            if judge==0:
                self.ax1.legend(fontsize = 13, frameon=False, loc='best').set_draggable(state=True)
                self.ax1.set_xlabel(self.entry_Xname.get(),fontsize=14+a)
                self.ax1.set_ylabel(self.entry_Y1name.get(),fontsize=14+a)
                self.ax1.tick_params(labelsize=13+a)
            else:
                lines, labels = self.ax1.get_legend_handles_labels()
                lines2, labels2 = self.ax2.get_legend_handles_labels()
                self.ax2.legend(lines + lines2, labels + labels2, frameon=False, loc='best').set_draggable(state=True)
                self.ax1.set_xlabel(self.entry_Xname.get(),fontsize=14+a)
                self.ax1.set_ylabel(self.entry_Y1name.get(),fontsize=14+a)
                self.ax2.set_ylabel(self.entry_Y2name.get(),fontsize=14+a)
                self.ax1.tick_params(labelsize=13+a)
                self.ax2.tick_params(labelsize=13+a)
            
            self.LogAxis()
            self.Axislimiter(judge)
            self.generate_ticks(judge)
            #plt.legend(fontsize=13,frameon=False)
            #plt.grid()
            self.save() #save関数はplt.showより前に置く必要がある
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

        if self.var_LogX[0].get()==True:
            x = np.log10(self.data[:,int(self.combobox_X[i].get())-1])
        else:
            x = self.data[:,int(self.combobox_X[i].get())-1]
        
        y = self.data[:,i]
        deg = int(self.entry_Degree[i].get())

        if (self.var_LogY1[0].get()==True)&(self.var_Y1[i].get()==True):
            y = np.log10(self.data[:,i])
            return 10**(np.poly1d(np.polyfit(x, y, deg))(x))

        elif (self.var_LogY2[0].get()==True)&(self.var_Y2[i].get()==True):
            y = np.log10(self.data[:,i])
            return 10**(np.poly1d(np.polyfit(x, y, deg))(x))

        return np.poly1d(np.polyfit(x, y, deg))(x)

    def Axislimiter(self, judge):
        if (self.entry_Xrange_min.get()!="")&(self.entry_Xrange_max.get()!=""):
            self.ax1.set_xlim([float(self.entry_Xrange_min.get()), float(self.entry_Xrange_max.get())])
            
        if (self.entry_Y1range_min.get()!="")&(self.entry_Y1range_max.get()!=""):
            self.ax1.set_ylim([float(self.entry_Y1range_min.get()), float(self.entry_Y1range_max.get())])

        if judge==1:
            if (self.entry_Y2range_min.get()!="")&(self.entry_Y2range_max.get()!=""):
                self.ax2.set_ylim([float(self.entry_Y2range_min.get()), float(self.entry_Y2range_max.get())])

    def generate_ticks(self, judge):
        if (self.entry_Xtick.get() != "")&(self.var_LogX[0].get()==False):
            self.ax1.xaxis.set_minor_locator(plt.MultipleLocator(float(self.entry_Xtick.get())))
        if (self.entry_Y1tick.get() != "")&(self.var_LogY1[0].get()==False):
            self.ax1.yaxis.set_minor_locator(plt.MultipleLocator(float(self.entry_Y1tick.get())))
        
        if judge == 1:
            if (self.entry_Xtick.get() != "")&(self.var_LogX[0].get()==False):
                self.ax2.xaxis.set_minor_locator(plt.MultipleLocator(float(self.entry_Xtick.get())))
            if (self.entry_Y2tick.get() != "")&(self.var_LogY2[0].get()==False):
                self.ax2.yaxis.set_minor_locator(plt.MultipleLocator(float(self.entry_Y2tick.get())))

    def centerline(self):
        root.update_idletasks()
        x = self.frameL.winfo_height()
        y = self.frameL.winfo_height()

        if (x > y):
            self.canvas["height"] = x
        else:
            self.canvas["height"] = y

    #設定の保存
    def save(self):
        path = self.get_folderpath(self.filepath)
        filename = self.get_filename(self.filepath)
        f = open(path+filename+"_GG.txt", 'w')
        f.write(self.output_config())
        f.close()

    def output_config(self):
        config = ""

        config = config + "X-axis name:" + self.entry_Xname.get() + "\n"
        config = config + "Y1-axis name:" + self.entry_Y1name.get() + "\n"
        config = config + "Y2-axis name:" + self.entry_Y2name.get() +"\n"
        config = config + "X-range:" + self.entry_Xrange_min.get() + "," + self.entry_Xrange_max.get() + "," + self.entry_Xtick.get() + "\n"
        config = config + "Y1-range:" + self.entry_Y1range_min.get() + "," + self.entry_Y1range_max.get() + "," + self.entry_Y1tick.get() + "\n"
        config = config + "Y2-range:" + self.entry_Y2range_min.get() + "," + self.entry_Y2range_max.get() + "," + self.entry_Y2tick.get() + "\n"
        for i in range(self.column):
            config = config + "X:" + self.combobox_X[i].get() + ","
            config = config + "Y1:" + str(self.var_Y1[i].get()) + ","
            config = config + "Y2:" + str(self.var_Y2[i].get()) + ","
            config = config + "Label:" + self.entry_Label[i].get() + ","
            config = config + "Marker:" + self.combobox_Marker[i].get() + ","
            config = config + "Line:" + self.combobox_Line[i].get() + ","
            config = config + "Approx:" + self.combobox_Approx[i].get() + ","
            config = config + "Degree:" + self.entry_Degree[i].get() + ","
            config = config + "Approx Label:" + self.entry_ApproxLabel[i].get() + "\n"

        config = config + "LogX:" + str(self.var_LogX[0].get()) + "\n"
        config = config + "LogY1:" + str(self.var_LogY1[0].get()) + "\n"
        config = config + "LogY2:" + str(self.var_LogY2[0].get()) + "\n" 

        return config

    #設定の読み込み
    def load(self):
        path = self.get_folderpath(self.filepath)
        filename = self.get_filename(self.filepath)
        if os.path.exists(path+filename+"_GG.txt"):
            f = open(path+filename+"_GG.txt")
            config = f.read()
            self.input_config(config)
            f.close()
        else:
            pass

    #設定の適用
    def input_config(self, config):
        graph_config = config.split("\n")

        Xname = graph_config[0].split(":")
        self.entry_Xname.insert(tk.END, Xname[1])

        Y1name = graph_config[1].split(":")
        self.entry_Y1name.insert(tk.END, Y1name[1])

        Y2name = graph_config[2].split(":")
        self.entry_Y2name.insert(tk.END, Y2name[1])

        Xrange = graph_config[3].split(":")
        Xparam = Xrange[1].split(",")
        self.entry_Xrange_min.insert(tk.END, Xparam[0])
        self.entry_Xrange_max.insert(tk.END, Xparam[1])
        self.entry_Xtick.insert(tk.END, Xparam[2])

        Y1range = graph_config[4].split(":")
        Y1param = Y1range[1].split(",")
        self.entry_Y1range_min.insert(tk.END, Y1param[0])
        self.entry_Y1range_max.insert(tk.END, Y1param[1])
        self.entry_Y1tick.insert(tk.END, Y1param[2])

        Y2range = graph_config[5].split(":")
        Y2param = Y2range[1].split(",")
        self.entry_Y2range_min.insert(tk.END, Y2param[0])
        self.entry_Y2range_max.insert(tk.END, Y2param[1])
        self.entry_Y2tick.insert(tk.END, Y2param[2])        
        
        for i in range(self.column):
            data_config = graph_config[6+i].split(",")
            X = data_config[0].split(":")
            self.combobox_X[i].set(X[1])

            Y1 = data_config[1].split(":")
            self.var_Y1[i].set(Y1[1])

            Y2 = data_config[2].split(":")
            self.var_Y2[i].set(Y2[1])

            label = data_config[3].split(":")
            self.entry_Label[i].insert(tk.END, label[1])

            marker = data_config[4].split(":")
            self.combobox_Marker[i].set(marker[1])

            line = data_config[5].split(":")
            self.combobox_Line[i].set(line[1])

            approx = data_config[6].split(":")
            self.combobox_Approx[i].set(approx[1])

            degree = data_config[7].split(":")
            self.entry_Degree[i].insert(tk.END, degree[1])

            aplabel = data_config[8].split(":")
            self.entry_ApproxLabel[i].insert(tk.END, aplabel[1])

        LogX = graph_config[6+self.column].split(":")
        self.var_LogX[0].set(LogX[1])

        LogY1 = graph_config[6+self.column+1].split(":")
        self.var_LogY1[0].set(LogY1[1])

        LogY2 = graph_config[6+self.column+2].split(":")
        self.var_LogY2[0].set(LogY2[1])

    #操作ファイルのフォルダパス取得
    def get_folderpath(self, filepath):
        while(filepath[-1]!="/"):
            filepath = filepath[:-1]
        folderpath = filepath
        return folderpath
    
    #操作ファイルの拡張子なし名称取得
    def get_filename(self, filepath):
        filename =""
        while(filepath[-1]!="/"):
            filename = filepath[-1] + filename
            filepath = filepath[:-1]
        while(filename[-1]!="."):
            filename = filename[:-1]
        return filename

root = tk.Tk()
root.title(u"GraphGen ver2.1")
root.resizable(0, 0)
app = App(master=root)
app.mainloop()