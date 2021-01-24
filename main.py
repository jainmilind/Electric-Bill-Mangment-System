import tkinter as tk
import csv

perunitcost=6.5

def create_account(l):
    with open('user_file.csv','a',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(l)
    l1=[l[0]]+(["_"]*12)
    with open('user_units_2019.csv','a',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(l1)
    with open('user_units_2020.csv','a',newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(l1)

def check_account(e1,e2):
        uid = str(e1.get())
        upass = str(e2.get())
        with open("user_file.csv",'r') as f:
            re=csv.reader(f)
            l=[i for i in re]
            for i in l:
                if len(i)>0 and (i[0] == uid and i[2] == upass):
                    return True
            return False

def check_admin(e1,e2):
    try:
        a = str(e1.get())
        b = str(e2.get())
        with open("adminfile.csv", 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                d = dict(row)
                if d["admin_id"] == a and d["admin_pass"] == b:
                    return True
        return False

    except:
        root2 = tk.Tk()
        root2.title("Invalid input")
        root2.geometry("+300+300")
        tk.Label(root2, text="YOUR INPUT WAS INVALID", fg='red', font=(None, 25, 'bold')).grid(row=0, column=0)
        return False

def main():
    def user():
        root2 = tk.Toplevel()
        root2.title("ELECTRIC BILL MANAGMENT SYSTEM(user)")
        root2.geometry('+500+300')
        img = tk.PhotoImage(file=r'user.png')
        tk.Label(root2 , image=img).grid(row=3, column=2)
        tk.Label(root2, text="Select One ", fg='green', font=(None, 20, 'bold')).grid(row=0, column=2)
        tk.Button(root2, text="Login", fg="blue", font=(None, 15, 'bold'), bd=5, command=userlogin).grid(row=4, column=1)
        tk.Button(root2, text="Sign Up", fg="blue", font=(None, 15, 'bold'), bd=5, command=usernew).grid(row=4, column=3)
        tk.Button(root2, text="QUIT", fg="red", font=(None, 15, 'bold'), bd=5, command=root2.destroy).grid(row=4, column=2)
        root2.mainloop()

    def usernew():
        root3 = tk.Toplevel()
        root3.geometry('+500+300')
        root3.title("ELECTRIC BILL MANAGMENT SYSTEM(usersignup)")
        tk.Label(root3, text="Sign-up", fg='red', font=("castellar", 20, 'bold')).grid(row=0, column=1)
        tk.Label(root3, text="Enter Userid ->", font=(None, 15, 'bold')).grid(row=1, column=0)
        tk.Label(root3, text="Enter Username ->", font=(None, 15, 'bold')).grid(row=2, column=0)
        tk.Label(root3, text="Enter Password ->", font=(None, 15, 'bold')).grid(row=3, column=0)
        tk.Label(root3, text="Enter ContactNo. ->", font=(None, 15, 'bold')).grid(row=4, column=0)
        tk.Label(root3, text="Enter City ->", font=(None, 15, 'bold')).grid(row=5, column=0)
        tk.Label(root3, text="Enter Address ->", font=(None, 15, 'bold')).grid(row=6, column=0)

        e1 = tk.Entry(root3, width=30, insertwidth=4, bd=7)
        e1.grid(row=1, column=1)
        e2 = tk.Entry(root3, width=30, insertwidth=4, bd=7)
        e2.grid(row=2, column=1)
        e3 = tk.Entry(root3, width=30, insertwidth=4, bd=7, show="*")
        e3.grid(row=3, column=1)
        e4 = tk.Entry(root3, width=30, insertwidth=4, bd=7)
        e4.grid(row=4, column=1)
        e5 = tk.Entry(root3, width=30, insertwidth=4, bd=7)
        e5.grid(row=5, column=1)
        e6 = tk.Entry(root3, width=30, insertwidth=4, bd=7)
        e6.grid(row=6, column=1)

        def new1():
            try:
                uid = int(e1.get())
                uname = str(e2.get())
                upass = str(e3.get())
                ucont = str(e4.get())
                ucity = str(e5.get())
                uadd = str(e6.get())
                user_list = [uid, uname, upass, ucont, ucity, uadd]
                create_account(user_list)
                tk.Label(root3, text="Account was Successfully created", font=(None, 8, 'bold')).grid(row=9, column=1)
            except:
                tk.Label(root3, text="Please enter all the data correctly", font=(None, 8, 'bold')).grid(row=9, column=1)
        tk.Button(root3, text="Submit", fg="blue", font=(None, 15, 'bold'), bd=5, command=new1).grid(row=7, column=2)
        tk.Button(root3, text="EXIT", fg="blue", font=(None, 15, 'bold'), bd=5, command=root3.destroy).grid(row=7, column=0)

    def userlogin():
        root4 = tk.Toplevel()
        root4.geometry('+500+300')
        root4.title("ELECTRIC BILL MANAGMENT SYSTEM(userlogin)")
        tk.Label(root4, text="Login", fg='red', font=("castellar", 20, 'bold')).grid(row=0, column=1)
        tk.Label(root4, text="Enter userid ->", font=(None, 15, 'bold')).grid(row=1, column=0)
        tk.Label(root4, text="Enter password ->", font=(None, 15, 'bold')).grid(row=2, column=0)

        e1 = tk.Entry(root4, width=30, insertwidth=4, bd=7)
        e1.grid(row=1, column=1)
        e2 = tk.Entry(root4, width=30, show="*", insertwidth=4, bd=7)
        e2.grid(row=2, column=1)
        def data():
            if (check_account(e1,e2)):
                root5 = tk.Tk()
                root5.geometry("800x200+0+0")
                root5.title("ELECTRIC BILL MANAGMENT SYSTEM(billgenerator)")
                tk.Label(root5, text="Enter the month and year of which you need data", fg='red',
                                 font=("castellar", 12, 'bold')).grid(row=0, column=1)
                tk.Label(root5, text="Enter Month ->", font=("castellar", 15, 'bold')).grid(row=1, column=0)
                tk.Label(root5, text="Enter Year ->", font=("castellar", 15, 'bold')).grid(row=2, column=0)
                #dropdown bar stuff
                l1 = ["January", "February", "March","April", "May", "June", "July", "August", "September", "October", "November", "December"]
                e1c = tk.StringVar(root5)
                e1c.set(l1[0])
                drop1 = tk.OptionMenu(root5, e1c, *l1)
                drop1.config(width=24)
                drop1.grid(row=1, column=1)

                l2 = [ '2019','2020']
                e2c = tk.StringVar(root5)
                e2c.set(l2[0])
                drop2 = tk.OptionMenu(root5, e2c, *l2)
                drop2.config(width=24)
                drop2.grid(row=2, column=1)

                def calculate1():
                    uid = str(e1.get())
                    umont = str(e1c.get())
                    uyear = int(e2c.get())
                    data2=[]
                    with open("user_file.csv",'r') as f:
                        re=csv.reader(f)
                        l=[i for i in re]
                        for i in l:
                            if len(i)>0 and i[0] == uid:
                                data2=i
                                break
                    if (len(data2) == 0):
                        tk.Label(root5, text='Data not avaliable').grid(row=8, column=1)
                    else:
                        try:
                            with open("user_file.csv", 'r') as f:
                                re = csv.reader(f)
                                l = [i for i in re]
                                for i in l:
                                    if i[0] == uid:
                                        a1=i[0]
                                        a2=i[1]
                                        a4=i[3]
                                        a5=i[4]
                                        a6=i[5]
                            root11 = tk.Tk()
                            root11.geometry('+0+0')
                            root11.title("ELECTRIC BILL MANAGMENT SYSTEM(bill)")
                            tk.Label(root11, text="INVOICE", font=("castellar", 20, 'bold')).grid(row=0, column=3)

                            tk.Label(root11, text="Customer details:", font=("castellar", 15, 'bold')).grid(row=2,
                                                                                                            column=0)
                            tk.Label(root11, text="Customer id ->", font=("castellar", 15, 'bold')).grid(row=3,
                                                                                                         column=0)
                            tk.Label(root11, text="Customer Name ->", font=("castellar", 15, 'bold')).grid(row=4,
                                                                                                           column=0)
                            tk.Label(root11, text="Customer contact no. ->", font=("castellar", 15, 'bold')).grid(row=5,
                                                                                                                  column=0)
                            tk.Label(root11, text="Customer city ->", font=("castellar", 15, 'bold')).grid(row=6,
                                                                                                           column=0)
                            tk.Label(root11, text="Customer address ->", font=("castellar", 15, 'bold')).grid(row=7,
                                                                                                              column=0)
                            tk.Label(root11, text=a1, font=(None, 12)).grid(row=3, column=1)
                            tk.Label(root11, text=a2, font=(None, 12)).grid(row=4, column=1)
                            tk.Label(root11, text=a4, font=(None, 12)).grid(row=5, column=1)
                            tk.Label(root11, text=a5, font=(None, 12)).grid(row=6, column=1)
                            tk.Label(root11, text=a6, font=(None, 12)).grid(row=7, column=1)

                            if uyear == 2020:
                                with open("user_units_2020.csv", 'r') as file:
                                    csv_file = csv.DictReader(file)
                                    for row in csv_file:
                                        d=dict(row)
                                        if d["User_id"] == uid:
                                            b4 = d[umont]
                                            b5 = float(b4) * perunitcost
                                b2 = umont
                                b3 = uyear
                            if uyear == 2019:
                                with open("user_units_2019.csv", 'r') as file:
                                    csv_file = csv.DictReader(file)
                                    for row in csv_file:
                                        d=dict(row)
                                        if d["User_id"] == uid:
                                            b4 = d[umont]
                                            b5 = float(b4) * perunitcost
                                b2 = umont
                                b3 = uyear

                            tk.Label(root11, text="   Month  ", font=("castellar", 15, 'bold')).grid(row=2, column=2)
                            tk.Label(root11, text="   Year   ", font=("castellar", 15, 'bold')).grid(row=2, column=3)
                            tk.Label(root11, text="    Units consumed   ", font=("castellar", 15, 'bold')).grid(row=2,
                                                                                                                column=4)
                            tk.Label(root11, text="    Amount to be paid   ", font=("castellar", 15, 'bold')).grid(
                                row=2, column=5)

                            tk.Label(root11, text = b2, font=(None, 12)).grid(row=4, column=2)
                            tk.Label(root11, text = b3, font=(None, 12)).grid(row=4, column=3)
                            tk.Label(root11, text = b4, font=(None, 12)).grid(row=4, column=4)
                            tk.Label(root11, text = b5, font=(None, 12)).grid(row=4, column=5)

                            tk.Label(root11, text="--------------------------------------------------").grid(row=1,
                                                                                                             column=0)
                            tk.Label(root11, text="------------------------").grid(row=1, column=1)
                            tk.Label(root11, text="------------------------").grid(row=1, column=2)
                            tk.Label(root11, text="------------------------").grid(row=1, column=3)
                            tk.Label(root11, text="-----------------------------------------").grid(row=1, column=4)
                            tk.Label(root11, text="-----------------------------------------").grid(row=1, column=5)

                            tk.Label(root11, text="-------------------------").grid(row=5, column=2)
                            tk.Label(root11, text="-------------------------").grid(row=5, column=3)
                            tk.Label(root11, text="------------------------------------------").grid(row=5, column=4)
                            tk.Label(root11, text="------------------------------------------").grid(row=5, column=5)

                            tk.Label(root11, text="-------------------------").grid(row=3, column=2)
                            tk.Label(root11, text="-------------------------").grid(row=3, column=3)
                            tk.Label(root11, text="------------------------------------------").grid(row=3, column=4)
                            tk.Label(root11, text="------------------------------------------").grid(row=3, column=5)

                            tk.Button(root11, text="EXIT", fg="red", font=(None, 15, 'bold'), bd=5,
                                      command=root11.destroy).grid(row=9, column=6)
                            root11.mainloop()
                        except:
                            root21 = tk.Tk()
                            root21.geometry("+300+300")
                            root21.title("ERROR")
                            tk.Label(root21, text="Data not found",fg='red', font=("castellar", 15, 'bold')).grid(row=0,
                                                                                                            column=0)
                            root21.mainloop()

                tk.Button(root5, text="Log out", fg="red", font=(None, 15, 'bold'), bd=5, command=root5.destroy).grid(row=10, column=1)
                tk.Button(root5, text="Generate bill ", fg="blue", font=(None, 15, 'bold'), bd=5,
                               command=calculate1).grid(row=7, column=1)
                root5.mainloop()

            else:
                tk.Label(root4, text="Please enter correct username and password", font=(None, 8, 'bold')).grid(row=5, column=0)
        img = tk.PhotoImage(file=r'userlogin.png')
        tk.Label(root4 , image=img ).grid(row=3,column=0)
        tk.Button(root4, text="Submit", fg="blue", font=(None, 15, 'bold'), bd=5, command=data).grid(row=3, column=1)
        tk.Button(root4, text="QUIT", fg="red", font=(None, 12, 'bold'), bd=5, command=root4.destroy).grid(row=4, column=1)
        root4.mainloop()

    def admin():
        root6 = tk.Toplevel()
        root6.geometry('+500+300')
        root6.title("ELECTRIC BILL MANAGMENT SYSTEM(admin login)")

        tk.Label(root6, text="Login", fg='red', font=("castellar", 20, 'bold')).grid(row=0, column=1)
        tk.Label(root6, text="Enter id ->", font=(None, 15, 'bold')).grid(row=2, column=0)
        tk.Label(root6, text="Enter Password ->", font=(None, 15, 'bold')).grid(row=3, column=0)

        e1 = tk.Entry(root6, width=30, insertwidth=4, bd=7)
        e1.grid(row=2, column=1)
        e2 = tk.Entry(root6, width=30, insertwidth=4, show="*", bd=7)
        e2.grid(row=3, column=1)

        def datad():
            if (check_admin(e1,e2)):
                root7 = tk.Toplevel()
                root7.geometry('+500+300')
                root7.title("ELECTRIC BILL MANAGMENT SYSTEM(admin)")
                tk.Label(root7, text="Welcome", fg='red', font=("castellar", 20, 'bold')).grid(row=0, column=1)
                tk.Label(root7, text="Please select anyone of following", fg='red',
                                 font=("castellar", 20, 'bold')).grid(row=2, column=1)

                def updata():

                    root8 = tk.Tk()
                    root8.geometry('+500+300')
                    root8.title("ELECTRIC BILL MANAGMENT SYSTEM(admin user data update")
                    tk.Label(root8, text="Enter userid (whose data will update) ->", font=(None, 15, 'bold')).grid(row=1, column=0)
                    tk.Label(root8, text="Enter New user name ->", font=(None, 15, 'bold')).grid(row=2, column=0)
                    tk.Label(root8, text="Enter New password ->", font=(None, 15, 'bold')).grid(row=3, column=0)
                    tk.Label(root8, text="Enter New Contact No ->", font=(None, 15, 'bold')).grid(row=4, column=0)
                    tk.Label(root8, text="Enter New City ->", font=(None, 15, 'bold')).grid(row=5, column=0)
                    tk.Label(root8, text="Enter New address ->", font=(None, 15, 'bold')).grid(row=6, column=0)

                    e1 = tk.Entry(root8, width=30, insertwidth=4, bd=7)
                    e1.grid(row=1, column=1)
                    e2 = tk.Entry(root8, width=30, insertwidth=4, bd=7)
                    e2.grid(row=2, column=1)
                    e3 = tk.Entry(root8, width=30, show="*", insertwidth=4, bd=7)
                    e3.grid(row=3, column=1)
                    e4 = tk.Entry(root8, width=30, insertwidth=4, bd=7)
                    e4.grid(row=4, column=1)
                    e5 = tk.Entry(root8, width=30, insertwidth=4, bd=7)
                    e5.grid(row=5, column=1)
                    e6 = tk.Entry(root8, width=30, insertwidth=4, bd=7)
                    e6.grid(row=6, column=1)

                    def updatedata():
                        try:
                            nuid = str(e1.get())
                            nuname = str(e2.get())
                            nupass = str(e3.get())
                            nucont = str(e4.get())
                            nucity = str(e5.get())
                            nuadd = str(e6.get())
                        except:
                            root42=tk.Tk()
                            root42.geometry("+300+300")
                            root42.title("Please Enter properly")
                            tk.Label(root42 , text="PLEASE ENTER ALL VALUES PROPERLY" , fg='red' ,font=(None, 25, 'bold')).grid(row=3, column=0)
                        def check3():
                            with open("user_file.csv", 'r') as file:
                                csv_file = csv.DictReader(file)
                                for row in csv_file:
                                    d = dict(row)
                                    if d['User_id'] == nuid:
                                        return True
                                return False

                        if (check3()):
                            lines = []
                            with open("user_file.csv", 'r') as file:
                                csv_file = csv.DictReader(file)
                                d1 = []
                                l1 = {}
                                for row in csv_file:
                                    d = dict(row)
                                    if d["User_id"] == nuid:
                                        l1 = d
                                    else:
                                        d1.append(d)
                                with open('user_file.csv', 'w', newline='\n') as file:
                                    fieldnames = ['User_id','User_Name','User_passwd','User_contact','User_city','User_address']
                                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                                    writer.writeheader()
                                    for i in d1:
                                        writer.writerow(i)
                                    l1["User_Name"] = nuname
                                    l1["User_passwd"] = nupass
                                    l1["User_contact"] = nucont
                                    l1["User_city"] = nucity
                                    l1["User_address"] = nuadd
                                    writer.writerow(l1)

                            tk.Label(root8, text="Successfully updated", font=(None, 8, 'bold')).grid(row=9, column=1)
                        else:
                            tk.Label(root8, text="Please enter correct userid", font=(None, 8, 'bold')).grid(row=11, column=1)

                    tk.Button(root8, text="Update", fg="blue", font=(None, 12, 'bold'), bd=5, command=updatedata).grid(row=8, column=1)
                    tk.Button(root8, text="QUIT", fg="red", font=(None, 12, 'bold'), bd=5, command=root8.destroy).grid(row=10, column=1)

                def consuni():
                    root9 = tk.Tk()
                    root9.geometry('+500+300')
                    root9.title("ELECTRIC BILL MANAGMENT SYSTEM(admin units consumed)")

                    tk.Label(root9, text="Enter userid ->", font=(None, 15, 'bold')).grid(row=1, column=0)
                    tk.Label(root9, text="Enter Month ->", font=(None, 15, 'bold')).grid(row=2, column=0)
                    tk.Label(root9, text="Enter Year ->", font=(None, 15, 'bold')).grid(row=3, column=0)
                    tk.Label(root9, text="Enter units consumed ->", font=(None, 15, 'bold')).grid(row=4, column=0)

                    e1 = tk.Entry(root9, width=30, insertwidth=4, bd=7)
                    e1.grid(row=1, column=1)
                    l1 = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]
                    e2 = tk.StringVar(root9)
                    e2.set(l1[0])
                    drop1 = tk.OptionMenu(root9, e2, *l1)
                    drop1.config(width=24)
                    drop1.grid(row=2, column=1)

                    l2 = ['2019','2020']
                    e3 = tk.StringVar(root9)

                    e3.set(l2[0])
                    drop2 = tk.OptionMenu(root9, e3, *l2)
                    drop2.config(width=24)
                    drop2.grid(row=3, column=1)
                    e4 = tk.Entry(root9, width=30, insertwidth=4, bd=7)
                    e4.grid(row=4, column=1)
                    def check27(e1) :
                        with open("user_file.csv",'r') as f:
                            r = csv.reader(f)
                            l=[i for i in r]
                            for i in l:
                                if len(i)>0 and i[0] == str(e1.get()):
                                    return True
                            return False

                    def consumunitsinput():
                        if (check27(e1)):
                            uid = str(e1.get())
                            umon = str(e2.get())
                            uyr = int(e3.get())
                            nun = float(e4.get())
                            if uyr == 2020:
                                with open("user_units_2020.csv", 'r') as file:
                                    csv_file = csv.DictReader(file)
                                    d1=[]
                                    l1={}
                                    for row in csv_file:
                                        d = dict(row)
                                        if d["User_id"] == uid :
                                            l1 = d
                                        else:
                                            d1.append(d)
                                    with open('user_units_2020.csv', 'w', newline='\n') as file:
                                        fieldnames = ["User_id","January", "February", "March","April", "May", "June", "July", "August", "September", "October", "November", "December"]
                                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                                        writer.writeheader()
                                        for i in d1:
                                            writer.writerow(i)
                                        l1[umon] = nun
                                        writer.writerow(l1)
                            if uyr == 2019 :
                                with open("user_units_2019.csv", 'r') as file:
                                    csv_file = csv.DictReader(file)
                                    d1 = []
                                    for row in csv_file:
                                        d = dict(row)
                                        if d["User_id"] == uid:
                                            l1 = d
                                        else:
                                            d1.append(d)
                                    with open('user_units_2019.csv', 'w', newline='\n') as file:
                                        fieldnames = ["User_id", "January", "February", "March", "April", "May",
                                                          "June", "July", "August", "September", "October", "November",
                                                          "December"]
                                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                                        writer.writeheader()
                                        for i in d1:
                                            writer.writerow(i)
                                        l1[umon] = nun
                                        writer.writerow(l1)
                        else:
                            root42 = tk.Tk()
                            root42.geometry("+300+300")
                            root42.title("Please Enter properly")
                            tk.Label(root42, text="User id doesnot exist", fg='red',
                                     font=(None, 25, 'bold')).grid(row=3, column=0)

                        tk.Label(root9, text="Successfully Entered", font=(None, 8, 'bold')).grid(row=9, column=1)

                    tk.Button(root9, text="Submit", fg="blue", font=(None, 12, 'bold'), bd=5,
                              command=consumunitsinput).grid(row=8, column=1)
                    tk.Button(root9, text="QUIT", fg="red", font=(None, 12, 'bold'), bd=5, command=root9.destroy).grid(row=10, column=1)

                def dele():
                    root10 = tk.Tk()
                    root10.geometry('+500+300')
                    root10.title("ELECTRIC BILL MANAGEMENT SYSTEM(admin user data delete)")

                    tk.Label(root10, text="Enter userid (to be deleted) ->", font=(None, 15, 'bold')).grid(row=1, column=0)
                    e1 = tk.Entry(root10, width=30, insertwidth=4, bd=7)
                    e1.grid(row=1, column=1)
                    def checkdel():
                        uid = str(e1.get())
                        with open("user_file.csv",'r') as f:
                            reader = csv.reader(f)
                            reader = [i for i in reader]
                            for row in reader:
                                if row[0] == uid:
                                    return True
                        return False
                    def dele1():
                        if (checkdel()):
                            uid = str(e1.get())
                            lines = []
                            with open("user_file.csv", 'r') as f:
                                reader = csv.reader(f)
                                reader = [i for i in reader]
                                for row in reader:
                                    if row[0] == uid:
                                        l1 = row
                                    else:
                                        lines.append(row)
                            with open('user_file.csv', 'w',newline='\n') as writeFile:
                                writer = csv.writer(writeFile)
                                writer.writerows(lines)
                            lines = []
                            with open("user_units_2020.csv", 'r') as f:
                                reader = csv.reader(f)
                                reader = [i for i in reader]
                                for row in reader:
                                    if row[0] == uid:
                                        l1 = row
                                    else:
                                        lines.append(row)
                            with open('user_units_2020.csv', 'w',newline='\n') as writeFile:
                                writer = csv.writer(writeFile)
                                writer.writerows(lines)
                            lines = []
                            with open("user_units_2019.csv", 'r') as f:
                                reader = csv.reader(f)
                                reader = [i for i in reader]
                                for row in reader:
                                    if row[0] == uid:
                                        l1 = row
                                    else:
                                        lines.append(row)
                            with open('user_units_2019.csv', 'w',newline='\n') as writeFile:
                                writer = csv.writer(writeFile)
                                writer.writerows(lines)
                            tk.Label(root10, text="Successfully Deleted", font=(None, 8, 'bold')).grid(row=9, column=1)
                        else:
                            tk.Label(root10, text="USER ID DOESN'T EXIST", font=(None, 8, 'bold')).grid(row=9, column=1)

                    tk.Button(root10, text="Delete", fg="blue", font=(None, 12, 'bold'), bd=5, command=dele1).grid(row=8, column=1)
                    tk.Button(root10, text="QUIT", fg="red", font=(None, 12, 'bold'), bd=5, command=root10.destroy).grid(row=10, column=1)
                    root10.mainloop()

                img = tk.PhotoImage(file=r'admin.png')
                tk.Label(root7, image=img).grid(row=1, column=1)
                tk.Button(root7, text="Update Users Data", fg="green", font=(None, 12, 'bold'), bd=5,
                               command=updata).grid(row=3, column=0)
                tk.Button(root7, text="Enter units consumed by user", fg="green", font=(None, 12, 'bold'), bd=5,
                               command=consuni).grid(row=3, column=1)
                tk.Button(root7, text="Delete Users Data", fg="green", font=(None, 12, 'bold'), bd=5, command=dele).grid(row=3, column=2)
                tk.Button(root7, text="    Log out    ", fg="red", font=(None, 12, 'bold'), bd=5,
                               command=root7.destroy).grid(row=4, column=2)

                root7.mainloop()

            else:
                tk.Label(root6, text="Please enter correct username and password", font=(None, 8, 'bold')).grid(row=5, column=1)
        img = tk.PhotoImage(file=r'admingood.png')
        tk.Label(root6, image=img).grid(row=1,column=1)
        tk.Button(root6, text='Submit', fg='blue', font=(None, 12, 'bold'), bd=5, command=datad).grid(row=4, column=2)
        tk.Button(root6, text="QUIT", fg="red", font=(None, 12, 'bold'), bd=5, command=root6.destroy).grid(row=5, column=2)
        root6.mainloop()


    root1 = tk.Tk()
    root1.geometry('+500+300')
    root1.title("ELECTRIC BILL MANAGMENT SYSTEM")
    tk.Label(root1, text="Select one", fg='red', font=("castellar", 18, 'bold')).grid(row=1, column=2)
    tk.Button(root1, text="User", fg="blue", font=(None, 12, 'bold'), bd=5, command=user).grid(row=4, column=1)
    tk.Button(root1, text="Admin", fg="blue", font=(None, 12, 'bold'), bd=5, command=admin).grid(row=4, column=3)
    tk.Button(root1, text="QUIT", fg="red", font=(None, 12, 'bold'), bd=5, command=root1.destroy).grid(row=4, column=2)
    img1 = tk.PhotoImage(file=r"user.png")
    tk.Label(root1, image=img1).grid(row=3, column=1)
    img2 = tk.PhotoImage(file=r'adminstart.png')
    tk.Label(root1 , image=img2).grid(row=3 , column=3)
    root1.mainloop()

if __name__ == "__main__":
    main()