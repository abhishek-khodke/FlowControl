emp_list = [{"id":1, "name":"abc", "salary":75000}, {"id":2, "name":"xyz", "salary":45000}, {"id":3, "name":"pqr", "salary":95000}]

# inp = input("Enter your choice:-user_name/user_id:-")
# user_name = (input("Enter a emp name:- ")) 
# user_id = int(input("Enter a emp id:-"))
# inp = input("Enter your choice:-user_name/user_id")
   

while True: 
    user_name = (input("Enter a emp name:- "))
    user_id = int(input("Enter a emp id:-")) 
    for d in emp_list:
        if d.get("name") == user_name:
            print(f'''Emp Name:- {d.get("name")}
Emp ID:- {d.get("id")}
Emp Salary:- {d.get("salary")}
''')        
       
    inp = input("Would you like to continue:- Y/N ")  # Y or N

    if inp.lower() in ["y", "yes"]:
        pass
    else:
        print("Thank you for using application.")
        break



