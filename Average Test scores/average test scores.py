#Isaac Arthur
#9/18
import math

def test_avg():
    test1=float(input("What was your first test score? "))
    test2=float(input("What was your second test score? "))
    test3=float(input("What was your third test score? "))
    test4=float(input("What was your fourth test score? "))
    test5=float(input("What was your fith test score? "))
    test6=float(input("What was your sixth test score? "))
    test7=float(input("What was your seventh test score? "))
    test8=float(input("What was your eighth test score? "))
    test9=float(input("What was your ninth test score? "))
    test10=float(input("What was your tenth test score? "))

    lrg_num=test1+test2+test3+test4+test5+test6+test7+test8+test9+test10
    avgtest= lrg_num/10
    print("Your avarage test score is",avgtest)
    return avgtest


test_avg()
    
