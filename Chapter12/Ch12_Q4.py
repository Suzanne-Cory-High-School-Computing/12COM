lines = [line.strip() for line in open('students.txt')]
f = open('students2.txt','w')

for line in lines:
    entry = line.split("\t")
    fullname = entry[0].split(' ')
    firstname = fullname[0].capitalize()
    lastname = fullname[-1].capitalize()
    email = entry[1]
    number = entry[-1]
    print('First name: ',firstname,'Last name: ',lastname,'Email: ',email,'Number: ',number,file=f)