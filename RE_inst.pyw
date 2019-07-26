# -*- coding: utf-8 -*-
import tkinter
import re
import pyperclip

def paste0():
	text0_2_0.insert(tkinter.INSERT,str(pyperclip.paste()))

def test_text(text_test):
    try:
        comand_re = re.compile('{}'.format(text_test))
        text0_2_1.delete(1.0, tkinter.END)
        v = comand_re.findall(text0_2_0.get(1.0, 'end-1c'))
        text0_2_1.insert(tkinter.INSERT, str(v))
    except re.error:
        test_text('')


def control():
    global Check_a
    global Check_b
    a = text0_1.get(1.0, 'end-1c')
    B = text0_2_0.get(1.0, 'end-1c')
    if a != Check_a or B != Check_b:
        Check_a, Check_b = a, B
        lab['text'] = f're.compile("{str(a)}")'
        test_text(str(a)) if a != '' else text0_2_1.delete(1.0, tkinter.END)
        windo.after(100, control)
    windo.after(100, control)


####################
Check_a = None
Check_b = None
####################


windo = tkinter.Tk()
windo.geometry('666x380')
windo['bg'] = '#abb86e'
#____________________________ SET TK ____________________________#

lab = tkinter.Label(windo, text=r're.compile("{ }")', font=("Helvetica", 14))
text0_1 = tkinter.Text(windo, width=5, height=2, bg='#ffffff')

frame0 = tkinter.Frame(windo, bg='#abb86e')
frame1 = tkinter.Frame(windo, bg='#abb86e')
lab_text0_2_0 = tkinter.Label(frame1, text='Исходный текст',bg='#ccc36e')
text0_2_0 = tkinter.Text(frame0, width=5, height=1, bg='#ffffff')


lab_text0_2_1 = tkinter.Label(frame1, text='Результат',bg='#ccc36e')
text0_2_1 = tkinter.Text(frame0, width=5, height=1, bg='#ffffff')

bat_past = tkinter.Button(windo,bg='#bda760',relief=tkinter.GROOVE,text='PAST',command=paste0)

#____________________________ PACK ____________________________#

lab.pack(fill=tkinter.BOTH, padx=10, pady=10)
text0_1.pack(fill=tkinter.BOTH, padx=10, pady=10)



frame1.pack(fill=tkinter.BOTH)
lab_text0_2_0.pack(side='left', fill=tkinter.BOTH, expand=True)
lab_text0_2_1.pack(side='left', fill=tkinter.BOTH, expand=True)

frame0.pack(fill=tkinter.BOTH, expand=True)
text0_2_0.pack(side='left', fill=tkinter.BOTH, expand=True, padx=10, pady=10)
text0_2_1.pack(side='left', fill=tkinter.BOTH, expand=True, padx=10, pady=10)
bat_past.pack(fill=tkinter.BOTH)
#________________________________________________________#
control()
windo.mainloop()


"""
def les():
	# https://regex101.com/
	# Найти знаение между символами
	a = r'C:\\Program Files\\Image-Line\\Downloader\\Update'
	# Обезательно (.*?)
	x = r'\\'
	re.compile(r'(.*?){}'.format(x))
import re
a = r'C:\\Program Files\\Image-Line\\Downloader\\Update'
b = re.compile(r'[\\w-]+')
c = b.findall(a)
print(a)
print(b)
print(c)
"""
