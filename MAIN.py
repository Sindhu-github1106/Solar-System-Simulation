import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ursina import *
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import messagebox
import mysql.connector as mys
import tabulate
from tkinter import font

con=mys.connect(host='localhost', user='root', passwd='1106', database='space')
cur=con.cursor()

pluto=open("content/pluto.txt","r")
eris=open("content/eris.txt")
ceres=open("content/ceres.txt")
first=open("content/terres.txt")
last=open("content/jovians.txt")
moon=open("content/moons.txt")
bear=open("content/bear.txt")
leo=open("content/leo.txt")
orion=open("content/orion.txt")

def dwarf():
    mywin=Toplevel(root)
    mywin.geometry("1175x600")
    
    
    def pluto_():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        frame = Frame(win, width=600, height=400)
        frame.pack()
        label2 = Label( frame, text = "Pluto",font="Times 25")
        label2.pack(pady = 50)
    
        img = PhotoImage(file = "templates/pluto.png")
        
        label = Label(frame, image = img)
        label.pack()

        label2 = Label( frame, text = pluto.read(),font="Times 14")
        label2.pack(pady = 50)
        pluto.seek(0)
        win.mainloop()
        
    def eris_():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        frame = Frame(win, width=600, height=400)
        frame.pack()
        label2 = Label( frame, text = "Eris",font="Times 25")
        label2.pack(pady = 50)
    
        img = PhotoImage(file = "templates/eris.png")
        
        label = Label(frame, image = img)
        label.pack()

        label2 = Label( frame, text = eris.read(),font="Times 14")
        label2.pack(pady = 50)
        eris.seek(0)
        win.mainloop()
        
    def ceres_():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        frame = Frame(win, width=600, height=400)
        frame.pack()
        label2 = Label( frame, text = "Ceres",font="Times 25")
        label2.pack(pady = 50)
    
        img = PhotoImage(file = "templates/ceres.png")
        
        label = Label(frame, image = img)
        label.pack()

        label2 = Label( frame, text = ceres.read(),font="Times 14")
        label2.pack(pady = 50)
        ceres.seek(0)
        win.mainloop()
        
    bbg = PhotoImage(file = "templates/dwarfplanet.jpg")

    label4 = Label( mywin, image = bbg)
    label4.place(x = 0, y = 0)

    label3 = Label( mywin, text = "DWARF PLANETS",font="Times 30")
    label3.pack(pady = 50)
    
    myFont = font.Font(family='Helvetica', size=17)

    button_1 = Button(mywin,text="𝙋𝙇𝙐𝙏𝙊",command=pluto_)
    button_1['font']=myFont
    button_1.pack(pady=20)
    
    button_2 = Button(mywin,text="𝙀𝙍𝙄𝙎",command=eris_)
    button_2['font']=myFont
    button_2.pack(pady=20)
    
    button_3 = Button(mywin,text="𝘾𝙀𝙍𝙀𝙎",command=ceres_)
    button_3['font']=myFont
    button_3.pack(pady=20)
    
    mywin.mainloop()

#     button2 = Button( frame1, text="ERIS",command=eris)
#     button2.pack(pady = 20)


def planets():
    mywin=Toplevel(root)
    mywin.geometry("1600x1000")
    
    
    def terrestrials():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        frame = Frame(win, width=600, height=400)
        frame.pack()
        label2 = Label( frame, text = "TERRESTRIALS",font="Times 25")
        label2.pack(pady = 50)
    
        img = PhotoImage(file = "templates/first.png")
        
        label = Label(frame, image = img)
        label.pack()

        label2 = Label( frame, text = first.read(),font="Times 14")
        label2.pack(pady = 50)
        first.seek(0)
        win.mainloop()
        
    def jovians():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        frame = Frame(win, width=600, height=400)
        frame.pack()
        label2 = Label( frame, text = "JOVIANS",font="Times 25")
        label2.pack(pady = 50)
    
        img = PhotoImage(file = "templates/last.png")
        
        label = Label(frame, image = img)
        label.pack()

        label2 = Label( frame, text = last.read(),font="Times 14")
        label2.pack(pady = 50)
        last.seek(0)
        win.mainloop()
        
        
    bbg = PhotoImage(file = "templates/bgg.png")

    label4 = Label( mywin, image = bbg)
    label4.place(x = 0, y = 0)

    label3 = Label( mywin, text = "PLANETS OF OUR SOLAR SYSTEM",font="Times 30")
    label3.pack(pady = 30)
    
    click_btn1= PhotoImage(file='templates/first.png')

    #Let us create a label for button event
    #img_label= Label(image=click_btn)

    #Let us create a dummy button and pass the image
    button2= Button(mywin, image=click_btn1,command= terrestrials,borderwidth=0)
    button2.pack(pady=30)
    
    click_btn= PhotoImage(file='templates/last.png')

    #Let us create a label for button event
    #img_label= Label(image=click_btn)

    #Let us create a dummy button and pass the image
    button= Button(mywin, image=click_btn,command= jovians,borderwidth=0)
    button.pack(pady=30)
    
    mywin.mainloop()



def moon__():
    mywin=Toplevel(root)
    mywin.geometry("1540x790")
    
    
    def moon1():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        frame = Frame(win, width=600, height=400)
        frame.pack()
        label2 = Label( frame, text = "MOONS",font="Times 25")
        label2.pack(pady = 50)
    
        img = PhotoImage(file = "templates/moon.png")
        
        label = Label(frame, image = img)
        label.pack()

        label2 = Label( frame, text = moon.read(),font="Times 14")
        label2.pack(pady = 50)
        moon.seek(0)
        win.mainloop()
        
    def moon_graph():
        planets = ['MERCURY','VENUS','EARTH','MARS','JUPITER','SATURN','URANUS','NEPTUNE']
        moons = [0,0,1,2,80,83,27,14]

        plt.bar(planets,moons)
        plt.title('HOW MANY MOONS DOES EVERY PLANET HAVE ?')
        x_pos=np.arange(len(planets))
        plt.bar(x_pos,moons,color=['black','black','purple','orange','pink','lime','crimson','cyan'],edgecolor='black')
        plt.xticks(x_pos,planets)
        plt.show()
        
        
    bbg = PhotoImage(file = "templates/moons.png")

    label4 = Label( mywin, image = bbg)
    label4.place(x = 0, y = 0)

    label3 = Label( mywin, text = "MOONS",font="Times 30")
    label3.pack(pady = 50)

    click_btn1= PhotoImage(file='moon.png')
    button2= Button(mywin, image=click_btn1,command= moon1,borderwidth=0)
    button2.pack(side=LEFT,padx=200,pady=30)
    
    click_btn= PhotoImage(file='graph.png')
    button2= Button(mywin, image=click_btn,command= moon_graph,borderwidth=0)
    button2.pack(side=LEFT,padx=1,pady=30)
    
    mywin.mainloop()



def constel():
    mywin=Toplevel(root)
    mywin.geometry("1175x600")
    
    
    def greatbear():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        frame = Frame(win, width=600, height=400)
        frame.pack()
        label2 = Label( frame, text = "GREAT BEAR",font="Times 25")
        label2.pack(pady = 50)
    
        img = PhotoImage(file = "templates/bear.png")
        
        label = Label(frame, image = img)
        label.pack()

        label2 = Label( frame, text = bear.read(),font="Times 14")
        label2.pack(pady = 50)
        bear.seek(0)
        win.mainloop()
        
    def orion1():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        frame = Frame(win, width=600, height=400)
        frame.pack()
        label2 = Label( frame, text = "ORION",font="Times 25")
        label2.pack(pady = 50)
    
        img = PhotoImage(file = "templates/orion.png")
        
        label = Label(frame, image = img)
        label.pack()

        label2 = Label( frame, text = orion.read(),font="Times 14")
        label2.pack(pady = 50)
        orion.seek(0)
        win.mainloop()
    
    def leo1():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        frame = Frame(win, width=600, height=400)
        frame.pack()
        label2 = Label( frame, text = "Leo",font="Times 25")
        label2.pack(pady = 50)
    
        img = PhotoImage(file = "templates/leo.png")
        
        label = Label(frame, image = img)
        label.pack()

        label2 = Label( frame, text = bear.read(),font="Times 14")
        label2.pack(pady = 50)
        leo.seek(0)
        win.mainloop()

        
        
    bbg = PhotoImage(file = "templates/constel.png")

    label4 = Label( mywin, image = bbg)
    label4.place(x = 0, y = 0)

    label3 = Label( mywin, text = "CONTELLATIONS",font="Times 30")
    label3.pack(pady = 50)
    
    myFont = font.Font(family='Helvetica', size=17)

    button_1 = Button(mywin,text="𝙂𝙍𝙀𝘼𝙏 𝘽𝙀𝘼𝙍",command=greatbear)
    button_1['font']=myFont
    button_1.pack(pady=20)
    
    button_2 = Button(mywin,text="𝙊𝙍𝙄𝙊𝙉",command=orion1)
    button_2['font']=myFont
    button_2.pack(pady=20)
    
    button_2 = Button(mywin,text="𝙇𝙀𝙊",command=leo1)
    button_2['font']=myFont
    button_2.pack(pady=20)
    
    mywin.mainloop()
    
def planetarium():
    mywin=Toplevel(root)
    mywin.geometry("1300x800")
    
    def book_now():
        win=Toplevel(mywin)
        win.geometry("1600x1000")
    
        answer1 = simpledialog.askstring("Input", "Enter Name:",parent=mywin)
        answer2 = simpledialog.askinteger("Input", "Enter Phone number:",parent=mywin)
        answer3 = simpledialog.askinteger("Input", "Enter Credit Card number:",parent=mywin)
        answer4 = simpledialog.askinteger("Input", "Enter Numer of tickets:",parent=mywin)
        
        cur.execute(f"insert into bookings values({answer2},'{answer1}',{answer3},{answer4});")
        con.commit()
        mywin.mainloop()
        
    bbg = PhotoImage(file = "templates/planet.png")

    label4 = Label( mywin, image = bbg)
    label4.place(x = 0, y = 0)

    label3 = Label( mywin, text = "PLANETARIUM",font="Times 25")
    label3.pack(pady = 20)
    
    img = PhotoImage(file = "templates/planetarium.png")
        
    label = Label(mywin, image = img)
    label.pack()
    
    label = Label( mywin, text ='''𝘼𝙩 𝙩𝙝𝙞𝙨 𝙥𝙡𝙖𝙘𝙚, 𝙗𝙚𝙖𝙪𝙩𝙮 𝙨𝙝𝙞𝙣𝙚𝙨, 𝙖𝙣𝙙 𝙨𝙚𝙘𝙧𝙚𝙩𝙨 𝙖𝙧𝙚 𝙪𝙣𝙘𝙤𝙫𝙚𝙧𝙚𝙙.
    𝙄𝙩 𝙞𝙨 𝙩𝙝𝙚 𝙗𝙞𝙜 𝙖𝙣𝙙 𝙨𝙤𝙥𝙝𝙞𝙨𝙩𝙞𝙘𝙖𝙩𝙚𝙙 𝙥𝙡𝙖𝙣𝙚𝙩𝙖𝙧𝙞𝙪𝙢 𝙩𝙝𝙖𝙩 𝙡𝙤𝙤𝙠𝙨 𝙡𝙞𝙠𝙚 𝙩𝙝𝙚 𝙨𝙪𝙣 𝙛𝙧𝙤𝙢 𝙤𝙪𝙩𝙨𝙞𝙙𝙚, 
    𝙗𝙪𝙩 𝙞𝙩 𝙨𝙝𝙞𝙣𝙚𝙨 𝙬𝙞𝙩𝙝 𝙨𝙘𝙞𝙚𝙣𝙘𝙚 𝙖𝙣𝙙 𝙠𝙣𝙤𝙬𝙡𝙚𝙙𝙜𝙚. 𝙄𝙣𝙨𝙞𝙙𝙚, 𝙞𝙩 𝙞𝙨 𝙮𝙤𝙪𝙧 𝙜𝙖𝙩𝙚𝙬𝙖𝙮 𝙩𝙤 𝙩𝙝𝙚 𝙙𝙚𝙚𝙥𝙚𝙨𝙩 𝙨𝙚𝙘𝙧𝙚𝙩𝙨
    𝙤𝙛 𝙩𝙝𝙚 𝙪𝙣𝙞𝙫𝙚𝙧𝙨𝙚 𝙖𝙣𝙙 𝙩𝙝𝙚 𝙗𝙧𝙞𝙜𝙝𝙩𝙚𝙨𝙩 𝙫𝙞𝙚𝙬𝙨 𝙤𝙛 𝙩𝙝𝙚 𝙨𝙠𝙮. 𝘽𝙤𝙤𝙠 𝙮𝙤𝙪𝙧 𝙩𝙞𝙘𝙠𝙚𝙩 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙬𝙤 𝙝𝙪𝙣𝙙𝙧𝙚𝙙 𝙨𝙠𝙮
    𝙚𝙣𝙩𝙝𝙪𝙨𝙞𝙖𝙨𝙩𝙨 𝙞𝙣 𝙖 𝙟𝙤𝙪𝙧𝙣𝙚𝙮 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚 𝙘𝙤𝙨𝙢𝙤𝙨 𝙬𝙞𝙩𝙝 𝙖 𝙥𝙞𝙘𝙩𝙪𝙧𝙚 𝙤𝙛 𝙩𝙝𝙚 𝙨𝙠𝙮 𝙗𝙡𝙖𝙣𝙠𝙚𝙩𝙞𝙣𝙜 𝙮𝙤𝙪 𝙖𝙗𝙤𝙫𝙚
    𝙮𝙤𝙪𝙧 𝙝𝙚𝙖𝙙 𝙖𝙣𝙙 𝙖 𝙢𝙞𝙣𝙙-𝙘𝙖𝙥𝙩𝙞𝙫𝙖𝙩𝙞𝙣𝙜 𝙨𝙤𝙪𝙣𝙙 𝙩𝙤 𝙚𝙭𝙥𝙡𝙤𝙧𝙚 𝙩𝙝𝙚 𝙨𝙠𝙮, 𝙩𝙝𝙚 𝙘𝙤𝙣𝙨𝙩𝙚𝙡𝙡𝙖𝙩𝙞𝙤𝙣𝙨, 𝙩𝙝𝙚 𝙥𝙡𝙖𝙣𝙚𝙩𝙨𝙖𝙣𝙙
    𝙩𝙝𝙚 𝙗𝙧𝙞𝙜𝙝𝙩𝙚𝙨𝙩 𝙤𝙛 𝙨𝙩𝙖𝙧𝙨. 𝙁𝙤𝙧 𝙟𝙪𝙨𝙩 20 𝙙𝙝𝙨.''',font="Times 14") 
    label.pack(pady = 20)
    
    myFont = font.Font(family='Helvetica', size=17)
    
    button5 = Button(mywin, text="𝔹𝕆𝕆𝕂 ℕ𝕆𝕎",command=book_now)
    button5['font']=myFont
    button5.pack(pady = 2)
    
    mywin.mainloop()

def zodiac():
    ws=Toplevel(root)
    ws.title("Python Guides")

    answer1 = simpledialog.askstring("Inputt", "Which month were you born in ? ex: september",parent=ws)
    if answer1 is not None:
    #        pass #print("Your first name is ", answer1)
             month=answer1
             print(answer1)
    else:
        print("blank error: Please Restart")

    answer1 = simpledialog.askinteger("Input", "Which day of the month were you born on ? ex: 29 ",parent=ws,minvalue=0, maxvalue=100)
    if answer1 is not None:
            day=answer1
            if month.lower() == 'december':
                astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
            elif month.lower() == 'january':
                astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
            elif month.lower() == 'february':
                astro_sign = 'Aquarius' if (day < 19) else 'pisces'
            elif month.lower() == 'march':
                astro_sign = 'Pisces' if (day < 21) else 'aries'
            elif month.lower() == 'april':
                astro_sign = 'Aries' if (day < 20) else 'taurus'
            elif month.lower() == 'may':
                astro_sign = 'Taurus' if (day < 21) else 'gemini'
            elif month.lower() == 'june':
                astro_sign = 'Gemini' if (day < 21) else 'cancer'
            elif month.lower() == 'july':
                astro_sign = 'Cancer' if (day < 23) else 'leo'
            elif month.lower() == 'august':
                astro_sign = 'Leo' if (day < 23) else 'virgo'
            elif month.lower() == 'september':
                astro_sign = 'Virgo' if (day < 23) else 'libra'
            elif month.lower() == 'october':
                astro_sign = 'Libra' if (day < 23) else 'scorpio'
            elif month.lower() == 'november':
                astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
    #print("Your Astrological sign is :",astro_sign)    
            else:
                print('ERROR')
    ws.title('YOUR ZODIAC SIGN')
    ws.geometry('100x100')
    messagebox.showinfo(title= None, message='YOU ARE A '+astro_sign.upper()+'!')
    ws.mainloop()

def merch():
    mywin=Toplevel(root)
    mywin.geometry("1450x700")
    bbg = PhotoImage(file = "templates/merch.png")

    label4 = Label( mywin, image = bbg)
    label4.place(x = 0, y = 0)
    mywin.mainloop()
    
def weight():
    mywin=Toplevel(root)
    mywin.geometry("1450x700")
    bbg = PhotoImage(file = "templates/.png")

    label4 = Label( mywin, image = bbg)
    label4.place(x = 0, y = 0)

root = Tk()
root.geometry("1600x1000")
root.state("zoomed")
bg = PhotoImage(file = "templates/bgg.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

#frame = Frame(root, width=600, height=400)
#frame.pack(pady=20)

# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("logo.png"))
# 
# # Create a Label Widget to display the text or Image
# label = Label(frame, image = img)
# label.pack()

click_btn_= PhotoImage(file='templates/logo.png')
button2= Button(root, image=click_btn_,command= merch,borderwidth=0)
button2.pack(pady=20)

label3 = Label( root, text = '''𝗧𝗵𝗲 𝗺𝗮𝗶𝗻 𝗮𝗶𝗺 𝗶𝘀 𝘁𝗼 𝗵𝗮𝗿𝗻𝗲𝘀𝘀 𝗿𝗲𝘀𝗲𝗮𝗿𝗰𝗵 𝗮𝗻𝗱 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗺𝗲𝗻𝘁 𝗶𝗻 𝘁𝗵𝗲 𝗳𝗶𝗲𝗹𝗱 𝗼𝗳 𝗮𝘀𝘁𝗿𝗼𝗻𝗼𝗺𝘆 𝗮𝗻𝗱 𝘀𝗽𝗮𝗰𝗲 
𝘀𝗰𝗶𝗲𝗻𝗰𝗲𝘀. 𝗕𝗟𝗨𝗘 𝗢𝗥𝗜𝗚𝗜𝗡 𝘀𝘁𝘂𝗱𝗶𝗲𝘀 𝗘𝗮𝗿𝘁𝗵, 𝗶𝗻𝗰𝗹𝘂𝗱𝗶𝗻𝗴 𝗶𝘁𝘀 𝗰𝗹𝗶𝗺𝗮𝘁𝗲, 𝗼𝘂𝗿 𝗦𝘂𝗻, 𝗮𝗻𝗱 𝗼𝘂𝗿 𝘀𝗼𝗹𝗮𝗿 𝘀𝘆𝘀𝘁𝗲𝗺 
𝗮𝗻𝗱 𝗯𝗲𝘆𝗼𝗻𝗱. 𝗪𝗲 𝗰𝗼𝗻𝗱𝘂𝗰𝘁 𝗿𝗲𝘀𝗲𝗮𝗿𝗰𝗵, 𝘁𝗲𝘀𝘁𝗶𝗻𝗴, 𝗮𝗻𝗱 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗺𝗲𝗻𝘁 𝘁𝗼 𝗮𝗱𝘃𝗮𝗻𝗰𝗲 𝗮𝗲𝗿𝗼𝗻𝗮𝘂𝘁𝗶𝗰𝘀, 
𝗶𝗻𝗰𝗹𝘂𝗱𝗶𝗻𝗴 𝗲𝗹𝗲𝗰𝘁𝗿𝗶𝗰 𝗽𝗿𝗼𝗽𝘂𝗹𝘀𝗶𝗼𝗻 𝗮𝗻𝗱 𝘀𝘂𝗽𝗲𝗿𝘀𝗼𝗻𝗶𝗰 𝗳𝗹𝗶𝗴𝗵𝘁. 𝗪𝗲 𝗱𝗲𝘃𝗲𝗹𝗼𝗽 𝗮𝗻𝗱 𝗳𝘂𝗻𝗱 𝘀𝗽𝗮𝗰𝗲 𝘁𝗲𝗰𝗵𝗻𝗼𝗹𝗼𝗴𝗶𝗲𝘀 
𝘁𝗵𝗮𝘁 𝘄𝗶𝗹𝗹 𝗲𝗻𝗮𝗯𝗹𝗲 𝗳𝘂𝘁𝘂𝗿𝗲 𝗲𝘅𝗽𝗹𝗼𝗿𝗮𝘁𝗶𝗼𝗻 𝗮𝗻𝗱 𝗯𝗲𝗻𝗲𝗳𝗶𝘁 𝗹𝗶𝗳𝗲 𝗼𝗻 𝗘𝗮𝗿𝘁𝗵.''', font= "Helvetica 14")
label3.pack(pady = 20)

#buttons

myFont = font.Font(family='Helvetica', size=15)

button2 = Button(root, text="𝙈𝘼𝙄𝙉 𝙋𝙇𝘼𝙉𝙀𝙏𝙎",command=planets)
button2['font']=myFont
button2.pack(pady = 2)

button1 = Button(root,text="𝘿𝙒𝘼𝙍𝙁 𝙋𝙇𝘼𝙉𝙀𝙏𝙎",command=dwarf)
button1['font']=myFont
button1.pack(pady=2)

button3 = Button(root, text="𝙈𝙊𝙊𝙉𝙎",command=moon__)
button3['font']=myFont
button3.pack(pady = 2)

button4 = Button(root, text="𝘾𝙊𝙉𝙎𝙏𝙀𝙇𝙇𝘼𝙏𝙄𝙊𝙉𝙎",command=constel)
button4['font']=myFont
button4.pack(pady = 2)

button5 = Button(root, text="𝙋𝙇𝘼𝙉𝙀𝙏𝘼𝙍𝙄𝙐𝙈",command=planetarium)
button5['font']=myFont
button5.pack(pady = 2)

button5 = Button(root, text="ꜰɪɴᴅ ᴏᴜᴛ ʏᴏᴜʀ ᴢᴏᴅɪᴀᴄ ꜱɪɢɴ!",command=zodiac)
button5['font']=myFont
button5.pack(pady = 2)

root.mainloop()

x=(input("DO YOU WANT ACCESS ADMIN SITE:"))
if x.lower() in 'yes':
    pwd=int(input("ENTER PASSWORD:"))
    if pwd==0000:
        cur.execute(f"select * from bookings;")
        res=cur.fetchall()
        print(tabulate.tabulate(res,headers=['Phone No.','Name','Credit Card No.:','Tickets booked'],tablefmt='fancy_grid'))
