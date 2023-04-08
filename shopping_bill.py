from tkinter import *
import json, os
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("billing software")

        #____variable declaration_____________________________________
        self.qty=IntVar()
        self.prev_qty=IntVar()
        self.new_qty=IntVar()
        self.price=IntVar()
        self.new_price=IntVar()        
        self.prev_price=IntVar()
        self.org_price=IntVar()
        self.date=StringVar()
        self.count=0
        self.init_count=1
        self.current_count=0
        self.genFlagError=0
        self.saveClicked=0
        self.stampValue=0
        self.bill_no=IntVar()
        self.generateClicked=IntVar()
        self.buyNowClicked=0
        self.l=[]
        self.autoSave=0
        self.autoclear=0
        self.searchBill=0
        self.subTotal=IntVar()
        self.Total=IntVar()
        self.Discount=IntVar()
        self.ITEMS=StringVar()
        self.date_string=StringVar()
        self.time_string=StringVar() 
        self.custName=StringVar()
        self.custMobile=StringVar()
        self.custEmail=StringVar()

        self.bill_folder_path="C:/Users/ABDULRAUF/Downloads/modern login/"
        self.picture_path="C:/Users/ABDULRAUF/Downloads/modern login/bill_system/"
        self.database_path="C:/Users/ABDULRAUF/Downloads/modern login/bill_system/"

        #______________________First section: (images on top widgets)______________________________________________________________________________________________
        
        # Left Image
        img12=Image.open(self.picture_path+"EngineOil.jpg")
        img12=img12.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img12)

        lb1_12img=Label(self.root,image=self.photoimg)
        lb1_12img.place(x=0,y=0,width=500,height=130)

        # Middle Image
        img_13=Image.open(self.picture_path+"MultipleOil.jpg")
        img_13=img_13.resize((500,130),Image.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_13)

        lbl_13img1=Label(self.root,image=self.photoimg_1)
        lbl_13img1.place(x=500,y=0,width=500,height=130)

        # Right Image
        img_2=Image.open(self.picture_path+"EngineOil.jpg")
        img_2=img_2.resize((520,130),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=1000,y=0,width=520,height=130)

        #_____________________________ Second section:(Enterprice name, data and time widget)_________________________________________________________________________

        lbl_title=Label(self.root,text="ALHAJI OLAWORE ENTERPRISES",font=("times new roman",35,"bold"),bg="blue",fg="white")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        #__________________________Time and Date__________________________________
        def time_show():
            self.time_string=strftime('%H:%M:%S')
            time_lbl.config(text=self.time_string)
            time_lbl.after(1000,time_show)

        time_lbl=Label(lbl_title,font=("times new roman",16,"bold"),bg="blue",fg="white")
        time_lbl.place(x=0,y=0,width=120,height=45)
        time_show()

        def date_show():
            self.date_string=strftime('%x')
            date_lbl.config(text=self.date_string)
            
        date_lbl=Label(lbl_title,font=("times new roman",16,"bold"),bg="blue",fg="white")
        date_lbl.place(x=1410,y=0,width=120,height=45)
        date_show()
        
        # __________________Third section: Main Widgets: (Customer frame, Product frame, Middle picture frame, Bill search and Bill charges frame)__________________________

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)
        
        # __________________ Customer Widgets__________________________________________________

        cust_Frame=LabelFrame(Main_Frame,text="customer",font=("times new roman",12,"bold"),bg="white",fg="blue")
        cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lblcustName=Label(cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name",bd=4)
        self.lblcustName.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.txtcustName=ttk.Entry(cust_Frame,font=("arial",10,"bold"),textvariable=self.custName,width=24)
        self.txtcustName.grid(row=0,column=1,sticky=W,padx=5,pady=2)
      

        self.lbl_mob=Label(cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(cust_Frame,font=("times new roman",10,"bold"),textvariable=self.custMobile,width=24)
        self.entry_mob.grid(row=1,column=1)

        self.lblEmail=Label(cust_Frame,font=("arial",12,"bold"),bg="white", text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(cust_Frame,font=("arial",10,"bold"),textvariable=self.custEmail,width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
          
        #_____________________product labelframe_____________________________________________
        product_Frame=LabelFrame(Main_Frame,text="product",font=("times new roman",12,"bold"),bg="white",fg="blue")
        product_Frame.place(x=370,y=5,width=620,height=140)

        
        self.Database=json.load(open (self.database_path+"Database.json", "r"))#{'oil':[5,10],"brake oil":[1,2],'machine tube':['180*260','175*200']}
        self.Category=list(self.Database.keys())        
        # ____category_____  
        self.lblCategory=Label(product_Frame,font=("arial",12,"bold"),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.combo_Category=ttk.Combobox(product_Frame,font=("arial",10,"bold"),values=self.Category,width=24,state="readonly")
        self.combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_Category.set("select")
        self.combo_Category.bind('<<ComboboxSelected>>',self.Product_name_func)                   
        
        #____Product_Name____
        self.lblProductName=Label(product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lblProductName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.combo_ProductName=ttk.Combobox(product_Frame,font=("arial",10,"bold"),width=24,state="readonly")
        self.combo_ProductName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combo_ProductName.bind('<<ComboboxSelected>>',self.litre_size_func)
        

        # ____litre_size Name____
        self.lbllitre_size=Label(product_Frame,font=("arial",12,"bold"),bg="white",text="Litres",bd=4)
        self.lbllitre_size.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.Combolitre_size=ttk.Combobox(product_Frame,state="readonly",font=("arial",10,"bold"),width=24)
        self.Combolitre_size.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.Combolitre_size.bind('<<ComboboxSelected>>',self.price_func)

        # _______price______
        self.lblprice=Label(product_Frame,font=("arial",12,"bold"),bg="white",text="Price",bd=4)
        self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.Comboprice=ttk.Entry(product_Frame,state="readonly",font=("arial",10,"bold"),textvariable=self.price,width=26)
        self.Comboprice.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        

        # ______Qty_______
        
        self.lblQty=Label(product_Frame,font=("arial",12,"bold"),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(product_Frame,font=("arial",10,"bold"),state="disabled",textvariable=self.qty,width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        self.ComboQty.bind("<Leave>",self.change_price)
        self.ComboQty.bind('<Return>',self.change_price)
     
        # ________Bill search________
        search_Frame=Frame(Main_Frame,bd=2,bg="white")
        search_Frame.place(x=1020,y=15,width=500,height=40)

        self.lblBill=Label(search_Frame,font=("arial",12,"bold"),fg="white",bg="blue",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_search=ttk.Entry(search_Frame,font=("arial",10,"bold"),width=24)
        self.txt_Entry_search.grid(row=0,column=1,sticky=W,padx=2)

        self.Btnsearch=Button(search_Frame,text="Search",font=("arial",10,"bold"),command=self.search_bill,bg="blue",fg="white",width=15,cursor="hand2")
        self.Btnsearch.grid(row=0,column=2)

        #_______midle Frame:(Middle pictures)_____
        Middleframe=Frame(Main_Frame,bd=10)
        Middleframe.place(x=10,y=150,width=980,height=1340)

        # Left Image
        img_14=Image.open(self.picture_path+"MultipleOil.jpg")
        img_14=img_14.resize((490,340),Image.LANCZOS)
        self.photoimg_14=ImageTk.PhotoImage(img_14)

        lbl_14img1=Label(Middleframe,image=self.photoimg_14)
        lbl_14img1.place(x=0,y=0,width=490,height=340)

        # Right Image
        img_15=Image.open(self.picture_path+"EngineOil.jpg")
        img_15=img_15.resize((490,340),Image.LANCZOS)
        self.photoimg_15=ImageTk.PhotoImage(img_15)
        
        lbl_img15=Label(Middleframe,image=self.photoimg_15)
        lbl_img15.place(x=490,y=0,width=500,height=340)

        #________RightFrame Bill Area_________
        RigthlabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="blue")
        RigthlabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y=Scrollbar(RigthlabelFrame,orient=VERTICAL)
        self.textarea=Text(RigthlabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",state="normal",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)  
        self.textarea.pack(fill=BOTH,expand=1)

        
        #____Bill counter labelframe___________
        Bottom_frame=LabelFrame(Main_Frame,text="Bill Counter",font=("time new roman",12,"bold"),bg="white",fg="blue")
        Bottom_frame.place(x=0,y=485,width=20080,height=125)

        self.lbl_text=Label(Bottom_frame,font=("arial",12,"bold"),bg="white",text="Sub_Total",bd=4)
        self.lbl_text.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountsubTotal=ttk.Entry(Bottom_frame,textvariable=self.subTotal,font=("arial",10,"bold"),state="readonly",width=24)
        self.txtAmountsubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_text=Label(Bottom_frame,font=("arial",12,"bold"),bg="white",text="Discount(%)",bd=4)
        self.lbl_text.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.discount=ttk.Entry(Bottom_frame,textvariable=self.Discount,font=("arial",10,"bold"),state="readonly",width=24)
        self.discount.grid(row=1,column=1,sticky=W,padx=5,pady=2) 

        self.lbl_text=Label(Bottom_frame,font=("arial",12,"bold"),bg="white",text="Total",bd=4)
        self.lbl_text.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_frame,textvariable=self.Total,font=("arial",10,"bold"),state="readonly",width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2) 

        
        # ______________________________Button Widgets_____________________________________________
        Btn_frame=Frame(Bottom_frame,bd=2,bg="white")
        Btn_frame.place(x=320,y=0)

        self.BtnAddTocart=Button(Btn_frame,height=2,text="Add To cart",font=("arial",15,"bold"),state="disabled",command=self.Add2Cart,bg="blue",fg="white",width=15,cursor="hand2")
        self.BtnAddTocart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_frame,height=2,text="Generate Bill",font=("arial",15,"bold"),state="disabled",bg="blue",command=self.checkCustInfoThenGenerateBill,fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnClear=Button(Btn_frame,height=2,text="ClearAll",font=("arial",15,"bold"),bg="blue",state="disabled",command=self.autoClearFunc,fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=2)

        self.BtnSave=Button(Btn_frame,height=2,text="Save Bill",font=("arial",15,"bold"),bg="blue",state="disabled",command=self.autoSaveFunc,fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=3)       

        self.BtnBuyNow=Button(Btn_frame,height=2,text="BuyNow",font=("arial",15,"bold"),command=self.buyNow,state="disabled",bg="blue",fg="white",width=15,cursor="hand2")
        self.BtnBuyNow.grid(row=0,column=4)      

        self.BtnExit=Button(Btn_frame,height=2,text="Exit",font=("arial",15,"bold"),bg="blue",fg="white",command=self.Ext,width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.Welcome()

 ###___________________________________Call back function declaration  and Definition____________________________
        
    
    
    def Welcome(self):
        self.textarea.configure(state="normal")
        self.date.set(str(self.date_string))
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome to Alhaji Olawore Enterprises")
        self.textarea.insert(END,f"\n Date: {self.date.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.custName.get()}")
        self.textarea.insert(END,f"\n Phone Number: {self.custMobile.get()}")
        self.textarea.insert(END,f"\n Customer Email: {self.custEmail.get()}")
        self.textarea.insert(END,f"\n==================================================")
        self.textarea.insert(END,f"\n  Product\t\tLitres\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n==================================================")
        self.textarea.configure(state="disabled")
    
  
    
    def Product_name_func(self,e):
        self.BtnAddTocart.configure(state="active")
        self.ComboQty.configure(state="active")
        for i in self.Category:
            selected_category=self.combo_Category.get()
            if selected_category ==i:               
               self.combo_ProductName.config(value=list((self.Database.get(i)).keys()))
               self.combo_ProductName.set("select")
               self.Combolitre_size.set("")
               self.price.set(0)
               self.qty.set(0)
               break
   
    
    
    def litre_size_func(self,e):
        selected_productname=self.combo_ProductName.get()
        self.Combolitre_size.config(value=list((self.Database.get(self.combo_Category.get()))[selected_productname].keys()))
        self.Combolitre_size.set("select")
        self.price.set(0)
        self.qty.set(0)
        self.prev_qty=int(self.ComboQty.get())
        self.prev_price=int(self.Comboprice.get())
        

    def price_func(self,e):
        selected_litre_size=self.Combolitre_size.get()
        self.price.set(((self.Database.get(self.combo_Category.get()))[self.combo_ProductName.get()][selected_litre_size][1]))
        self.qty.set(1)
        self.org_price=int(self.Comboprice.get())
    

    def change_price(self,e):
        self.new_qty=int(self.ComboQty.get())
        self.ProductName_status=StringVar()
        self.litre_sizesel_status=StringVar()
        self.ProductName_status=self.combo_ProductName.get()
        self.litre_sizesel_status=self.Combolitre_size.get()
        print(self.prev_qty)
        if self.ProductName_status !="select" or self.litre_sizesel_status !="select":
            if self.new_qty !=self.prev_qty:
                self.new_price=int(self.ComboQty.get())* self.org_price
                self.price.set("")
                self.price.set(self.new_price)
                print(self.new_qty)
            else:
                self.price.set("")
                self.price.set(self.prev_price)
                print(self.new_price)
        else:
            self.prev_price.set(0)
            self.new_price.set(0)
            self.price.set("")
            self.price.set(0)
        self.prev_qty=self.new_qty
        self.prev_price=self.new_price
        print(self.org_price)
        print(self.Combolitre_size.get())

        
    def Add2Cart(self):
        self.BtnClear.configure(state='active')
        if self.searchBill==1:
            self.autoClearFunc()
            self.searchBill=0
            self.autoclear=0
        else:
        
            if self.Combolitre_size.get()=="select" or self.combo_ProductName.get()=="select":
                messagebox.showerror("ERROR","Your selection is not complete")
        
            else:
                if self.generateClicked.get()==0:
                    self.l.append(int(self.Comboprice.get()))
                    print(self.l)
                    self.Btngenerate_bill.configure(state="active")
                    self.textarea.configure(state="normal")
                    self.textarea.insert(END,f"\n{self.combo_ProductName.get()}\t\t  {self.Combolitre_size.get()}\t\t  {self.ComboQty.get()}\t\t{self.Comboprice.get()}")
                    self.textarea.configure(state="disabled")
                    self.subTotal.set(sum(self.l))
                    self.Total.set(sum(self.l))
                    
                elif self.buyNowClicked==1:
                    choosen_option=messagebox.askquestion("New Purchase","Start new purchase?")
                    if choosen_option=="yes": 
                        self.Welcome()
                        self.l=[]
                        self.subTotal.set("")
                        self.Total.set("")
                        self.Discount.set("")
                        self.buyNowClicked=0
                        self.saveClicked=0
                        self.stampValue=0
                        self.BtnSave.configure(state="disabled")
                        self.BtnBuyNow.configure(state="disabled")
                        self.BtnClear.configure(state="disabled")
                        self.combo_Category.set("select")
                        self.combo_ProductName.set("select")
                        self.Combolitre_size.set("select")
                        self.qty.set(0)
                        self.price.set(0)
                        self.generateClicked.set(0)                   
                else:
                    self.update_bill()
                    print(type(self.ITEMS))
                

   
    def checkCustInfoThenGenerateBill(self):
        if self.custName.get()=="":
            messagebox.showerror("ERROR","Fill Customer Name")
            self.genFlagError= 1
        elif self.custMobile.get()=="":
            messagebox.showerror("ERROR","Fill Customer Mobile number")
            self.genFlagError= 1             
        elif self.custEmail.get()=="":
            messagebox.showerror("ERROR","Fill Customer Email")
            self.genFlagError= 1
        else:
            try:
                float(self.entry_mob.get())
                self.Generate_Bill()
                self.genFlagError= 0
            except ValueError:
                messagebox.showerror("ERROR","Mobile input must be number") 
                self.genFlagError= 1
                
                

    def Generate_Bill(self):
        self.BtnBuyNow.configure(state="active")
        if self.Comboprice.get()=="0" or self.combo_ProductName.get()=="select":
            messagebox.showerror("ERROR","Please Add to Cart first")
        else:
            if  self.generateClicked.get()==0:
                self.ITEMS=self.textarea.get(9.0,"end")
                self.Welcome()
                print(self.ITEMS)
                self.textarea.configure(state="normal")            
                self.textarea.insert(END,f"\n{self.ITEMS}")            
                self.textarea.insert(END,f"\n==================================================")
                self.textarea.insert(END,f"\n Total:\t\t\t\t\t  {self.Total.get()}")
                self.textarea.insert(END,f"\n==================================================")
                self.textarea.configure(state="disabled")
                self.BtnSave.configure(state="active")
                self.generateClicked.set(1)
                print("y0u")
                
            else:
                self.textarea.configure(state="normal")
               
                self.textarea.delete(3.15,'3.16 lineend')
                self.textarea.insert(3.15,f" {self.txtcustName.get()}")
                self.textarea.delete(4.14,'4.16 lineend')
                self.textarea.insert(4.14,f" { self.entry_mob.get()}")
                self.textarea.delete(5.16,'5.16 lineend')
                self.textarea.insert(5.16,f" {self.txtEmail.get()}")
                self.textarea.configure(state="disabled")
                print("y0uuuu")
           
            

    def update_bill(self):
        
        self.textarea.configure(state="normal")
        self.textarea.delete("end-4l",END)
        self.generateClicked.set(0)
        self.saveClicked=0
        self.Add2Cart()       
        self.textarea.configure(state="disabled")
        print(self.generateClicked.get())
       

    def autoSaveFunc(self):
        if self.autoSave==1:
           self.Save_choosen_option=1
           self.stampValue=3
           self.Save_Bill()
           
        else:
            self.Save_choosen_option=messagebox.askyesno("Save Bill","Do you want to save bill?")
            self.stampValue=1
            self.Save_Bill()
            

       
    def Save_Bill(self):
            if self.Save_choosen_option==1 and self.saveClicked==0:
                self.checkCustInfoThenGenerateBill()
                print(self.genFlagError)
                print(self.saveClicked)
                if self.genFlagError==0 and self.saveClicked==0:
                    
                    self.count+=1
                    
                    self.stamp()
                    self.saveClicked=1 
                    self.textarea.configure(state="disabled")            
                    self.bill_data=self.textarea.get(1.0,END)
                    folder_name="test"
                    file_name='Bill_'+str(self.bill_no.get())+".txt"
                    dir_path=self.bill_folder_path+folder_name
                    file_path=os.path.join(dir_path,file_name)
                    if os.path.exists(dir_path):
                        with open(file_path,'w') as f1:
                            f1.write(self.bill_data)
                            messagebox.showinfo("Saved",f"Bill_ {self.bill_no.get()} saved successfully")
                            
                    else:
                         
                        self.stamp()
                        self.saveClicked=1
                        os.mkdir(folder_name)
                        os.chdir(f"{self.bill_folder_path}{folder_name}")
                        with open(file_path,'w') as f1:
                            f1.write(self.bill_data)
                            messagebox.showinfo("Saved",f"Bill_ {self.bill_no.get()} saved successfully")
                            

            elif self.Save_choosen_option==1 and self.saveClicked==1:
                self.checkCustInfoThenGenerateBill()
                if self.genFlagError==0:
                    self.current_count=self.count
                    self.buyNowClicked=0
                    self.stamp()         
                    self.bill_data=self.textarea.get(1.0,END)
                    folder_name="test"
                    file_name='Bill_'+str(self.bill_no.get())+".txt"
                    dir_path=self.bill_folder_path+folder_name
                    file_path=os.path.join(dir_path,file_name)
                    with open(file_path,'w') as f1:
                            f1.write(self.bill_data)
                            messagebox.showinfo("Override bill",f"Info updated on saved bill")
                            
                            
                           
                else:
                    messagebox.showerror("Update failed",f"Bill NOT updated, Input reqiured Customer info")
            elif self.Save_choosen_option==1 and self.search_bill==1:
                print("yessssss")
                
            else:
                messagebox.askokcancel("Mandatory","Bill must be saved") 
            
        

    def buyNow(self):   
        self.init_count=self.count+1    
        self.Discount.set(float(0))
        self.Total.set(self.total())
        self.BtnClear.configure(state="disabled")
        self.Btngenerate_bill.configure(state="disabled")
        self.BtnSave.configure(state="disabled")
        if self.buyNowClicked==0 and self.saveClicked==0:
            if self.Discount.get()!=0 and self.generateClicked.get()!=0:
                self.discountTotal()
                print("A")
                self.autoSave=1
                self.autoSaveFunc()
                self.autoSave=0
                messagebox.showinfo("Transaction complete", "Purchase Successful")
            else:
                self.autoSave=1
                self.autoSaveFunc()
                print("B")
                self.autoSave=0
                messagebox.showinfo("Transaction complete", "Purchase Successful")
            self.buyNowClicked=1
        elif self.buyNowClicked==0 and self.saveClicked==1:
            if self.Discount.get()!=0 and self.generateClicked.get()!=0:
                self.discountTotal()
                self.autoSave=1
                self.autoSaveFunc()
                self.autoSave=0
                print("C")
                messagebox.showinfo("Transaction complete", "Purchase Successful")
            else:
                messagebox.showinfo("Transaction complete", "Purchase Successful")
                self.autoSave=1
                self.autoSaveFunc()
                self.autoSave=0
                print("cc")
            self.buyNowClicked=1
        elif self.buyNowClicked==2 and self.saveClicked==1:
                self.buySaved()
                print("hi")
        else:
            print("D")
            choosen_option=messagebox.askquestion("Repeat Order","You are about to repeat Order")
            if choosen_option=="yes" and self.Discount.get()!=0:
                self.saveClicked=0
                self.discountTotal()
                self.textarea.configure(state="normal") 
                self.textarea.delete(2.15,'2.16 lineend')
                self.textarea.configure(state="disabled")
                self.autoSave=1
                self.autoSaveFunc()
                self.autoSave=0
                messagebox.showinfo("Transaction complete", "Purchase Successful")                 
            elif choosen_option=="yes" and self.Discount.get()==0:
                messagebox.showinfo("Transaction complete", "Purchase Successful")
                self.saveClicked=0
                # self.stamp()
                self.autoSave=1
                self.autoSaveFunc()
                self.autoSave=0
            else:
                self.saveClicked==1
        
                
        

    def total(self):
         total=float(self.txtAmountsubTotal.get())
         dis= float(self.discount.get())/100
         total=(total-(dis*total))
         return total


    def discountTotal(self):
        if self.buyNowClicked==0:
            self.textarea.configure(state="normal")
            self.textarea.delete("end-4l",END)
            self.textarea.insert(END,f"\n==================================================")
            self.textarea.insert(END,f"\n Subtotal:\t\t\t\t\t  {self.subTotal.get()}")
            self.textarea.insert(END,f"\n Discount:\t\t\t\t\t  {self.Discount.get()}%")
            self.textarea.insert(END,f"\n Total:\t\t\t\t\t  {self.Total.get()}")
            self.textarea.insert(END,f"\n==================================================")
            self.textarea.configure(state="disabled")



    def search_bill(self):
        folder_name="test"
        dir_path=self.bill_folder_path+folder_name
        if os.path.exists(dir_path):
            found="no"
            Bill_format="Bill_"+self.txt_Entry_search.get()
            for lookfor in os.listdir(dir_path):
                if lookfor.split('.')[0]==Bill_format:
                    file_no=Bill_format+'.txt'
                    file_path=dir_path+"/"+file_no
                    print(file_path)
                    f1=open(file_path,"r")
                    self.textarea.configure(state="normal")
                    self.textarea.delete(1.0,END)
                    for data in f1:
                        self.textarea.insert(END,data)
                    self.textarea.configure(state="disabled")
                    f1.close()
                    found="yes"
                    self.searchBill=1
                    self.autoclear=1
                    self.BtnBuyNow.configure(state="normal")
                    self.BtnSave.configure(state="disabled")
                    self.saveClicked=1
                    self.buyNowClicked=2
            if found=="no":
                messagebox.showerror("ERROR","Invalid Bill Number")
            self.BtnAddTocart.configure(state="disabled")
            self.Btngenerate_bill.configure(state="disabled")
            self.BtnClear.configure(state="disabled")
            
          
        else:
            messagebox.showerror("ERROR",f"No such folder: {dir_path} ")
        

    def autoClearFunc(self):
        if self.autoclear==1:
           self.clear_choosen_option="yes"
           self.clearAll()
        else:
            self.clear_choosen_option=messagebox.showwarning("AboutToClear","You ar about to clearAll items Add to Cart")
            self.clear_choosen_option=messagebox.askquestion("ClearAll","Sure to clear all items Added to Cart?")
            self.clearAll()

    def clearAll(self):
        if self.clear_choosen_option=="yes": 
            self.generateClicked.set(0)
            self.l=[]
            self.subTotal.set("")
            self.Total.set("")
            self.Discount.set("")
            self.Welcome()
            self.Btngenerate_bill.configure(state="disabled")
            self.BtnSave.configure(state="disabled")
            self.BtnBuyNow.configure(state="disabled")
    

    def stamp(self):
        self.textarea.configure(state="normal")
        # self.count+=1
        if self.searchBill==1:
            self.count=int(self.txt_Entry_search.get())
            print("E")
        elif self.searchBill==1 and self.buyNowClicked==1:
            self.count=self.current_count
            print("F")
        print("G")
        print(self.count)
        print(self.current_count)
        print(self.init_count)
        self.bill_no.set(self.count)
       
        self.textarea.delete(2.15,'2.16 lineend')
        self.textarea.insert(2.41,f"\t\t\t\t\tBill_no: {self.bill_no.get()}/{self.time_string}")
        if  self.saveClicked==0 and self.stampValue==1:
            self.textarea.insert(END,"\t\t\t\t\t\n  SAVED ")
            
        elif  self.buyNowClicked==0 and self.stampValue==3:
              self.textarea.insert(END,f"\t\t\t\t\t\n  PURCHASED ")

        elif self.saveClicked==1 and self.stampValue==1:
             self.textarea.delete('end-1l','end-1l lineend')
             self.textarea.insert(INSERT,"  SAVED ")

        elif  self.buyNowClicked==1 and self.stampValue==3:
               self.textarea.delete('end-1l','end-1l lineend')
               self.textarea.insert(END,f"  PURCHASED ")
        self.textarea.configure(state="disabled")
        
    
    def buySaved(self):
        self.textarea.configure(state="normal") 
        self.textarea.delete(2.6,'2.16 lineend')
        self.textarea.insert(2.7,f" {self.date.get()}")
        self.textarea.configure(state="disabled")
        self.stamp()
        print("H")
        self.buyNowClicked=1
        self.saveClicked=1
        messagebox.showinfo("Transaction complete", "Purchase Successful")


    def Ext(self):
        choosen_option=messagebox.askquestion("Exiting","Are you sure you want to EXIT?")
        if choosen_option=="yes": 
            self.root.destroy()
        else:
            pass


        

if __name__ == "__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()