#lab 10 menu
import LAB10A
#import LAB10B


def mmenu():
    while(True):
        mm_choice=input("Enter a or b to choose he system ou want to work with\na. IP system\nb. DNS system\nq. if you want to quit\nenter your choice: ")
        if (mm_choice=="a"):
            LAB10A.amenu()
        elif(mm_choice=="b"):
            print("DNS")
        elif(mm_choice=="q"):
            break
        else:
            print("invalid choice, please enter a or b, q to quit")
    print("Thank you for using our system\nlogging out")