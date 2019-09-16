import Student 
class Mark(Student) :
    try:
        def __init__(self,prn,rolln,name,block,dob,contact,email,markoot,markcnt):#constructor
            Student.__init__(self,prn,rolln,name,block,dob,contact,email)
            self.__marklist={"OOT":markoot,"CN":markcnt}
    except:
        print("Not valid data")
    def __del__(self):
        Mark.noofstudents-=1
    @property 
    def marklist(self):
        return self.__marklist
    @marklist.setter 
    def marklist(self,markoot,markcnt):
        if (markoot < 100 and markoot > 0) and (markcnt > 0 and markcnt < 100):
            self.__marklist={"OOT":markoot,"CN":markcnt}
        else:
            print("These are invalid marks")        
    
    def printmarks(self):
        print("Marks in OOT are:"+str(self.marklist.get("OOT")))
        print("Marks in CN:"+str(self.marklist.get("CN")))
def insertion():#function for inserting object in list as well as creating objects 
    try:
        studentsprn=int(input("Enter the prn number"))
        if studentsprn == None or studentsprn <= 0 :
            print("Invalid PRN")
            insertion()            
        studentsrolln = int(input("Enter the Roll Number : "))
        if studentsrolln ==None or studentsrolln <= 0 :
            print("Invalid Roll no.")
            insertion() 
        studentsname = input("Enter the Name : ")
        if studentsname == None or studentsname.isalpha() == False :
            print("Invalid Name")
            insertion()  
        studentsblock = int(input("Enter the Block number :B"))
        studentsblock = "B"+str(studentsblock)
        dobd=int(input("Enter day of birth"))
        dobm=int(input("Enter the month in number"))
        doby=int(input("Enter the year"))
        if dobd > 31 or dobd < 1 or dobm > 12 or dobm < 1 or doby > 2018 :
            print("Invalid date")
            insertion()
        studentsdob=str(dobd)+"/"+str(dobm)+"/"+str(doby)
        studentscontact = int(input("Enter the Contact Number : "))
        if studentscontact != None and studentscontact > 1000000000 and studentscontact < 9999999999:
            studentsemail = input("Enter the E-mail address : ")
        else:
            print("invalid contact")
            insertion()            
        if re.match(r"\S+1@\S.+[a-z]",studentsemail)==False : 
            print("invalid email")
            insertion()
        marksoot=int(input("Marks obtained in oot"))
        markscnt=int(input("Marks obtained in cnt"))
        if (marksoot < 100 and marksoot > 0) and (markscnt > 0 and markscnt < 100):
            studlist.append(Mark(studentsprn,studentsrolln,studentsname,studentsblock,studentsdob,studentscontact,studentsemail,marksoot,markscnt))
        else:
            print("Invalid marks reenter marks")
    except:
        print("Re enter the values Something went wrong!")
        insertion()
updatesucc=0
studlist = []
def main():#main function
    choice= 0
    while choice != 7:
        print ('1.Insert \n 2.Delete \n 3.Update \n 4.Search \n 5.Print all \n 6.Total no. of Students\n 7.Print marks of students \n 8.Exit' )#menu
        choice = int(input("\nEnter your choice : "))
        if choice == 1:
            addStudents = int(input("Enter how many students you want : "))
            for objec in range(addStudents):
                insertion()
        elif choice == 2:#Deletion code            
            print("1.Delete by prn \n 2.Delete by Roll Number \n ")#deletion menu
            deletechoice =  input("Enter your choice : ")
            if deletechoice == 1:#delete by PRN
                id = int(input("\nEnter the PRN : "))
                for objec in studlist:                
                    if objec.prn == id:
                        studlist.remove(objec)
            elif deletechoice == 2:#delete by roll no.
                deleteid = int(input("\nEnter the Roll Number : "))            
                for objec in studlist:
                    if objec.rolln == deleteid:
                        studlist.remove(objec)
            else: print("Invalid choice")                
        elif choice == 3: #updation 
            updateastudent = int(input("\nEnter the PRN : "))        
            for objec in studlist:
                if objec.prn == updateastudent: #updatemenu
                    print(" \n 1.PRN \n 2.Roll Number \n 3.Name \n 4.Block \n 5.Contact \n 6.E-mail \n 7.Date of Birth \n 8.College name \n 9.marks \n 10. back")
                    updatechoice = int(input("\nEnter your choice : "))
                    if updatechoice == 1:#update PRN
                        try:
                           newprn = int(input("\nEnter new PRN : "))
                           objec.prn = newprn
                           print("Updation successful")
                           objec.printmembers()
                        except:
                           print("Invalid data") 
                    elif updatechoice == 2:#update Rollno.
                        try:
                            newrolln = int(input("\nEnter new Roll Number : "))
                            objec.rolln = newrolln
                            print("Updation successful")
                            objec.printmembers()
                        except :
                            print("Something went wrong")
                    elif updatechoice == 3:#Update Name
                        try:
                            newname = input("\nEnter new Name : ")
                            objec.name = newname
                            print("Updation successful")
                            objec.printmembers()
                        except:
                            print("Something went wrong")
                    elif updatechoice == 4:#update Block
                        try :
                            newblock = input("\nEnter new Block : ")
                            objec.block = newblock
                            print("Updation successful")
                            objec.printmembers()
                        except :
                            print("Invalid data")
                    elif updatechoice == 5:#update contact no.
                        newcontact = input("\nEnter new Contact Number : ")
                        objec.contact = newcontact
                        print("Updation successful")
                        objec.printmembers()
                    elif updatechoice == 6:#update Email
                        newemail = input("Enter new E-mail : ")
                        objec.email = newemail
                        print("Updation successful")
                        objec.printmembers()
                    elif updatechoice == 7:#update Date of Birth
                        dobd=int(input("Enter day of birth"))
                        dobm=int(input("Enter the month in number"))
                        doby=int(input("Enter the year"))
                        if dobd > 31 or dobd < 1 or dobm > 12 or dobm < 1 or doby > 2018 :
                            print("Invalid date")
                        else:
                            studentsdob=str(dobd)+str(dobm)+str(doby)
                            objec.dob=studentsdob
                            print("Updation successful")
                            objec.printmembers()
                    elif updatechoice == 8:#update College name
                        clgna=input("Enter the college name:")
                        Mark.upclgname(clgna)
                    elif updatechoice == 9:#update Marks
                        markch=int(input("Which subject's marks do you have to update: \n 1. OOT 2. CN "))
                        if markch == 1 :
                            upmark=int(input("Enter the updated marks"))
                            if upmark > -1 and upmark < 101:
                                upmark={"OOT":upmark}
                                objec.marklist.update(upmark)
                            else:
                                print("Invalid marks")
                        elif markch == 2 :
                            upmark=int(input("Enter the updated marks"))
                            if upmark > -1 and upmark < 101:
                                upmark={"CN":upmark}
                                objec.marklist.update(upmark)
                            else:
                                print("Invalid marks")
                        else:
                            print("invalid choice")
                    elif updatechoice == 10:
                        main()                        
                    else: print ("Invalid Choice")
        elif choice == 4:#Searching Code
            print ("1.Search by PRN \n    2.Search by Name \n    3.Search by contact ")#searching menu
            choices = int(input("Enter your choice : "))
            if choices == 1:# Searching by PRN
                sprn = int(input("Enter the PRN : "))
                for objec in studlist:                
                    if objec.prn == sprn:
                        objec.printmembers()                    
            elif choices == 2:# Searching by Name
                 sname = input("Enter the Name of User :")            
                 for objec in studlist:
                    if objec.name == sname: objec.printmembers()
            elif choices == 3: #Searching by Contact 
                 searchcontact = input("Enter the Contact Number of student: ")
                 for objec in studlist:
                    if objec.contact == searchcontact: objec.printmembers()
        elif choice == 5:#Printing all The students
            print("Total no. of Students are :"+Student.numos()+"Students are:") 
            for objec in studlist:
                objec.printmembers()
                objec.printmarks()
            print("College Name:"+objec.collegename)
            print("Total no. of students:"+str(objec.noofstudents))
        elif choice == 6:
            objec.numos()
        elif choice == 7:
            sprn = int(input("Enter the PRN : "))
            for objec in studlist:                
                if objec.prn == sprn:
                    objec.printmarks()
        elif choice == 8: break    
        else :
            print('Invalid Choice')
main()