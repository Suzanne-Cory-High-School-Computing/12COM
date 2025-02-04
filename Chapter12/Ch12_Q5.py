lines = [line.strip() for line in open('namelist.txt')]
match = input('Enter the initials: ')
count = 0

for line in lines:
    name = line.split(' ')
    if(len(name) == 2): #two names
        fname = name[0]
        mname = ""
        lname = name[-1]
#        print('The current name is',fname,lname,'with',len(name),'words')
#        print('Matching fname[0] of',fname[0],'with match[0] of',match[0])
#        print('Matching lname[0] of',lname[0],'with match[-1] of',match[-1])
    else: #three names
        fname = name[0]
        mname = name[1]
        lname = name[-1]
#        print('The current name is',fname,mname,lname,'with',len(name),'words')
#        print('Matching fname[0] of',fname[0],'with match[0] of',match[0])
#        print('Matching mname[0] of',mname[0],'with match[1] of',match[1])
#        print('Matching lname[0] of',lname[0],'with match[-1] of',match[-1])

#    print('The length of the initials to match is',len(match))
    if(len(match)==2 and fname[0]==match[0] and lname[0]==match[-1]): #two initials two names
        count += 1
        print(fname,mname,lname,'matches the initials',match)
    elif(len(match)==3 and len(name)==3):
         if(fname[0]==match[0] and mname[0]==match[1] and lname[0]==match[-1]): #three initials three names
            count += 1
            print(fname,mname,lname,'matches the initials',match)

'''
if(count>0):
    print(count,'matches for the initials',match)
else:
    print('No matches for the initials',match)
'''