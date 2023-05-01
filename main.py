from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from oracledb import *
from datetime import datetime


def adminmenu():

    def change_password():

        def new_pass():

            def exit_np():
                np.destroy()

            def update_pass():
                cur = oraclestart()
                cur.execute(
                    f"update auth_users set password='{newp.get()}' where username='admin'")

                success = showinfo("PASSWORD UPDATED",
                                   "Password Successfully Updated")
                if success == "ok":
                    np.destroy()
                    root4.destroy()
                    adminmenu()
                cur.execute("commit")

            np = Tk()
            np.geometry("100x100")
            np.maxsize(100, 100)
            np.minsize(100, 100)
            np.title("NEW PASSWORD")
            np.maxsize(330, 230)
            np.minsize(330, 230)
            npf = Frame(np, highlightbackground="black", highlightthickness=2)
            npf.place(x=30, y=20, width=270, height=150)
            a = Label(npf, text="NEW PASSWORD", fg="blue",
                      font="comicsansms 15 bold").pack(pady=15)
            new_p = StringVar()
            newp = Entry(npf, textvariable=new_p, show="*",
                         highlightbackground="black", highlightthickness=2)
            newp.pack(pady=10)
            ch = Button(npf, highlightbackground="black",
                        highlightthickness=2, text="Change", fg="blue", font="comicsansms 10 bold", command=update_pass)
            enp = Button(np, text="Exit", fg="white", bg="black",
                         font="comicsansms 10 bold", highlightbackground="black", command=exit_np)
            enp.pack(side="bottom", anchor="nw", pady=30, padx=30)
            ch.pack(pady=10)
            np.mainloop()

        def exit_cp():
            cpp.destroy()

        def cp():
            cur = oraclestart()
            cur.execute(
                f"select password from auth_users where password='{p_pass.get()}'")
            pas = cur.fetchall()
            if pas != []:
                if pas[0][0] == p_pass.get():
                    cpp.destroy()
                    new_pass()
                else:
                    wp = askretrycancel("WRONG PASSWORD", "Password is Wrong")
                    if wp:
                        cpp.destroy()
                        change_password()
                    else:
                        cpp.destroy()
            else:
                Pde = askretrycancel("Invalid Password",
                                     "Wrong Password")
                if Pde:
                    cpp.destroy()
                    change_password()
                else:
                    cpp.destroy()
        cpp = Tk()
        cpp.title("CHANGE PASSWORD")
        cpp.geometry("300x250")
        cpp.maxsize(330, 230)
        cpp.minsize(330, 230)
        ecpf = Button(cpp, text="Exit", fg="white", bg="black",
                      font="comicsansms 10 bold", highlightbackground="black", command=exit_cp)
        ecpf.pack(side="bottom", anchor="nw", pady=30, padx=30)
        cpf = Frame(cpp, borderwidth=10,
                    highlightbackground="black", highlightthickness=2)
        cpf.place(x=30, y=20, width=270, height=150)
        a = Label(cpf, text="Previous Password",
                  fg="blue", font="comicsansms 15 bold").pack(padx=30)
        pre_pas = StringVar()
        p_pass = Entry(cpf, textvariable=pre_pas, show="*",
                       highlightbackground="black", highlightthickness=2)
        p_pass.pack(pady=20)
        print(p_pass)
        enter = Button(cpf, text="Verify", fg="blue",
                       font="comicsansms 10 bold", highlightbackground="black", highlightthickness=2, command=cp)
        enter.pack()
        cpp.mainloop()

    def exit_admin_menu():
        root4.destroy()
        menu()

    def additem():
        def itemadded():
            cur = oraclestart()
            cur.execute(
                f"insert into menu values('{iname.get()}',{iprice.get()},'{itemtype.get()}')")
            success = showinfo("Item Added",
                               "Item Added Succesfully")
            cur.execute("commit")
            if success == "ok":
                ai.destroy()
                root4.destroy()
                adminmenu()

        def exit_new_item():
            ai.destroy()
        ai = Tk()
        ai.title("New Item")
        ai.geometry("500x450")
        ai.minsize(400, 450)
        ai.maxsize(400, 450)
        aif = Frame(ai, highlightbackground="black",
                    highlightthickness=2, borderwidth=10, pady=10)
        a = Label(ai, text="New Item", fg="blue",
                  font="comicsansms 15 bold").pack(pady=15)
        name = StringVar()
        price = IntVar()
        itype = StringVar()

        n = Label(aif, text="Name", font="comicsansma 10 bold",
                  fg="black").pack(pady=7)
        iname = Entry(aif, textvariable=name,
                      highlightbackground="black", highlightthickness=2)
        iname.pack()
        p = Label(aif, text="Price", font="comicsansma 10 bold",
                  fg="black").pack(pady=7)
        iprice = Entry(aif, textvariable=price,
                       highlightbackground="black", highlightthickness=2)
        iprice.pack()
        t = Label(aif, text="Type", font="comicsansma 10 bold",
                  fg="black").pack(pady=7)
        itemtype = Entry(aif, textvariable=itype,
                         highlightbackground="black", highlightthickness=2)
        itemtype.pack()
        t = Label(aif, text="burger,pizza,snack,", font="comicsansma 10 bold",
                  fg="grey").pack()
        t = Label(aif, text="maincource,Bread,baverage", font="comicsansma 10 bold",
                  fg="grey").pack()

        e = Button(ai, text="Exit", fg="white", bg="black",
                   font="comicsansms 10 bold", highlightbackground="black", command=exit_new_item)
        e.pack(side="bottom", anchor="nw", pady=30, padx=30)
        enter = Button(aif, text="  ADD  ", fg="blue",
                       highlightbackground="black", highlightthickness=2, command=itemadded)
        enter.pack(pady=4, side="bottom")
        aif.place(x=70, y=60, width=270, height=300)
        ai.mainloop()

    def delete_item():
        def exit_di():
            di.destroy()

        def itemdeleted():
            cur = oraclestart()
            cur.execute(f"select name from menu where name='{dname.get()}'")
            row = cur.fetchall()
            if row != []:
                cur.execute(f"delete from menu where name='{dname.get()}'")
                cur.execute("commit")
                success = showinfo("Item Deleted",
                                   "Item Deleted Succesfully")
                if success == "ok":
                    di.destroy()
                    root4.destroy()
                    adminmenu()
            else:
                fail = askretrycancel("Item not Found", "Item not Found")
                if fail:
                    di.destroy()
                    delete_item()
                else:
                    di.destroy()

        di = Tk()
        di.title("Delete Item")
        di.geometry("300x250")
        di.minsize(300, 250)
        di.maxsize(300, 250)
        dif = Frame(di, highlightbackground="black",
                    highlightthickness=2, borderwidth=10, pady=10)
        a = Label(di, text="Delete Item", fg="blue",
                  font="comicsansms 15 bold").pack(pady=15)
        name = StringVar()
        n = Label(dif, text="Name", font="comicsansma 10 bold",
                  fg="black").pack(pady=7)
        dname = Entry(dif, textvariable=name,
                      highlightbackground="black", highlightthickness=2)
        dname.pack()
        enter = Button(dif, text="DELETE", fg="blue",
                       highlightbackground="black", highlightthickness=2, command=itemdeleted)
        enter.pack(pady=10)
        edi = Button(di, text="Exit", fg="white", bg="black",
                     font="comicsansms 10 bold", highlightbackground="black", command=exit_di)
        edi.pack(side="bottom", anchor="nw", pady=20, padx=50)
        dif.place(x=50, y=50, width=200, height=150)
        di.mainloop()

    def update_item():
        def exit_ui():
            ui.destroy()

        def itemupdated():
            cur = oraclestart()
            cur.execute(f"select name from menu where name='{uname.get()}'")
            row = cur.fetchall()
            if row != []:
                # ui.destroy()
                update_menu()
            else:
                fail = askretrycancel("Item not Found", "Item not Found")
                if fail:
                    ui.destroy()
                    update_item()
                else:
                    ui.destroy()

        def update_menu():

            def price_update():
                def exit_pu():
                    pu.destroy()
                    update_menu()

                def priceup():
                    cur = oraclestart()
                    cur.execute(
                        f"update menu set price={newprice.get()} where name='{uname.get()}'")
                    cur.execute("commit")
                    success = showinfo(
                        "Item Updated", "Item Updated Successfully")
                    if success == "ok":
                        pu.destroy()
                        update_menu()
                um.destroy()
                pu = Tk()
                pu.geometry("300x250")
                pu.title("New Price")
                pu.maxsize(300, 250)
                pu.minsize(300, 250)
                puf = Frame(pu, borderwidth=10,
                            highlightbackground="black", highlightthickness=2)
                puf.place(x=50, y=50, width=200, height=150)
                a = Label(pu, text="Update Price", fg="blue",
                          font="comicsansms 15 bold").pack(pady=15)
                b = Label(puf, text="New Price", fg="blue",
                          font="comicsansms 10 bold").pack(pady=10)
                nprice = StringVar()
                newprice = Entry(puf, textvariable=nprice,
                                 highlightbackground="black", highlightthickness=2)
                newprice.pack(pady=5)
                unewprice = Button(puf, text="UPDATE", fg="blue",
                                   highlightbackground="black", highlightthickness=2, command=priceup).pack(pady=5)
                edi = Button(pu, text="Exit", fg="white", bg="black",
                             font="comicsansms 10 bold", highlightbackground="black", command=exit_pu)
                edi.pack(side="bottom", anchor="nw", pady=20, padx=50)
                pu.mainloop()

            def desc_update():
                def exit_du():
                    du.destroy()
                    update_menu()

                def descup():
                    cur = oraclestart()
                    cur.execute(
                        f"update menu set name='{newname.get()}' where name='{uname.get()}'")
                    cur.execute("commit")
                    success = showinfo(
                        "Item Updated", "Item Updated Successfully")
                    if success == "ok":
                        du.destroy()
                        root4.destroy()
                        adminmenu()
                um.destroy()
                du = Tk()
                du.title("New Name")
                du.geometry("300x250")
                du.maxsize(300, 250)
                du.minsize(300, 250)
                duf = Frame(du, borderwidth=10,
                            highlightbackground="black", highlightthickness=2)
                duf.place(x=50, y=50, width=200, height=150)
                a = Label(du, text="Update Name", fg="blue",
                          font="comicsansms 15 bold").pack(pady=15)
                b = Label(duf, text="New Name", fg="blue",
                          font="comicsansms 10 bold").pack(pady=10)
                ndesc = StringVar()
                newname = Entry(duf, textvariable=ndesc,
                                highlightbackground="black", highlightthickness=2)
                newname.pack(pady=5)
                unewdesc = Button(duf, text="UPDATE", fg="blue",
                                  highlightbackground="black", highlightthickness=2, command=descup).pack(pady=5)
                edi = Button(du, text="Exit", fg="white", bg="black",
                             font="comicsansms 10 bold", highlightbackground="black", command=exit_du)
                edi.pack(side="bottom", anchor="nw", pady=20, padx=50)
                du.mainloop()

            def exit_um():
                um.destroy()
                ui.destroy()
            um = Tk()
            um.title("Update Item")
            um.geometry("300x250")
            um.maxsize(300, 250)
            um.minsize(300, 250)
            a = Label(um, text="Update Item", fg="blue",
                      font="comicsansms 15 bold").pack(pady=15)
            edi = Button(um, text="Exit", fg="white", bg="black",
                         font="comicsansms 10 bold", highlightbackground="black", command=exit_um)
            edi.pack(side="bottom", anchor="nw", pady=20, padx=50)
            umf = Frame(um, borderwidth=10,
                        highlightbackground="black", highlightthickness=2)
            umf.place(x=50, y=50, width=200, height=150)
            priceu = Button(umf, text="     Price    ", font="comicsansms 15 bold", fg="blue", bg="white",
                            highlightbackground="black", highlightthickness=2, command=price_update)
            descu = Button(umf, text="    Name    ", font="comicsansms 15 bold", fg="blue", bg="white",
                           highlightbackground="black", highlightthickness=2, command=desc_update)
            priceu.pack(pady=10)
            descu.pack(pady=10)
            um.mainloop()
        ui = Tk()
        ui.title("Update Item")
        ui.geometry("300x250")
        ui.maxsize(300, 250)
        ui.minsize(300, 250)
        uif = Frame(ui, highlightbackground="black",
                    highlightthickness=2, borderwidth=10, pady=10)
        a = Label(ui, text="Update Item", fg="blue",
                  font="comicsansms 15 bold").pack(pady=15)
        name = StringVar()
        n = Label(uif, text="Name", font="comicsansma 10 bold",
                  fg="black").pack(pady=7)
        uname = Entry(uif, textvariable=name,
                      highlightbackground="black", highlightthickness=2)
        uname.pack()
        enter = Button(uif, text="UPDATE", fg="blue",
                       highlightbackground="black", highlightthickness=2, command=itemupdated)
        enter.pack(pady=10)
        eui = Button(ui, text="Exit", fg="white", bg="black",
                     font="comicsansms 10 bold", highlightbackground="black", command=exit_ui)
        eui.pack(side="bottom", anchor="nw", pady=20, padx=50)
        uif.place(x=50, y=50, width=200, height=150)
        ui.mainloop()

    def bills():
        def exit_bill():
            bil_root.destroy()
        bil_root = Tk()
        bil_root.geometry("500x500")
        bil_root.title("Bills")
        ml = Label(bil_root, text="Bills",
                   font="comicsansms 15 bold", fg="blue")
        ml.pack(pady=10)
        bar = Scrollbar(bil_root)
        bar.pack(side=RIGHT, fill=Y)
        with open("bills.txt", "r") as file:

            l = Listbox(bil_root,
                        yscrollcommand=bar.set, height=20)
            for i in file:
                l.insert(END, f"{i}")

            l.pack(pady=5, fill=BOTH)
        bar.config(command=l.yview)
        eb = Button(bil_root, text="Exit", fg="white", bg="black",
                    font="comicsansms 10 bold", highlightbackground="black", command=exit_bill)
        eb.pack(side="bottom", anchor="nw", pady=20, padx=50)
        bil_root.mainloop()

    def show_staff():
        def search_emp():
            def search():
                def exit_emps():
                    emps.destroy()
                    se.destroy()
                cur = oraclestart()
                cur.execute(f"select * from emp where id={sss.get()}")
                row = cur.fetchall()
                if row != []:
                    emps = Tk()
                    emps.geometry("1400x200")
                    emps.title("search employee")
                    emps.maxsize(1400, 200)
                    emps.minsize(1400, 200)
                    stable = ttk.Treeview(emps, columns=(
                        1, 2, 3, 4, 5, 6, 7), show="headings", height="5")
                    stable.pack()
                    eui = Button(emps, text="Exit", fg="white", bg="black",
                                 font="comicsansms 10 bold", highlightbackground="black", command=exit_emps)
                    eui.pack(side="bottom", anchor="nw", pady=20, padx=50)
                    stable.heading(1, text="Id")
                    stable.heading(2, text="Name")
                    stable.heading(3, text="Mobile")
                    stable.heading(4, text="Address")
                    stable.heading(5, text="Salary")
                    stable.heading(6, text="Post")
                    stable.heading(7, text="Joining Date and Time")
                    for i in row:
                        stable.insert('', 'end', value=i)
                    emps.mainloop()
                else:
                    fail = askretrycancel("Not Found", "Employee Not Found")
                    if fail:
                        se.destroy()
                        search_emp()
                    else:
                        se.destroy()
                        ss.destroy()

            def exit_se():
                se.destroy()
            se = Tk()
            se.geometry("330x230")
            se.title("Search")
            se.maxsize(330, 230)
            se.minsize(330, 230)
            sef = Frame(se, highlightbackground="black",
                        highlightthickness=2)
            sef.place(x=30, y=20, width=270, height=150)
            a = Label(sef, text="Employee Id", fg="blue",
                      font="comicsansms 15 bold").pack(pady=15)
            sse = IntVar()
            sss = Entry(sef, textvariable=sse,
                        highlightbackground="black", highlightthickness=2)
            sss.pack(pady=10)
            ese = Button(sef, text="Search", highlightbackground="black",
                         highlightthickness=2, fg="blue", font="comicsansms 10 bold", command=search)
            ese.pack()
            eui = Button(se, text="Exit", fg="white", bg="black",
                         font="comicsansms 10 bold", highlightbackground="black", command=exit_se)
            eui.pack(side="bottom", anchor="nw", pady=20, padx=50)
            se.mainloop()

        def exit_ss():
            ss.destroy()
        ss = Tk()
        ss.geometry("1400x700")
        ss.maxsize(1400, 700)
        ss.minsize(1400, 700)
        ss.title("Employees")
        a = Label(ss, text="Employees", fg="red",
                  font="comicsansms 15 bold").pack(pady=10)
        sui = Button(ss, text="Search", fg="white", bg="black",
                     font="comicsansms 10 bold", highlightbackground="black", command=search_emp)
        sui.pack(anchor="se", padx=5, pady=5)
        ssf = Frame(ss)
        ssf.pack()
        bar = Scrollbar(ssf)
        bar.pack(sid=RIGHT, fill=Y)
        table = ttk.Treeview(ssf, columns=(
            1, 2, 3, 4, 5, 6, 7), show="headings", height="25", yscrollcommand=bar.set)
        table.pack(fill=Y)
        bar.config(command=table.yview)
        eui = Button(ss, text="Exit", fg="white", bg="black",
                     font="comicsansms 10 bold", highlightbackground="black", command=exit_ss)
        eui.pack(side="bottom", anchor="nw", pady=20, padx=50)
        table.heading(1, text="Id")
        table.heading(2, text="Name")
        table.heading(3, text="Mobile")
        table.heading(4, text="Address")
        table.heading(5, text="Salary")
        table.heading(6, text="Post")
        table.heading(7, text="Joining Date and Time")
        cur = oraclestart()
        cur.execute("select * from emp")
        rows = cur.fetchall()
        for i in rows:
            table.insert('', 'end', values=i)

        ss.mainloop()

    def staff():
        def exit_s():
            s.destroy()

        def hire():
            def exithiring():
                h.destroy()

            def empadded():
                cur = oraclestart()
                cur.execute(
                    f"insert into emp(name,mobile,address,salary,post,joining_date) values('{ename.get()}',{emob.get()},'{eadd.get()}',{esal.get()},'{epost.get()}',(select sysdate from dual))")
                cur.execute("commit")
                success = showinfo("Hired", "Hired Successfully")
                if success == "ok":
                    h.destroy()
                    s.destroy()
                    root4.destroy()
                    adminmenu()
            h = Tk()
            h.geometry("500x550")
            h.maxsize(500, 550)
            h.minsize(500, 550)
            h.title("Hiring")
            hf = Frame(h, highlightbackground="black",
                       highlightthickness=2, borderwidth=10, pady=10)

            name = StringVar()
            mobile = IntVar()
            address = StringVar()
            salary = IntVar()
            post = StringVar()

            n = Label(h, text="Hiring Employee", font="comicsansma 15 bold",
                      fg="Blue").pack(pady=7)
            n = Label(hf, text="Employee Details", font="comicsansma 13 bold",
                      fg="blue").pack(pady=7)
            n = Label(hf, text="Name", font="comicsansma 10 bold",
                      fg="black").pack()
            ename = Entry(hf, textvariable=name,
                          highlightbackground="black", highlightthickness=2)
            ename.pack()
            n = Label(hf, text="Mobile", font="comicsansma 10 bold",
                      fg="black").pack(pady=5)
            emob = Entry(hf, textvariable=mobile,
                         highlightbackground="black", highlightthickness=2)
            emob.pack(pady=5)
            n = Label(hf, text="Address", font="comicsansma 10 bold",
                      fg="black").pack(pady=5)
            eadd = Entry(hf, textvariable=address,
                         highlightbackground="black", highlightthickness=2)
            eadd.pack()
            n = Label(hf, text="Salary", font="comicsansma 10 bold",
                      fg="black").pack(pady=5)
            esal = Entry(hf, textvariable=salary,
                         highlightbackground="black", highlightthickness=2)
            esal.pack(pady=5)
            n = Label(hf, text="Post", font="comicsansma 10 bold",
                      fg="black").pack()
            epost = Entry(hf, textvariable=post,
                          highlightbackground="black", highlightthickness=2)
            epost.pack()
            e = Button(h, text="Exit", fg="white", bg="black",
                       font="comicsansms 10 bold", highlightbackground="black", command=exithiring)
            e.pack(side="bottom", anchor="nw", pady=30, padx=30)
            enter = Button(hf, text="  ADD  ", fg="blue",
                           highlightbackground="black", highlightthickness=2, command=empadded)
            enter.pack(pady=7, side="bottom")
            hf.place(x=70, y=60, width=370, height=400)

            h.mainloop()

        def fire():

            def search_e():
                cur = oraclestart()
                cur.execute(f"select name from emp where id={f.get()}")
                row = cur.fetchall()
                if row != []:
                    ok = askquestion("Fire", "Do you want to fire")
                    if ok == "yes":
                        cur.execute(
                            f"delete from emp where id={f.get()}")
                        cur.execute("commit")
                        success = showinfo("Fired",
                                           "Fired Succesfully")
                        if success == "ok":
                            fire_e.destroy()
                            s.destroy()
                            root4.destroy()
                            adminmenu()
                    else:
                        fire_e.destroy()
                        s.destroy()
                        root4.destroy()
                        adminmenu()

                else:
                    fail = askretrycancel("Item not Found", "Item not Found")
                    if fail:
                        fire_e.destroy()
                        fire()
                    else:
                        fire_e.destroy()
                        s.destroy()

            def exit_fire():
                fire_e.destroy()
            fire_e = Tk()
            fire_e.geometry("330x230")
            fire_e.title("FIRE")
            fire_e.maxsize(330, 230)
            fire_e.minsize(330, 230)
            fire_ef = Frame(fire_e, highlightbackground="black",
                            highlightthickness=2)
            fire_ef.place(x=30, y=20, width=270, height=150)
            a = Label(fire_ef, text="Employee Id", fg="blue",
                      font="comicsansms 15 bold").pack(pady=15)
            fe = IntVar()
            f = Entry(fire_ef, textvariable=fe,
                      highlightbackground="black", highlightthickness=2)
            f.pack(pady=10)
            ch = Button(fire_ef, highlightbackground="black",
                        highlightthickness=2, text="  Fire  ", fg="blue", font="comicsansms 10 bold", command=search_e)
            ef = Button(fire_e, text="Exit", fg="white", bg="black",
                        font="comicsansms 10 bold", highlightbackground="black", command=exit_fire)
            ef.pack(side="bottom", anchor="nw", pady=30, padx=30)
            ch.pack(pady=10)
            fire_e.mainloop()

        def promotion():
            def exit_promo():
                promo_e.destroy()

            def search_efp():
                def uppost():

                    def exitefpp():
                        uss.destroy()
                        pro.destroy()
                        promo_e.destroy()
                        s.destroy()

                    def update_efp():
                        cur = oraclestart()
                        cur.execute(
                            f"update emp set post='{npp.get()}' where id={f.get()}")
                        cur.execute("commit")
                        success = showinfo(
                            "Promotion", "Promoted Successfully")
                        if success == "ok":
                            uss.destroy()
                            pro.destroy()
                            promo_e.destroy()
                            s.destroy()
                    uss = Tk()
                    uss.geometry("330x230")
                    uss.maxsize(330, 230)
                    uss.minsize(330, 230)
                    uss.title("New Salary")
                    usff = Frame(uss, highlightbackground="black",
                                 highlightthickness=2)
                    a = Label(usff, text="New Post", fg="blue",
                              font="comicsansms 15 bold").pack(pady=15)
                    np = StringVar()
                    npp = Entry(usff, textvariable=np,
                                highlightbackground="black", highlightthickness=2)
                    npp.pack(pady=10)
                    prom = Button(
                        usff, text="Promote", font="comicsansms 10 bold", highlightbackground="black", highlightthickness=2, fg="blue", command=update_efp)
                    prom.pack(pady=7)
                    exx = Button(uss, text="Exit", fg="white", bg="black",
                                 font="comicsansms 10 bold", highlightbackground="black", command=exitefpp)
                    exx.pack(side="bottom", anchor="nw", pady=30, padx=30)
                    usff.place(x=30, y=20, width=270, height=150)
                    uss.mainloop()

                def upsal():
                    def exitefp():
                        us.destroy()
                        pro.destroy()
                        promo_e.destroy()
                        s.destroy()

                    def update_efp():
                        cur = oraclestart()
                        cur.execute(
                            f"update emp set salary={n.get()} where id={f.get()}")
                        cur.execute("commit")
                        success = showinfo(
                            "Promotion", "Promoted Successfully")
                        if success == "ok":
                            us.destroy()
                            pro.destroy()
                            promo_e.destroy()
                            s.destroy()
                    us = Tk()
                    us.geometry("330x230")
                    us.maxsize(330, 230)
                    us.minsize(330, 230)
                    us.title("New Salary")
                    usf = Frame(us, highlightbackground="black",
                                highlightthickness=2)
                    a = Label(usf, text="New Salary", fg="blue",
                              font="comicsansms 15 bold").pack(pady=15)
                    ns = IntVar()
                    n = Entry(usf, textvariable=ns,
                              highlightbackground="black", highlightthickness=2)
                    n.pack(pady=10)
                    prom = Button(
                        usf, text="Promote", font="comicsansms 10 bold", highlightbackground="black", highlightthickness=2, fg="blue", command=update_efp)
                    prom.pack(pady=7)
                    ex = Button(us, text="Exit", fg="white", bg="black",
                                font="comicsansms 10 bold", highlightbackground="black", command=exitefp)
                    ex.pack(side="bottom", anchor="nw", pady=30, padx=30)
                    usf.place(x=30, y=20, width=270, height=150)
                    us.mainloop()

                def exit_pro():
                    pro.destroy()
                    promo_e.destroy()
                cur = oraclestart()
                cur.execute(f"select name from emp where id={f.get()}")
                row = cur.fetchall()
                if row != []:
                    pro = Tk()
                    pro.geometry("330x230")
                    pro.maxsize(330, 230)
                    pro.minsize(330, 230)
                    pro.title("Promotion")
                    prof = Frame(pro, highlightbackground="black",
                                 highlightthickness=2)
                    prof.place(x=30, y=20, width=270, height=150)
                    a = Label(prof, text="Promotion", fg="blue",
                              font="comicsansms 15 bold").pack(pady=10)
                    sal = Button(
                        prof, text="   Salary   ", font="comicsansms 10 bold", highlightbackground="black", highlightthickness=2, fg="blue", command=upsal)
                    sal.pack(pady=7)
                    post = Button(
                        prof, text="     Post    ", font="comicsansms 10 bold", highlightbackground="black", highlightthickness=2, fg="blue", command=uppost)
                    post.pack(pady=7)
                    ef = Button(pro, text="Exit", fg="white", bg="black",
                                font="comicsansms 10 bold", highlightbackground="black", command=exit_pro)
                    ef.pack(side="bottom", anchor="nw", pady=30, padx=30)
                    ch.pack(pady=10)
                    pro.mainloop()
                else:
                    fail = askretrycancel("Not Found", "Not Found")
                    if fail:
                        promo_e.destroy()
                        promotion()
                    else:
                        promo_e.destroy()
                        s.destroy()

            promo_e = Tk()
            promo_e.geometry("330x230")
            promo_e.title("Promotion")
            promo_e.maxsize(330, 230)
            promo_e.minsize(330, 230)
            promo_ef = Frame(promo_e, highlightbackground="black",
                             highlightthickness=2)
            promo_ef.place(x=30, y=20, width=270, height=150)
            a = Label(promo_ef, text="Employee Id", fg="blue",
                      font="comicsansms 15 bold").pack(pady=15)
            fe = IntVar()
            f = Entry(promo_ef, textvariable=fe,
                      highlightbackground="black", highlightthickness=2)
            f.pack(pady=10)
            ch = Button(promo_ef, highlightbackground="black",
                        highlightthickness=2, text="  Search  ", fg="blue", font="comicsansms 10 bold", command=search_efp)
            ef = Button(promo_e, text="Exit", fg="white", bg="black",
                        font="comicsansms 10 bold", highlightbackground="black", command=exit_promo)
            ef.pack(side="bottom", anchor="nw", pady=30, padx=30)
            ch.pack(pady=10)
            promo_e.mainloop()

        s = Tk()
        s.title("Staff Management")
        s.geometry("300x250")
        s.maxsize(300, 250)
        s.minsize(300, 250)
        a = Label(s, text="Staff Management", fg="blue",
                  font="comicsansms 15 bold").pack(pady=15)
        edi = Button(s, text="Exit", fg="white", bg="black",
                     font="comicsansms 10 bold", highlightbackground="black", command=exit_s)
        edi.pack(side="bottom", anchor="nw", pady=20, padx=50)
        sf = Frame(s, borderwidth=10,
                   highlightbackground="black", highlightthickness=2)
        sf.place(x=50, y=50, width=200, height=150)
        ehire = Button(sf, text="       Hire      ", font="comicsansms 10 bold", fg="blue", bg="white",
                       highlightbackground="black", highlightthickness=2, command=hire)
        efire = Button(sf, text="       Fire      ", font="comicsansms 10 bold", fg="blue", bg="white",
                       highlightbackground="black", highlightthickness=2, command=fire)
        epromo = Button(sf, text="  Promotion  ", font="comicsansms 10 bold", fg="blue", bg="white",
                        highlightbackground="black", highlightthickness=2, command=promotion)
        ehire.pack(pady=5)
        efire.pack(pady=5)
        epromo.pack(pady=5)
        s.mainloop()

    root4 = Tk()
    root4.geometry("500x450")
    root4.minsize(500, 450)
    root4.maxsize(500, 450)
    root4.title("Admin Screen")
    frame = Frame(root4, borderwidth=10,
                  highlightbackground="black", highlightthickness=2, pady=10)
    a = Label(root4, text="ADMIN", fg="blue", font="comicsansms 15 bold")
    a.pack(pady=10)
    add = Button(frame, text="        ADD ITEM        ", bg="white",
                 fg="black", font="comicsansms 10 bold", command=additem)
    add.pack()
    dell = Button(frame, text="     DELETE  ITEM     ", bg="white",
                  fg="black", font="comicsansms 10 bold", command=delete_item)
    dell.pack(pady=10)
    update = Button(frame, text="     UPDATE  ITEM     ",
                    bg="white", fg="black", font="comicsansms 10 bold", command=update_item)
    update.pack()
    bill = Button(frame, text="       VIEW BILLS       ", bg="white",
                  fg="black", font="comicsansms 10 bold", command=bills)
    bill.pack(pady=10)
    staff = Button(frame, text="STAFF MANAGEMENT",
                   bg="white", fg="black", font="comicsansms 10 bold", command=staff)
    staff.pack()
    stafff = Button(frame, text="            STAFF            ",
                    bg="white", fg="black", font="comicsansms 10 bold", command=show_staff)
    stafff.pack(pady=10)
    cpass = Button(frame, text=" CHANGE PASSWORD ",
                   bg="white", fg="black", font="comicsansms 10 bold", command=change_password)
    cpass.pack()
    b = Button(root4, text="Exit", fg="white", bg="black", font="comicsansms 10 bold",
               command=exit_admin_menu)
    b.pack(side="bottom", anchor="nw", pady=50, padx=40)
    frame.place(x=110, y=60, width=300, height=300)
    root4.mainloop()


def oraclestart():
    connection = connect(user="SYSTEM", password="cutie",
                         dsn="555goru:1521/XE")
    cursor = connection.cursor()
    return cursor


def menu():
    list = []

    def spaceing(n, m):
        sum = m+n
        result = ""
        for i in range(40-sum):
            result += " "
        return result

    def cart():

        def get_mobile():
            def bill():
                a = em.get()
                try:
                    c = len(a)
                    b = int(a)
                    if c == 10:
                        with open('bills.txt', 'a') as file:
                            file.write(f"\nMobile: {em.get()}\n")
                            file.write(
                                f"Item x Quantity{spaceing(0,0)}Price                          {datetime.now()}\n")
                            for i in list:

                                file.write(
                                    f"{i[0]} x {i[2]}{spaceing(len(str(i[0])),len(str(i[2])))}{i[1]}\n")
                            file.write(f"Total         {total}\n")
                            file.write(
                                "-----------------------------------------------------------------------------------------------\n")
                            success = showinfo(
                                "Order Placed", "Order Placed Successfylly.....")

                            list.clear()

                            po.destroy()
                    else:
                        fail = showinfo("Invalid Mobile",
                                        "Mobile No. must contain 10 digits")
                        if fail == "ok":
                            po.destroy()
                except ValueError:
                    fail = showinfo("Invalid Mobile",
                                    "Mobile No. Should be Numeric")
                    if fail == "ok":
                        po.destroy()

            mobile = IntVar()
            wcart.destroy()
            po = Tk()
            po.geometry("400x350")
            po.maxsize(300, 250)
            po.minsize(300, 250)
            po.title("Place Order")
            m = Label(po, text="   Mobile   ",
                      font="comocsansms 15 bold", fg="green")
            em = Entry(po, textvariable=mobile,
                       highlightbackground="black", highlightthickness=2)
            place_ordr = Button(po, text=" Done ", fg="blue",
                                font="comicsansms 10 bold", command=bill)
            m.pack(pady=30)
            em.pack(pady=10)
            place_ordr.pack(pady=20)
            po.mainloop()

        def exit_cart():
            wcart.destroy()

        def cancel_order():
            list.clear()
            wcart.destroy()
        total = 0
        wcart = Tk()
        wcart.title("Cart")
        wcart.geometry("600x400")
        wcartf = Frame(wcart)
        wcartf.pack()
        bar = Scrollbar(wcartf)
        bar.pack(side=RIGHT, fill=Y)
        table = ttk.Treeview(wcartf, columns=(1, 2, 3), show="headings",
                             height=10, yscrollcommand=bar.set)
        table.heading(1, text="Name")
        table.heading(2, text="Price")
        table.heading(3, text="Quantity")
        for i in list:
            table.insert('', 'end', values=i)
        table.pack()
        bar.config(command=table.yview)
        for i in list:

            total = total+(int(i[1])*int(i[2]))
        t = Label(wcart, text=f"Total       {total}",
                  fg="blue", font="comicsansms 20 bold")
        t.pack()
        place_o = Button(wcart, text=" Done ", fg="blue",
                         font="comicsansms 10 bold", command=get_mobile)
        cancel_o = Button(wcart, text="Cancel", fg="red",
                          font="comicsansms 10 bold", command=cancel_order)
        exit_c = Button(wcart, text="  Exit  ", fg="white",
                        bg="black", font="comicsansms 10 bold", command=exit_cart)
        exit_c.pack(side=BOTTOM, anchor="ne", pady=5, padx=10)
        cancel_o.pack(side=BOTTOM, anchor="ne", pady=5, padx=10)
        place_o.pack(side=BOTTOM, anchor="ne", pady=5, padx=10)
        wcart.mainloop()

    def menu_frames_upper(item_type):

        def get_upper_values(a):

            def add_item_u():

                ulist = []

                ulist.append(name)
                ulist.append(price)
                if eqt.get() == "":
                    ulist.append(1)
                else:
                    ulist.append(eqt.get())
                list.append(ulist)

                print(list)
                up_val.destroy()

            def exit_mfu():
                up_val.destroy()

            sel_items = table.focus()
            details = table.item(sel_items)
            name = details.get("values")[0]
            price = details.get("values")[1]

            qty = IntVar()

            if item_type == "burger":
                up_val = Tk()
                up_val.title("ADD")
                up_val.geometry("500x350")
                iname = Label(up_val, text=name,
                              font="comicsansms 20 bold", fg="purple").pack()

                iprice = Label(up_val, text=f"Price          {price} Rs.",
                               font="comicsansms 10 bold").pack(pady=20)
                cancel = Button(up_val, text="Cancel", fg="red", font="comicsansms 10 bold",
                                command=exit_mfu)

                add = Button(up_val, text="  Add  ", fg="blue", font="comicsansms 10 bold",
                             command=add_item_u)
                qt = Label(up_val, text="Quantity   ",
                           font="comocsansms 15 bold", fg="green")
                eqt = Entry(up_val, textvariable=qty,
                            highlightbackground="black", highlightthickness=2)
                qt.place(x=190, y=160)
                eqt.place(x=180, y=200)

                cancel.place(x=320, y=290)
                add.place(x=400, y=290)

            elif item_type == "pizza":
                up_val = Tk()
                up_val.title("ADD")
                up_val.geometry("500x350")
                iname = Label(up_val, text=name,
                              font="comicsansms 20 bold", fg="purple").pack()

                iprice = Label(up_val, text=f"Price          {price}",
                               font="comicsansms 10 bold").pack(pady=20)
                cancel = Button(up_val, text="Cancel",  fg="red", font="comicsansms 10 bold",
                                command=exit_mfu)
                add = Button(up_val, text="  Add  ", fg="blue", font="comicsansms 10 bold", command=add_item_u
                             )

                qt = Label(up_val, text="Quantity   ",
                           font="comocsansms 15 bold", fg="green")
                eqt = Entry(up_val, textvariable=qty,
                            highlightbackground="black", highlightthickness=2)

                qt.place(x=190, y=160)
                eqt.place(x=180, y=200)

                cancel.place(x=320, y=290)
                add.place(x=400, y=290)
            elif item_type == "maincource":
                up_val = Tk()
                up_val.title("ADD")
                up_val.geometry("500x350")
                iname = Label(up_val, text=name,
                              font="comicsansms 20 bold", fg="purple").pack()

                iprice = Label(up_val, text=f"Price          {price}",
                               font="comicsansms 10 bold").pack(pady=20)
                cancel = Button(up_val, text="Cancel", fg="red", font="comicsansms 10 bold",
                                command=exit_mfu)
                add = Button(up_val, text="  Add  ", fg="blue", font="comicsansms 10 bold", command=add_item_u
                             )
                qt = Label(up_val, text="Quantity   ",
                           font="comocsansms 15 bold", fg="green")
                eqt = Entry(up_val, textvariable=qty,
                            highlightbackground="black", highlightthickness=2)
                qt.place(x=190, y=160)
                eqt.place(x=180, y=200)

                cancel.place(x=320, y=290)
                add.place(x=400, y=290)

            up_val.mainloop()

        item_frame_upper = Frame(umf, highlightbackground="black",
                                 highlightthickness=2)
        item_frame_upper.pack(fill="y", side=LEFT, padx=40)
        u_item_label = Label(item_frame_upper, text=f"{item_type}s".capitalize(), fg="white",
                             bg="black", font="comicsansms 20 bold", highlightbackground="white", highlightthickness=2, relief=SUNKEN)
        u_item_label.pack(fill=X)
        bar = Scrollbar(item_frame_upper)
        bar.pack(side=RIGHT, fill=Y)
        table = ttk.Treeview(item_frame_upper, columns=(1, 2), show="headings",
                             height=10, selectmode=BROWSE, yscrollcommand=bar.set)
        table.heading(1, text="Name")
        table.heading(2, text="Price")
        cur = oraclestart()
        cur.execute(f"select name, price from menu where type='{item_type}'")
        um_rows = cur.fetchall()
        for i in um_rows:
            table.insert('', 'end', values=i)
        table.bind("<Double-1>", get_upper_values)
        table.pack()
        bar.config(command=table.yview)

    def menu_frames_lower(item_type):
        qty = IntVar()

        def get_lower_values(a):
            def exit_lfu():
                lp_val.destroy()

            def add_item_l():

                llist = []

                llist.append(name)
                llist.append(price)
                if eqt.get() == "":
                    llist.append(1)
                else:
                    llist.append(eqt.get())
                list.append(llist)

                print(list)
                lp_val.destroy()

            sel_items = table.focus()
            details = table.item(sel_items)
            name = details.get("values")[0]
            price = details.get("values")[1]
            if item_type == "baverage":
                lp_val = Tk()
                lp_val.title("ADD")
                lp_val.geometry("500x350")
                iname = Label(lp_val, text=name,
                              font="comicsansms 20 bold", fg="purple").pack()

                iprice = Label(lp_val, text=f"Price          {price}",
                               font="comicsansms 10 bold").pack(pady=20)
                cancel = Button(lp_val, text="Cancel", fg="red", font="comicsansms 10 bold",
                                command=exit_lfu)
                add = Button(lp_val, text="  Add  ", fg="blue",
                             font="comicsansms 10 bold", command=add_item_l)
                qt = Label(lp_val, text="Quantity   ",
                           font="comocsansms 15 bold", fg="green")
                eqt = Entry(lp_val, textvariable=qty,
                            highlightbackground="black", highlightthickness=2)
                qt.place(x=190, y=160)
                eqt.place(x=180, y=200)
                cancel.place(x=320, y=290)
                add.place(x=400, y=290)
            elif item_type == "snack":
                lp_val = Tk()
                lp_val.title("ADD")
                lp_val.geometry("500x350")
                iname = Label(lp_val, text=name,
                              font="comicsansms 20 bold", fg="purple").pack()

                iprice = Label(lp_val, text=f"Price          {price}",
                               font="comicsansms 10 bold").pack(pady=20)
                cancel = Button(lp_val, text="Cancel", fg="red", font="comicsansms 10 bold",
                                command=exit_lfu)
                add = Button(lp_val, text="  Add  ", fg="blue", font="comicsansms 10 bold", command=add_item_l
                             )
                qt = Label(lp_val, text="Quantity   ",
                           font="comocsansms 15 bold", fg="green")
                eqt = Entry(lp_val, textvariable=qty,
                            highlightbackground="black", highlightthickness=2)
                qt.place(x=190, y=160)
                eqt.place(x=180, y=200)
                cancel.place(x=320, y=290)
                add.place(x=400, y=290)
            elif item_type == "Bread":
                lp_val = Tk()
                lp_val.title("ADD")
                lp_val.geometry("500x350")
                iname = Label(lp_val, text=name,
                              font="comicsansms 20 bold", fg="purple").pack()

                iprice = Label(lp_val, text=f"Price          {price}",
                               font="comicsansms 10 bold").pack(pady=20)
                cancel = Button(lp_val, text="Cancel", fg="red", font="comicsansms 10 bold",
                                command=exit_lfu)
                add = Button(lp_val, text="  Add  ", fg="blue", font="comicsansms 10 bold", command=add_item_l
                             )
                qt = Label(lp_val, text="Quantity   ",
                           font="comocsansms 15 bold", fg="green")
                eqt = Entry(lp_val, textvariable=qty,
                            highlightbackground="black", highlightthickness=2)
                qt.place(x=190, y=160)
                eqt.place(x=180, y=200)
                cancel.place(x=320, y=290)
                add.place(x=400, y=290)

            lp_val.mainloop()
        item_frame_lower = Frame(lmf, highlightbackground="black",
                                 highlightthickness=2)
        item_frame_lower.pack(fill="y", side=LEFT, padx=40)
        if (item_type == "baverage"):
            l_item_label = Label(item_frame_lower, text=f"daserts and {item_type}s".capitalize(), fg="white",
                                 bg="black", font="comicsansms 20 bold", highlightbackground="white", highlightthickness=2, relief=SUNKEN)
            l_item_label.pack(fill=X)
        else:
            l_item_label = Label(item_frame_lower, text=f"{item_type}s".capitalize(), fg="white",
                                 bg="black", font="comicsansms 20 bold", highlightbackground="white", highlightthickness=2, relief=SUNKEN)
            l_item_label.pack(fill=X)
        bar = Scrollbar(item_frame_lower)
        bar.pack(side=RIGHT, fill=Y)
        table = ttk.Treeview(item_frame_lower, columns=(1, 2), show="headings",
                             height=10, yscrollcommand=bar.set)
        table.heading(1, text="Name")
        table.heading(2, text="Price")
        table.bind("<Double-1>", get_lower_values)
        cur = oraclestart()
        cur.execute(f"select name, price from menu where type='{item_type}'")
        lm_rows = cur.fetchall()
        for i in lm_rows:
            table.insert('', 'end', values=i)
        table.pack()
        bar.config(command=table.yview)

    def up():

        def chk():
            cur = oraclestart()
            cur.execute(
                f"select password from auth_users where username='{username.get()}'")
            # print(
            #     f"select password from auth_users where username='{username.get()}'")
            row = cur.fetchall()
            if row != []:
                if row[0][0] == password.get():
                    root1.destroy()
                    root3.destroy()
                    adminmenu()

                else:
                    pvalue = askretrycancel(
                        "Invalid Password", "wrong password..")
                    if pvalue:
                        root1.destroy()
                        up()
                    else:
                        root1.destroy()

            else:
                uvalue = askretrycancel(
                    "Invalid username", "wrong username..")
                if uvalue:
                    root1.destroy()
                    up()
                else:
                    root1.destroy()
        root1 = Tk()
        root1.title("LOGIN PAGE")
        root1.geometry("300x250")
        root1.maxsize(300, 250)
        root1.minsize(300, 250)
        logo = Frame(root1, borderwidth=10,
                     highlightbackground="black", highlightthickness=2, pady=10)
        logo.place(x=30, y=20, width=250, height=190)
        u = Label(logo, text="Username").pack(padx=30)
        user = StringVar()
        # user.set("")
        username = Entry(logo, textvariable=user,
                         highlightbackground="black", highlightthickness=2)
        username.pack()

        pas = StringVar()
        # print(user.get())
        p = Label(logo, text="Password").pack(padx=30)
        password = Entry(logo, textvariable=pas, show="*",
                         highlightbackground="black", highlightthickness=2)
        password.pack(pady=8)
        a = Button(logo, text="Login", fg="blue",
                   font="comicsansms 10 bold", highlightbackground="black", highlightthickness=2, command=chk)
        a.pack(pady=4)
        root1.mainloop()

    root3 = Tk()
    root3.geometry("1900x900")
    root3.title("RESTAURENT MANAGEMENT SYSTEM")
    logo = Frame(root3, bg="red", highlightbackground="black",
                 highlightthickness=4)
    logo.pack(fill="x")
    admin = Button(root3, text="Admin", bg="black", fg="white",
                   font="comicsansms 10 bold", borderwidth=5, relief=SUNKEN, command=up)
    admin.pack()
    cart = Button(root3, text="  CART  ", bg="black", fg="white",
                  font="comicsansms 10 bold", borderwidth=5, relief=SUNKEN, command=cart)
    cart.place(x=1400, y=85)
    rms = Label(logo, text="RESTAURENT MANAGEMENT SYSTEM",
                bg="red", fg="white", font="comicsansms 18 bold")
    rms.pack(pady=20)
    umf = Frame(root3)
    umf.place(x=10, y=120)
    lmf = Frame(root3)
    lmf.place(x=10, y=450)
    item_type_list_upper = ['burger', 'pizza',
                            'maincource']
    item_type_list_lower = ['baverage', 'snack',
                            'Bread']

    for i in item_type_list_upper:
        menu_frames_upper(i)
    for j in item_type_list_lower:
        menu_frames_lower(j)

    root3.mainloop()


menu()
