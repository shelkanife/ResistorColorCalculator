#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import Combobox
from functools import partial
from calc import  Calc
from metrics import font_label,font_title,sizes,label_xy,colors_tolerance,label_text,colors_list,hex_color,torelance_values,paths

class Window:
    def __init__(self,title,size):
        self.window=Tk()
        self.window.title(title)
        self.window.geometry(size)
        self.window.resizable(False,True)

        #SETTING CONTAINER
        #main container
        self.main_frame=LabelFrame(self.window)
        #radio buttons
        self.stripes_frame=Frame(self.main_frame)
        self.img_key=IntVar()
        #imagen and label stripes
        self.img_frame=Frame(self.main_frame)
        self.bg_img=Label(self.img_frame)
        self.stripes=[Label(self.img_frame) for _ in range(5)]
        #combo boxes
        self.select_frame=Frame(self.main_frame)
        self.combo_labels=[Label(self.select_frame) for x in range(5)]
        self.combo_stripes=[Combobox(self.select_frame,state='readonly') for x in range(5)]
        #------------------------------------------
        #RESULT CONTAINER
        self.result=LabelFrame(self.window)
        #resistor value and isComercial? info
        self.info_frame=Frame(self.result)
        self.result_frame=Frame(self.info_frame)
        self.conversion_frame=Frame(self.info_frame)
        self.conversion_key=IntVar(value=1)
        self.ohms=Entry(self.result_frame)
        self.tolerance=Entry(self.result_frame)
        self.comercial_frame=Frame(self.info_frame)
        self.is_comercial=Entry(self.comercial_frame)
        #------------------------------------------
        self.controller=Calc()

        self.generate_layout()
        self.window.mainloop()

    def generate_layout(self):
        _4spripes=Radiobutton(self.stripes_frame,text="4 stripes",variable=self.img_key,value=4,font=font_label,command=self.change_resistor_img)
        _4spripes.grid(row=0,column=0,padx=3)
        _5spripes=Radiobutton(self.stripes_frame,text="5 stripes",variable=self.img_key,value=5,font=font_label,command=self.change_resistor_img)
        _5spripes.grid(row=0,column=1,padx=3)
        # _6spripes=Radiobutton(self.stripes_frame,text="6 stripes",variable=self.stripes,value=6,command=self.change_resistor_img)
        # _6spripes.grid(row=0,column=2)
        
        self.main_frame.config(text='Settings',font=font_title)
        self.stripes_frame.pack(padx=10,pady=10)
        self.main_frame.pack()

        self.bg_img.config(relief=SUNKEN,background='#fff')
        self.bg_img.pack(padx=10)

        self.create_stripes()
        
        self.img_frame.pack()

        self.create_selects()
        self.select_frame.pack()

        _4spripes.select()
        self.change_resistor_img()

        self.create_resistor_value()
        self.info_frame.pack()

        self.create_conversion_frame()

        self.result.config(text='Result',font=font_title)
        self.result.pack(padx=9,pady=9,fill=BOTH,expand=True)

    def create_resistor_value(self):
        Label(self.result_frame,text='Resistor total value: ',font=font_label).grid(row=0,column=0)
        self.ohms.config(state='readonly',justify=CENTER,font=font_label)
        self.ohms.grid(row=0,column=1)
        
        Label(self.result_frame,text='Tolerance:',font=font_label).grid(row=1,column=0)
        self.tolerance.config(state='readonly',justify=CENTER,font=font_label)
        self.tolerance.grid(row=1,column=1)
        
        self.result_frame.config(relief=RIDGE,highlightbackground='black',highlightthickness=1)
        self.result_frame.grid(row=0,column=0,pady=15,padx=0)
        
        Label(self.comercial_frame,text='EIA nearest value',font=font_label).pack()
        self.is_comercial.config(state='disabled',justify=CENTER)
        self.is_comercial.pack()
        self.comercial_frame.config(relief=RIDGE,highlightbackground='black',highlightthickness=1)
        self.comercial_frame.grid(row=0,column=2,padx=50,sticky=W)

    def create_stripes(self):
        for i,stripe in enumerate(self.stripes):
            stripe.config(width=sizes[i][0],height=sizes[i][1],
                bg='#f1edec',borderwidth=1,relief='solid',state='disabled')
            stripe.place(x=label_xy[i][0],y=label_xy[i][1])

    def create_selects(self):
        # --------- Tolerance stripe ------
        self.combo_stripes[4].config(font=font_label,width=7)
        self.combo_stripes[4]['values']=colors_tolerance
        self.combo_stripes[4].bind("<<ComboboxSelected>>",partial(self.change_color_stripe,self.stripes[4],self.combo_stripes[4]))
        self.combo_labels[4].config(text=label_text[4],font=font_label)
        self.combo_labels[4].grid(row=0,column=4)
        self.combo_stripes[4].grid(row=1,column=4,padx=8,pady=3)
        self.combo_stripes[4].set("golden")
        self.change_color_stripe(self.stripes[4],self.combo_stripes[4],None)

        # --------- Color stripes ---------
        for i,combo_stripe in enumerate(self.combo_stripes[0:4]):
            combo_stripe.config(font=font_label,width=7)
            combo_stripe['values']=colors_list
            combo_stripe.bind("<<ComboboxSelected>>",partial(self.change_color_stripe,self.stripes[i],combo_stripe))
            self.combo_labels[i].config(text=label_text[i],font=font_label)
            self.combo_labels[i].grid(row=0,column=i)
            combo_stripe.grid(row=1,column=i,padx=8,pady=3)
            combo_stripe.set("black")
            self.change_color_stripe(self.stripes[i],combo_stripe,None)

        

    def change_color_stripe(self,stripe:Label,combo:Combobox,event)->None:
        color=combo.get()
        stripe.config(bg=hex_color[color])
        index=self.combo_stripes.index(combo)
        if index > 3: 
            self.chance_tolerance_value(color)
            return
        self.controller.change_stripe_value(color,index)
        self.change_total()
        
    def chance_tolerance_value(self,color):
        self.tolerance.config(state='normal')
        self.tolerance.delete(0,'end')
        self.tolerance.insert(0,torelance_values[color])
        self.tolerance.config(state='readonly')
        self.change_EIA()

    def change_EIA(self):
        value=self.controller.find_standard_resistand_value(self.combo_stripes[4].get())
        self.is_comercial['state']='normal'
        self.is_comercial.delete(0,'end')
        self.is_comercial.insert(0,value)
        self.is_comercial['state']='readonly'

    def change_total(self):
        self.controller.compute_total(self.img_key.get())
        total=self.controller.change_ohms_mesurement(self.conversion_key.get())
        self.ohms.config(state='normal')
        self.ohms.delete(0,'end')
        self.ohms.insert(0,total)
        self.ohms.config(state='readonly')
        self.change_EIA()
        
    def change_resistor_img(self):
        key=self.img_key.get()
        if key == 4:
            self.stripes[2].place_forget()
            self.combo_stripes[2].grid_forget()
            self.combo_labels[2].grid_forget()
        else:
            self.stripes[2].place(x=label_xy[2][0],y=label_xy[2][1])
            self.combo_labels[2].grid(row=0,column=2,)
            self.combo_stripes[2].grid(row=1,column=2)
        _path=paths[str(key)]
        photo=PhotoImage(file=_path)
        self.bg_img.config(image=photo)
        self.bg_img.image=photo
        self.controller.compute_total(key)
        self.change_ohms_mesurement()
        self.change_EIA()

    def create_conversion_frame(self):
        ohms=Radiobutton(self.conversion_frame,text="Ω  ",variable=self.conversion_key,value=1,font=font_label,command=self.change_ohms_mesurement)
        ohms.pack()
        Kohms=Radiobutton(self.conversion_frame,text="KΩ",variable=self.conversion_key,value=1_000,font=font_label,command=self.change_ohms_mesurement)
        Kohms.pack()
        Gohms=Radiobutton(self.conversion_frame,text="MΩ",variable=self.conversion_key,value=1_000_000,font=font_label,command=self.change_ohms_mesurement)
        Gohms.pack()
        self.conversion_frame.grid(row=0,column=1)
        ohms.select()
        
    def change_ohms_mesurement(self):
        new_total=self.controller.change_ohms_mesurement(self.conversion_key.get())
        self.ohms.config(state='normal')
        self.ohms.delete(0,'end')
        self.ohms.insert(0,new_total)
        self.ohms.config(state='readonly')    