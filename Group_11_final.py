import tkinter as tk
from tkinter import ttk
import pymysql
from datetime import datetime
from datetime import date, timedelta


LARGEFONT = ("Raleway", 35)
SMALLFONT = ("Raleway", 12)

conn = pymysql.connect(host='localhost',
                        user='root',
                        password = "password",
                        db='Library',)
cur = conn.cursor()

class Store_info(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Store_info, cls).__new__(cls)
            cls.instance.initialized=False
        return cls.instance
#change and access thru method
#has information of its own data that the other class need to use

    def __init__(self):
        if (self.initialized):
            return
        self.member_create_id = ""
        self.book_search = ()
        self.initialized=True
        
    def create_username(self,x):
        self.member_create_id = x
        
    def get_username(self):
        return self.member_create_id
    
    def create_book_search(self,x):
        self.book_search = x
        
    def get_book_search(self):
        return self.book_search
        
########################################################################
###################        Mother of all class            ##############
########################################################################


####################MEMBERSHIP###################################################################################################
#MembershipMenuFrame,
#CreationFrame,SuccessCreationFrame,ErrorCreationFrame,
#MemberDeletionFrame,DeletionCfmFrame,SuccessDeletionFrame,ErrorDeletionFrame,
#UpdateMemberInputIDFrame,UpdateInfoFrame,ConfirmationFrame,SuccessUpdateFrame,ErrorUpdateFrame

####################BOOKS#######################################################################################################
#BookMenuFrame,
#BookAcqFrame,BookAcqSuccessFrame,BookAcqFailFrame,
#BookWithdrawFrame,BookWithdrawCfmFrame,
#BookWithdrawSuccessFrame,BookWithdrawFailLoanReservedFrame, BookWithdrawFailLoanFrame, BookWithdrawFailReservedFrame, BookWithdrawFailMissingFrame

####################LOANS#######################################################################################################
#LoanMenuFrame,BookBorrowFrame,BookLoanMissingDetails,BorrowFailNoMemberOrBook,BorrowFailFineFrame,LoanTwoBooks,ErrorReservedBySb,BkOnLoanUntilFrame,BorrowCfmFrame,BorrowSuccessFrame
#BookReturnFrame,NoSuchLoanFrame,ReturnCfmFrame,FineIncurredFrame,ReturnSuccessFrame

####################RESERVATION#################################################################################################
#ReservationMenuFrame
#BookReservationFrame,WrongDetailsForResFrame,ConfirmationReservationFrame,SuccessReservationFrame,ErrorTwoReservationFrame,ErrorOutstandingFineFrame,BookIsReservedFrame
#CancelReservationFrame,ConfirmationCancellationFrame,SuccessReservationCancellationFrame,NoSuchReservationFrame,CannotCancel

####################FINES#######################################################################################################
#FineMenuFrame,FinePaymentFrame,NoSuchPersonInFinesFrame,FailNoFineFrame,FailWrongAmountFrame,PaymentCfmFrame,PaymentSuccessFrame

####################REPORTS#####################################################################################################
#ReportsMenuFrame,SearchBookFrame,ErrorOneValueOnlySearchFrame,SearchBookBorrowedByMem


class LibraryApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        
        for F in (MainMenuFrame, MembershipMenuFrame, CreationFrame, SuccessCreationFrame, ErrorCreationFrame, MemberDeletionFrame, DeletionCfmFrame, SuccessDeletionFrame, ErrorDeletionFrame, UpdateMemberInputIDFrame, UpdateInfoFrame, ConfirmationFrame, SuccessUpdateFrame, ErrorUpdateFrame,BookMenuFrame,BookAcqFrame,BookAcqSuccessFrame,BookAcqFailFrame,BookWithdrawFrame,BookWithdrawCfmFrame,BookWithdrawSuccessFrame,BookWithdrawFailLoanReservedFrame,BookWithdrawFailLoanFrame,BookWithdrawFailReservedFrame, BookWithdrawFailMissingFrame,FineMenuFrame,FinePaymentFrame,NoSuchPersonInFinesFrame,FailNoFineFrame,FailWrongAmountFrame,PaymentCfmFrame,PaymentSuccessFrame, ReservationMenuFrame,WrongDetailsForResFrame,BookReservationFrame,ConfirmationReservationFrame,SuccessReservationFrame,BookIsReservedFrame,ErrorTwoReservationFrame,ErrorOutstandingFineFrame,CancelReservationFrame,ConfirmationCancellationFrame,SuccessReservationCancellationFrame,NoSuchReservationFrame,CannotCancel,LoanMenuFrame,BookBorrowFrame,BookLoanMissingDetails,BorrowFailNoMemberOrBook,BorrowFailFineFrame,LoanTwoBooks,ErrorReservedBySb,BkOnLoanUntilFrame,BorrowCfmFrame,BorrowSuccessFrame,BookReturnFrame,NoSuchLoanFrame,ReturnCfmFrame,FineIncurredFrame,ReturnSuccessFrame,ReportsMenuFrame,SearchBookFrame,ErrorOneValueOnlySearchFrame,SearchBookBorrowedByMem):
        
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(MainMenuFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.refresh()
        
    def get_page(self, page_class):
        return self.frames[page_class]
        
########################################################################
###################        Main Menu Page                 ##############
########################################################################
  
class MainMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 5)
            
        membership_button = ttk.Button(self, text =" Membership", command = lambda : controller.show_frame(MembershipMenuFrame))
        
        membership_button.grid(row = 1, column = 1)
        
        books_button = ttk.Button(self, text =" Book ", command = lambda : controller.show_frame(BookMenuFrame))
        books_button.grid(row = 1, column = 2)
        
        loans_button = ttk.Button(self, text =" Loans ", command = lambda : controller.show_frame(LoanMenuFrame))
        loans_button.grid(row = 1, column = 3)
        
        reservation_button = ttk.Button(self, text =" Reservation ", command = lambda : controller.show_frame(ReservationMenuFrame))
        reservation_button.grid(row = 2, column = 1)

        fine_button = ttk.Button(self, text =" Fines ", command = lambda :controller.show_frame(FineMenuFrame))
        fine_button.grid(row = 2, column = 2)
        
        report_button = ttk.Button(self, text =" Reports ", command = lambda : controller.show_frame(ReportsMenuFrame))
        report_button.grid(row = 2, column = 3)
        
    def refresh(self):
        pass
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

########################################################################
###################        Membership Frames              ##############
########################################################################
#13 Frames
#MembershipMenuFrame,
#CreationFrame,SuccessCreationFrame,ErrorCreationFrame
#MemberDeletionFrame,DeletionCfmFrame,SuccessDeletionFrame,ErrorDeletionFrame,
#UpdateMemberInputIDFrame,UpdateInfoFrame,ConfirmationFrame,SuccessUpdateFrame,ErrorUpdateFrame

# first frame Membership Menu
class MembershipMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 5)
        label = ttk.Label(self, text ="Select one of the Options below:", font = LARGEFONT)
        label.grid(row = 0, column = 2)
        
        member_creation = ttk.Button(self, text ="Membership Creation",
                            command = lambda : controller.show_frame(CreationFrame))
        member_creation.grid(row = 1, column = 2)
        
        member_deletion = ttk.Button(self, text ="Membership Deletion",
                            command = lambda : controller.show_frame(MemberDeletionFrame))
        member_deletion.grid(row = 2, column = 2)
        
        member_update = ttk.Button(self, text ="Membership Update",
                            command = lambda : controller.show_frame(UpdateMemberInputIDFrame))
        member_update.grid(row = 3, column = 2)
            
        main_menu_btn = ttk.Button(self, text ="Back To Main Menu",
                                    command = lambda : controller.show_frame(MainMenuFrame))
     
        main_menu_btn.grid(row = 4, column = 2)
        
    def refresh(self):
        pass
  
  
# second window frame creation page
class CreationFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        MembershipID = tk.StringVar()
        Name = tk.StringVar()
        Faculty = tk.StringVar()
        PhoneNum = tk.StringVar()
        EmailAdd = tk.StringVar()
        
        label0 = ttk.Label(self, text='To Create Member, Please Enter Requested Information Below', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Membership ID:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)
        textbox1 = ttk.Entry(self, textvariable = MembershipID, font = SMALLFONT)
        textbox1.grid(row = 2, column = 2)
        
        label2 = ttk.Label(self, text="Name:", font = SMALLFONT)
        label2.grid(row = 3, column = 1)
        textbox2 = ttk.Entry(self,textvariable = Name, font = SMALLFONT)
        textbox2.grid(row = 3, column = 2)
        
        label3 = ttk.Label(self, text="Faculty:", font = SMALLFONT)
        label3.grid(row = 4, column = 1)
        textbox3 = ttk.Entry(self, textvariable = Faculty, font = SMALLFONT)
        textbox3.grid(row = 4, column = 2)
        
        label4 = ttk.Label(self, text="Phone Number:", font = SMALLFONT)
        label4.grid(row = 5, column = 1)
        textbox4 = ttk.Entry(self, textvariable = PhoneNum, font = SMALLFONT)
        textbox4.grid(row = 5, column = 2)
        
        label5 = ttk.Label(self, text="Email Address:", font = SMALLFONT)
        label5.grid(row = 6, column = 1)
        textbox5 = ttk.Entry(self, textvariable= EmailAdd ,font = SMALLFONT)
        textbox5.grid(row = 6, column = 2)
        
        creation_member_btn = ttk.Button(self, text ="Create Member",
                            command = lambda : check_if_can_create_member(), width = 20)
     
        creation_member_btn.grid(row = 9, column = 1)
        
        main_menu_btn = ttk.Button(self, text ="Back To Main Menu", width = 20, command = lambda : controller.show_frame(MainMenuFrame))
                            
        main_menu_btn.grid(row = 9, column = 3)
        
        # Need to connect to SQL to check
        def check_if_can_create_member():
            flag = True
            cur.execute("select * from Member")
            output = cur.fetchall()
            #we create our own member
            global getMemberID
            getMemberID = MembershipID.get()
            MembershipID.set("")
            global getName
            getName = Name.get()
            Name.set("")
            global getFaculty
            getFaculty = Faculty.get()
            Faculty.set("")
            global getPhoneNum
            getPhoneNum = PhoneNum.get()
            PhoneNum.set("")
            global getEmailAddress
            getEmailAddress = EmailAdd.get()
            EmailAdd.set("")
            
            created_member = (getMemberID, getName, getFaculty, getPhoneNum, getEmailAddress)
            
            #two condition to check
            
            #condition 1 (Not empty/Incomplete)
            
            for element in created_member:
                if element:
                    continue
                else:
                    flag = False
                    break
            
            #condition 2 (Member already exists,same membership ID)
            for member in output:
                if created_member[0] == member[0]:
                    flag = False
                    break
                    
            if flag == False:
                return controller.show_frame(ErrorCreationFrame)
            #need to send info over to sql
            sql = "INSERT INTO Member (ID, Name, Faculty, PhoneNumber, Email) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql,created_member)
            conn.commit()
            return controller.show_frame(SuccessCreationFrame)
            
    def refresh(self):
        pass

# third window frame success
class SuccessCreationFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)
        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))
        canvas.create_text(450, 300, text="ALS Membership created", fill="black", font=("RALEWAY", 25))
        btn = ttk.Button(self, text='Return to Create function',command = lambda : controller.show_frame(CreationFrame))
        btn.place(x=350,y=500)
    def refresh(self):
        pass

# fourth window frame error

class ErrorCreationFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Member already exists; missing\nor incomplete fields.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Create function',command = lambda : controller.show_frame(CreationFrame))
        btn.place(x=350,y=500)
    def refresh(self):
        pass

# fifth window frame delete
class MemberDeletionFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 5)
        
        MembershipID = tk.StringVar()
        
        label0 = ttk.Label(self, text='To Delete Member, Please Enter Membership ID:',)
        label0.grid(row = 0, column = 2)
        
        label1 = ttk.Label(self, text='Membership ID:', font = SMALLFONT)
        label1.grid(row = 2, column = 1)
        textbox1 = ttk.Entry(self, textvariable = MembershipID, font = SMALLFONT)
        textbox1.grid(row = 2, column = 2)
        
        def extract_info_from_id():
            cur.execute("select * from Member")
            output = cur.fetchall()
            global getMemberID
            global extract_member
            extract_member = ()
            getMemberID = MembershipID.get()
            MembershipID.set("")
            if getMemberID == "":
                return
            for member in output:
                if member[0] == getMemberID:
                    extract_member = member
            if extract_member:
                return controller.show_frame(DeletionCfmFrame)
            
        
        deletion_member_btn = ttk.Button(self, text ="Delete Member",
                            command = lambda : extract_info_from_id() , width = 20)
     
        # putting the button in its place by
        # using grid
        deletion_member_btn.grid(row = 4, column = 1)
        
        membership_menu_button = ttk.Button(self, text ="Back to Membership Menu ",
                            command = lambda : controller.show_frame(MembershipMenuFrame), width = 20)
  
        membership_menu_button.grid(row = 4, column = 3)
        
    
    def refresh(self):
        pass
    
# fifth window frame DeletionCfmFrame
class DeletionCfmFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(columnspan = 5, rowspan = 10)

        self.labeltext = ttk.Label(self, text = "Please confirm details\nto be correct " , font = LARGEFONT)
        self.labeltext.grid(row = 1, column = 2)
        
        self.label0 = ttk.Label(self, text="Member ID", font = SMALLFONT,)
        self.label0.grid(row = 2, column = 1)
        
        self.label1 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label1.grid(row = 2, column = 2)
        
        self.label2 = ttk.Label(self, text="Name", font = SMALLFONT,)
        self.label2.grid(row = 3, column = 1)
        
        self.label3 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label3.grid(row = 3, column = 2)
        
        self.label4 = ttk.Label(self, text= "Faculty", font = SMALLFONT,)
        self.label4.grid(row = 4, column = 1)
        
        self.label5 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label5.grid(row = 4, column = 2)
        
        self.label6 = ttk.Label(self, text="Phone Number", font = SMALLFONT,)
        self.label6.grid(row = 5, column = 1)
        
        self.label7 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label7.grid(row = 5, column = 2)
        
        self.label8 = ttk.Label(self, text= "Email Address", font = SMALLFONT,)
        self.label8.grid(row = 6, column = 1)
        
        self.label9 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label9.grid(row = 6, column = 2)
        

        btn1 = ttk.Button(self, text='Return to Delete function',command = lambda : controller.show_frame(MemberDeletionFrame))
        btn1.place(x=550,y=550)
        

        btn2 = ttk.Button(self, text='Confirm deletion',command = lambda : check_if_can_delete_member())
        btn2.place(x=50,y=550)
        

        
        def check_if_can_delete_member() :
            flag1,flag2,flag3 = True,True,False
            #global bkkk_acc
            #cur.execute("select * from BookUpdated")
            #resbksss = cur.fetchall()
            #for ele in resbksss:
                #if ele[13] == extract_member[0]:
                    #bkkk_acc = ()
                    #bkkk_acc = ele[0]
                    #flag3 = True
                        
            
            #Check if got loan
            cur.execute("select * from BookUpdated")
            all_bkssssss = cur.fetchall()
            for elee in all_bkssssss:
                if elee[12] == extract_member[0]:

                    flag1 = False
            
            #Check if got fines
            cur.execute("select * from Fine")
            output = cur.fetchall()
            for member_fine in output:
                if member_fine[0] == extract_member[0]:
                    if int(member_fine[1]) > 0:
                        flag2 = False
                        
            if flag1 and flag2 == True:
                sql = "DELETE FROM Member WHERE ID = %s"
                x = extract_member[0]
                cur.execute(sql,x)
                conn.commit()
                #if got any reserved book
                #if flag3:
                    #sql = "UPDATE bookupdated SET MemberReserveID = %s WHERE AccessionNumber = %s"
                    #val = (None, bkkk_acc)
                    #cur.execute(sql,val)
                    #conn.commit()
                        
                return controller.show_frame(SuccessDeletionFrame)
            if flag1 == False or flag2 == False:
                return controller.show_frame(ErrorDeletionFrame)
                
    def refresh(self):
        self.label1.config(text = extract_member[0])
        self.label3.config(text = extract_member[1])
        self.label5.config(text = extract_member[2])
        self.label7.config(text = extract_member[3])
        self.label9.config(text = extract_member[4])
        

# sixth window frame success
class SuccessDeletionFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Member successfully deleted.", fill="black", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Delete function',command = lambda : controller.show_frame(MemberDeletionFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        pass

# seventh window frame error
class ErrorDeletionFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Member has loans,\nreservations or outstanding fines.", fill="yellow", font=("RALEWAY", 25))
        btn = ttk.Button(self, text='Return to Delete function',command = lambda : controller.show_frame(MemberDeletionFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        pass

# eighth window frame update and input ID
class UpdateMemberInputIDFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        self.UserInfo = Store_info()
        MembershipID = tk.StringVar()
        
        label0 = ttk.Label(self, text='To Update A Member, Please Enter Membership ID:',)
        label0.grid(row = 0, column = 2)
        
        label1 = ttk.Label(self, text='Membership ID:', font = SMALLFONT)
        label1.grid(row = 5, column = 1)

        self.textbox1 = ttk.Entry(self, textvariable = MembershipID, font = SMALLFONT)
        self.textbox1.grid(row = 5, column = 2)
 
        #get text variable and send to next frame
                
        def send_info_to_updateinfo_frame(MembershipID):
            #send the username
            global extract_member_for_update
            flag = False
            self.UserInfo.create_username(MembershipID.get())
            MembershipID.set("")
            x = self.UserInfo.get_username()
            if x:
                cur.execute("select * from Member")
                output = cur.fetchall()
                for member in output:
                    if x == member[0]:
                        extract_member_for_update = member
                        flag = True
                        break
            if flag:
                return controller.show_frame(UpdateInfoFrame)
            else:
                return
        update_member_btn = ttk.Button(self, text ="Update Member",
                            command = lambda : send_info_to_updateinfo_frame(MembershipID) , width = 20)
     
        # putting the button in its place by
        # using grid
        update_member_btn.grid(row = 9, column = 1)
        
        return_membership_menu_button = ttk.Button(self, text ="Back to Membership Menu ",
                            command = lambda : controller.show_frame(MembershipMenuFrame), width = 20)

        return_membership_menu_button.grid(row = 9, column = 3)
    def refresh(self):
        pass
        
           


# ninth window frame update and input ID
class UpdateInfoFrame(tk.Frame):
    def __init__(self, parent, controller):
    
        self.controller = controller
        self.UserInfo = Store_info()
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
       
        MembershipID = tk.StringVar()
        Name = tk.StringVar()
        Faculty = tk.StringVar()
        PhoneNum = tk.StringVar()
        EmailAdd = tk.StringVar()
        
        self.labeltext = ttk.Label(self, text = "Please Enter Requested Information Below: " , font = SMALLFONT)
        self.labeltext.grid(row = 1, column = 2)
        
        self.label0 = ttk.Label(self, text="Membership ID", font = SMALLFONT,)
        self.label0.grid(row = 2, column = 1)
        
        self.label1 = ttk.Label(self, text = self.UserInfo.get_username() , font = SMALLFONT)
        self.label1.grid(row = 2, column = 2)
        
        self.label2 = ttk.Label(self, text="Name:", font = SMALLFONT)
        self.label2.grid(row = 3, column = 1)
        self.textbox2 = ttk.Entry(self,textvariable = Name, font = SMALLFONT)
        self.textbox2.grid(row = 3, column = 2)
        
        self.label3 = ttk.Label(self, text="Faculty:", font = SMALLFONT)
        self.label3.grid(row = 4, column = 1)
        self.textbox3 = ttk.Entry(self, textvariable = Faculty, font = SMALLFONT)
        self.textbox3.grid(row = 4, column = 2)
        
        self.label4 = ttk.Label(self, text="Phone Number:", font = SMALLFONT)
        self.label4.grid(row = 5, column = 1)
        self.textbox4 = ttk.Entry(self, textvariable = PhoneNum, font = SMALLFONT)
        self.textbox4.grid(row = 5, column = 2)
        
        self.label5 = ttk.Label(self, text="Email Address:", font = SMALLFONT)
        self.label5.grid(row = 6, column = 1)
        self.textbox5 = ttk.Entry(self, textvariable= EmailAdd ,font = SMALLFONT)
        self.textbox5.grid(row = 6, column = 2)
        
        def extract_and_go_to_confirmation():
        
            global updateName
            global updateFac
            global updatePhonenum
            global updateEmailAdd
            updateName = Name.get()
            Name.set("")
            updateFac = Faculty.get()
            Faculty.set("")
            updatePhonenum = PhoneNum.get()
            PhoneNum.set("")
            updateEmailAdd = EmailAdd.get()
            EmailAdd.set("")
            return controller.show_frame(ConfirmationFrame)
        
        creation_member_btn = ttk.Button(self, text ="Update Member",
                            command = lambda : extract_and_go_to_confirmation(), width = 20)
     
        # putting the button in its place by
        # using grid
        creation_member_btn.grid(row = 9, column = 1)
        
        main_menu_btn = ttk.Button(self, text ="Back To Membership Menu ",
                            command = lambda : controller.show_frame(MembershipMenuFrame), width = 20)
     
        main_menu_btn.grid(row = 9, column = 4)

    def refresh(self):
        self.label1.config(text = self.UserInfo.get_username())
        
           
# tenth window frame error
class ConfirmationFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.UserInfo = Store_info()
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(columnspan = 5, rowspan = 10)
        
        self.labeltext = ttk.Label(self, text = "Please confirm details to be correct " , font = LARGEFONT)
        self.labeltext.grid(row = 1, column = 2)
        
        self.label0 = ttk.Label(self, text="Member ID", font = SMALLFONT,)
        self.label0.grid(row = 2, column = 1)
        
        self.label1 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label1.grid(row = 2, column = 2)
        
        self.label2 = ttk.Label(self, text="Name", font = SMALLFONT,)
        self.label2.grid(row = 3, column = 1)
        
        self.label3 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label3.grid(row = 3, column = 2)
        
        self.label4 = ttk.Label(self, text= "Faculty", font = SMALLFONT,)
        self.label4.grid(row = 4, column = 1)
        
        self.label5 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label5.grid(row = 4, column = 2)
        
        self.label6 = ttk.Label(self, text="Phone Number", font = SMALLFONT,)
        self.label6.grid(row = 5, column = 1)
        
        self.label7 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label7.grid(row = 5, column = 2)
        
        self.label8 = ttk.Label(self, text= "Email Address", font = SMALLFONT,)
        self.label8.grid(row = 6, column = 1)
        
        self.label9 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label9.grid(row = 6, column = 2)
        
        #add button and link
        def update_member():
            flag = True
            
            tuple_to_check = (updateName,updateFac,updatePhonenum,updateEmailAdd)
            for ele in tuple_to_check:
                if ele:
                    continue
                else:
                    flag = False
                    break
            if flag == False:
                return controller.show_frame(ErrorUpdateFrame)
                    
            a = extract_member_for_update[1]
            b = extract_member_for_update[2]
            c = extract_member_for_update[3]
            d = extract_member_for_update[4]
            
            sql = "UPDATE Member SET Name = %s WHERE Name = %s"
            val = (updateName, a)
            cur.execute(sql, val)
            conn.commit()
            
            sql = "UPDATE Member SET Faculty = %s WHERE Faculty = %s"
            val = (updateFac, b)
            cur.execute(sql, val)
            conn.commit()
            
            sql = "UPDATE Member SET PhoneNumber = %s WHERE PhoneNumber = %s"
            val = (updatePhonenum, c)
            cur.execute(sql, val)
            conn.commit()
            
            
            sql = "UPDATE Member SET Email = %s WHERE Email = %s"
            val = (updateEmailAdd, d)
            cur.execute(sql, val)
            conn.commit()
            
            return controller.show_frame(SuccessUpdateFrame)
            
        update_cfm_button = ttk.Button(self, text ="Confirm update",
                            command = lambda : update_member(), width = 20)
     
        update_cfm_button.grid(row = 9, column = 2)
        
        update_cfm_button = ttk.Button(self, text ="Back to update function",
                            command = lambda : controller.show_frame(UpdateInfoFrame), width = 20)
    
        update_cfm_button.grid(row = 9, column = 3)
        
    def refresh(self):
        self.label1.config(text = self.UserInfo.get_username())
        self.label3.config(text = updateName)
        self.label5.config(text = updateFac)
        self.label7.config(text = updatePhonenum)
        self.label9.config(text = updateEmailAdd)
           
# eleventh window frame error
class SuccessUpdateFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)
        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))
        canvas.create_text(450, 300, text="ALS Membership updated", fill="black", font=("RALEWAY", 25))
        
        cr8btn = ttk.Button(self, text='Create another Member',command = lambda : controller.show_frame(CreationFrame))
        cr8btn.place(x=200,y=500)
        
        upd8btn = ttk.Button(self, text='Back to Update Function',command = lambda : controller.show_frame(UpdateInfoFrame))
        upd8btn.place(x=600,y=500)
        
    def refresh(self):
        pass
           
# twelth window frame error
class ErrorUpdateFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Missing or incomplete fields.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Update function',command = lambda : controller.show_frame(UpdateInfoFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        pass




############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
########################################################################
###################        Books Frames                   ##############
########################################################################
#BookMenuFrame, BookAcqFrame, BookAcqSuccessFrame, BookAcqFailFrame, BookWithdrawFrame, BookWithdrawCfmFrame, BookWithdrawSuccessFrame,BookWithdrawFailLoanReservedFrame, BookWithdrawFailLoanFrame, BookWithdrawFailReservedFrame, BookWithdrawFailMissingFrame

#BookMenuFrame,BookAcqFrame,BookAcqSuccessFrame,BookAcqFailFrame,BookWithdrawFrame,BookWithdrawCfmFrame,BookWithdrawSuccessFrame,BookWithdrawFailLoanReservedFrame, BookWithdrawFailLoanFrame, BookWithdrawFailReservedFrame, BookWithdrawFailMissingFrame

class BookMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 800, height = 600)
        canvas.grid(columnspan = 5, rowspan = 5)

        # select options
        self.label = ttk.Label(self, text ="Select one of the Options below:", font = LARGEFONT)
        self.label.grid(row = 0, column = 2)
         
        # button to acquire books
        book_acquisition = ttk.Button(self, text ="Book Acquisition",
                            command = lambda : controller.show_frame(BookAcqFrame))
  
        # putting the button in its place by
        # using grid
        book_acquisition.grid(row = 1, column = 2)
        
        # button to withdraw book
        book_withdrawal = ttk.Button(self, text ="Book Withdrawal",
                            command = lambda : controller.show_frame(BookWithdrawFrame))
     
        # putting the button in its place by
        # using grid
        book_withdrawal.grid(row = 2, column = 2)
        
        # button to return to main menu
        main_menu_btn = ttk.Button(self, text ="Back To Main Menu",
                            command = lambda : controller.show_frame(MainMenuFrame))
     
        # putting the button in its place by
        # using grid
        main_menu_btn.grid(row = 3, column = 2)

    def refresh(self):
        pass

class BookAcqFrame(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        AccessionNumber = tk.StringVar()
        Title = tk.StringVar()
        Authors = tk.StringVar()
        ISBN = tk.StringVar()
        Publisher = tk.StringVar()
        PublicationYear = tk.StringVar()
        
        self.label0 = ttk.Label(self, text='For new book acquisition, please enter required information below:', font = SMALLFONT)
        self.label0.grid(row = 1, column = 2)
        
        self.label1 = ttk.Label(self, text="Accession Number:", font = SMALLFONT,)
        self.label1.grid(row = 2, column = 1)
        textbox1 = ttk.Entry(self, textvariable = AccessionNumber, font = SMALLFONT)
        textbox1.grid(row = 2, column = 2)
        
        self.label2 = ttk.Label(self, text="Title:", font = SMALLFONT)
        self.label2.grid(row = 3, column = 1)
        textbox2 = ttk.Entry(self,textvariable = Title , font = SMALLFONT)
        textbox2.grid(row = 3, column = 2)
        
        self.label3 = ttk.Label(self, text="Authors", font = SMALLFONT) #multiple authors
        self.label3.grid(row = 4, column = 1)
        textbox3 = ttk.Entry(self, textvariable = Authors , font = SMALLFONT)
        textbox3.grid(row = 4, column = 2)
        
        self.label4 = ttk.Label(self, text="ISBN:", font = SMALLFONT)
        self.label4.grid(row = 5, column = 1)
        textbox4 = ttk.Entry(self, textvariable = ISBN , font = SMALLFONT)
        textbox4.grid(row = 5, column = 2)
        
        self.label5 = ttk.Label(self, text="Publisher:", font = SMALLFONT)
        self.label5.grid(row = 6, column = 1)
        textbox5 = ttk.Entry(self, textvariable= Publisher ,font = SMALLFONT)
        textbox5.grid(row = 6, column = 2)

        self.label6 = ttk.Label(self, text="Publication Year:", font = SMALLFONT)
        self.label6.grid(row = 7, column = 1)
        textbox6 = ttk.Entry(self, textvariable= PublicationYear ,font = SMALLFONT)
        textbox6.grid(row = 7, column = 2)
        
        add_book_btn = ttk.Button(self, text ="Add New Book", command = lambda : check_if_can_acquire())
        add_book_btn.grid(row = 9, column = 1)

        def check_if_can_acquire() :
            flag = True
            cur.execute("select * from book")
            output = cur.fetchall()
            global getAccNum
            getAccNum = AccessionNumber.get()
            AccessionNumber.set("")
            global getTitle
            getTitle = Title.get()
            Title.set("")
            global getAuthors
            getAuthors = Authors.get()
            Authors.set("")
            global getISBN
            getISBN = ISBN.get()
            ISBN.set("")
            global getPublisher
            getPublisher = Publisher.get()
            Publisher.set("")
            global getPubYear
            getPubYear = PublicationYear.get()
            PublicationYear.set("")
            AuthorList = getAuthors.split(",")
            if len(AuthorList) == 3:
                Author1 = AuthorList[0]
                Author2 = AuthorList[1]
                Author3 = AuthorList[2]
            if len(AuthorList) == 2:
                Author1 = AuthorList[0]
                Author2 = AuthorList[1]
                Author3 = ""
            if len(AuthorList) == 1:
                Author1 = AuthorList[0]
                Author2 = ""
                Author3 = ""

            created_book = (getAccNum, getTitle, Author1, Author2, Author3, getISBN, getPublisher, getPubYear)
            
            if not created_book[0] or not created_book[1] or not created_book[2] or not created_book[5] or not created_book[6] or not created_book[7]:
                flag = False
                
            if flag == False:
                return controller.show_frame(BookAcqFailFrame)
                
            for book in output:
                if created_book[0] == book[0]:
                    flag = False
                    break
            if flag == False:
                return controller.show_frame(BookAcqFailFrame)
            sql = "INSERT INTO book (AccessionNumber, Title, Author1, Author2, Author3, ISBN, Publisher, PublicationYear) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql,created_book)
            conn.commit()
            return controller.show_frame(BookAcqSuccessFrame)
            
        books_menu_btn = ttk.Button(self, text ="Back To Books Menu",
                            command = lambda : controller.show_frame(BookMenuFrame))
        books_menu_btn.grid(row = 9, column = 3)
        
    def refresh(self):
        pass

class BookAcqSuccessFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="New book added in library.", fill="black", font=("RALEWAY",25))

        btn = ttk.Button(self, text='Back to acquisition function',command = lambda : controller.show_frame(BookAcqFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass
        
        
class BookAcqFailFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book already added;\nduplicate, missing or\nincomplete fields.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to acquisition function',command = lambda : controller.show_frame(BookAcqFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass

class BookWithdrawFrame(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
            #Select options
        canvas = tk.Canvas(self, width = 800, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)

        AccessionNumber = tk.StringVar()
        
        self.label0 = ttk.Label(self, text='To remove outdated book from system, please enter required information below:', font = SMALLFONT)
        self.label0.grid(row = 1, column = 2)
        
        self.label1 = ttk.Label(self, text="                         Accession Number:", font = SMALLFONT,)
        self.label1.grid(row = 5, column = 1)
        textbox1 = ttk.Entry(self, textvariable = AccessionNumber, font = SMALLFONT)
        textbox1.grid(row = 5, column = 2)

        def extract_info_from_accnum():
            cur.execute("select * from book")
            output = cur.fetchall()
            global getAccNum
            global extract_book
            extract_book = ()
            getAccNum = AccessionNumber.get()
            AccessionNumber.set("")
            if AccessionNumber == "":
                return
            for book in output:
                if book[0] == getAccNum:
                    extract_book = book
            if extract_book:
                return controller.show_frame(BookWithdrawCfmFrame)
            return controller.show_frame(BookWithdrawFailMissingFrame)

        withdraw_book_btn = ttk.Button(self, text ="Withdraw Book",
                            command = lambda : extract_info_from_accnum())
     
        # putting the button in its place by
        # using grid
        withdraw_book_btn.grid(row = 9, column = 1)
        
        books_menu_btn = ttk.Button(self, text ="Back To Books Menu",
                            command = lambda : controller.show_frame(BookMenuFrame))
     
        # putting the button in its place by
        # using grid
        books_menu_btn.grid(row = 9, column = 3)

    def refresh(self):
        pass


class BookWithdrawCfmFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(columnspan = 5, rowspan = 10)

        label0 = ttk.Label(self, text="Please confirm details\nto be correct", font = LARGEFONT)
        label0.grid(row = 1, column = 2)
        
        self.label0 = ttk.Label(self, text="Accession Number", font = SMALLFONT,)
        self.label0.grid(row = 2, column = 1)
        
        self.label1 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label1.grid(row = 2, column = 2)
        
        self.label2 = ttk.Label(self, text="Title", font = SMALLFONT,)
        self.label2.grid(row = 3, column = 1)
        
        self.label3 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label3.grid(row = 3, column = 2)
        
        self.label4 = ttk.Label(self, text= "Authors", font = SMALLFONT,)
        self.label4.grid(row = 4, column = 1)
        
        self.label5 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label5.grid(row = 4, column = 2)
        
        self.label6 = ttk.Label(self, text="ISBN", font = SMALLFONT,)
        self.label6.grid(row = 5, column = 1)
        
        self.label7 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label7.grid(row = 5, column = 2)
        
        self.label8 = ttk.Label(self, text= "Publisher", font = SMALLFONT,)
        self.label8.grid(row = 6, column = 1)
        
        self.label9 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label9.grid(row = 6, column = 2)
        
        self.label10 = ttk.Label(self, text= "Publication Year", font = SMALLFONT,)
        self.label10.grid(row = 7, column = 1)
        
        self.label11 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label11.grid(row = 7, column = 2)

        btn1 = ttk.Button(self, text='Return to Delete function',command = lambda : controller.show_frame(BookWithdrawFrame))
        btn1.grid(row = 9, column = 4)
        

        btn2 = ttk.Button(self, text='Confirm deletion',command = lambda : check_if_can_withdraw())
        btn2.grid(row = 9, column = 1)

    
        def check_if_can_withdraw() : #12 is loaned #13 is reserved line 1052
            bookisreserved = False
            bookisloaned = False
            bookisreservedloaned = False
            cur.execute("select * from bookupdated")
            output = cur.fetchall()
            for book in output:
                if extract_book[0] == book[0]:
                    identifiedbook = book
                    if identifiedbook[12] and identifiedbook[13]:
                        bookisreservedloaned = True
                        break
                    if identifiedbook[12]:
                        bookisloaned = True
                    if identifiedbook[13]:
                        bookisreserved = True
                        
                        
            if bookisreservedloaned:
                return controller.show_frame(BookWithdrawFailLoanReservedFrame)
            if bookisloaned:
                return controller.show_frame(BookWithdrawFailLoanFrame)
            if bookisreserved:
                return controller.show_frame(BookWithdrawFailReservedFrame)
            else:
                sql = "DELETE FROM book WHERE AccessionNumber = %s"
                x = extract_book[0]
                cur.execute(sql,x)
                conn.commit()
                return controller.show_frame(BookWithdrawSuccessFrame)

            
    def refresh(self):
        self.label1.config(text = extract_book[0])
        self.label3.config(text = extract_book[1])
        self.label5.config(text = list(extract_book[2:5]))
        self.label7.config(text = extract_book[5])
        self.label9.config(text = extract_book[6])
        self.label11.config(text = extract_book[7])
        
        
class BookWithdrawSuccessFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book successfully withdrawn.", fill="black", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to withdrawal function',command = lambda : controller.show_frame(BookWithdrawFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass

class BookWithdrawFailLoanReservedFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book is currently on loan and is reserved", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to withdrawal function',command = lambda : controller.show_frame(BookWithdrawFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass

class BookWithdrawFailLoanFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book is currently on loan.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to withdrawal function',command = lambda : controller.show_frame(BookWithdrawFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass


class BookWithdrawFailReservedFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book is currently reserved.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to withdrawal function',command = lambda : controller.show_frame(BookWithdrawFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass


class BookWithdrawFailMissingFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book is not in library", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to withdrawal function',command = lambda : controller.show_frame(BookWithdrawFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass
        
        
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
########################################################################
###################        Loans      Frames              ##############
########################################################################
#LoanMenuFrame,BookBorrowFrame,BookLoanMissingDetails,BorrowFailNoMemberOrBook,BorrowFailFineFrame,LoanTwoBooks,ErrorReservedBySb,BkOnLoanUntilFrame,BorrowCfmFrame,

class LoanMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 800, height = 600)
        canvas.grid(columnspan = 5, rowspan = 5)

        # select options
        self.label = ttk.Label(self, text ="Select one of the Options below:", font = LARGEFONT)
        self.label.grid(row = 0, column = 2)
         
        # button to acquire books
        book_borrowing = ttk.Button(self, text ="Book Borrowing",
                            command = lambda : controller.show_frame(BookBorrowFrame))
  
        # putting the button in its place by
        # using grid
        book_borrowing.grid(row = 1, column = 2)
        
        # button to withdraw book
        book_return = ttk.Button(self, text ="Book Returning",
                            command = lambda : controller.show_frame(BookReturnFrame))
     
        # putting the button in its place by
        # using grid
        book_return.grid(row = 2, column = 2)
        
        # button to return to main menu
        main_menu_btn = ttk.Button(self, text ="Back To Main Menu",
                            command = lambda : controller.show_frame(MainMenuFrame))
     
        # putting the button in its place by
        # using grid
        main_menu_btn.grid(row = 3, column = 2)

    def refresh(self):
        pass


class BookBorrowFrame(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
            #Select options
        canvas = tk.Canvas(self, width = 800, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)

        AccessionNumber = tk.StringVar()
        MembershipID = tk.StringVar()
        
        self.label0 = ttk.Label(self, text='To borrow a book, please enter information below', font = SMALLFONT)
        self.label0.grid(row = 1, column = 2)
        
        self.label1 = ttk.Label(self, text="                         Accession Number:", font = SMALLFONT,)
        self.label1.grid(row = 5, column = 1)
        textbox1 = ttk.Entry(self, textvariable = AccessionNumber, font = SMALLFONT)
        textbox1.grid(row = 5, column = 2)

        self.label2 = ttk.Label(self, text="                         Membership ID:", font = SMALLFONT,)
        self.label2.grid(row = 6, column = 1)
        textbox2 = ttk.Entry(self, textvariable = MembershipID, font = SMALLFONT)
        textbox2.grid(row = 6, column = 2)

        def check_if_details_are_correct():
            flag = False
            global getAcc_borrow_book,getMem_borrow_book
            getAcc_borrow_book = AccessionNumber.get()
            AccessionNumber.set("")
            getMem_borrow_book = MembershipID.get()
            MembershipID.set("")
            if getAcc_borrow_book:
                if getMem_borrow_book:
                    flag = True
            if flag == False:
                return controller.show_frame(BookLoanMissingDetails)
            #check if valid book/member
            bookcorrect = False
            membercorrect = False
            
            #2exec
            cur.execute("select * from book")
            all_book = cur.fetchall()
            cur.execute("select * from Member")
            all_member = cur.fetchall()
            for ele in all_book:
                if ele[0] == getAcc_borrow_book:
                    bookcorrect = True
            for mem in all_member:
                if mem[0] == getMem_borrow_book:
                    membercorrect = True

            if bookcorrect == False or membercorrect == False:
                return controller.show_frame(BorrowFailNoMemberOrBook)
            
            #check for fines
            cur.execute("select * from Fine")
            finetab = cur.fetchall()
            for row in finetab:
                if row[0] == getMem_borrow_book:
                    if int(row[1]) > 0:
                        return controller.show_frame(BorrowFailFineFrame)
            #getAcc_borrow_book,getMem_borrow_book
            #2 exec
            
            global borrow_bk_extract
            global mem_extract
            
            cur.execute("select * from book")
            allll_bkkk = cur.fetchall()
            for bkkk in allll_bkkk:
                if bkkk[0] == getAcc_borrow_book:
                    borrow_bk_extract = bkkk
                    break
                    
            cur.execute("select * from Member")
            all_memmm = cur.fetchall()
            for elle in all_memmm:
                if elle[0] == getMem_borrow_book:
                    mem_extract = elle
                    break

                        
            global checkifexistin_updt_book
            checkifexistin_updt_book = False

            cur.execute("select * from BookUpdated")
            updt_book = cur.fetchall()
            
            for AccN,*args in updt_book:
                if AccN == getAcc_borrow_book:
                    checkifexistin_updt_book = True
                    break
                    
                    
            counter_for_loans = 0
            for AccN,*args,memberid_borrow,memberid_reserve in updt_book:
                if getMem_borrow_book == memberid_borrow:
                    counter_for_loans += 1
                
            if counter_for_loans >= 2:
                return controller.show_frame(LoanTwoBooks)
                    
            if checkifexistin_updt_book == False:
                return controller.show_frame(BorrowCfmFrame)
            
            if checkifexistin_updt_book == True:
                for accN,*args,brwdt,reservedt,rtndte,duedt,memidbr,memidrs in updt_book:
                    if accN == getAcc_borrow_book:
                        if duedt:
                            global nxtframe_send_date
                            nxtframe_send_date = duedt
                            return controller.show_frame(BkOnLoanUntilFrame)
                            

            #need to check if reserve and check if 2 loans
            if checkifexistin_updt_book == True:
                #AccN,MemberBorrow,MemberRes
                #check if reserve, then check if loan then check if got fines
                #getAcc_borrow_book,getMem_borrow_book
                
                flag_for_reserve = False
                I_reserve_flag = False
                for AccN,*args,bd,rd,rtnd,dd,memberid_borrow,memberid_reserve in updt_book:
                    if getAcc_borrow_book == AccN:
                        if memberid_reserve:
                            flag_for_reserve = True
                            if memberid_reserve == getMem_borrow_book:
                                if ((date.today()-rd).days) >= 0:
                                    I_reserve_flag = True

                counter_for_loans = 0
                for AccN,*args,memberid_borrow,memberid_reserve in updt_book:
                    if getMem_borrow_book == memberid_borrow:
                        counter_for_loans += 1

                if counter_for_loans == 2:
                    return controller.show_frame(LoanTwoBooks)
                if flag_for_reserve:
                    if I_reserve_flag:
                        return controller.show_frame(BorrowCfmFrame)
                    return controller.show_frame(ErrorReservedBySb)
            
            return controller.show_frame(BorrowCfmFrame)
                


        borrow_book_btn = ttk.Button(self, text ="Borrow Book",
                            command = lambda : check_if_details_are_correct())
        borrow_book_btn.grid(row = 9, column = 1)
        
        loan_menu_btn = ttk.Button(self, text ="Back To Loan Menu",
                            command = lambda : controller.show_frame(LoanMenuFrame))
        loan_menu_btn.grid(row = 9, column = 3)

            
    def refresh(self):
        pass

class BkOnLoanUntilFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9,columnspan=5)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))
        
        self.label1 = ttk.Label(self, text= "Book on loan until: ", font = SMALLFONT,)
        self.label1.grid(row = 5, column = 1)
        
        self.label2 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label2.grid(row = 5, column = 2)
        
        btn = ttk.Button(self, text='Return to Borrow function',command = lambda : controller.show_frame(BookBorrowFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        self.label2.config(text = nxtframe_send_date)
        
        
class ErrorReservedBySb(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book is on reservation", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Borrow function',command = lambda : controller.show_frame(BookBorrowFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass

class LoanTwoBooks(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Member loan quota exceeded", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Borrow function',command = lambda : controller.show_frame(BookBorrowFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass


class BookLoanMissingDetails(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Missing Details.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Book Borrowing function',command = lambda : controller.show_frame(BookBorrowFrame))
        
        btn.place(x=350,y=500)

    def refresh(self):
        pass


class BorrowFailNoMemberOrBook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="No such member/book exists.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Book Borrowing function',command = lambda : controller.show_frame(BookBorrowFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass


class BorrowFailFineFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Member has outstanding fines", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Borrow function',command = lambda : controller.show_frame(BookBorrowFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass



class BorrowCfmFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        label0 = ttk.Label(self, text='Confirm Reservation Details To Be Correct', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Accession Number:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)

        self.label1_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label1_1.grid(row = 2, column = 2)
        
        label2 = ttk.Label(self, text="Book Title:", font = SMALLFONT)
        label2.grid(row = 3, column = 1)

        self.label2_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label2_1.grid(row = 3, column = 2)

        label3 = ttk.Label(self, text="Borrow Date:", font = SMALLFONT)
        label3.grid(row = 4, column = 1)

        self.label3_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label3_1.grid(row = 4, column = 2)

        label4 = ttk.Label(self, text="Membership ID:", font = SMALLFONT)
        label4.grid(row = 5, column = 1)
        
        self.label4_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label4_1.grid(row = 5, column = 2)
        
        label5 = ttk.Label(self, text="Member Name", font = SMALLFONT)
        label5.grid(row = 6, column = 1)

        self.label5_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label5_1.grid(row = 6, column = 2)

        label6 = ttk.Label(self, text="Due Date", font = SMALLFONT)
        label6.grid(row = 7, column = 1)

        self.label6_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label6_1.grid(row = 7, column = 2)

        def send_to_sql():
            #check if this book is in updated books
            #if yes:-> update
            #if no:-> create
            newchck = False
            cur.execute("select * from BookUpdated")
            bkkupdate = cur.fetchall()
            for AccN,*args in bkkupdate:
                if AccN == borrow_bk_extract[0]:
                    newchck = True
                    break
            flag_I_reserve = True
            for bka,*args, memresID in bkkupdate:
                if bka == borrow_bk_extract[0] and memresID == mem_extract[0]:
                    flag_I_reserve = True
            
            if newchck:
                if flag_I_reserve:
                    sql = "UPDATE BookUpdated SET MemberReserveID = %s WHERE AccessionNumber = %s"
                    val = (None,borrow_bk_extract[0])
                    cur.execute(sql, val)
                    conn.commit()
                #means it exists
                #just update
                
                sql = "UPDATE BookUpdated SET BorrowDate = %s WHERE AccessionNumber = %s"
                val = (date.today(),borrow_bk_extract[0])
                cur.execute(sql, val)
                conn.commit()

                sql = "UPDATE BookUpdated SET DueDate = %s WHERE AccessionNumber = %s"
                val = (date.today() + timedelta(days=14),borrow_bk_extract[0])
                cur.execute(sql, val)
                conn.commit()
                
                sql = "UPDATE BookUpdated SET MemberBorrowID = %s WHERE AccessionNumber = %s"
                val = (mem_extract[0],borrow_bk_extract[0])
                cur.execute(sql, val)
                conn.commit()
                return controller.show_frame(BorrowSuccessFrame)
                
            if newchck == False:
                sql = "INSERT INTO BookUpdated (AccessionNumber,Title,Author1,Author2,Author3,ISBN,Publisher,PublicationYear,BorrowDate,ReserveDate,ReturnDate,DueDate,MemberBorrowID,MemberReserveID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                newtup = borrow_bk_extract + (date.today(),None,None, date.today() + timedelta(days = 14),mem_extract[0],None)
                
                cur.execute(sql,newtup)
                conn.commit()
                return controller.show_frame(BorrowSuccessFrame)
                
            
            
            
        btn1 = ttk.Button(self, text='Return to Borrow function',command = lambda : controller.show_frame(LoanMenuFrame))
        btn1.place(x=550,y=550)

        btn2 = ttk.Button(self, text='Confirm Loan', command = lambda : send_to_sql())
        btn2.place(x=50,y=550)
        
    def refresh(self):
        self.label1_1.config(text = borrow_bk_extract[0])
        self.label2_1.config(text = borrow_bk_extract[1])
        self.label3_1.config(text = date.today())
        self.label4_1.config(text = mem_extract[0])
        self.label5_1.config(text = mem_extract[1])
        self.label6_1.config(text = date.today() + timedelta(days=14))
        


class BorrowSuccessFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book successfully borrowed.", fill="black", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Borrow function',command = lambda : controller.show_frame(BookBorrowFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass
        
        
class BookReturnFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        AccessionNumber = tk.StringVar()
        ReturnDate = tk.StringVar()
        
        label0 = ttk.Label(self, text='To Return a Book, Please Enter Information Below:', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Accession Number:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)
        textbox1 = ttk.Entry(self, textvariable = AccessionNumber, font = SMALLFONT)
        textbox1.grid(row = 2, column = 2)
    
        label2 = ttk.Label(self, text="Return Date:(YYYY-MM-DD)", font = SMALLFONT)
        label2.grid(row = 3, column = 1)
        textbox3 = ttk.Entry(self, textvariable = ReturnDate, font = SMALLFONT)
        textbox3.grid(row = 3, column = 2)
        
        def check_if_can_return():
            global retdate
            retdate =ReturnDate.get()
            ReturnDate.set("")
            global accnum
            accnum = AccessionNumber.get()
            AccessionNumber.set("")
            loanexists = False
            cur.execute("select * from bookupdated")
            books = cur.fetchall()
            global memberid
            memberid = ()
            global extract_loan
            extract_loan = ()
            global GetDueDate
            #retdate GetDueDate
            global createFine
            
            
            for book in books:
                if book[0] == accnum and book[12]:
                    memberid = book[12]
                    extract_loan = book
                    loanexists = True
                    GetDueDate = book[11]
                    retdate2 = datetime.strptime(retdate, "%Y-%m-%d").date()
                    createFine = (retdate2 - GetDueDate).days
                    if createFine < 0:
                        createFine = 0
            cur.execute("select * from Member")
            output = cur.fetchall()
            global membername
            for member in output:
                if memberid == member[0]:
                    membername = member[1]
                    
            if loanexists == False:
                return controller.show_frame(NoSuchLoanFrame)
            else:
                return controller.show_frame(ReturnCfmFrame)
    

        return_book_btn = ttk.Button(self, text ="Return Book", command = lambda : check_if_can_return(), width = 20)
     
        return_book_btn.grid(row = 9, column = 1)
        
        main_menu_btn = ttk.Button(self, text ="Back To Loans Menu", width = 20, command = lambda : controller.show_frame(LoanMenuFrame))
                            
        main_menu_btn.grid(row = 9, column = 3)

    def refresh(self):
        pass


class NoSuchLoanFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="No such book on loan.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Return to Borrow function',command = lambda : controller.show_frame(BookReturnFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass

        
class ReturnCfmFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        label0 = ttk.Label(self, text='Confirm Return Details To Be Correct', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Accession Number:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)
        self.label1_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label1_1.grid(row = 2, column = 2)
        
        label2 = ttk.Label(self, text="Book Title:", font = SMALLFONT)
        label2.grid(row = 3, column = 1)
        self.label2_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label2_1.grid(row = 3, column = 2)

        label3 = ttk.Label(self, text="Membership ID:", font = SMALLFONT)
        label3.grid(row = 4, column = 1)
        self.label3_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label3_1.grid(row = 4, column = 2)

        label4 = ttk.Label(self, text="Membership Name:", font = SMALLFONT)
        label4.grid(row = 5, column = 1)
        self.label4_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label4_1.grid(row = 5, column = 2)
        
        label5 = ttk.Label(self, text="Return Date:", font = SMALLFONT)
        label5.grid(row = 6, column = 1)
        self.label5_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label5_1.grid(row = 6, column = 2)

        label6 = ttk.Label(self, text="Fine($):", font = SMALLFONT)
        label6.grid(row = 7, column = 1)
        self.label6_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label6_1.grid(row = 7, column = 2)

        def returnbook():
            cur.execute("select * from bookupdated")
            output = cur.fetchall()
            accnum = extract_loan[0]
            memberid = extract_loan[12]
            fineincurred = False
            if int(createFine) != 0 :
                fineincurred = True
                fineaddedflag = False
                cur.execute("select * from Fine")
                finez = cur.fetchall()
                for ele in finez:
                    if ele[0] == memberid:
                        sql = "UPDATE Fine SET Amount = %s WHERE MemberID = %s"
                        #findouthowmuchatfirst
                        val = (createFine + int(ele[1]), memberid)
                        cur.execute(sql,val)
                        conn.commit()
                        #update
                        fineaddedflag = True
                        break
                    else:
                        continue
                if fineaddedflag == False:
                    #add a new row
                    sql = "INSERT INTO Fine (MemberID, Amount) VALUES (%s, %s)"
                    val = (memberid,createFine)
                    cur.execute(sql, val)
                    conn.commit()
                
            # fineincurred = True
            for book in output:
                if (book[0] == accnum) and (book[12] == memberid):
                    if book[13]:
                        sql = "UPDATE bookupdated SET MemberBorrowID = %s WHERE AccessionNumber = %s"
                        val = (None, accnum)
                        cur.execute(sql,val)
                        conn.commit()
                        
                        sql = "UPDATE bookupdated SET DueDate = %s WHERE AccessionNumber = %s"
                        val = (None, accnum)
                        cur.execute(sql,val)
                        conn.commit()
                                                
                        break
                    else:
                        sql = "DELETE FROM bookupdated WHERE AccessionNumber = %s"
                        val = accnum
                        cur.execute(sql,val)
                        conn.commit()
                        break

            if fineincurred:
                return controller.show_frame(FineIncurredFrame)
            return controller.show_frame(ReturnSuccessFrame)



        # NEED BACKEND CODING
        delete_reservation_btn = ttk.Button(self, text ="Confirm return",
                            command = lambda : returnbook(), width = 25)
     
        delete_reservation_btn.grid(row = 9, column = 1)
        
        main_menu_btn = ttk.Button(self, text ="Back To Return Function",
                            command = lambda : controller.show_frame(BookReturnFrame), width = 25)
                            
        main_menu_btn.grid(row = 9, column = 4)

        # NEEDS BACKEND CODING
        # Need to connect to SQL to check
    

    def refresh(self):
        self.label1_1.config(text = extract_loan[0])
        self.label2_1.config(text = extract_loan[1])
        self.label3_1.config(text = memberid)
        self.label4_1.config(text = membername)
        self.label5_1.config(text = retdate)
        self.label6_1.config(text = createFine )
                
class FineIncurredFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book returned successfully but has fines.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to Return function',command = lambda : controller.show_frame(BookReturnFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass
                
class ReturnSuccessFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book successfully returned.", fill="black", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to Return function',command = lambda : controller.show_frame(BookReturnFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
########################################################################
###################        Reservation Frames             ##############
########################################################################
#Frames
#ReservationMenuFrame
#BookReservationFrame,WrongDetailsForResFrame,ConfirmationReservationFrame,SuccessReservationFrame,ErrorTwoReservationFrame,ErrorOutstandingFineFrame
#CancelReservationFrame,ConfirmationCancellationFrame,SuccessReservationCancellationFrame,ErrorOutstandingFineFrame




class ReservationMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 5)
        label = ttk.Label(self, text ="Select one of the Options below:", font = LARGEFONT)
        label.grid(row = 0, column = 2)
        
        book_reservation = ttk.Button(self, text ="Reserve a Book",
                            command = lambda : controller.show_frame(BookReservationFrame),width = 20)
        book_reservation.grid(row = 1, column = 2)
        
        cancel_reservation = ttk.Button(self, text ="Cancel Reservation",
                            command = lambda : controller.show_frame(CancelReservationFrame),width = 20)
        cancel_reservation.grid(row = 2, column = 2)
        
            
        main_menu_btn = ttk.Button(self, text ="Back To Main Menu",
                            command = lambda : controller.show_frame(MainMenuFrame), width = 20)
     
        main_menu_btn.grid(row = 4, column = 2)
        
    def refresh(self):
        pass

class BookReservationFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        AccessionNumber = tk.StringVar()
        MembershipID = tk.StringVar()
        ReserveDate = tk.StringVar()
        
        label0 = ttk.Label(self, text='To Reserve a Book, Please Enter Information Below', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Accession Number:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)
        textbox1 = ttk.Entry(self, textvariable = AccessionNumber, font = SMALLFONT)
        textbox1.grid(row = 2, column = 2)
        
        label2 = ttk.Label(self, text="Membership ID:", font = SMALLFONT)
        label2.grid(row = 3, column = 1)
        textbox2 = ttk.Entry(self,textvariable = MembershipID, font = SMALLFONT)
        textbox2.grid(row = 3, column = 2)
        
        label3 = ttk.Label(self, text="Reserve Date:(YYYY-MM-DD)", font = SMALLFONT)
        label3.grid(row = 4, column = 1)
        textbox3 = ttk.Entry(self, textvariable = ReserveDate, font = SMALLFONT)
        textbox3.grid(row = 4, column = 2)
        def check_if_details_is_correct():
            #extract the books and see if accesion number is valid
            #extract tbe member and see if valid member
            flag1 = False
            flag2 = False
            cur.execute("select * from book")
            books_from_db = cur.fetchall()
            cur.execute("select * from member")
            member_in_db = cur.fetchall()
            global check_accession_for_reservation
            global check_member_for_reservation
            check_accession_for_reservation = AccessionNumber.get()
            xxx = AccessionNumber.get()
            AccessionNumber.set("")
            check_member_for_reservation = MembershipID.get()
            MembershipID.set("")
            get_reserve_date = ReserveDate.get()
            ReserveDate.set("")
            check_elem = (check_member_for_reservation,check_accession_for_reservation,get_reserve_date)
            global inputreserveDate
            inputreserveDate = get_reserve_date
            for ele in check_elem:
                if ele:
                    continue
                else:
                    return controller.show_frame(WrongDetailsForResFrame)
            
            for member in member_in_db:
                if member[0] == check_member_for_reservation:
                    check_member_for_reservation = member
                    flag1 = True
                    break
                    
            for book in books_from_db:
                if book[0] == check_accession_for_reservation:
                    check_accession_for_reservation = book
                    flag2 = True
                    break
                    
            if (flag1 == False and flag2 == False):
                return controller.show_frame(WrongDetailsForResFrame)
                
            cur.execute("select * from Bookupdated")
            books_from_BU = cur.fetchall()
            for bkk in books_from_BU:
                if bkk[0] == xxx:
                    if bkk[13]:
                        return controller.show_frame(BookIsReservedFrame)
            return controller.show_frame(ConfirmationReservationFrame)
        
        reserve_book_btn = ttk.Button(self, text ="Reserve Book",
                            command = lambda : check_if_details_is_correct() , width = 20)
     
        reserve_book_btn.grid(row = 9, column = 1)
        
        main_menu_btn = ttk.Button(self, text ="Back To Reservations Menu",
                            command = lambda : controller.show_frame(ReservationMenuFrame), width = 20)
                            
        main_menu_btn.grid(row = 9, column = 4)
            
    def refresh(self):
        pass
        
class BookIsReservedFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Book is Reserved", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to Reserve function',command = lambda : controller.show_frame(BookReservationFrame))
        btn.place(x=350,y=500)
    def refresh(self):
        pass

class WrongDetailsForResFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Incorrect or Missing Details", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to Reserve function',command = lambda : controller.show_frame(BookReservationFrame))
        btn.place(x=350,y=500)
    def refresh(self):
        pass

class ConfirmationReservationFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        label0 = ttk.Label(self, text='Confirm Reservation Details To Be Correct', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Accession Number:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)

        self.label1_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label1_1.grid(row = 2, column = 2)
        
        label2 = ttk.Label(self, text="Book Title:", font = SMALLFONT)
        label2.grid(row = 3, column = 1)

        self.label2_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label2_1.grid(row = 3, column = 2)

        label3 = ttk.Label(self, text="Membership ID:", font = SMALLFONT)
        label3.grid(row = 4, column = 1)

        self.label3_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label3_1.grid(row = 4, column = 2)

        label4 = ttk.Label(self, text="Membership Name:", font = SMALLFONT)
        label4.grid(row = 5, column = 1)
        
        self.label4_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label4_1.grid(row = 5, column = 2)
        
        label5 = ttk.Label(self, text="Reserve Date:", font = SMALLFONT)
        label5.grid(row = 6, column = 1)

        self.label5_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label5_1.grid(row = 6, column = 2)

        def check_if_can_reserve():
            flag = True
            #3 scenario
            cur.execute("select * from BookUpdated")
            output = cur.fetchall()
            counter_for_reservation = 0
            memberID = check_member_for_reservation[0]
            
            secondflag=False
            for book in output:
                if check_accession_for_reservation[0] in book:
                    secondflag = True
                    
            for *args,MemberBorrowID,MemberReserveID in output:
                if MemberReserveID == memberID:
                    counter_for_reservation += 1
            if counter_for_reservation == 2:
                return controller.show_frame(ErrorTwoReservationFrame)
            global reservememberfine
            cur.execute("select * from Fine")
            finestable = cur.fetchall()
            for member_fine in finestable:
                if member_fine[0] == memberID:
                    if int(member_fine[1]) > 0:
                        reservememberfine = member_fine[1]
                        flag = False
            if flag == False:
                return controller.show_frame(ErrorOutstandingFineFrame)

            # 2 books on reservation
            # outstanding fine
            # success
            # 3 return frames
            # if then x if then x if then x
            bookexist_in_book_updated_flag = False
            global toeditbookinbookupdated
            toeditbookinbookupdated = ()
            for bk in output:
                if bk[0] == check_accession_for_reservation[0]:
                    bookexist_in_book_updated_flag = True
                    toeditbookinbookupdated = bk
                    
            if bookexist_in_book_updated_flag == False:

                global newtup
                newtup = ()
                #need to add integer date inside to_add
                to_add = (None,inputreserveDate,None,None,None,memberID)
                newtup = check_accession_for_reservation
                newtup += to_add

                if flag == True:
                    #create reservation
                    sql = "INSERT INTO BookUpdated (AccessionNumber,Title,Author1,Author2,Author3,ISBN,Publisher,PublicationYear,BorrowDate,ReserveDate,ReturnDate,DueDate,MemberBorrowID,MemberReserveID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"
                    cur.execute(sql,newtup)
                    conn.commit()
                    return controller.show_frame(SuccessReservationFrame)
            else:
                #update reserve date
                #update member reserve id
                #update member isreserved 1/0
                #get what is old reserve date
                sql = "UPDATE BookUpdated SET ReserveDate = %s WHERE AccessionNumber = %s"
                val = (inputreserveDate,toeditbookinbookupdated[0])
                cur.execute(sql, val)
                conn.commit()

                sql = "UPDATE BookUpdated SET MemberReserveID = %s WHERE AccessionNumber = %s"
                val = (check_member_for_reservation[0],toeditbookinbookupdated[0])
                cur.execute(sql, val)
                conn.commit()
                
                
                return controller.show_frame(SuccessReservationFrame)
                
        
        
        reserve_book_btn = ttk.Button(self, text ="Confirm Reservation",
                            command = lambda : check_if_can_reserve(), width = 20)
     
        reserve_book_btn.grid(row = 9, column = 1)
        
        main_menu_btn = ttk.Button(self, text ="Back To Reserve Function",
                            command = lambda : controller.show_frame(BookReservationFrame), width = 20)
                            
        main_menu_btn.grid(row = 9, column = 4)

        #check_member_for_reservation become a member
        #check_accession_for_reservation become a book
                        
    def refresh(self):
        self.label1_1.config(text = check_accession_for_reservation[0])
        self.label2_1.config(text = check_accession_for_reservation[1])
        self.label3_1.config(text = check_member_for_reservation[0])
        self.label4_1.config(text = check_member_for_reservation[1])
        self.label5_1.config(text = inputreserveDate)


class SuccessReservationFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)
        
        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Reservation Created", fill="black", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to Reservation Function',command = lambda : controller.show_frame(BookReservationFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        pass

class ErrorTwoReservationFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Member currently has\n2 Books on Reservation", fill="yellow", font=("RALEWAY", 25))
                        
        btn = ttk.Button(self, text='Back to Reserve function',command = lambda : controller.show_frame(BookReservationFrame))
        btn.place(x=350,y=500)
    def refresh(self):
        pass
        
class ErrorOutstandingFineFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9,columnspan=5)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))
        
        self.label1 = ttk.Label(self, text= "Member has Outstanding Fine of:", font = SMALLFONT,)
        self.label1.grid(row = 5, column = 1)
        
        self.label2 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label2.grid(row = 5, column = 2)
        
        btn = ttk.Button(self, text='Return to Reserve function',command = lambda : controller.show_frame(BookReservationFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        self.label2.config(text = reservememberfine)


class CancelReservationFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        AccessionNumber = tk.StringVar()
        MembershipID = tk.StringVar()
        ReserveDate = tk.StringVar()
        
        label0 = ttk.Label(self, text='To Cancel a Reservation, Please Enter Information Below:', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Accession Number:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)
        textbox1 = ttk.Entry(self, textvariable = AccessionNumber, font = SMALLFONT)
        textbox1.grid(row = 2, column = 2)
        
        label2 = ttk.Label(self, text="Membership ID:", font = SMALLFONT)
        label2.grid(row = 3, column = 1)
        textbox2 = ttk.Entry(self,textvariable = MembershipID, font = SMALLFONT)
        textbox2.grid(row = 3, column = 2)
        
        label3 = ttk.Label(self, text="Cancel Date:(YYYY-MM-DD)", font = SMALLFONT)
        label3.grid(row = 4, column = 1)
        textbox3 = ttk.Entry(self, textvariable = ReserveDate, font = SMALLFONT)
        textbox3.grid(row = 4, column = 2)
        
        def check_if_can_cancel():
            global resdate
            resdate = ReserveDate.get()
            ReserveDate.set("")
            global accnum
            accnum = AccessionNumber.get()
            AccessionNumber.set("")
            global memberid
            memberid = MembershipID.get()
            MembershipID.set("")
            reservationexists = False
            cur.execute("select * from bookupdated")
            books = cur.fetchall()
            global extract_reservation
            extract_reservation = ()
            cur.execute("select * from Member")
            output = cur.fetchall()
            global membername
            for member in output:
                if memberid == member[0]:
                    membername = member[1]
                    
            cannotcancelFlag = True
            for book in books:
                if book[0] == accnum and book[13] == memberid:
                    extract_reservation = book
                    reservationexists = True
                    if book[12]:
                        cannotcancelFlag = False
            
                    
            if reservationexists == False:
                return controller.show_frame(NoSuchReservationFrame)
            else:
                if cannotcancelFlag == True:
                    return controller.show_frame(CannotCancel)
                else:
                    return controller.show_frame(ConfirmationCancellationFrame)
    

        cancel_reservation_btn = ttk.Button(self, text ="Cancel Reservation", command = lambda : check_if_can_cancel(), width = 20)
     
        cancel_reservation_btn.grid(row = 9, column = 1)
        
        main_menu_btn = ttk.Button(self, text ="Back To Reservations Menu", width = 20, command = lambda : controller.show_frame(ReservationMenuFrame))
                            
        main_menu_btn.grid(row = 9, column = 3)

    def refresh(self):
        pass
        
        
class ConfirmationCancellationFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        label0 = ttk.Label(self, text='Confirm Cancellation Details To Be Correct', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Accession Number:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)
        self.label1_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label1_1.grid(row = 2, column = 2)
        
        label2 = ttk.Label(self, text="Book Title:", font = SMALLFONT)
        label2.grid(row = 3, column = 1)
        self.label2_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label2_1.grid(row = 3, column = 2)

        label3 = ttk.Label(self, text="Membership ID:", font = SMALLFONT)
        label3.grid(row = 4, column = 1)
        self.label3_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label3_1.grid(row = 4, column = 2)

        label4 = ttk.Label(self, text="Membership Name:", font = SMALLFONT)
        label4.grid(row = 5, column = 1)
        self.label4_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label4_1.grid(row = 5, column = 2)
        
        label5 = ttk.Label(self, text="Cancellation Date:", font = SMALLFONT)
        label5.grid(row = 6, column = 1)
        self.label5_1 = ttk.Label(self, text="xxx:", font = SMALLFONT,)
        self.label5_1.grid(row = 6, column = 2)

        def delete():
            cur.execute("select * from bookupdated")
            output = cur.fetchall()
            accnum = extract_reservation[0]
            memberid = extract_reservation[13]
            for book in output:
                if book[0] == accnum and book[13] == memberid and book[12]:
                    sql = "UPDATE bookupdated SET MemberReserveID = %s WHERE AccessionNumber = %s"
                    val = (None, accnum)
                    cur.execute(sql,val)
                    conn.commit()
                    return controller.show_frame(SuccessReservationCancellationFrame)
                else:
                    sql = "DELETE FROM bookupdated WHERE AccessionNumber = %s"
                    val = accnum
                    cur.execute(sql,val)
                    conn.commit()
                    return controller.show_frame(SuccessReservationCancellationFrame)



        # NEED BACKEND CODING
        delete_reservation_btn = ttk.Button(self, text ="Confirm Cancellation",
                            command = lambda : delete(), width = 25)
     
        delete_reservation_btn.grid(row = 9, column = 1)
        
        main_menu_btn = ttk.Button(self, text ="Back To Cancellation Function",
                            command = lambda : controller.show_frame(CancelReservationFrame), width = 25)
                            
        main_menu_btn.grid(row = 9, column = 4)

        # NEEDS BACKEND CODING
        # Need to connect to SQL to check
  

    def refresh(self):
        self.label1_1.config(text = extract_reservation[0])
        self.label2_1.config(text = extract_reservation[1])
        self.label3_1.config(text = extract_reservation[13])
        self.label4_1.config(text = membername)
        self.label5_1.config(text = resdate)
        
class SuccessReservationCancellationFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))
        # NEEDS BACKEND LINK TO AMOUNT
        canvas.create_text(450, 300, text="Reservation Cancelled", fill="black", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to Cancellation Function',command = lambda : controller.show_frame(CancelReservationFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        pass

class CannotCancel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))
        # NEEDS BACKEND LINK TO AMOUNT
        canvas.create_text(450, 300, text="Member cannot cancel", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to Cancellation Function',command = lambda : controller.show_frame(CancelReservationFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        pass

class NoSuchReservationFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))
        # NEEDS BACKEND LINK TO AMOUNT
        canvas.create_text(450, 300, text="Member has no such reservation", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to Cancellation Function',command = lambda : controller.show_frame(CancelReservationFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        pass

        
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
########################################################################
###################        Fines Frames                   ##############
########################################################################
#FineMenuFrame,
#FinePaymentFrame,FailNoFineFrame,FailWrongAmountFrame,PaymentCfmFrame,PaymentSuccessFrame

class FineMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 800, height = 600)
        canvas.grid(columnspan = 5, rowspan = 5)

        # select options
        self.label = ttk.Label(self, text ="Select one of the Options below:", font = LARGEFONT)
        self.label.grid(row = 0, column = 2)
         
        # button to acquire books
        book_borrowing = ttk.Button(self, text ="Fine Payment",
                            command = lambda : controller.show_frame(FinePaymentFrame))
  
        # putting the button in its place by
        # using grid
        book_borrowing.grid(row = 1, column = 2)

        main_menu_btn = ttk.Button(self, text ="Back To Main Menu", width = 20, command = lambda : controller.show_frame(MainMenuFrame))
                            
        main_menu_btn.grid(row = 3, column = 2)

    def refresh(self):
        pass


class FinePaymentFrame(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 800, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)

        MembershipID = tk.StringVar()
        PaymentDate = tk.StringVar()
        PaymentAmount = tk.StringVar()
        
        self.label0 = ttk.Label(self, text='To pay a fine, please enter information below:', font = SMALLFONT)
        self.label0.grid(row = 1, column = 2)
        
        self.label1 = ttk.Label(self, text="                         Membership ID:", font = SMALLFONT,)
        self.label1.grid(row = 3, column = 1)
        textbox1 = ttk.Entry(self, textvariable = MembershipID, font = SMALLFONT)
        textbox1.grid(row = 3, column = 2)

        self.label2 = ttk.Label(self, text="                         Payment Date (dd/mm/yyyy):", font = SMALLFONT,)
        self.label2.grid(row = 4, column = 1)
        textbox1 = ttk.Entry(self, textvariable = PaymentDate, font = SMALLFONT)
        textbox1.grid(row = 4, column = 2)

        self.label2 = ttk.Label(self, text="                         Payment Amount($):", font = SMALLFONT,)
        self.label2.grid(row = 5, column = 1)
        textbox1 = ttk.Entry(self, textvariable = PaymentAmount, font = SMALLFONT)
        textbox1.grid(row = 5, column = 2)
    
        pay_fine_btn = ttk.Button(self, text ="Pay Fine",
                            command = lambda : check_if_can_pay())
        pay_fine_btn.grid(row = 9, column = 1)
        
        loan_menu_btn = ttk.Button(self, text ="Back To Fines Menu",
                            command = lambda : controller.show_frame(FineMenuFrame))
     
        # putting the button in its place by
        # using grid
        loan_menu_btn.grid(row = 9, column = 3)

        def check_if_can_pay():
            hasfine = False
            amountcorrect = False
            global getMemberID
            getMemberID = MembershipID.get()
            MembershipID.set("")
            global extract_member
            extract_member = ()
            global getPaymentAmount
            getPaymentAmount = PaymentAmount.get()
            PaymentAmount.set("")
            global paydate
            paydate = PaymentDate.get()
            PaymentDate.set("")
            cur.execute("select * from Fine")
            output = cur.fetchall()
            flag = False

            for member in output:
                if member[0] == getMemberID:
                    flag = True
            if flag == False:
                return controller.show_frame(NoSuchPersonInFinesFrame)
                
            for member in output:
                if member[0] == getMemberID:
                    extract_member = member
                    hasfine = True
                    flag = True
                    if int(extract_member[1]) == int(getPaymentAmount):
                        amountcorrect = True

            if hasfine == False:
                return controller.show_frame(FailNoFineFrame)
            if amountcorrect == False:
                return controller.show_frame(FailWrongAmountFrame)
            else:
                return controller.show_frame(PaymentCfmFrame)
            
    def refresh(self):
        pass


class NoSuchPersonInFinesFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="No Such Member.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to payment function',command = lambda : controller.show_frame(FinePaymentFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass


class FailNoFineFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Member has no fine.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to payment function',command = lambda : controller.show_frame(FinePaymentFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass


class FailWrongAmountFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Incorrect fine payment amount.", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to payment function',command = lambda : controller.show_frame(FinePaymentFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass


class PaymentCfmFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(columnspan = 5, rowspan = 10)

        self.labeltext = ttk.Label(self, text = "Please confirm details\nto be correct " , font = LARGEFONT)
        self.labeltext.grid(row = 1, column = 2)
        
        self.label0 = ttk.Label(self, text="Payment Due:", font = SMALLFONT,)
        self.label0.grid(row = 2, column = 1)
        
        self.label1 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label1.grid(row = 2, column = 2)
        
        self.label2 = ttk.Label(self, text="Member ID", font = SMALLFONT,)
        self.label2.grid(row = 3, column = 1)
        
        self.label3 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label3.grid(row = 3, column = 2)

        self.label4 = ttk.Label(self, text= "Payment Date", font = SMALLFONT,)
        self.label4.grid(row = 4, column = 1)
        
        self.label5 = ttk.Label(self, text= "xxx", font = SMALLFONT,)
        self.label5.grid(row = 4, column = 2)


        btn1 = ttk.Button(self, text='Return to payment function',command = lambda : controller.show_frame(FinePaymentFrame))
        btn1.place(x=550,y=550)
        

        btn2 = ttk.Button(self, text='Confirm payment',command = lambda : pay_fine())
        btn2.place(x=50,y=550)

        def pay_fine():
            sql = "DELETE FROM Fine WHERE MemberID = %s"
            x = extract_member[0]
            cur.execute(sql,x)
            conn.commit()
            return controller.show_frame(PaymentSuccessFrame)

    def refresh(self):
        self.label1.config(text = "$" + extract_member[1])
        self.label3.config(text = extract_member[0])
        self.label5.config(text = paydate)


class PaymentSuccessFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'limegreen')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Success!", fill="black", font=("RALEWAY",50))

        canvas.create_text(450, 300, text="Fine successfully paid", fill="black", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to payment function',command = lambda : controller.show_frame(FinePaymentFrame))
        btn.place(x=350,y=500)

    def refresh(self):
        pass



############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
########################################################################
###################        Reports    Frames              ##############
########################################################################

#ReportsMenuFrame
#SearchBookFrame
class ReportsMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        label = ttk.Label(self, text ="Select one of the Options below:", font = LARGEFONT)
        label.grid(row = 0, column = 2)

        book_search = ttk.Button(self, text ="Book Search", width = 20, command = lambda : controller.show_frame(SearchBookFrame))
        book_search.grid(row = 2, column = 2)
        
        def popup1(x):
            win = tk.Toplevel()
            for i in range(len(x)):
                for j in range(len(x[0])):
                    self.label1 = ttk.Label(win, text= books_on_loan_with_header[i][j], font = SMALLFONT,)
                    self.label1.config(text = books_on_loan_with_header[i][j])
                    self.label1.grid(row=i, column=j)
            b = ttk.Button(win, text="Back to search function", command=win.destroy)
            b.grid(row=i+1, column=j+1)


        def display_books_on_loan():
            cur.execute("select * from bookupdated")
            output = cur.fetchall()
            books_on_loan = ()
            for book in output:
                if book[12]:
                    books_on_loan += (book,)
            global books_on_loan_with_header
            books_on_loan_with_header = ()
            books_on_loan_with_header += (("Accession Number","Title","Authors","ISBN","Publisher","Year"),)

            for book in books_on_loan:
                    newbook = ()
                    newbook = book[:2] + (book[2] + "," + book[3] + "," + book[4],) + book[5:]
                    books_on_loan_with_header += (newbook,)

            return popup1(books_on_loan_with_header)
            

        book_on_loan = ttk.Button(self, text ="Books on Loan", width = 20, command = lambda : display_books_on_loan())
        book_on_loan.grid(row = 3, column = 2)

        def popup2(x):
            win = tk.Toplevel()
            for i in range(len(x)):
                for j in range(len(x[0])):
                    self.label1 = ttk.Label(win, text= books_with_reservation_with_header[i][j], font = SMALLFONT,)
                    self.label1.config(text = books_with_reservation_with_header[i][j])
                    self.label1.grid(row=i, column=j)
            b = ttk.Button(win, text="Back to search function", command=win.destroy)
            b.grid(row=i+1, column=j+1)


        def display_books_on_reservation():
            cur.execute("select * from bookupdated")
            output = cur.fetchall()
            books_with_reservation = ()
            for book in output:
                if book[13]:
                    books_with_reservation += (book,)
            global books_with_reservation_with_header
            books_with_reservation_with_header = ()
            books_with_reservation_with_header += (("Accession Number","Title","Authors","ISBN","Publisher","Year"),)

            for book in books_with_reservation:
                    newbook = ()
                    newbook = book[:2] + (book[2] + "," + book[3] + "," + book[4],) + book[5:]
                    books_with_reservation_with_header += (newbook,)

            return popup2(books_with_reservation_with_header)

        book_on_reservation = ttk.Button(self, text ="Books on Reservation", width = 20, command = lambda : display_books_on_reservation())
        book_on_reservation.grid(row = 4, column = 2)
        
        def popup3(x):
            win = tk.Toplevel()
            for i in range(len(x)):
                for j in range(len(x[0])):
                    self.label1 = ttk.Label(win, text= x[i][j], font = SMALLFONT,)
                    self.label1.config(text = x[i][j])
                    self.label1.grid(row=i, column=j)
            b = ttk.Button(win, text="Back to search function", command=win.destroy)
            b.grid(row=i+1, column=j+1)


        def display_members_with_fines():
            cur.execute("select * from Fine")
            output = cur.fetchall()
            members_with_fines = ()
            cur.execute("select * from Member")
            memberinfo = cur.fetchall()

            for member in output:
                members_with_fines += (member[0],)

            global members_with_fines_with_header
            members_with_fines_with_header = ()
            members_with_fines_with_header += (("Membership ID", "Name", "Faculty", "Phone Number", "Email Address"),)

            for member in members_with_fines:
                for memberrr in memberinfo:
                    if member == memberrr[0]:
                        newmember = ()
                        newmember = memberrr[0:5]
                        members_with_fines_with_header += ((newmember),)

            return popup3(members_with_fines_with_header)


        outstanding_fine = ttk.Button(self, text ="Outstanding Fines", width = 20, command = lambda : display_members_with_fines())
     
        outstanding_fine.grid(row = 5, column = 2)
        
        book_on_to_member = ttk.Button(self, text ="Books on Loan to Member", width = 20, command = lambda:controller.show_frame(SearchBookBorrowedByMem))
     
        book_on_to_member.grid(row = 6, column = 2)
                
        main_menu_btn = ttk.Button(self, text ="Back To Main Menu", width = 20, command = lambda: controller.show_frame(MainMenuFrame))
     
        main_menu_btn.grid(row = 9, column = 2)
        
    def refresh(self):
        pass

class SearchBookFrame(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.UserInfo = Store_info()
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        InputTitle = tk.StringVar()
        InputAuthors = tk.StringVar()
        InputISBN = tk.StringVar()
        InputPublisher = tk.StringVar()
        InputPublicationYear = tk.StringVar()
        
        label0 = ttk.Label(self, text='Search based on one of the categories below', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Title:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)
        textbox1 = ttk.Entry(self, textvariable = InputTitle, font = SMALLFONT)
        textbox1.grid(row = 2, column = 2)
        
        label2 = ttk.Label(self, text="Authors:", font = SMALLFONT)
        label2.grid(row = 3, column = 1)
        textbox2 = ttk.Entry(self,textvariable = InputAuthors, font = SMALLFONT)
        textbox2.grid(row = 3, column = 2)
        
        label3 = ttk.Label(self, text="ISBN:", font = SMALLFONT)
        label3.grid(row = 4, column = 1)
        textbox3 = ttk.Entry(self, textvariable = InputISBN, font = SMALLFONT)
        textbox3.grid(row = 4, column = 2)
        
        label4 = ttk.Label(self, text="Publisher:", font = SMALLFONT)
        label4.grid(row = 5, column = 1)
        textbox4 = ttk.Entry(self, textvariable = InputPublisher, font = SMALLFONT)
        textbox4.grid(row = 5, column = 2)
        
        label5 = ttk.Label(self, text="Publication Year:", font = SMALLFONT)
        label5.grid(row = 6, column = 1)
        textbox5 = ttk.Entry(self, textvariable= InputPublicationYear ,font = SMALLFONT)
        textbox5.grid(row = 6, column = 2)


        def popupBonus(x):
            win = tk.Toplevel()
            for i in range(len(x)):
                for j in range(len(x[0])):
                    self.label1 = ttk.Label(win, text= x[i][j], font = SMALLFONT,)
                    self.label1.config(text = x[i][j])
                    self.label1.grid(row=i, column=j)
            b = ttk.Button(win, text="Back to search function", command=win.destroy)
            b.grid(row=i+1, column=j+1)
            

        global TitleToSearch
        global AuthorsToSearch
        global ISBNToSearch
        global PublisherToSearch
        global PublicationYearToSearch
        
        def create_book_search_results():
            #create table
            
            TitleToSearch = InputTitle.get()
            InputTitle.set("")
            
            AuthorsToSearch = InputAuthors.get()
            InputAuthors.set("")
            
            ISBNToSearch = InputISBN.get()
            InputISBN.set("")
            
            PublisherToSearch = InputPublisher.get()
            InputPublisher.set("")
            
            PublicationYearToSearch = InputPublicationYear.get()
            InputPublicationYear.set("")
            
            #Make sure one word per box
            
            create_variable = (TitleToSearch,AuthorsToSearch,ISBNToSearch,PublisherToSearch,PublicationYearToSearch)
            flag = True
            for element in create_variable:
                if " " in element or "," in element:
                    flag = False
            if flag == False:
                return controller.show_frame(ErrorOneValueOnlySearchFrame)
            
            if flag == True:
                cur.execute("select * from Book")
                output = cur.fetchall()
                global to_output_books_found
                to_output_books_found = ()
                for book in output:
                    if TitleToSearch:
                        for element in book[1].split():
                            if element == TitleToSearch:
                                if book not in to_output_books_found:
                                    to_output_books_found += (book,)
                        
                    if AuthorsToSearch:
                        for element in book[2].split():
                            if element == AuthorsToSearch:
                                if book not in to_output_books_found:
                                    to_output_books_found += (book,)

                        for element in book[3].split():
                            if element == AuthorsToSearch:
                                if book not in to_output_books_found:
                                    to_output_books_found += (book,)
                                    
                        for element in book[4].split():
                            if element == AuthorsToSearch:
                                if book not in to_output_books_found:
                                    to_output_books_found += (book,)
                                    
                    if ISBNToSearch:
                        for element in book[5].split():
                            if element == ISBNToSearch:
                                if book not in to_output_books_found:
                                    to_output_books_found += (book,)
                                    
                    if PublisherToSearch:
                        for element in book[6].split():
                            if element == PublisherToSearch:
                                if book not in to_output_books_found:
                                    to_output_books_found += (book,)

                    if PublicationYearToSearch:
                        for element in book[7].split():
                            if element == PublicationYearToSearch:
                                if book not in to_output_books_found:
                                    to_output_books_found += (book,)

                global cleaned_output_book_found
                cleaned_output_book_found = ()
                cleaned_output_book_found += (("Accession Number","Title","Authors","ISBN","Publisher","Year"),)
                
                for book in to_output_books_found:
                    newbook = ()
                    newbook = book[:2] + (book[2] + "," + book[3] +","+ book[4],) + book[5:]
                    cleaned_output_book_found += (newbook,)


                #high level search
                    
                return popupBonus(cleaned_output_book_found)
            
    
    
        #create_book_search_results() add in below
        creation_book_search_btn = ttk.Button(self, text ="Search Book", width = 20, command = lambda : create_book_search_results() )
     
        creation_book_search_btn.grid(row = 9, column = 1)
        
        go_reports_menu = ttk.Button(self, text ="Back To Reports Menu", width = 20, command = lambda : controller.show_frame(ReportsMenuFrame))
                            
        go_reports_menu.grid(row = 9, column = 3)

        
        
    def refresh(self):
        pass
        

class ErrorOneValueOnlySearchFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self, width = 900, height = 600, bg = 'red')
        canvas.grid(rowspan = 9)

        canvas.create_text(450, 100, text="Error!", fill="yellow", font=("RALEWAY",50))

        canvas.create_text(450, 300, text= "More than one word provided for search field/attribute", fill="yellow", font=("RALEWAY", 25))

        btn = ttk.Button(self, text='Back to Search Book function', command = lambda : controller.show_frame(SearchBookFrame))
        btn.place(x=350,y=500)
        
    def refresh(self):
        pass
        
class SearchBookBorrowedByMem(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.UserInfo = Store_info()
        canvas = tk.Canvas(self, width = 900, height = 600)
        canvas.grid(columnspan = 5, rowspan = 10)
        
        InputmemID = tk.StringVar()

        label0 = ttk.Label(self, text='Books on Loan to Member', font = SMALLFONT)
        label0.grid(row = 1, column = 2)
        
        label1 = ttk.Label(self, text="Membership ID:", font = SMALLFONT,)
        label1.grid(row = 2, column = 1)
        
        textbox1 = ttk.Entry(self, textvariable = InputmemID, font = SMALLFONT)
        textbox1.grid(row = 2, column = 2)

        def member_search_report(x):
            win = tk.Toplevel()
            for i in range(len(x)):
                for j in range(len(x[0])):
                    self.label1 = ttk.Label(win, text= x[i][j], font = SMALLFONT,)
                    self.label1.config(text = x[i][j])
                    self.label1.grid(row=i, column=j)
            b = ttk.Button(win, text="Back to search function", command=win.destroy)
            b.grid(row=i+1, column=j+1)
            
            
        def create_pop_up_and_query():
            cur.execute("select * from BookUpdated")
            all_bks = cur.fetchall()
            new_tuple = (("Accession Number","Title","Authors","ISBN","Publisher","Year"),)
            for book in all_bks:
                if book[12] == InputmemID.get():
                    newbook = ()
                    newbook = book[:2] + (book[2] +","+ book[3] +","+ book[4],) + book[5:8]
                    new_tuple += (newbook,)
            InputmemID.set("")
            return member_search_report(new_tuple)
            
                    
        search_member_butn = ttk.Button(self, text ="Search Book", width = 20, command = lambda : create_pop_up_and_query() )
     
        search_member_butn.grid(row = 9, column = 1)
        
        go_reports_menu = ttk.Button(self, text ="Back To Reports Menu", width = 20, command = lambda : controller.show_frame(ReportsMenuFrame))
                            
        go_reports_menu.grid(row = 9, column = 3)
    def refresh(self):
        pass
        
app = LibraryApp()
app.mainloop()

