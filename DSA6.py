#Write a Python program to store first year percentage of students in array. Write
#function for sorting array of floating point numbers in ascending order using quick sort
#and display top five scores



def inperc():
    perc=[]
    n=int(input("Enter the number of students: "))
    for i in range(n):
        perc.append(float(input("Enter the percentage of student {0}: ".format(i+1))))
    return perc

def outperc(perc):
    for i in range(len(perc)):
        print(perc[i], sep = "\n")   #sep means seperator, just like "\t" it is used

def perpartition(perc,start,end):
    pivot = perc[start]
    lower_bound=start+1
    upper_bound=end
    while True:
        while lower_bound <=upper_bound and perc[lower_bound] <= pivot:
            lower_bound +=1
        while lower_bound <= upper_bound and perc[upper_bound] >=pivot:
            upper_bound -=1
        if lower_bound <=upper_bound:
            perc[lower_bound], perc[upper_bound] = perc[upper_bound], perc[lower_bound]
        else:
            break
    perc[start], perc[upper_bound]=perc[upper_bound], perc[start]
    return upper_bound

def quicksort(perc,start,end):
    while start < end:
        partition = perpartition(perc,start,end)
        quicksort(perc,start, partition-1)
        quicksort(perc,partition+1,end)
        return perc
op=1
unsortedperc = []
sortedperc = []
while(op==1):
    print("\n..........MENU.............")
    print("\n1. Accept the percentage of students")
    print("\n2. Display the percentage of students")
    print("\n3. Perform quick sort on the data")
    print("\nEnter your choice: ")
    ch=int(input())
    if(ch==1):
        unsortedperc = inperc()
        break
    elif(ch==2):
        outperc(unsortedperc)
        break
    elif(ch==3):
        print("Percentage of students after performing quick sort: ")
        sortedperc=quicksort(unsortedperc,0,len(unsortedperc)-1)
        outperc(sortedperc)
        break
    else:
        print("WRONG CHOICE!!!!")
    print("Do you want to perfomr again? IF yes press 1 else 0: ")
    op=int(input())    
