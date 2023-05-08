import tkinter
n = 0
def click():
    global n
    n+=1
    print(n)
    if n==10:
        print('good')
    if n==50:
       print('very good')
    if n==100:
        print('super')
    if n==500:
        print('topg')
    if n==1000:
        print('hacker')

w = tkinter.Tk()
w.title('clickme')
l = tkinter.Label(w, text='CLICK ME', font=('bold',50))
l.pack()
b = tkinter.Button(w, text='Click me')
b.config(command=click)
b.pack()

w.mainloop()