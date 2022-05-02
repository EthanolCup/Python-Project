#Author: Dalvin Wray
#Date Created: April 7, 2022
#Course: ITT103
#Purpose: The purpose of this program is to calculate and print the commision recieved by a sales person at JamEx Limited.


#Importing the CSV library and writer package from the csv library to store the data that will be calculated. 
import csv
from csv import writer

def genesis(trigger = "Start"):

    #Creation of a CSV file 
    filename= 'JamExLimited Commissions.csv'
    headers=['Sales Person Number','Class','Commision']
    with open(filename, 'w') as file:
        w = csv.writer(file) 
        w.writerow(headers)
    
    while trigger=="Start":
        
        print("Hello!!!! please input the required information to calculate the sales person's commision.")
        print('\n')
        print("At the end of the program you may return to the folder that you launched the program from \n to find a CSV file containing the commisions that were calculated")
        print('\n')
        Class = int(input("Please input the sales person's class here: "))
        sales_amt = int(input("Please input the sales person's sales amount here: "))
        sales_pers_num = int(input("Please input the sales person's number here: "))
        class1a = sales_amt * .06
        class1b = sales_amt * .07
        class1c = sales_amt * .10
        class2a = sales_amt * .04
        class2b = sales_amt * .06
        class3a = sales_amt * .045

        #This part of the program will calculate the commission as long as the inputs are valid
        if Class <= 3 and  Class >=1:
            if Class == 1:
                if sales_amt <= 1000:
                    print("{} from Class {} should recieve {}".format(sales_pers_num,Class,class1a))
                    #This part of the code will attach the calulation along with the Class and sales person's number to the csv file
                    with open(filename, 'a',newline='') as cfile:
                        writer_object = writer(cfile)
                        writer_object.writerow([sales_pers_num,Class,class1a])
                        cfile.close
                
                elif sales_amt > 1000 and sales_amt < 2000:
                    print("{} from Class {} should recieve {}".format(sales_pers_num,Class,class1b))
                    #This part of the code will attach the calulation along with the Class and sales person's number to the csv file
                    with open(filename, 'a',newline='') as cfile:
                        writer_object = writer(cfile)
                        writer_object.writerow([sales_pers_num,Class,class1b])
                        cfile.close
                
                elif sales_amt >= 2000:
                    print("{} from Class {} should recieve {}".format(sales_pers_num,Class,class1c))
                    #This part of the code will attach the calulation along with the Class and sales person's number to the csv file
                    with open(filename, 'a',newline='') as cfile:
                        writer_object = writer(cfile)
                        writer_object.writerow([sales_pers_num,Class,class1c])
                        cfile.close
            
            elif Class == 2:
                if sales_amt < 1000:
                    print("{} from Class {} should recieve {}".format(sales_pers_num,Class,class2a))
                    #This part of the code will attach the calulation along with the Class and sales person's number to the csv file
                    with open(filename, 'a',newline='') as cfile:
                        writer_object = writer(cfile)
                        writer_object.writerow([sales_pers_num,Class,class2a])
                        cfile.close
                elif sales_amt >= 1000:
                    print("{} from Class {} should recieve {}".format(sales_pers_num,Class,class2b))
                    #This part of the code will attach the calulation along with the Class and sales person's number to the csv file
                    with open(filename, 'a',newline='') as cfile:
                        writer_object = writer(cfile)
                        writer_object.writerow([sales_pers_num,Class,class2b])
                        cfile.close
            
            elif Class == 3:
                print("{} from Class {} should recieve {}".format(sales_pers_num,Class,class3a))
                #This part of the code will attach the calulation along with the Class and sales person's number to the csv file
                with open(filename, 'a',newline='') as cfile:
                    writer_object = writer(cfile)
                    writer_object.writerow([sales_pers_num,Class,class3a])
                    cfile.close
            
            #This part of the code will either end the code or continue it based on the user's input
            terminator = input("If you wish to stop the programme type 'Yes', if not press the Enter Key to Continue: ")
            if terminator == "Yes":
                break
            elif terminator == "yes":
                break
            elif terminator == "YES":
                break
        else:
            print("ERROR!!!! INVALID CLASS TRY AGAIN")   

    print("You will find the csv file in the same folder you launched this program from")
    print("Please rename it after the program is finished so that when you run the program again it does not overwrite it")
    print('\n')
    print("Have an Awesome Day!!!!") 
genesis()
