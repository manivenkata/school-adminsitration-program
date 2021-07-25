#School Administration Program

import csv

def write_info_csv(info_list):
    with open("student_info.csv","a",newline="")as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell()==0: 
            writer.writerow(["name","age","contact_number","email_id"])
       
        writer.writerow(info_list)
 
if __name__ == "__main__": 
    condition = True 
    student_num = 1 
    while(condition): 
        student_info = input("enter the #{} student information in the form of name, age, contact_number, email_id:".format(student_num)) 
       
        student_info_list = student_info.split(" ") 
        
        print("\nentered information is:-\nname:- {}\nage:- {}\ncontact_number:- {}\nemail_id:-".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3])) 
        
        choice_check = input("check your details are correct\n if correct type yes if not no:-") 
        
        if choice_check == "yes": 
            write_info_csv(student_info_list) 
            
            condition_check = input("if you want to give the another student information type yess if not no:-") 
            if condition_check == "yes": 
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
            else: 
                choice_check == "no" 
                print("re-enter the student info:")
