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
        self.createframe()
        self.createframeL(self.frameL)
        self.createframeR(self.frameR)
        self.createframeC(self.frameC)

    #左、中心、右にframeを定義（左はグラフ基本構造、中心は中央線、右はプロットデータ情報）
    def createframe(self):
        self.frameL = tk.Frame(self)
        self.frameC = tk.Frame(self)
        self.frameR = tk.Frame(self)
        self.frameL.grid(row=0, column=0, sticky=tk.NW)
        self.frameC.grid(row=0, column=1, sticky=tk.NW)
        self.frameR.grid(row=0, column=2, sticky=tk.NW)

    # フレーム初期化
    def frame_destroy(self):
        self.frameL.destroy()
        self.frameC.destroy()
        self.frameR.destroy()

    # 左frame生成
    def createframeL(self, frame):
        #-----各軸のラベル設定ボックス-----
        tk.Label(frame, text="X-axis name" ).grid(row=0, column=0)
        tk.Label(frame, text="Y1-axis name").grid(row=1, column=0)
        tk.Label(frame, text="Y2-axis name").grid(row=2, column=0)

        self.entry_Xname  = tk.Entry(frame, justify=tk.CENTER)
        self.entry_Y1name = tk.Entry(frame, justify=tk.CENTER)
        self.entry_Y2name = tk.Entry(frame, justify=tk.CENTER)

        self.entry_Xname .grid(row=0, column=1, columnspan=3)
        self.entry_Y1name.grid(row=1, column=1, columnspan=3)
        self.entry_Y2name.grid(row=2, column=1, columnspan=3)

        #-----線-----
        self.line1 = tk.Canvas(frame, width=200, height=1, bg="black")
        self.line1.grid(row=3, column=0, columnspan=4)

        #-----各軸の範囲設定ボックス-----
        tk.Label(frame, text="begin"  ).grid(row=4, column=1)
        tk.Label(frame, text="end"    ).grid(row=4, column=2)
        tk.Label(frame, text="tick"   ).grid(row=4, column=3)

        #x軸の範囲設定
        tk.Label(frame, text="X-range").grid(row=5, column=0)

        self.entry_Xrange_min = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Xrange_max = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Xtick      = tk.Entry(frame, justify=tk.CENTER, width=5)

        self.entry_Xrange_min.grid(row=5, column=1)
        self.entry_Xrange_max.grid(row=5, column=2)
        self.entry_Xtick     .grid(row=5, column=3)

        #y1軸の範囲設定
        tk.Label(frame, text="Y1-range").grid(row=6, column=0)

        self.entry_Y1range_min = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Y1range_max = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Y1tick      = tk.Entry(frame, justify=tk.CENTER, width=5)

        self.entry_Y1range_min.grid(row=6, column=1)
        self.entry_Y1range_max.grid(row=6, column=2)
        self.entry_Y1tick     .grid(row=6, column=3)

        #y2軸の範囲設定
        tk.Label(frame, text="Y2-range").grid(row=7, column=0)

        self.entry_Y2range_min = tk.Entry(frame, justify=tk.CENTER, width=5)  
        self.entry_Y2range_max = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_Y2tick      = tk.Entry(frame, justify=tk.CENTER, width=5)

        self.entry_Y2range_min.grid(row=7, column=1)
        self.entry_Y2range_max.grid(row=7, column=2)
        self.entry_Y2tick     .grid(row=7, column=3)

        #-----線-----
        self.line2 = tk.Canvas(frame, width=200, height=1, bg="black")
        self.line2.grid(row=8, column=0, columnspan=4)

        #-----ラベルと目盛のフォントサイズ設定-----
        tk.Label(frame, text="Font size").grid(row=9 , column=1, columnspan=2)
        tk.Label(frame, text="label"    ).grid(row=10, column=0)
        tk.Label(frame, text="tick"     ).grid(row=10, column=2)

        self.entry_fontsize_of_label = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_fontsize_of_tick  = tk.Entry(frame, justify=tk.CENTER, width=5)

        self.entry_fontsize_of_label.insert(tk.END,24)
        self.entry_fontsize_of_tick .insert(tk.END,20)

        self.entry_fontsize_of_label.grid(row=10, column=1)
        self.entry_fontsize_of_tick .grid(row=10, column=3)

        #-----線----
        self.line3 = tk.Canvas(frame, width=200, height=1, bg="black")
        self.line3.grid(row=11, column=0, columnspan=4)

        #-----sci表記の指定-----
        tk.Label(frame, text="X"  ).grid(row=12, column=1)
        tk.Label(frame, text="Y1" ).grid(row=12, column=2)
        tk.Label(frame, text="Y2" ).grid(row=12, column=3)
        tk.Label(frame, text="sci").grid(row=13, column=0)
        self.var_sciX  = []
        self.var_sciY1 = []
        self.var_sciY2 = []

        self.var_sciX .append(tk.BooleanVar())
        self.var_sciY1.append(tk.BooleanVar())
        self.var_sciY2.append(tk.BooleanVar())

        self.checkbutton_sciX  = tk.Checkbutton(frame, variable=self.var_sciX )
        self.checkbutton_sciY1 = tk.Checkbutton(frame, variable=self.var_sciY1)
        self.checkbutton_sciY2 = tk.Checkbutton(frame, variable=self.var_sciY2)

        self.checkbutton_sciX .grid(row=13, column=1)
        self.checkbutton_sciY1.grid(row=13, column=2)
        self.checkbutton_sciY2.grid(row=13, column=3)

        #-----線----
        self.line4 = tk.Canvas(frame, width=200, height=1, bg="black")
        self.line4.grid(row=14, column=0, columnspan=4)

        #-----マーカーサイズ、ライン幅の指定-----
        tk.Label(frame, text="MarkerSize").grid(row=15, column=0)
        tk.Label(frame, text="LineWidth" ).grid(row=16, column=0)

        self.entry_MarkerSize = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_LineWidth  = tk.Entry(frame, justify=tk.CENTER, width=5)

        self.entry_MarkerSize.insert(tk.END, 10)
        self.entry_LineWidth .insert(tk.END, 2.5)

        self.entry_MarkerSize.grid(row=15, column=1)
        self.entry_LineWidth .grid(row=16, column=1)

        tk.Label(frame, text="pt").grid(row=15, column=2)
        tk.Label(frame, text="pt").grid(row=16, column=2)
        
        #-----グリッドの表示・非表示切り替え-----
        tk.Label(frame, text="grid").grid(row=17, column=0)
        self.var_grid = []
        self.var_grid.append(tk.BooleanVar())
        self.checkbutton_grid = tk.Checkbutton(frame, variable=self.var_grid)
        self.checkbutton_grid.grid(row=17, column=1)

        #-----ウィンドウサイズ-----
        tk.Label(frame, text="WindowSize").grid(row=18, column=0)
        tk.Label(frame, text="x"         ).grid(row=18, column=2)

        self.entry_WindowWidth  = tk.Entry(frame, justify=tk.CENTER, width=5)
        self.entry_WindowHeight = tk.Entry(frame, justify=tk.CENTER, width=5)

        self.entry_WindowWidth .insert(tk.END, 6)
        self.entry_WindowHeight.insert(tk.END, 6)

        self.entry_WindowWidth .grid(row=18, column=1)
        self.entry_WindowHeight.grid(row=18, column=3)

        #-----線----
        self.line5 = tk.Canvas(frame, width=200, height=1, bg="black")
        self.line5.grid(row=19, column=0, columnspan=4)

        #-----encoding指定-----
        encode = ["utf-8","shift-jis"]
        tk.Label(frame, text="encoding").grid(row=20, column=0)
        self.combobox_encoding = ttk.Combobox(frame, width=5, values=encode, justify=tk.CENTER)
        self.combobox_encoding.current(0)
        self.combobox_encoding.grid(row=21,column=0)

        #-----グラフ設定更新ボタン-----
        tk.Button(frame, text="Output", command=self.graph).grid(row=20, column=2, columnspan=2)

        #-----ファイル取り込みボタン-----
        tk.Button(frame, text="Import file", command=self.importfile).grid(row=21, column=2, columnspan=2)

    # 中央frame作成
    def createframeC(self, frame):
        root.update_idletasks()
        self.canvas = tk.Canvas(frame, width=1, height=1, bg="black")
        self.canvas.pack()
        self.centerline()

    # 右frame作成
    def createframeR(self, frame):
        tk.Label(frame, text="Dataname"   , justify=tk.CENTER).grid(row=0, column=0 )
        tk.Label(frame, text="X"          , justify=tk.CENTER).grid(row=0, column=1 )
        tk.Label(frame, text="Y1"         , justify=tk.CENTER).grid(row=0, column=2 )
        tk.Label(frame, text="Y2"         , justify=tk.CENTER).grid(row=0, column=3 )
        tk.Label(frame, text="Label"      , justify=tk.CENTER).grid(row=0, column=4 )
        tk.Label(frame, text="Marker"     , justify=tk.CENTER).grid(row=0, column=5 )
        tk.Label(frame, text="FaceColor"  , justify=tk.CENTER).grid(row=0, column=6 )
        tk.Label(frame, text="Line"       , justify=tk.CENTER).grid(row=0, column=7 )
        tk.Label(frame, text="Color"      , justify=tk.CENTER).grid(row=0, column=8 )
        tk.Label(frame, text="Approx"     , justify=tk.CENTER).grid(row=0, column=9 )
        tk.Label(frame, text="Degree"     , justify=tk.CENTER).grid(row=0, column=10)
        tk.Label(frame, text="ApproxLabel", justify=tk.CENTER).grid(row=0, column=11)

    # ファイル取り込み
    def importfile(self):
        check_path = self.get_filepath(tk.filedialog.askopenfilename())

        # 例外処理
        if(not check_path):
            return
        else:
            self.filepath = check_path
        

        self.df = pd.read_csv(self.filepath,encoding=self.combobox_encoding.get())
        self.data = self.df.values
        self.frame_destroy()
        self.createframe()
        self.createframeL(self.frameL)
        self.createframeR(self.frameR)
        self.createframeC(self.frameC)
        self.graphconfig(self.frameR)
        self.centerline()
        self.input_config()

    # ファイルパス取得時の例外処理
    def get_filepath(self, path):
        if not path.endswith(".csv"):
            tk.messagebox.showinfo("File error","Filetype must be a .csv")
            return 0
        
        return path

    # グラフのconfig変更GUI生成
    def graphconfig(self, frame):
        self.row = len(self.data)
        self.column = max([len(v) for v in self.data])

        # データ名ラベル
        # X軸コンボボックス             
        # Y1軸チェックボタン              
        # Y2軸チェックボタン  
        # Label入力ボックス            
        # Markerコンボボックス
        # Marker_Colorコンボボックス
        # Marker_FaceColorコンボボックス
        # Lineコンボボックス 
        # Colorコンボボックス           
        # 近似曲線コンボボックス
        # 次数エントリーボックス
        # 近似曲線Labelエントリーボックス

        self.Dataname           = []
        self.combobox_X         = []
        self.var_Y1             = []
        self.var_Y2             = []
        self.checkbutton_Y1     = []
        self.checkbutton_Y2     = []
        self.entry_Label        = []
        self.combobox_Marker    = []
        self.combobox_FaceColor = []
        self.combobox_Line      = []
        self.combobox_Color     = []
        self.combobox_Approx    = []
        self.entry_Degree       = []
        self.entry_ApproxLabel  = []

        X_values      = []
        Marker_values = ["None", "〇", "△", "▽", "□", "◇", "×", "＋"]
        Line_values   = ["None","Solid", "Dotted", "Broken", "Dot-dash"]
        Color_values  = ["black", "white", "red", "green", "blue", "orange", "None"]
        Approx_values = ["None", "Polyfit"]

        for i in range(self.column):
            X_values.append(i+1) 

        for i in range(self.column):
            self.Dataname          .append(tk.Label(frame, text=self.df.columns[i], justify=tk.CENTER))
            self.combobox_X        .append(ttk.Combobox(frame, state="readonly", width=5 , values=X_values, justify=tk.CENTER))
            self.var_Y1            .append(tk.BooleanVar())
            self.checkbutton_Y1    .append(tk.Checkbutton(frame, variable=self.var_Y1[i]))
            self.var_Y2            .append(tk.BooleanVar())
            self.checkbutton_Y2    .append(tk.Checkbutton(frame, variable=self.var_Y2[i]))
            self.entry_Label       .append(tk.Entry(frame, justify=tk.RIGHT, width=10))
            self.combobox_Marker   .append(ttk.Combobox(frame, state="readonly", width=5 , values=Marker_values, justify=tk.CENTER))
            self.combobox_FaceColor.append(ttk.Combobox(frame, state="readonly", width=5 , values=Color_values , justify=tk.CENTER))
            self.combobox_Line     .append(ttk.Combobox(frame, state="readonly", width=10, values=Line_values  , justify=tk.CENTER))
            self.combobox_Color    .append(ttk.Combobox(frame, state="readonly", width=5 , values=Color_values , justify=tk.CENTER))
            self.combobox_Approx   .append(ttk.Combobox(frame, state="readonly", width=10, values=Approx_values, justify=tk.CENTER))
            self.entry_Degree      .append(tk.Entry(frame, justify=tk.CENTER, width=5 ))
            self.entry_ApproxLabel .append(tk.Entry(frame, justify=tk.CENTER, width=10))

            self.combobox_X[i]        .current(0)
            self.combobox_Marker[i]   .current(1)
            self.combobox_FaceColor[i].current(0)
            self.combobox_Line[i]     .current(1)
            self.combobox_Color[i]    .current(0)
            self.combobox_Approx[i]   .current(0)

            self.Dataname[i]          .grid(row=i+1, column=0 )
            self.combobox_X[i]        .grid(row=i+1, column=1 )
            self.checkbutton_Y1[i]    .grid(row=i+1, column=2 )
            self.checkbutton_Y2[i]    .grid(row=i+1, column=3 )
            self.entry_Label[i]       .grid(row=i+1, column=4 )
            self.combobox_Marker[i]   .grid(row=i+1, column=5 , padx=2)
            self.combobox_FaceColor[i].grid(row=i+1, column=6 , padx=2)
            self.combobox_Line[i]     .grid(row=i+1, column=7 , padx=2)
            self.combobox_Color[i]    .grid(row=i+1, column=8 , padx=2)
            self.combobox_Approx[i]   .grid(row=i+1, column=9 , padx=2)
            self.entry_Degree[i]      .grid(row=i+1, column=10, padx=2)
            self.entry_ApproxLabel[i] .grid(row=i+1, column=11, padx=2)


        # 対数軸設定
        tk.Label(frame, text="Log axis").grid(row=self.column+1, column=3)
        tk.Label(frame, text="X"       ).grid(row=self.column+1, column=4)
        tk.Label(frame, text="Y1"      ).grid(row=self.column+1, column=5)
        tk.Label(frame, text="Y2"      ).grid(row=self.column+1, column=6)

        self.var_LogX  = []
        self.var_LogY1 = []
        self.var_LogY2 = []

        self.var_LogX .append(tk.BooleanVar())
        self.var_LogY1.append(tk.BooleanVar())
        self.var_LogY2.append(tk.BooleanVar())

        self.checkbutton_LogX  = tk.Checkbutton(frame, variable=self.var_LogX )
        self.checkbutton_LogY1 = tk.Checkbutton(frame, variable=self.var_LogY1)
        self.checkbutton_LogY2 = tk.Checkbutton(frame, variable=self.var_LogY2)

        self.checkbutton_LogX .grid(row=self.column+2, column=4)
        self.checkbutton_LogY1.grid(row=self.column+2, column=5)
        self.checkbutton_LogY2.grid(row=self.column+2, column=6)

        # 軸反転設定
        tk.Label(frame, text="Invert axis").grid(row=self.column+3, column=3)
        tk.Label(frame, text="X"       ).grid(row=self.column+3, column=4)
        tk.Label(frame, text="Y1"      ).grid(row=self.column+3, column=5)
        tk.Label(frame, text="Y2"      ).grid(row=self.column+3, column=6)

        self.var_InvertX  = []
        self.var_InvertY1 = []
        self.var_InvertY2 = []

        self.var_InvertX .append(tk.BooleanVar())
        self.var_InvertY1.append(tk.BooleanVar())
        self.var_InvertY2.append(tk.BooleanVar())

        self.checkbutton_InvertX  = tk.Checkbutton(frame, variable=self.var_InvertX )
        self.checkbutton_InvertY1 = tk.Checkbutton(frame, variable=self.var_InvertY1)
        self.checkbutton_InvertY2 = tk.Checkbutton(frame, variable=self.var_InvertY2)

        self.checkbutton_InvertX .grid(row=self.column+4, column=4)
        self.checkbutton_InvertY1.grid(row=self.column+4, column=5)
        self.checkbutton_InvertY2.grid(row=self.column+4, column=6)


    # グラフ描画
    def graph(self):

        def func():
            self.existY2 = 0

            fig = plt.figure(figsize=(float(self.entry_WindowWidth.get()),float(self.entry_WindowHeight.get())))
            self.ax1 = fig.add_subplot(1,1,1)

            for i in range(self.column):
                if self.var_Y2[i].get()==True:
                    self.ax2 = self.ax1.twinx()
                    break

            # グラフ描画
            for i in range(self.column):
                x = int(self.combobox_X[i].get())-1
              
                if (self.var_Y1[i].get()==True)&(self.combobox_Approx[i].get()=="None"):
                    self.ax1.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_Label[i].get(), color=self.trans_color(self.combobox_Color[i].get()), markerfacecolor=self.trans_color(self.combobox_FaceColor[i].get()), markersize=self.entry_MarkerSize.get(), linewidth=self.entry_LineWidth.get())
     
                if (self.var_Y2[i].get()==True)&(self.combobox_Approx[i].get()=="None"):
                    self.ax2.plot(self.data[:,x], self.data[:,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_Label[i].get(), color=self.trans_color(self.combobox_Color[i].get()), markerfacecolor=self.trans_color(self.combobox_FaceColor[i].get()), markersize=self.entry_MarkerSize.get(), linewidth=self.entry_LineWidth.get())
                    self.existY2 = 1

            # 近似曲線描画
            for i in range(self.column):
                x = int(self.combobox_X[i].get())-1

                # 近似曲線を滑らかにするためにデータ点を増やす
                self.lastnum_of_data=0
                for j in range(self.row):
                    if(pd.isna(self.data[self.lastnum_of_data,x])==False):
                        self.lastnum_of_data = self.lastnum_of_data + 1
                e = (self.data[self.lastnum_of_data-1,x]-self.data[0,x])/100
                self.approxdata = np.arange(self.data[0,x],self.data[self.lastnum_of_data-1,x]+e,e)

                if self.combobox_Approx[i].get()!="None":
                    if self.var_Y1[i].get()==True:
                        self.ax1.plot(self.data[:self.lastnum_of_data,x], self.data[:self.lastnum_of_data,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls="None", label=self.entry_Label[i].get(), color=self.trans_color(self.combobox_Color[i].get()), markerfacecolor=self.trans_color(self.combobox_FaceColor[i].get()), markersize=self.entry_MarkerSize.get())
                        self.ax1.plot(self.approxdata, self.ApproxLine(i), marker="None", ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_ApproxLabel[i].get(), color=self.combobox_Color[i].get(), linewidth=self.entry_LineWidth.get())
                    if self.var_Y2[i].get()==True:
                        self.ax2.plot(self.data[:self.lastnum_of_data,x], self.data[:self.lastnum_of_data,i], marker=self.trans_marker(self.combobox_Marker[i].get()), ls="None", label=self.entry_Label[i].get(), color=self.trans_color(self.combobox_Color[i].get()), markerfacecolor=self.trans_color(self.combobox_FaceColor[i].get()), markersize=self.entry_MarkerSize.get())
                        self.ax2.plot(self.approxdata, self.ApproxLine(i), marker="None", ls=self.trans_line(self.combobox_Line[i].get()), label=self.entry_ApproxLabel[i].get(), color=self.combobox_Color[i].get(), linewidth=self.entry_LineWidth.get())
                        self.existY2 = 1

            # ラベル・目盛生成
            fontsize_of_label = int(self.entry_fontsize_of_label.get())
            fontsize_of_tick  = int(self.entry_fontsize_of_tick.get())
            if self.existY2==0:
                self.ax1.legend(fontsize = fontsize_of_label-3, frameon=False, loc='best').set_draggable(state=True)
                self.ax1.set_xlabel(self.entry_Xname.get() ,fontsize=fontsize_of_label)
                self.ax1.set_ylabel(self.entry_Y1name.get(),fontsize=fontsize_of_label)
                self.ax1.tick_params(labelsize=fontsize_of_tick, direction='in', which='both', top=True, right=True)
                self.ax1.tick_params(which='major', length=10)
                self.ax1.tick_params(which='minor', length=5)
            else:
                lines , labels  = self.ax1.get_legend_handles_labels()
                lines2, labels2 = self.ax2.get_legend_handles_labels()
                self.ax2.legend(lines + lines2, labels + labels2, frameon=False, loc='best', fontsize = fontsize_of_label-3).set_draggable(state=True)
                self.ax1.set_xlabel(self.entry_Xname.get() ,fontsize=fontsize_of_label)
                self.ax1.set_ylabel(self.entry_Y1name.get(),fontsize=fontsize_of_label)
                self.ax2.set_ylabel(self.entry_Y2name.get(),fontsize=fontsize_of_label)
                self.ax1.tick_params(labelsize=fontsize_of_tick, direction='in', which='both', top=True)
                self.ax1.tick_params(which='major', length=10)
                self.ax1.tick_params(which='minor', length=5 )
                self.ax2.tick_params(labelsize=fontsize_of_tick, direction='in', which='both')
                self.ax2.tick_params(which='major', length=10)
                self.ax2.tick_params(which='minor', length=5 )
            
            self.sci()
            self.LogAxis()
            self.InvertAxis()
            self.Axislimiter()
            self.generate_ticks()
            
            if(self.var_grid[0].get()==True):
                plt.grid()

            self.output_config() #save関数はplt.showより前に置く必要がある
            plt.tight_layout()
            plt.show()

        return func()

    # 各軸をsci表記にする
    def sci(self):
        fontsize_of_sci = int(self.entry_fontsize_of_tick.get())
        if self.var_sciX[0].get()==True:
            self.ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
            self.ax1.ticklabel_format(style="sci", axis="x",scilimits=(0,0))
            self.ax1.xaxis.get_offset_text().set_fontsize(fontsize_of_sci)

        if self.var_sciY1[0].get()==True:
            self.ax1.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
            self.ax1.ticklabel_format(style="sci", axis="y",scilimits=(0,0))
            self.ax1.yaxis.get_offset_text().set_fontsize(fontsize_of_sci)

        if (self.var_sciY2[0].get()==True)&(self.existY2):
            self.ax2.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
            self.ax2.ticklabel_format(style="sci", axis="y",scilimits=(0,0))
            self.ax2.yaxis.get_offset_text().set_fontsize(fontsize_of_sci)

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

    # 文字表記の色をカラーコードへ変換
    def trans_color(self, color):
        if color=="black":
            return "#000000"
        elif color=="white":
            return "#ffffff"
        elif color=="red":
            return "#ff0000"
        elif color=="green":
            return "#008000"
        elif color=="blue":
            return "#0000FF"
        elif color=="orange":
            return "#F58220"
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

    def InvertAxis(self):
        if self.var_InvertX[0].get()==True:
            self.ax1.invert_xaxis()
        
        if self.var_InvertY1[0].get()==True:
            self.ax1.invert_yaxis()

        if self.var_InvertY2[0].get()==True:
            self.ax2.invert_yaxis()    

    # 近似曲線の計算
    def ApproxLine(self, i):

        if self.var_LogX[0].get()==True:
            x = np.log10(self.data[:self.lastnum_of_data,int(self.combobox_X[i].get())-1])
        else:
            x = self.data[:self.lastnum_of_data,int(self.combobox_X[i].get())-1]
        
        y = self.data[:self.lastnum_of_data,i]
        deg = int(self.entry_Degree[i].get())

        if (self.var_LogY1[0].get()==True)&(self.var_Y1[i].get()==True):
            y = np.log10(self.data[:self.lastnum_of_data,i])
            print(np.poly1d(np.polyfit(x, y, deg)))
            return 10**(np.poly1d(np.polyfit(x, y, deg))(self.approxdata))

        elif (self.var_LogY2[0].get()==True)&(self.var_Y2[i].get()==True):
            y = np.log10(self.data[:self.lastnum_of_data,i])
            print(np.poly1d(np.polyfit(x, y, deg)))
            return 10**(np.poly1d(np.polyfit(x, y, deg))(self.approxdata))
        else:
            print(np.poly1d(np.polyfit(x, y, deg)))
            return np.poly1d(np.polyfit(x, y, deg))(self.approxdata)

    # 軸の上限、下限設定
    def Axislimiter(self):
        if (self.entry_Xrange_min.get()!="")&(self.entry_Xrange_max.get()!=""):
            self.ax1.set_xlim([float(self.entry_Xrange_min.get()), float(self.entry_Xrange_max.get())])
            
        if (self.entry_Y1range_min.get()!="")&(self.entry_Y1range_max.get()!=""):
            self.ax1.set_ylim([float(self.entry_Y1range_min.get()), float(self.entry_Y1range_max.get())])

        if self.existY2==1:
            if (self.entry_Y2range_min.get()!="")&(self.entry_Y2range_max.get()!=""):
                self.ax2.set_ylim([float(self.entry_Y2range_min.get()), float(self.entry_Y2range_max.get())])

    # 目盛生成
    def generate_ticks(self):
        if (self.entry_Xtick.get() != "")&(self.var_LogX[0].get()==False):
            self.ax1.xaxis.set_minor_locator(plt.MultipleLocator(float(self.entry_Xtick.get())))
        if (self.entry_Y1tick.get() != "")&(self.var_LogY1[0].get()==False):
            self.ax1.yaxis.set_minor_locator(plt.MultipleLocator(float(self.entry_Y1tick.get())))
        
        if self.existY2 == 1:
            if (self.entry_Xtick.get() != "")&(self.var_LogX[0].get()==False):
                self.ax2.xaxis.set_minor_locator(plt.MultipleLocator(float(self.entry_Xtick.get())))
            if (self.entry_Y2tick.get() != "")&(self.var_LogY2[0].get()==False):
                self.ax2.yaxis.set_minor_locator(plt.MultipleLocator(float(self.entry_Y2tick.get())))

    # センターフレームの線の長さ設定
    def centerline(self):
        root.update_idletasks()
        x = self.frameL.winfo_height()
        y = self.frameR.winfo_height()

        if (x > y):
            self.canvas["height"] = x
        else:
            self.canvas["height"] = y

    # 現在のconfigをtxtファイルに出力
    def output_config(self):
        path = self.get_folderpath(self.filepath)
        filename = self.get_filename(self.filepath)
        f = open(path+filename+"_GG.txt", 'w')

        config = ""
        config = config + "X-axis name:"     + self.entry_Xname.get()             + "\n"
        config = config + "Y1-axis name:"    + self.entry_Y1name.get()            + "\n"
        config = config + "Y2-axis name:"    + self.entry_Y2name.get()            + "\n"
        config = config + "X-range:"         + self.entry_Xrange_min.get()        + "," + self.entry_Xrange_max.get()       + "," + self.entry_Xtick.get() + "\n"
        config = config + "Y1-range:"        + self.entry_Y1range_min.get()       + "," + self.entry_Y1range_max.get()      + "," + self.entry_Y1tick.get() + "\n"
        config = config + "Y2-range:"        + self.entry_Y2range_min.get()       + "," + self.entry_Y2range_max.get()      + "," + self.entry_Y2tick.get() + "\n"
        config = config + "Label font size:" + self.entry_fontsize_of_label.get() + "," + self.entry_fontsize_of_tick.get() + "\n"
        config = config + "sci:"             + str(self.var_sciX[0].get())        + "," + str(self.var_sciY1[0].get())      + "," + str(self.var_sciY2[0].get()) + "\n" 
        config = config + "MarkerSize:"      + self.entry_MarkerSize.get()        + "\n"
        config = config + "LineWidth:"       + self.entry_LineWidth.get()         + "\n"
        config = config + "grid:"             + str(self.var_grid[0].get())        + "\n"
        config = config + "Windowsize:"       + self.entry_WindowWidth.get()       + "," + self.entry_WindowHeight.get()     + "\n"
        for i in range(self.column):
            config = config + "X:"            + self.combobox_X[i].get()         + ","
            config = config + "Y1:"           + str(self.var_Y1[i].get())        + ","
            config = config + "Y2:"           + str(self.var_Y2[i].get())        + ","
            config = config + "Label:"        + self.entry_Label[i].get()        + ","
            config = config + "Marker:"       + self.combobox_Marker[i].get()    + ","
            config = config + "FaceColor:"    + self.combobox_FaceColor[i].get() + ","
            config = config + "Line:"         + self.combobox_Line[i].get()      + ","
            config = config + "Color:"        + self.combobox_Color[i].get()     + ","
            config = config + "Approx:"       + self.combobox_Approx[i].get()    + ","
            config = config + "Degree:"       + self.entry_Degree[i].get()       + ","
            config = config + "Approx Label:" + self.entry_ApproxLabel[i].get()  + "\n"

        config = config + "LogX:"  + str(self.var_LogX[0] .get())  + "\n"
        config = config + "LogY1:" + str(self.var_LogY1[0].get()) + "\n"
        config = config + "LogY2:" + str(self.var_LogY2[0].get()) + "\n" 

        f.write(config)
        f.close()

    # 前回のconfigを取り込み反映
    def input_config(self):
        path = self.get_folderpath(self.filepath)
        filename = self.get_filename(self.filepath)
        if os.path.exists(path+filename+"_GG.txt"):
            f = open(path+filename+"_GG.txt")
            config = f.read()

            config = config.split("\n")

            Xname = config[0].split(":")
            self.entry_Xname.insert(tk.END, Xname[1])

            Y1name = config[1].split(":")
            self.entry_Y1name.insert(tk.END, Y1name[1])

            Y2name = config[2].split(":")
            self.entry_Y2name.insert(tk.END, Y2name[1])

            Xrange = config[3].split(":")
            Xparam = Xrange[1].split(",")
            self.entry_Xrange_min.insert(tk.END, Xparam[0])
            self.entry_Xrange_max.insert(tk.END, Xparam[1])
            self.entry_Xtick.insert(tk.END, Xparam[2])

            Y1range = config[4].split(":")
            Y1param = Y1range[1].split(",")
            self.entry_Y1range_min.insert(tk.END, Y1param[0])
            self.entry_Y1range_max.insert(tk.END, Y1param[1])
            self.entry_Y1tick.insert(tk.END, Y1param[2])

            Y2range = config[5].split(":")
            Y2param = Y2range[1].split(",")
            self.entry_Y2range_min.insert(tk.END, Y2param[0])
            self.entry_Y2range_max.insert(tk.END, Y2param[1])
            self.entry_Y2tick.insert(tk.END, Y2param[2])

            fontsizerange = config[6].split(":")
            fontsizeparam = fontsizerange[1].split(",")
            self.entry_fontsize_of_label.delete(0,tk.END)
            self.entry_fontsize_of_tick.delete(0,tk.END)
            self.entry_fontsize_of_label.insert(tk.END, fontsizeparam[0])
            self.entry_fontsize_of_tick.insert(tk.END, fontsizeparam[1])

            scirange = config[7].split(":")
            sciparam = scirange[1].split(",")
            self.var_sciX[0].set(sciparam[0])
            self.var_sciY1[0].set(sciparam[1])
            self.var_sciY2[0].set(sciparam[2])

            MarkerSize = config[8].split(":")
            self.entry_MarkerSize.delete(0,tk.END)
            self.entry_MarkerSize.insert(tk.END, MarkerSize[1])

            LineWidth = config[9].split(":")
            self.entry_LineWidth.delete(0,tk.END)
            self.entry_LineWidth.insert(tk.END, LineWidth[1])

            grid = config[10].split(":")
            self.var_grid[0].set(grid[1])

            WindowSize  = config[11].split(":")
            Windowparam = WindowSize[1].split(",")
            self.entry_WindowWidth .delete(0, tk.END)
            self.entry_WindowHeight.delete(0,tk.END)
            self.entry_WindowWidth .insert(tk.END, Windowparam[0])
            self.entry_WindowHeight.insert(tk.END, Windowparam[1])
            
            for i in range(self.column):
                data_config = config[12+i].split(",")
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

                FaceColor = data_config[5].split(":")
                self.combobox_FaceColor[i].set(FaceColor[1])

                line = data_config[6].split(":")
                self.combobox_Line[i].set(line[1])

                Color = data_config[7].split(":")
                self.combobox_Color[i].set(Color[1])

                approx = data_config[8].split(":")
                self.combobox_Approx[i].set(approx[1])

                degree = data_config[9].split(":")
                self.entry_Degree[i].insert(tk.END, degree[1])

                aplabel = data_config[10].split(":")
                self.entry_ApproxLabel[i].insert(tk.END, aplabel[1])

            LogX = config[12+self.column].split(":")
            self.var_LogX[0].set(LogX[1])

            LogY1 = config[12+self.column+1].split(":")
            self.var_LogY1[0].set(LogY1[1])

            LogY2 = config[12+self.column+2].split(":")
            self.var_LogY2[0].set(LogY2[1])

            f.close()
        else:
            pass

    # 操作ファイルのフォルダパス取得
    def get_folderpath(self, filepath):
        while(filepath[-1]!="/"):
            filepath = filepath[:-1]
        folderpath = filepath
        return folderpath
    
    # 操作ファイルの拡張子なし名称取得
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