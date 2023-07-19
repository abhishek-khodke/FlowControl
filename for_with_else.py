min = int(input("Enter min range: "))  
max = int(input("Enter max range: "))  
  
for num in range(min,max + 1):  
   if num > 2:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
            print(num) 