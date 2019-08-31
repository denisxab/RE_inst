# -*- coding: utf-8 -*-
"""
Re утилита
"""
# pylint: disable=C0103
import re
import tkinter
import pyperclip


class Re_inp:
    """docstring for Re_inp"""

    def __init__(self):
        super(Re_inp, self).__init__()
        self.Check_a = None
        self.Check_b = None
        self.Windows = tkinter.Tk()
        self.Windows.geometry('666x380')
        self.Windows['bg'] = '#abb86e'
        self.lab = tkinter.Label(
            self.Windows, text=r're.compile("{ }")', font=("Helvetica", 14))
        self.text0_1 = tkinter.Text(
            self.Windows, width=5, height=2, bg='#ffffff')
        self.frame0 = tkinter.Frame(self.Windows, bg='#abb86e')
        self.frame1 = tkinter.Frame(self.Windows, bg='#abb86e')
        self.text0_2_0 = tkinter.Label(
            self.frame1, text='Исходный текст', bg='#ccc36e')
        self.text0_2_0 = tkinter.Text(
            self.frame0, width=5, height=1, bg='#ffffff')
        self.text0_2_1 = tkinter.Label(
            self.frame1, text='Результат', bg='#ccc36e')
        self.text0_2_1 = tkinter.Text(
            self.frame0, width=5, height=1, bg='#ffffff')
        self.bat_past = tkinter.Button(
            self.Windows, bg='#bda760', relief=tkinter.GROOVE, text='PAST', command=self.paste0)

        self.pack()
        self.control()

        self.Windows.mainloop()

    def pack(self):
        self.lab.pack(fill=tkinter.BOTH, padx=10, pady=10)
        self.text0_1.pack(fill=tkinter.BOTH, padx=10, pady=10)
        self.frame1.pack(fill=tkinter.BOTH)
        self.text0_2_0.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.text0_2_1.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.frame0.pack(fill=tkinter.BOTH, expand=True)
        self.text0_2_0.pack(side='left', fill=tkinter.BOTH,
                            expand=True, padx=10, pady=10)
        self.text0_2_1.pack(side='left', fill=tkinter.BOTH,
                            expand=True, padx=10, pady=10)
        self.bat_past.pack(fill=tkinter.BOTH)

    def pack_forget(self):
        self.lab.pack_forget()
        self.text0_1.pack_forget()
        self.frame1.pack_forget()
        self.lab_self.text0_2_0.pack_forget()
        self.lab_self.text0_2_1.pack_forget()
        self.frame0.pack_forget()
        self.text0_2_0.pack_forget()
        self.text0_2_1.pack_forget()
        self.bat_past.pack_forget()

    def test_text(self, text_test: str):
        try:
            self.lab['fg'] = '#000000'
            comand_re = re.compile('{}'.format(text_test))
            self.text0_2_1.delete(1.0, tkinter.END)
            v = comand_re.findall(re.escape(self.text0_2_0.get(1.0, 'end-1c')))
            if not v:
                self.lab['fg'] = '#e05555'
            else:
                self.text0_2_1.insert(tkinter.INSERT, str(v))
        except re.error:
            self.lab['fg'] = '#e05555'

    def control(self):
        a = self.text0_1.get(1.0, 'end-1c')
        B = self.text0_2_0.get(1.0, 'end-1c')
        if a != self.Check_a or B != self.Check_b:  # pylint: disable=E0601
            self.Check_a, self.Check_b = a, B
            self.lab['text'] = f're.compile("{str(a)}")'
            self.test_text(str(a)) if a != '' else self.text0_2_1.delete(
                1.0, tkinter.END)  # pylint: disable=W0106
            self.Windows.after(100, self.control)
        self.Windows.after(100, self.control)

    def paste0():
        self.text0_2_0.insert(tkinter.INSERT, str(pyperclip.paste()))


if __name__ == '__main__':
    Re_inp()
