from time import time
from tkinter import * 
main1=Tk()
main1.geometry("300x750")
main1.title("CHat bot")
main1.configure(bg="black")
e1=Entry(main1,width=45)
e1.pack()
def fullwp():
    import wikipedia
    wikipedia.set_lang("en")
    answer=wikipedia.summary(e1.get())
    ff=LabelFrame(main1,text="WIKIPEDIA FULL PAGE SEARCH RESULT",width=200)
    ff.pack()
    asn=Label(ff,text=answer)
    asn.pack()
    start=time()
    ff.after(55000,ff.destroy)
    end=time()
def remove_newlines(fname):
    flist=open(fname).readlines()
    return [s.rstrip('\n')for s in flist]
def ansr():
    a=e1.get()
    p=0
    fo=open("quest.txt")
    fy=open("ans.txt")
    fod=remove_newlines('quest.txt')
    foy=remove_newlines('ans.txt')
    t=0
    for i in fod:
        if i==a:
            t=1
            ko=("=> "+str(foy[p]))
            asn=Label(main1,text=ko)
            asn.pack()
            start=time()
            main1.after(5000,asn.destroy)
            end=time()
            break
        p=p+1
    if t==0:
        try:
            import wikipedia
            wikipedia.set_lang("en")
            answer=wikipedia.summary(a,sentences=1)
            fa=LabelFrame(main1,text="WIKIPEDIA SEARCH RESULT",width=200)
            fa.pack()
            asn=Label(fa,text=answer)
            asn.pack()
            mb=Button(fa,text="SHOW MORE",command=fullwp,height=1,width=4)
            mb.pack()
            start=time()
            fa.after(55000,fa.destroy)
            end=time()
        except:
            an=Label(main1,text="I CANT UNDERSTAND , BE CLEAR ")
            an.pack()
            start=time()
            an.after(5000,an.destroy)
            end=time()
        

#process
but1=Button(main1,text='ENTER',command=ansr)
but1.pack()
main1.mainloop()

