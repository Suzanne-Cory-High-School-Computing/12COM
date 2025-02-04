for i in range(1,201):
    if(i%5==2): #2 left over when split evenly among 5 people
        if(i%6==3): #3 left over when split evenly among 6 people
            if(i%7==2): #2 left over when split evenly among 7 people
                print('There are',i,'pieces in the bowl.')