from tkinter import *
from tkinter import ttk
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software By Irfan")
        bg_color = "maroon"
        title = Label(self.root, text = "Grocery Store",bd=12, relief=GROOVE,bg = bg_color,fg = "Gold", font= ("times new roman",30,"bold"), pady=2).pack(fill=X)

        #===========Variables=============
        #===========Cosmatics=============
        self.soap = IntVar()
        self.bath_combo_val = StringVar()
        self.bath_combo_var = StringVar()

        self.face_cream = IntVar()
        self.fc_combo_var = StringVar()
        self.fc_combo_val = StringVar()

        self.face_wash = IntVar()
        self.fw_combo_var = StringVar()
        self.fw_combo_val = StringVar()

        self.spray=IntVar()
        self.bs_combo_var = StringVar()
        self.bs_combo_val = StringVar()

        self.gel=IntVar()
        self.hg_combo_var = StringVar()
        self.hg_combo_val = StringVar()

        self.lotion=IntVar()
        self.bl_combo_var = StringVar()
        self.bl_combo_val = StringVar()

        
        #===========greocery============
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #=============Cold Drinks========
        self.maza=IntVar()
        self.coke=IntVar()
        self.frooty=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #==============Total Product Price & Tax Variables====
        self.cosmatic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmatic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        self.Total_bill=StringVar()
        #============Customer============
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        #===============Dictionary=======
        self.soap_dict ={'Dettol':'20',
                  'Lux':'30',
                  'Cynthol':'35',
                  'No.1':'20',
                  'Dove':'40',
                  'Santoor':'18',
                  'Pears':'35'
                 }

        self.fc_dict={'Ponds FC':'60',
                      'Fair&Lovly':'55',
                      'Fair&Handsome':'65',
                      'Boroplus':'40',
                       'Gori':'75',
                      'Classic White':'70',
                      'Skinlight':'75'
                     }

        self.fw_dict={'Garnier Men':'65',
                      'Himalaya Neem':'60',
                      'Patanjali FW':'55',
                      'Ponds FW':'50',
                      'Charcol FW':'75',
                      'Nivea FW':'65'
                     }

        self.bs_dict={'Fogg':'180',
                      'Wild Stone':'200',
                      'Yardly London':'220',
                      'AXE':'180',
                      'Engage':'200',
                      'Nivea':'180',
                      'Cynthol BS':'199'
                     }

        self.hg_dict={'Set Wet HG':'30',
                      'Wild Stone HG':'40',
                      'Garnier HG':'25'
                      }

        self.bl_dict={'Vasline':'35',
                      'Boroline':'40',
                      'Olay':'35',
                      'Joy':'25',
                      'Nova':'30'
                    }

        ##==========Customer Detail Frame
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,text = "Customer Details", font=("times new roman", 18,"bold"),fg="gold",bg = bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1, text="Customer Name",bg=bg_color,fg="white", font=("times new roman", 18, "bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone No.",bg=bg_color,fg="white", font=("times new roman", 18, "bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt = Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl = Label(F1, text="Bill no.",bg=bg_color,fg="white", font=("times new roman", 18, "bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt = Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn = Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)


        #========== Costmatics Frame ========
        cosmocolor = "yellow"
        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,text = "Cosmatics", font=("times new roman", 18,"bold"),fg="gold",bg = bg_color)
        F2.place(x=5,y=180,width=325, height=380)

        bath_lbl = Label(F2,text="Bath soap",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt = Entry(F2,width=4,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=2,padx=3,pady=10)

        bath_combo=ttk.Combobox(F2,width=7,font=("times new roman",12,"bold"),textvariable=self.bath_combo_var,
                                 values=['Dettol','Lux','Cynthol','No.1','Dove','Santoor','Pears'])
        bath_combo.grid(row=0,column=1,padx=10,pady=10)
        bath_combo.bind("<<ComboboxSelected>>", self.bathfunc)



        Face_cream_lbl = Label(F2,text="Face Cream",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt = Entry(F2,width=4,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=2,padx=3,pady=10)

        Face_cream_combo = ttk.Combobox(F2, width=7, font=("times new roman", 12, "bold"), textvariable=self.fc_combo_var,
                                  values=['Ponds FC', 'Fair&Lovly', 'Fair&Handsome', 'Boroplus', 'Gori', 'Classic White', 'Skinlight'])
        Face_cream_combo.grid(row=1, column=1, padx=10, pady=10)
        Face_cream_combo.bind("<<ComboboxSelected>>", self.fc_func)



        Face_w_lbl = Label(F2,text="Face Wash",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt = Entry(F2,width=4,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=2,padx=10,pady=10)
        Face_wash_combo = ttk.Combobox(F2, width=7, font=("times new roman", 12, "bold"),textvariable=self.fw_combo_var,
                                        values=['Garnier Men', 'Himalaya Neem', 'Patanjali FW', 'Ponds FW', 'Charcol FW','Nivea FW'])
        Face_wash_combo.grid(row=2, column=1, padx=10, pady=10)
        Face_wash_combo.bind("<<ComboboxSelected>>", self.fw_func)



        Body_s_lbl = Label(F2,text="Body Spray",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Body_s_txt = Entry(F2,width=4,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=2,padx=10,pady=10)
        Body_s_combo = ttk.Combobox(F2, width=7, font=("times new roman", 12, "bold"),textvariable=self.bs_combo_var,
                                       values=['Fogg', 'Wild Stone', 'Yardly London', 'AXE','Engage','Nivea','Cynthol'])
        Body_s_combo.grid(row=3,column=1, padx=10, pady=10)
        Body_s_combo.bind("<<ComboboxSelected>>", self.bs_func)



        Hair_g_lbl = Label(F2,text="Hair Gel",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt = Entry(F2,width=4,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=2,padx=10,pady=10)
        Hair_g_combo = ttk.Combobox(F2, width=7, font=("times new roman", 12, "bold"), textvariable=self.hg_combo_var,
                                    values=['Set Wet HG', 'Wild Stone HG', 'Garnier HG'])
        Hair_g_combo.grid(row=4, column=1, padx=10, pady=10)
        Hair_g_combo.bind("<<ComboboxSelected>>", self.hg_func)


        Body_l_lbl = Label(F2,text="Body Lotion",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_l_txt = Entry(F2,width=4,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=2,padx=10,pady=10)
        Body_l_combo = ttk.Combobox(F2, width=7, font=("times new roman", 12, "bold"), textvariable=self.bl_combo_var,
                                    values=['Vasline', 'Boroline', 'Olay', 'Joy', 'Nova'])
        Body_l_combo.grid(row=5, column=1, padx=10, pady=10)
        Body_l_combo.bind("<<ComboboxSelected>>", self.bl_func)


        #========== Grocery Frame ========
        F3 = LabelFrame(self.root,bd=10,relief=GROOVE,text = "Grocery", font=("times new roman", 18,"bold"),fg="gold",bg = bg_color)
        F3.place(x=335,y=180,width=325, height=380)

        rice_lbl = Label(F3,text="Rice",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt = Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        oil_cream_lbl = Label(F3,text="Food Oil",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        oil_cream_txt = Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Daal_w_lbl = Label(F3,text="Daal",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Daal_w_txt = Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Wheat_lbl = Label(F3,text="Wheat",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Wheat_txt = Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Sugar_lbl = Label(F3,text="Sugar",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Sugar_txt = Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Tea_lbl = Label(F3,text="Tea",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Tea_txt = Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #========== Cold Drink Frame ========
        F4 = LabelFrame(self.root,bd=10,relief=GROOVE,text = "Cold Drinks", font=("times new roman", 18,"bold"),fg="gold",bg = bg_color)
        F4.place(x=665,y=180,width=325, height=380)

        Maza_lbl = Label(F4,text="Maza",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Maza_txt = Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Coke_cream_lbl = Label(F4,text="Coka Cola",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Coke_cream_txt = Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Frooty_lbl = Label(F4,text="Frooty",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Frooty_txt = Entry(F4,width=10,textvariable=self.frooty,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        ThumbsUp_lbl = Label(F4,text="Thumbs Up",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        ThumbsUp_txt = Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Limca_lbl = Label(F4,text="Limca",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Limca_txt = Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Sprite_lbl = Label(F4,text="Sprite",font=("time new roman",15, "bold"),bg=bg_color,fg=cosmocolor).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Sprite_txt = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)



        # ========== Bill Area Frame ========
        F5 =Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000, y=180, width=348, height=380)
        bill_title = Label(F5,text="Bill Area",font=("arial 15 bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #========== Button Frame =======
        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 18, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl=Label(F6,text="Total Cosmatic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmatic_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Cold-Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl = Label(F6,text="Cosmatic Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18,textvariable=self.cosmatic_tax, font=("arial 10 bold"), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font=("arial 10 bold"), bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font=("arial 10 bold"), bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bd=2,bg="maroon",fg="white",pady=15,width=10,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,command=self.bill_area,text="Generate Bill",bd=2,bg="maroon",fg="white",pady=15,width=10,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,command=self.clear_data,text="Clear",bd=2,bg="maroon",fg="white",pady=15,width=10,font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bd=2,bg="maroon",fg="white",pady=15,width=10,font="arial 14 bold").grid(row=0,column=3,padx=5,pady=5)

        self.welcome_bill()


    #=========== Functions========================================
    def bathfunc(self,event):
        self.bath_combo_val=self.bath_combo_var.get()
        print(self.bath_combo_val)

    def fc_func(self,event):
        self.fc_combo_val=self.fc_combo_var.get()
        print(self.fc_combo_val)

    def fw_func(self,event):
        self.fw_combo_val=self.fw_combo_var.get()
        print(self.fw_combo_val)

    def bs_func(self,event):
        self.bs_combo_val=self.bs_combo_var.get()
        print(self.bs_combo_val)

    def hg_func(self,event):
        self.hg_combo_val = self.hg_combo_var.get()
        print(self.hg_combo_val)

    def bl_func(self,event):
        self.bl_combo_val = self.bl_combo_var.get()
        print(self.bl_combo_val)

    #====Total======================
    def total(self):
        #=== Bathsoap Combobox ======
        self.c_s_p=0
        if self.soap.get()!=0:
            for i in self.soap_dict:
                if i==self.bath_combo_val:
                    self.c_s_p=self.soap.get() * int(self.soap_dict[i])

        # === Face cream Combobox ======
        self.c_fc_p=0
        if self.face_cream.get()!=0:
            for j in self.fc_dict:
                if j==self.fc_combo_val:
                   self.c_fc_p=self.face_cream.get() * int(self.fc_dict[j])

        # ====== Face Wash Combobox============
        self.c_fw_p = 0
        if self.face_wash.get() != 0:
            for j in self.fw_dict:
                if j == self.fw_combo_val:
                    self.c_fw_p = self.face_wash.get() * int(self.fw_dict[j])

        # ====== Body Spray Combobox============
        self.c_bs_p = 0
        if self.spray.get() != 0:
            for j in self.bs_dict:
                if j == self.bs_combo_val:
                    self.c_bs_p = self.spray.get() * int(self.bs_dict[j])

        # ====== Hair Gel Combobox============
        self.c_hg_p = 0
        if self.gel.get() != 0:
            for j in self.hg_dict:
                if j == self.hg_combo_val:
                    self.c_hg_p = self.gel.get() * int(self.hg_dict[j])

        # ====== Body Lotion Combobox============
        self.c_bl_p = 0
        if self.lotion.get() != 0:
            for j in self.bl_dict:
                if j == self.bl_combo_val:
                    self.c_bl_p = self.lotion.get() * int(self.bl_dict[j])

        #self.c_fc_p=self.face_cream.get() * 120
        #self.c_fw_p=self.face_wash.get() * 60
        #self.c_bs_p=self.spray.get() * 180
        #self.c_hg_p=self.gel.get() * 140
        #self.c_bl_p=self.lotion.get() * 180

        self.total_cosmatic_price=float(
                                         self.c_s_p +
                                         self.c_fc_p +
                                         self.c_fw_p +
                                         self.c_bs_p +
                                         self.c_hg_p +
                                         self.c_bl_p
                                       )
        self.cosmatic_price.set("Rs. "+str(round((self.total_cosmatic_price),2)))
        self.c_tax=round((self.total_cosmatic_price * 0.05),2)
        self.cosmatic_tax.set("Rs. "+str(self.c_tax))



        self.g_r_p=(self.rice.get() * 60)
        self.g_fo_p=(self.food_oil.get() * 110)
        self.g_d_p=(self.daal.get() *80)
        self.g_w_p=(self.wheat.get() * 240)
        self.g_s_p=(self.sugar.get() * 45)
        self.g_t_p=(self.tea.get() * 150)

        self.total_grocery_price=float(
                                         self.g_r_p+
                                         self.g_fo_p+
                                         self.g_d_p+
                                         self.g_w_p+
                                         self.g_s_p+
                                         self.g_t_p
                                      )
        self.grocery_price.set("Rs. "+str(round((self.total_grocery_price),2)))
        self.g_tax=round((self.total_grocery_price * 0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))



        self.cd_m_p=(self.maza.get() * 60)
        self.cd_c_p=(self.coke.get() * 70)
        self.cd_f_p=(self.frooty.get() * 80)
        self.cd_t_p=(self.thumbsup.get() * 80)
        self.cd_l_p=(self.limca.get() * 75)
        self.cd_s_p=(self.sprite.get() * 75)

        self.total_drink_price = float(
                                         self.cd_m_p+
                                         self.cd_c_p+
                                         self.cd_f_p+
                                         self.cd_t_p+
                                         self.cd_l_p+
                                         self.cd_s_p
                                      )
        self.cold_drink_price.set("Rs. "+str(round((self.total_drink_price),2)))
        self.cd_tax =round((self.total_drink_price * 0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float( self.total_cosmatic_price+
                               self.total_grocery_price+
                               self.total_drink_price+
                               self.c_tax+
                               self.g_tax+
                               self.cd_tax
                              )

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome to Irfan Retail\n")
        self.textarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END, f"\n======================================")
        self.textarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n======================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        elif self.cosmatic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No product purchased")
        else:
            self.welcome_bill()
            #=======Cosmatic===
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n {self.bath_combo_val}\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n {self.fc_combo_val}\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n {self.fw_combo_val}\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n {self.bs_combo_val}\t\t{self.spray.get()}\t\t{self.c_bs_p}")
            if self.gel.get()!=0:
                self.textarea.insert(END,f"\n {self.hg_combo_val}\t\t{self.gel.get()}\t\t{self.c_hg_p}")
            if self.lotion.get()!=0:
                self.textarea.insert(END,f"\n {self.bl_combo_val}\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            # =======Grocery===
            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.rice.get() != 0:
                self.textarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.textarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            if self.sugar.get() != 0:
                self.textarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.textarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
            if self.daal.get() != 0:
                self.textarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")

            # =======Cold Drinks===
            if self.maza.get() != 0:
                self.textarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t\t{self.cd_m_p}")
            if self.thumbsup.get() != 0:
                self.textarea.insert(END, f"\n ThumbsUp\t\t{self.thumbsup.get()}\t\t{self.cd_t_p}")
            if self.frooty.get() != 0:
                self.textarea.insert(END, f"\n Frooty\t\t{self.frooty.get()}\t\t{self.cd_f_p}")
            if self.coke.get() != 0:
                self.textarea.insert(END, f"\n Coka Cola\t\t{self.coke.get()}\t\t{self.cd_c_p}")
            if self.sprite.get() != 0:
                self.textarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.cd_s_p}")
            if self.limca.get() != 0:
                self.textarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.cd_l_p}")

            #==========Taxex Bill
            self.textarea.insert(END, f"\n--------------------------------------")

            if self.cosmatic_tax.get()!='Rs. 0.0':
                self.textarea.insert(END, f"\n Cosmatic Tax\t\t\t{self.cosmatic_tax.get()}")
            if self.grocery_tax.get()!='Rs. 0.0':
                self.textarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!='Rs. 0.0':
                self.textarea.insert(END, f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")


            self.textarea.insert(END,f"\n Total Bill:\t\t\tRs. {self.Total_bill}")
            self.textarea.insert(END, f"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("customer_bill/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no:{self.bill_no.get()} is saved Successfully!")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("customer_bill/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"customer_bill/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"

        if present=="no":
            messagebox.showerror("Error","Invalid Bill no.")

    #=============clearing all Entry fields
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            # ===========Cosmatics=============
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

            # ===========greocery============
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # =============Cold Drinks========
            self.maza.set(0)
            self.coke.set(0)
            self.frooty.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # ==============Total Product Price & Tax Variables====
            self.cosmatic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmatic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ============Customer============
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")

            self.welcome_bill()


    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
root =Tk()

obj= Bill_App(root)
root.mainloop()