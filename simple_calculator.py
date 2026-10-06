#task 1-- simple calculator
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.
while True:
          
         while True:
                print("1.Addition")
                print("2.Subtraction")
                print("3.Multiplication")
                print("4.Division")
                operator=input("select the operator 1/2/3/4  ") #select operator
                if operator== "1" or operator== "2" or operator== "3" or operator== "4": #if user select above operators
                      break  #break loop 
                else:
                      print("invalid operator")
                      continue  
                
                
         number_1=float(input("Enter 1st number "))  # first number for calculation
         number_2=float(input("Enter 2nd number "))  # second number for calculation
     

         if(operator=="1"): 
                print(number_1 ,"+",number_2,"=",number_1+number_2)  #addition
         elif(operator=="2"):  
                print(number_1 ,"-",number_2,"=",number_1-number_2)   #subtraction
         elif(operator=="3"):
                print(number_1 ,"*",number_2,"=",number_1*number_2)  #multiplication
         elif(operator=="4"):
                print(number_1 ,"/",number_2,"=",number_1/number_2) #division
         else:
                print("Invalid operator please enter correct opeartor")    
               
         choice=input("do you want next calculation, yes/no  ")  # user want next calculation
         if choice!="no": 
            continue
         else:
            print(" Thankyou for using calculator \n calculator closed!")
            break 