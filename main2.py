import customtkinter
import tkinter
import mysql.connector

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()

app.title("Menstruation tracker")
app.geometry("900x700")

#placeholders
user= "lol"
passw="lol"
#sql query to search for login database here

global date, month, frames, username, password, Dframes, toplevel #dates
toplevel = None
frames={}
Dframes={}
username = ""
password = ""
date= ""
month= ""


con=mysql.connector.connect(host= '127.0.0.1' , password= '', user ='root',database='details')

if con.is_connected():
    print('done')


cur=con.cursor()







def login():

    login_user= user_entry.get()
    login_password = passwd.get()


    qu="SELECT (%s) from user where password= (%s);"
    val=(login_user,login_password)

    cur.execute(qu,val)

    rs=cur.fetchall()

    

    if (len(rs)!=0):
        print("logged in")
        frame1.pack_forget()
        frame2.pack(padx=20, pady= 19.5)
        global usr 
        usr=login_user
    else :
        tkinter.messagebox.showerror("Failed..","Invalid login details entered!", icon="error")

def signup():
    frame1.pack_forget()
    frame3.pack(padx=20, pady= 19.5)
    
def Prego_radio():
    pass

def mom_radio():
    pass

def regular_radio():
    pass

def submit_date():
    upd=int(date_update.get())
    upm=int(month_update.get())
    try:
        sql="update user set date=(%s) , month=(%s) where user_name= (%s);"
        val=(upd,upm,usr)
        
        cur.execute(sql,val)
        con.commit()

    except Exception as e:
        print(e)
def submit():


    date = int(e7.get())
    month= int(e71.get())
    username = e1.get()
    password= e2.get()

    try:

        sql = "INSERT INTO user (user_name,password,date,month)  VALUES (%s, %s, %s, %s);"
        val = (username,password,date,month)
        con.commit()
    except Exception as e:
        print("err",e)

    
    cur.execute(sql, val)

    
def back_login():
    frame3.pack_forget()
    frame1.pack(padx=20, pady= 19.5)


def ovul(date,month):
    fert= date +14
    fertile_window= fert
    return fertile_window

def per(date,month):
    blood= date +28
    periods=blood
    return periods

def next_month(masam1):
    global toplevel
    if toplevel is None or not toplevel.winfo_exists():
        toplevel = customtkinter.CTkToplevel(app)
        toplevel.geometry("600x700")
        (frames[masam1]).pack(padx=20, pady= 19.5)


    else:
        toplevel.focus()  # if window exists focus it





"""
##tool tip func
def show_tooltip(event):
    tooltip_label.place(x=event.x_root, y=event.y_root, anchor='nw')

def hide_tooltip(event):
    tooltip_label.place_forget()

root = tk.Tk()

# Create a tooltip label
tooltip_label = tk.Label(root, text="Enter your text here", background="lightyellow", relief="solid", borderwidth=1)
tooltip_label.place_forget()

# Create a text field
text_field = tk.Entry(root)
text_field.pack()

# Bind events to show/hide tooltip
text_field.bind("<Enter>", show_tooltip)
text_field.bind("<Leave>", hide_tooltip)
"""





















def calender_view():
    packed=""


    qu="SELECT date,month from user where user_name=(%s) ;"
    val=(usr,)

    cur.execute(qu,val)

    rs=cur.fetchall()

    date=rs[0][0]
    month = rs[0][1]
    masam = str(month)
    masam1 = str(month+1)


    if (date!=0):

        frame2.pack_forget()
        

        baby=ovul(date,month)
        blud=per(date,month)
        


        (frames[masam]).pack(padx=20, pady= 19.5)
        if masam == '1':
            d1  = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)
            d31 = customtkinter.CTkFrame(master = janf, width = 100, height= 80, corner_radius= 10)

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            d31.grid(row=5, column=3,pady= 1.02, padx=1)

            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day31= customtkinter.CTkLabel(master=d31, text= "31",width=90,height=70, fg_color='transparent', corner_radius = 8)


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day31.place(relx=.5,rely=.5, anchor = tkinter.CENTER) 

            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30
            Dframes['31']= d31


            overblud= blud
            if overblud > 31:
                overblud -=31


            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')
                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red')   
            




        elif masam == "2":
            d1  = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = febf, width = 100, height= 80, corner_radius= 10)
            

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            


            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            
            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29

            overblud= blud
            if overblud > 29:
                overblud-= 29



            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')       
                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red')      

        elif masam == "3":
            d1  = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)
            d31 = customtkinter.CTkFrame(master = marf, width = 100, height= 80, corner_radius= 10)

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            d31.grid(row=5, column=3,pady= 1.02, padx=1)


            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day31= customtkinter.CTkLabel(master=d31, text= "31",width=90,height=70, fg_color='transparent', corner_radius = 8)


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day31.place(relx=.5,rely=.5, anchor = tkinter.CENTER) 

            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30
            Dframes['31']= d31

            overblud= blud
            if overblud > 31:
                overblud -=31



            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')

                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red') 


        elif masam == "4":
            
            d1  = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = aprf, width = 100, height= 80, corner_radius= 10)
            

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            


            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)

            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30


            overblud= blud
            if overblud > 30:
                overblud -= 30



            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')

                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red')              

        elif masam == "5":
            d1  = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)
            d31 = customtkinter.CTkFrame(master = mayf, width = 100, height= 80, corner_radius= 10)

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            d31.grid(row=5, column=3,pady= 1.02, padx=1)


            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day31= customtkinter.CTkLabel(master=d31, text= "31",width=90,height=70, fg_color='transparent', corner_radius = 8)


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day31.place(relx=.5,rely=.5, anchor = tkinter.CENTER) 

            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30
            Dframes['31']= d31

            overblud= blud
            if overblud > 31:
                overblud -=31



            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')
                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red') 

        elif masam == "6":
            d1  = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = junf, width = 100, height= 80, corner_radius= 10)
            

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
           


            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            

            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)


            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30


            overblud= blud
            if overblud > 30:
                overblud -= 30



            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')

                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red') 

        elif masam == "7":
            d1  = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)
            d31 = customtkinter.CTkFrame(master = julf, width = 100, height= 80, corner_radius= 10)

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            d31.grid(row=5, column=3,pady= 1.02, padx=1)


            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day31= customtkinter.CTkLabel(master=d31, text= "31",width=90,height=70, fg_color='transparent', corner_radius = 8)


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day31.place(relx=.5,rely=.5, anchor = tkinter.CENTER) 


            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30
            Dframes['31']= d31

            overblud= blud
            if overblud > 31:
                overblud -=31



            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')
            
                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red') 


        elif masam == "8":
            d1  = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)
            d31 = customtkinter.CTkFrame(master = augf, width = 100, height= 80, corner_radius= 10)

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            d31.grid(row=5, column=3,pady= 1.02, padx=1)


            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day31= customtkinter.CTkLabel(master=d31, text= "31",width=90,height=70, fg_color='transparent', corner_radius = 8)


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day31.place(relx=.5,rely=.5, anchor = tkinter.CENTER) 


            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30
            Dframes['31']= d31

            overblud= blud
            if overblud > 31:
                overblud -=31



            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')

                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red') 



        elif masam == "9":
             
            d1  = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = sepf, width = 100, height= 80, corner_radius= 10)
            
            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            

            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)


            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30


            overblud= blud
            if overblud > 30:
                overblud -= 30



            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')

                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red') 



        elif masam == "10":
            d1  = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)
            d31 = customtkinter.CTkFrame(master = octf, width = 100, height= 80, corner_radius= 10)

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            d31.grid(row=5, column=3,pady= 1.02, padx=1)


            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day31= customtkinter.CTkLabel(master=d31, text= "31",width=90,height=70, fg_color='transparent', corner_radius = 8)


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day31.place(relx=.5,rely=.5, anchor = tkinter.CENTER) 


            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30
            Dframes['31']= d31


            overblud= blud
            if overblud > 31:
                overblud -=31


            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')

                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red') 


        elif masam == "11":
            d1  = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = novf, width = 100, height= 80, corner_radius= 10)
            
            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            

            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            

            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)


            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30
 

            overblud= blud
            if overblud > 30:
                overblud -= 30



            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')

                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red') 

        elif masam == "12":


            d1  = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d2  = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d3  = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d4  = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d5  = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d6  = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d7  = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d8  = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d9  = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d10 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d11 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d12 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d13 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d14 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d15 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d16 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d17 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d18 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d19 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d20 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d21 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d22 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d23 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d24 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d25 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d26 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d27 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d28 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d29 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d30 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)
            d31 = customtkinter.CTkFrame(master = decf, width = 100, height= 80, corner_radius= 10)

            d1.grid(row=1, column=1,pady= 1, padx=1)
            d2.grid(row=1, column=2,pady= 1.01, padx=1)
            d3.grid(row=1, column=3,pady= 1.02, padx=1)
            d4.grid(row=1, column=4,pady= 1.03, padx=1)
            d5.grid(row=1, column=5,pady= 1.04, padx=1)
            d6.grid(row=1, column=6,pady= 1.05, padx=1)
            d7.grid(row=1, column=7,pady= 1.06, padx=1)
            d8.grid(row=2, column=1,pady= 1, padx=1)
            d9.grid(row=2, column=2,pady= 1.01, padx=1)
            d10.grid(row=2, column=3,pady= 1.02, padx=1)
            d11.grid(row=2, column=4,pady= 1.03, padx=1)
            d12.grid(row=2, column=5,pady= 1.04, padx=1)
            d13.grid(row=2, column=6,pady= 1.05, padx=1)
            d14.grid(row=2, column=7,pady= 1.06, padx=1)
            d15.grid(row=3, column=1,pady= 1, padx=1)
            d16.grid(row=3, column=2,pady= 1.01, padx=1)
            d17.grid(row=3, column=3,pady= 1.02, padx=1)
            d18.grid(row=3, column=4,pady= 1.03, padx=1)
            d19.grid(row=3, column=5,pady= 1.04, padx=1)
            d20.grid(row=3, column=6,pady= 1.05, padx=1)
            d21.grid(row=3, column=7,pady= 1.06, padx=1)
            d22.grid(row=4, column=1,pady= 1, padx=1)
            d23.grid(row=4, column=2,pady= 1.01, padx=1)
            d24.grid(row=4, column=3,pady= 1.02, padx=1)
            d25.grid(row=4, column=4,pady= 1.03, padx=1)
            d26.grid(row=4, column=5,pady= 1.04, padx=1)
            d27.grid(row=4, column=6,pady= 1.05, padx=1)
            d28.grid(row=4, column=7,pady= 1.06, padx=1)
            d29.grid(row=5, column=1,pady= 1, padx=1)
            d30.grid(row=5, column=2,pady= 1.01, padx=1)
            d31.grid(row=5, column=3,pady= 1.02, padx=1)


            day1= customtkinter.CTkLabel(master=d1, text= "1",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day2= customtkinter.CTkLabel(master=d2, text= "2",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day3= customtkinter.CTkLabel(master=d3, text= "3",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day4= customtkinter.CTkLabel(master=d4, text= "4",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day5= customtkinter.CTkLabel(master=d5, text= "5",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day6= customtkinter.CTkLabel(master=d6, text= "6",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day7= customtkinter.CTkLabel(master=d7, text= "7",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day8= customtkinter.CTkLabel(master=d8, text= "8",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day9= customtkinter.CTkLabel(master=d9, text= "9",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day10= customtkinter.CTkLabel(master=d10, text= "10",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day11= customtkinter.CTkLabel(master=d11, text= "11",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day12= customtkinter.CTkLabel(master=d12, text= "12",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day13= customtkinter.CTkLabel(master=d13, text= "13",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day14= customtkinter.CTkLabel(master=d14, text= "14",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day15= customtkinter.CTkLabel(master=d15, text= "15",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day16= customtkinter.CTkLabel(master=d16, text= "16",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day17= customtkinter.CTkLabel(master=d17, text= "17",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day18= customtkinter.CTkLabel(master=d18, text= "18",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day19= customtkinter.CTkLabel(master=d19, text= "19",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day20= customtkinter.CTkLabel(master=d20, text= "20",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day21= customtkinter.CTkLabel(master=d21, text= "21",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day22= customtkinter.CTkLabel(master=d22, text= "22",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day23= customtkinter.CTkLabel(master=d23, text= "23",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day24= customtkinter.CTkLabel(master=d24, text= "24",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day25= customtkinter.CTkLabel(master=d25, text= "25",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day26= customtkinter.CTkLabel(master=d26, text= "26",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day27= customtkinter.CTkLabel(master=d27, text= "27",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day28= customtkinter.CTkLabel(master=d28, text= "28",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day29= customtkinter.CTkLabel(master=d29, text= "29",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day30= customtkinter.CTkLabel(master=d30, text= "30",width=90,height=70, fg_color='transparent', corner_radius = 8)
            day31= customtkinter.CTkLabel(master=d31, text= "31",width=90,height=70, fg_color='transparent', corner_radius = 8)


            day1.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day2.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day3.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day4.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day5.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day6.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day7.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day8.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day9.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day10.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day11.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day12.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day13.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day14.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day15.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day16.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day17.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day18.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day19.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day20.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day21.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day22.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day23.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day24.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day25.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day26.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day27.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day28.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day29.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day30.place(relx=.5,rely=.5, anchor = tkinter.CENTER)
            day31.place(relx=.5,rely=.5, anchor = tkinter.CENTER) 

            Dframes['1']= d1
            Dframes['2']= d2
            Dframes['3']= d3
            Dframes['4']= d4
            Dframes['5']= d5
            Dframes['6']= d6
            Dframes['7']= d7
            Dframes['8']= d8
            Dframes['9']= d9
            Dframes['10']= d10
            Dframes['11']= d11
            Dframes['12']= d12
            Dframes['13']= d13
            Dframes['14']= d14
            Dframes['15']= d15
            Dframes['16']= d16
            Dframes['17']= d17
            Dframes['18']= d18
            Dframes['19']= d19
            Dframes['20']= d20
            Dframes['21']= d21
            Dframes['22']= d22
            Dframes['23']= d23
            Dframes['24']= d24
            Dframes['25']= d25
            Dframes['26']= d26
            Dframes['27']= d27
            Dframes['28']= d28
            Dframes['29']= d29
            Dframes['30']= d30
            Dframes['31']= d31

            overblud= blud
            if overblud > 31:
                overblud -=31

            for i in range(1,31):
                if baby == i:
                    (Dframes[str(i)]).configure(fg_color='green')

                if blud == i:
                    (Dframes[str(i)]).configure(fg_color='red') 

        else:
            print("error")
        



        stat = customtkinter.CTkFrame(master = app, width = 600, height= 200, corner_radius= 10)
        stat.pack(padx=20, pady=30)
        Dinfo= customtkinter.CTkLabel(master=stat, text= "The next period date is displayed in red. If not then date is in next month",width=200,height=70, fg_color='transparent', corner_radius = 8)
        Dinfo1= customtkinter.CTkLabel(master=stat, text= "Period date:" ,width=90,height=70, fg_color='transparent', corner_radius = 8)
        Ddate = customtkinter.CTkLabel(master=stat, text= overblud ,width=90,height=70, fg_color='transparent', corner_radius = 8)
        Dinfo2= customtkinter.CTkLabel(master=stat, text= "The next ovulation is displayed in green. If not then date is in next month",width=200,height=70, fg_color='transparent', corner_radius = 8)
        Dinfo3= customtkinter.CTkLabel(master=stat, text= "Ovulation date:",width=90,height=70, fg_color='transparent', corner_radius = 8)
        Dovul = customtkinter.CTkLabel(master=stat, text= baby ,width=90,height=70, fg_color='transparent', corner_radius = 8)
        Dinfo.place(relx=0.5,rely=0.1, anchor= tkinter.CENTER)
        Dinfo1.place(relx=0.5,rely=0.35, anchor= tkinter.CENTER)
        Dinfo2.place(relx=0.5,rely=0.6, anchor= tkinter.CENTER)
        Dinfo3.place(relx=0.5,rely=0.85, anchor= tkinter.CENTER)
        Ddate.place(relx=0.8,rely=0.35, anchor= tkinter.CENTER)
        Dovul.place(relx=0.8,rely=0.85, anchor= tkinter.CENTER)







#############################################################################################################################################






#login frame

frame1 = customtkinter.CTkFrame(master= app, width= 500, height = 500, corner_radius = 10)

frame1.pack(padx=20, pady= 19.5)
font_title= customtkinter.CTkFont(family="title", size = 24)
font_title2 = customtkinter.CTkFont(family="title",size= 14)
Title= customtkinter.CTkLabel(master=frame1, text="Menstruation Tracker", width= 120, height = 25, fg_color= "transparent", font= font_title )
Title.place(relx=0.5, rely=0.25, anchor = tkinter.CENTER)

font_title.configure(family="new name")


user_entry= customtkinter.CTkEntry(master = frame1,
                            placeholder_text="User Id",
                            width=200,
                            height=35,
                            border_width=3,
                            corner_radius=10)

user_entry.place(relx=0.5, rely=0.4, anchor = tkinter.CENTER)

passwd= customtkinter.CTkEntry(master = frame1,
                            placeholder_text="Password",
                            width=200,
                            height=35,
                            show="*",
                            border_width=3,
                            corner_radius=10)

passwd.place(relx=0.5, rely=0.5 , anchor=tkinter.CENTER)

loginB= customtkinter.CTkButton(master=frame1, text="Login", command= login)
loginB.place(relx=0.5,rely=0.65, anchor= tkinter.CENTER)

signupB= customtkinter.CTkButton(master=frame1, text="Signup", command= signup)
signupB.place(relx=0.5,rely=0.725, anchor= tkinter.CENTER)



### Calender home 

#Usr= <extract username from sql>


frame2= customtkinter.CTkFrame(master= app, width= 850, height = 650, corner_radius= 15)


T1= customtkinter.CTkLabel(master= frame2, text="Welcome Back {}".format(username)  #replace with string containing username later,
                       , width= 120, height= 25, fg_color='transparent', corner_radius = 8, font= font_title)

T2= customtkinter.CTkLabel(master= frame2, text="Has your last period changed? \n If yes,Please enter the new date below! ", width= 200, height= 50, fg_color='transparent', corner_radius = 8,font = font_title2)

T3= customtkinter.CTkLabel(master= frame2, text="If not then Click on the button to calculate! ", width= 200, height= 50, fg_color='transparent', corner_radius = 8)


Update_LD= customtkinter.CTkLabel(master= frame2, text="Last period date:", width= 120, height= 25, fg_color='transparent', corner_radius = 8, font = font_title2)

date_update= customtkinter.CTkEntry(master = frame2,
                            placeholder_text="New date ",
                            width=100,
                            height=35,
                            border_width=3,
                            corner_radius=10)


month_update= customtkinter.CTkEntry(master = frame2,
                            placeholder_text="New month ",
                            width=100,
                            height=35,
                            border_width=3,
                            corner_radius=10)



T1.place(relx=0.5, rely=0.3, anchor = tkinter.CENTER)
T2.place(relx=0.5, rely=0.45, anchor = tkinter.CENTER)
T3.place(relx=0.5, rely=0.7, anchor = tkinter.CENTER)
Update_LD.place(relx=0.4, rely=0.55, anchor = tkinter.CENTER)
date_update.place(relx=0.555, rely=0.55, anchor = tkinter.CENTER)
month_update.place(relx=0.675, rely=0.55, anchor = tkinter.CENTER)

submitB= customtkinter.CTkButton(master=frame2, text="Submit", command= submit_date)
submitB.place(relx=0.5,rely=0.63, anchor= tkinter.CENTER)




loginB= customtkinter.CTkButton(master=frame2, text="Calculate!", command= calender_view)
loginB.place(relx=0.5,rely=0.75, anchor= tkinter.CENTER)










### signup frame

frame3= customtkinter.CTkFrame(master = app, width = 850, height= 750, corner_radius= 15)

#singup page

Cname= customtkinter.CTkLabel(master= frame3, text="Name:", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)
Cpass= customtkinter.CTkLabel(master= frame3, text="Password:", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)
Cconf= customtkinter.CTkLabel(master= frame3, text="Confirm Password:", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)


###


Cage= customtkinter.CTkLabel(master= frame3, text="Age:", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)
Cprego= customtkinter.CTkLabel(master= frame3, text="Currently Carrying?", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)
Cmom= customtkinter.CTkLabel(master= frame3, text="Mother?", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)

###

Clastdate= customtkinter.CTkLabel(master= frame3, text="Last period date and month :", width= 60, height= 25, fg_color='#5c5d5e', corner_radius = 8)

Cheight= customtkinter.CTkLabel(master= frame3, text="Height:", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)
Cweight= customtkinter.CTkLabel(master= frame3, text="Weight:", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)

####

Cregular= customtkinter.CTkLabel(master= frame3, text="Are your periods regular?", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)


#if not regular

Cdoctor= customtkinter.CTkLabel(master= frame3, text="Consulted doctor?", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)
Chealth= customtkinter.CTkLabel(master= frame3, text="Health issues(if any):", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)
Cmedicine= customtkinter.CTkLabel(master= frame3, text="Medications(if any):", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)
Ctype= customtkinter.CTkLabel(master= frame3, text="Type of medication:", width= 120, height= 25, fg_color='#5c5d5e', corner_radius = 8)

#submit

Cbcklogin= customtkinter.CTkButton(master=frame3, text="back to login" , command= back_login )
Cbcklogin.place(relx=0.8,rely=0.955, anchor= tkinter.CENTER)

Csubmit= customtkinter.CTkButton(master=frame3, text="Submit" , command= submit  )
Csubmit.place(relx=0.8,rely=0.855, anchor= tkinter.CENTER)


#placing

Cname.grid(row=1, column=1, pady=17, padx=(10, 700))
Cpass.grid(row=2, column=1, pady =17, padx=(10, 700))
Cconf.grid(row=3, column=1, pady =17, padx=(10, 700))
Cage.grid(row=4, column=1, pady =17, padx=(10, 700))
Cprego.grid(row=5, column=1, pady =17, padx=(10, 700))
Cmom.grid(row=6, column=1, pady =17, padx=(10, 700))
Clastdate.grid(row=7, column=1, pady =17, padx=(10, 700))
Cheight.grid(row=8, column=1, pady =17, padx=(10, 700))
Cweight.grid(row=9, column=1, pady =17, padx=(10, 700))
Cregular.grid(row=10, column=1, pady =17, padx=(10, 700))


#entries

e1= customtkinter.CTkEntry(master = frame3,
                            placeholder_text="ID",
                            width=200,
                            height=35,
                            border_width=3,
                            corner_radius=10)

e2= customtkinter.CTkEntry(master = frame3,
                            placeholder_text="Password",
                            width=200,
                            height=35,
                            show="*",
                            border_width=3,
                            corner_radius=10)
                        
e3= customtkinter.CTkEntry(master = frame3,
                            placeholder_text="Confirm password",
                            width=200,
                            height=35,
                            show="*",
                            border_width=3,
                            corner_radius=10)

                        
e4= customtkinter.CTkEntry(master = frame3,

                            width=200,
                            height=35,

                            border_width=3,
                            corner_radius=10)

e5= customtkinter.CTkEntry(master = frame3,

                            width=200,
                            height=35,

                            border_width=3,
                            corner_radius=10)

e6= customtkinter.CTkEntry(master = frame3,

                            width=200,
                            height=35,

                            border_width=3,
                            corner_radius=10)

e7= customtkinter.CTkEntry(master = frame3,

                            width=70,
                            height=35,

                            border_width=3,
                            corner_radius=10)

e71= customtkinter.CTkEntry(master = frame3,

                            width=70,
                            height=35,

                            border_width=3,
                            corner_radius=10)


e8= customtkinter.CTkEntry(master = frame3,

                            width=200,
                            height=35,

                            border_width=3,
                            corner_radius=10)

e9= customtkinter.CTkEntry(master = frame3,

                            width=200,
                            height=35,

                            border_width=3,
                            corner_radius=10)

e10= customtkinter.CTkEntry(master = frame3,

                            width=200,
                            height=35,

                            border_width=3,
                            corner_radius=10)




e1.place(relx=0.5,rely=0.055, anchor= tkinter.CENTER)
e2.place(relx=0.5,rely=0.155, anchor= tkinter.CENTER)
e3.place(relx=0.5,rely=0.255, anchor= tkinter.CENTER)
e4.place(relx=0.5,rely=0.355, anchor= tkinter.CENTER)

e7.place(relx=0.45,rely=0.655, anchor= tkinter.CENTER)
e71.place(relx=0.55,rely=0.655, anchor= tkinter.CENTER)
e8.place(relx=0.5,rely=0.755, anchor= tkinter.CENTER)
e9.place(relx=0.5,rely=0.855, anchor= tkinter.CENTER)
#e10.place(relx=0.5,rely=0.955, anchor= tkinter.CENTER)


#radio button
prego_var= tkinter.StringVar(value="")
mom_var= tkinter.StringVar(value="")
regular_var= tkinter.StringVar(value="")

pregoB_y= customtkinter.CTkRadioButton(master= frame3, text="Yes" , command= Prego_radio, variable= prego_var, value="y" )
pregoB_n= customtkinter.CTkRadioButton(master= frame3, text="No" , command= Prego_radio, variable= prego_var, value="n" )

pregoB_y.place(relx=0.5,rely=0.455, anchor= tkinter.CENTER)
pregoB_n.place(relx=0.6,rely=0.455, anchor= tkinter.CENTER)


momB_y= customtkinter.CTkRadioButton(master= frame3, text="Yes" , command= mom_radio, variable= mom_var, value="y" )
momB_n= customtkinter.CTkRadioButton(master= frame3, text="No" , command= mom_radio, variable= mom_var, value="n" )

momB_y.place(relx=0.5,rely=0.555, anchor= tkinter.CENTER)
momB_n.place(relx=0.6,rely=0.555, anchor= tkinter.CENTER)


regularB_y= customtkinter.CTkRadioButton(master= frame3, text="Yes" , command= regular_radio, variable= regular_var, value="y" )
regularB_n= customtkinter.CTkRadioButton(master= frame3, text="No" , command= regular_radio, variable= regular_var, value="n" )

regularB_y.place(relx=0.5,rely=0.955, anchor= tkinter.CENTER)
regularB_n.place(relx=0.6,rely=0.955, anchor= tkinter.CENTER)


janf = customtkinter.CTkFrame( master = app, width =  850, height=  650, corner_radius= 15)
febf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15)
marf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15) 
aprf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15) 
mayf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15) 
junf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15) 
julf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15) 
augf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15)
sepf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15)
octf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15)
novf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15)
decf = customtkinter.CTkFrame(master = app, width =  850, height=  650, corner_radius= 15)

frames["1"]= janf 
frames["2"]= febf
frames["3"]= marf
frames["4"]= aprf
frames["5"]= mayf
frames["6"]= junf
frames["7"]= julf
frames["8"]= augf
frames["9"]= sepf
frames["10"]= octf
frames["11"]= novf
frames["12"]= decf



















####################################################################################################################################
app.mainloop()




con.close()