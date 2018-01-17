from tkinter import messagebox
import tkinter
from tkinter import *


root = Tk()
root.title('Math')
root.resizable(0,0)


class application(Frame):

    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        global hit
        self.hit = False
        global ans
        self.ans = '0'
        self.create_display(25,'Pocket Calculator')

    # ------
    # ------
    def create_display(self,font_size,font_family):
        self.display = Entry(self, font=(font_family, font_size), borderwidth=10, relief=RAISED, justify=RIGHT,width=15,bg='black',fg='white')
        self.display.insert(0, '0')
        self.display.grid(row='0', column='0', columnspan=4)
        self.create_buttons(15, 'Verdana',1,1,'#282830','#ECF0F1')

    def get_buttons_text(self, txt):
        self.entry_text = self.display.get()
        self.last_index = len(self.entry_text)
        if self.entry_text == '0':
            self.display.delete(0,END)
            #self.display.insert(0,txt)
        if self.hit == True:
            self.display.delete(0, END)
            self.display.insert(self.last_index, txt)
            self.hit = False
        else:
            self.display.insert(self.last_index, txt)



    # ------ get value
    def evaluation(self):
       try:
            self.entry_text = self.display.get()
            self.ans= self.display.get()
            self.display.delete(0, END)
            self.display.insert(0,eval(self.entry_text))
            self.hit=True
       except:
           messagebox.showerror("Error", "Typing Error")

    # ------ init buttons
    def create_buttons(self,font_size, font_family,w,h,b,f):

        # ------ / * - C Buttons
        self.btn = Button(self, height=h,width=w, font=(font_family, font_size),bg=b,fg=f, borderwidth=0, text='C',command=lambda : self.display.delete(0, END))
        self.btn.grid(row=1, column=0, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='/',borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('/'))
        self.btn.grid(row=1, column=1, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='*', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('*'))
        self.btn.grid(row=1, column=2, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='-', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('-'))
        self.btn.grid(row=1, column=3, sticky='NWNESWSE')
        # ------ 7 8 9 + Buttons
        self.btn = Button(self, height=h, width=w, font=(font_family, font_size),text='7', bg=b, fg=f, borderwidth=0, command=lambda: self.get_buttons_text('7'))
        self.btn.grid(row=2,column=0, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='8', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('8'))
        self.btn.grid(row=2, column=1,sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='9', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('9'))
        self.btn.grid(row=2, column=2, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='+', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('+'))
        self.btn.grid(row=2, column=3, sticky='NWNESWSE',rowspan=2)
        # ------ 4 5 6
        self.btn = Button(self, height=h, width=w, font=(font_family, font_size), text='4', bg=b, fg=f, borderwidth=0, command=lambda: self.get_buttons_text('4'))
        self.btn.grid(row=3, column=0, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='5', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('5'))
        self.btn.grid(row=3, column=1, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='6', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('6'))
        self.btn.grid(row=3, column=2, sticky='NWNESWSE')
        # ----- 1 2 3 =
        self.btn = Button(self, height=h, width=w, font=(font_family, font_size), text='1', bg=b, fg=f, borderwidth=0, command=lambda: self.get_buttons_text('1'))
        self.btn.grid(row=4, column=0, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='2', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('2'))
        self.btn.grid(row=4, column=1, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='3', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('3'))
        self.btn.grid(row=4, column=2, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='=', borderwidth=0, bg=b, fg=f, command=lambda: self.evaluation())
        self.btn.grid(row=4, column=3, sticky='NWNESWSE', rowspan=2)
        # ------ 0 .
        self.btn = Button(self, height=h, width=w, font=(font_family, font_size), text='0', bg=b, fg=f, borderwidth=0, command=lambda: self.get_buttons_text('0'))
        self.btn.grid(row=5, column=0, columnspan=2, sticky='NWNESWSE')
        self.btn = Button(self, font=(font_family, font_size), text='.', borderwidth=0, bg=b, fg=f, command=lambda: self.get_buttons_text('.'))
        self.btn.grid(row=5, column=2, sticky='NWNESWSE')

        # ------ ans
        self.btn = Button(self, font=(font_family, font_size), text='Ans', borderwidth=1, bg=b, fg=f, command=lambda: self.display.insert( 0, eval(self.ans)))
        self.btn.grid(row=6, column=0, sticky='NWNESWSE',columnspan=4)





app = application(root).grid()
root.mainloop()