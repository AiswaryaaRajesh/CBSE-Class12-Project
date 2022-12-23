''' Board ROll Number - 14646472
    Name - Aiswaryaa Rajesh
    Class - 12F
    Project Team - Anhad Khurana, Saarthak Pant
'''


import pickle
import os

#1)Create a Record
def create_rec():
    f = open("criminaldb.dat","wb")
    ftxt = open("number.txt","w")
    ftxt.write('1000')
    ftxt.close()
    crimid = 1000
    while True:
        d = {}
        crimid+=1
        l=[]
        name = input("Name : ")
        l.append(name)
        age = input("Age : ")
        l.append(age)
        gender = input("Gender : ")
        l.append(gender)
        eyecol = input("Eye Colour : ")
        l.append(eyecol)
        print("** Enter all date in the format \"dd-mm-yyyy\" **")
        DOB = input("Date of Birth : ")
        l.append(DOB)
        DOA = input("Date of Admission : ")
        l.append(DOA)
        crime = input("Offense Type : ")
        l.append(crime)
        location = input("Location of Crime : ")
        l.append(location)
        term = input("Term : ")
        l.append(term)
        reldate = input("Release Date : ")
        l.append(reldate)
        DOD = input("Current Status (Alive/Dead/Not Known) : ")
        l.append(DOD)
        d[crimid]=l
        print(d)
        pickle.dump(d,f)
        ch=input("Do you want to enter more records(yes/no): ")
        print()
        ch = ch.lower()
        if ch=='no':
            print()
            break
    f.close()
    ftxt=open("number.txt","w")
    ftxt.write(str(crimid))
    ftxt.close()

#2)Append a Record
def append_rec():
    f=open("student.dat","ab")
    ftxt=open("number.txt","r+")
    crimid=int(ftxt.read())
    
    while True:
        d={}
        crimid+=1
        l=[]
        name = input("Name : ")
        l.append(name)
        age = input("Age : ")
        l.append(age)
        gender = input("Gender : ")
        l.append(gender)
        eyecol = input("Eye Colour : ")
        l.append(eyecol)
        print("** Enter all date in the format \"dd-mm-yyyy\" **")
        DOB = input("Date of Birth : ")
        l.append(DOB)
        DOA = input("Date of Admission : ")
        l.append(DOA)
        crime = input("Offense Type : ")
        l.append(crime)
        location = input("Location of Crime : ")
        l.append(location)
        term = input("Term : ")
        l.append(term)
        reldate = input("Release Date : ")
        l.append(reldate)
        DOD = input("Current Status (Alive/Dead/Not Known) : ")
        l.append(DOD)
        d[crimid]=l
        print(d)
        pickle.dump(d,f)
        ch=input("Do you want to enter more records(yes/no): ")
        print()
        ch = ch.lower()
        if ch=='no':
            print()
            break
    f.close()
    ftxt.seek(0)
    ftxt.write(str(crimid))
    ftxt.close()

#3) Display all Records
def display_all_rec():
    f = open("criminaldb.dat","rb")
    try:
        while True:
            d=pickle.load(f)
            for i in d:
                print("Criminal ID is ",i)
                print("Name is ",d[i][0])
                print("Age is ",d[i][1])
                print("Gender is ",d[i][2])
                print("Eye Colour is ",d[i][3])
                print("Date of Birth is ",d[i][4])
                print("Date of Admission is ",d[i][5])
                print("Offense Type is ",d[i][6])
                print("Location of Crime is ",d[i][7])
                print("Term is ",d[i][8])
                print("Date of release is ",d[i][9])
                print("Current Status is ",d[i][10])
                print()
            
    except EOFError:
        pass
    finally:
        f.close()

#4) Search Record by Current Status
def curstat_search_rec():
    if not os.path.isfile("criminaldb.dat"):   
        print("  File Not Found!! ")
    else:
        f=open("criminaldb.dat","rb")
        crs=input("Enter Current Status: ")
        crs=crs.lower()
        print()
        flag=0
        try:
            while True:
                d=pickle.load(f)
                for i in d:
                    if d[i][10].lower()==crs:
                        flag=1
                        print("Criminal ID is ",i)
                        print("Name is ",(d[i][0]))
                        print("Age is ",(d[i][1]))
                        print("Gender is ",(d[i][2]))
                        print("Eye Colour is ",(d[i][3]))
                        print("Date Of Birth is ",(d[i][4]))
                        print("Date Of Admission is ",(d[i][5]))
                        print("Offence Type is ",(d[i][6]))
                        print("Location Of Crime is ",(d[i][7]))
                        print("Term is ",(d[i][8]))
                        print("Release Date is ",(d[i][9]))
                        print("Current Status is ",(d[i][10]))
                        print()
                
        except EOFError:
            if flag==0:
                print("Current Status Not Found")
        finally:f.close()

#5)Search by Eye Colour
def eyecol_search_rec():
    if not os.path.isfile("criminaldb.dat"):   
        print("File Not Found!!")
    else:
        f = open("criminaldb.dat","rb")
        eyecol = input("Enter eye colour : ")
        eyecol.lower()
        print()
        flag=0
        try:
            while True:
                d=pickle.load(f)
                for i in d:
                    chk=d[i][3].lower()
                    if chk==eyecol:
                        flag=1
                        print("Criminal ID is ",i)
                        print("Name is ",d[i][0])
                        print("Age is ",d[i][1])
                        print("Gender is ",d[i][2])
                        print("Eye Colour is ",d[i][3])
                        print("Date of Birth is ",d[i][4])
                        print("Date of Admission is ",d[i][5])
                        print("Offense Type is ",d[i][6])
                        print("Location of Crime is ",d[i][7])
                        print("Term is ",d[i][8])
                        print("Date of release is ",d[i][9])
                        print("Current Status is ",d[i][10])
                        print()
        except EOFError:
            if flag==0:
                print("Sorry Eye Colour Not Found")
        finally:
            f.close()

#6)Search Record by Name
def name_search_rec():
    if not os.path.isfile("criminaldb.dat"):   
        print("  File Not Found!! ")
    else:
        f=open("criminaldb.dat","rb")
        nm=input("Enter Name: ")
        nm=nm.lower()
        flag=0
        try:
            while True:
                d=pickle.load(f)
                for i in d:
                    if d[i][0].lower()==nm:
                        flag=1
                        print("Criminal ID is ",i)
                        print("Name is ",(d[i][0]))
                        print("Age is ",(d[i][1]))
                        print("Gender is ",(d[i][2]))
                        print("Eye Colour is ",(d[i][3]))
                        print("Date Of Birth is ",(d[i][4]))
                        print("Date Of Admission is ",(d[i][5]))
                        print("Offence Type is ",(d[i][6]))
                        print("Location Of Crime is ",(d[i][7]))
                        print("Term is ",(d[i][8]))
                        print("Release Date is ",(d[i][9]))
                        print("Current Status is ",(d[i][10]))
                
        except EOFError:
            if flag==0:
                print("Sorry Name Not Found")
        finally:f.close()

#7)Search Record by Crime Committed
def crimecomm_search_rec():
    if not os.path.isfile("criminaldb.dat"):   
        print("File Not Found!!")
    else:
        f = open("criminaldb.dat","rb")
        comm = input("Enter crime committed : ")
        comm.lower()
        print()
        flag=0
        try:
            while True:
                d=pickle.load(f)
                for i in d:
                    chk=d[i][6].lower()
                    if chk==comm:
                        flag=1
                        print("Criminal ID is ",i)
                        print("Name is ",d[i][0])
                        print("Age is ",d[i][1])
                        print("Gender is ",d[i][2])
                        print("Eye Colour is ",d[i][3])
                        print("Date of Birth is ",d[i][4])
                        print("Date of Admission is ",d[i][5])
                        print("Offense Type is ",d[i][6])
                        print("Location of Crime is ",d[i][7])
                        print("Term is ",d[i][8])
                        print("Date of release is ",d[i][9])
                        print("Current Status is ",d[i][10])
                        print()
        except EOFError:
            if flag==0:
                print("Thankfully that crime has not been committed yet")
        finally:
            f.close()

#8)Modify Current Status of a Record
def modify_current_status():
    f1=open("criminaldb.dat","rb")
    f2=open("temp.dat","wb")
    cid=int(input("Enter Criminal ID which has to be modified : "))
    ds=input("Change Current Status to : ")
    print()
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            if cid in d:
                d[cid][10]=ds 
                flag=1
                pickle.dump(d,f2)
            else:
                    pickle.dump(d,f2)
            print(d)
    except EOFError:
        if flag==0: 
            print("Criminal ID not found!")
    finally:
        f1.close()
        f2.close()
    os.remove("criminaldb.dat")
    os.rename("temp.dat","criminaldb.dat")

#9) Modify Name of a Record
def modify_name():
    f1=open("criminaldb.dat","rb")
    f2=open("temp.dat","wb")
    cid=int(input("Enter Criminal ID which has to be modified : "))
    ds=input("Change Name to : ")
    print()
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            if cid in d:
                d[cid][0]=ds 
                flag=1
                pickle.dump(d,f2)
            else:
                    pickle.dump(d,f2)
            print(d)
    except EOFError:
        if flag==0: 
            print("Criminal ID not found!")
    finally:
        f1.close()
        f2.close()
    os.remove("criminaldb.dat")
    os.rename("temp.dat","criminaldb.dat")

#10) Delete a Record
def delete_rec():
    f1=open("criminaldb.dat","rb")
    f2=open("temp.dat","wb")
    crimid = input("Enter Criminal ID whose records have to be deleted : " )
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            for i in d:
                if crimid==d[i][0]:
                    flag=1
                    print("Record Deleted")
                else:
                    pickle.dump(d,f2)
    except EOFError:
        if flag==0: 
            print("Criminal ID not found")
    finally:
        f1.close()
        f2.close()

#11) Main Menu
def main():
    while True:
        print("1 => Create Record")
        print("2 => Append Record")
        print("3 => Display all Records")
        print("4 => Search Record by Current Status")
        print("5 => Search Record by Eye Colour")
        print("6 => Search Record by Name")
        print("7 => Search by Crime Committed")
        print("8 => Modify Record by Current Status")
        print("9 => Modify Record by Name")
        print("10 => Delete Record")
        print("11 => Exit")
        ch = input("Enter your choice: ")
        if ch=='1':
            create_rec()
        elif ch=='2':
            append_rec()
        elif ch=='3':
            display_all_rec()
        elif ch=='4':
            curstat_search_rec()
        elif ch=='5':
            eyecol_search_rec()
        elif ch=='6':
            name_search_rec()
        elif ch=='7':
            crimecomm_search_rec()
        elif ch=='8':
            modify_current_status()
        elif ch=='9':
            modify_name()  
        elif ch=='10':
            delete_rec()
        elif ch=='11':
            break
        else:
            print("invalid choice")
main()
