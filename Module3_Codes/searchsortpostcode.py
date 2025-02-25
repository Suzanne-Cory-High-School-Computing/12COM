from tkinter import *

# list containing postcodes
postcode_arr = []

# list containing sorted postcodes
postcode_arr_sorted = []

def process_file():
    input_file = "vic_postcodes_w.csv"
    between_chars = ","
    
    lines = [line.strip() for line in open(input_file)]

    for line in lines:
        entry = line.split(between_chars)
        print('line is: ',entry)
        print('postcode is: ',entry[0])
        postcode_arr.append(entry[0])
        output_label0.configure(text='{} has been loaded.'.format(input_file))

    print('Postcodes loaded: ',postcode_arr)


def linearsearch_postcode():
    postcode = entry1.get()
    found = 0
    found_indices = []

    print('The postcode being searched is',postcode)
    for i in range(len(postcode_arr)): # linear search
        if postcode_arr[i] == postcode:
            found = 1
            found_indices.append(i)
            print('Postcode',postcode,'has been found at index',i)

    if found == 0:
        print('Postcode',postcode,'not found.')
        output_label1.configure(text='Postcode {} not found.'.format(postcode))
    else:
        if len(found_indices)==1:
            output_label1.configure(text='Postcode {} has been found at index {}'.format(postcode,found_indices[0]))
        else:
            found_text = ""
            found_text += str(found_indices[0])
            for i in range(1,len(found_indices)):
                found_text += ","
                found_text += str(found_indices[i])
                output_label1.configure(text='Postcode {} has been found at the following indices: {}'.format(postcode,found_text))

def selection_sort():
    postcode_arr_sorted = postcode_arr
    for i in range(len(postcode_arr_sorted)):
        smallest = i
        for k in range (i+1,len(postcode_arr_sorted)):
            if postcode_arr_sorted[k] < postcode_arr_sorted[smallest]:
                smallest = k
        if smallest != i:
            temp = postcode_arr_sorted[smallest]
            postcode_arr_sorted[smallest] = postcode_arr_sorted[i]
            postcode_arr_sorted[i] = temp
    print('The sorted list is: ',postcode_arr_sorted)
    output_label2.configure(text='The postcode list has been sorted.')
    
root = Tk()

message_label0 = Label(text = 'Click PROCESS FILE to load postcodes',font=('Arial',16))
output_label0 = Label(font=('Arial',12))
process_button = Button(text='PROCESS FILE',font=('Arial',14), command=process_file)
message_label1 = Label(text = 'Postcode: ',font=('Arial',16))
entry1 = Entry(font=('Arial',14),width=10)
search_button = Button(text='START SEARCH', font=('Arial',14), command=linearsearch_postcode)
output_label1 = Label(font=('Arial',12))
selection_sort_button = Button(text='START SORT', font=('Arial',14), command=selection_sort)
output_label2 = Label(font=('Arial',12))

message_label0.grid(row=0,column=0,columnspan=2)
process_button.grid(row=0,column=2, columnspan=2)
output_label0.grid(row=1,column=0,columnspan=2)
message_label1.grid(row=2,column=0)
entry1.grid(row=2, column=1)
search_button.grid(row=3, column=1)
output_label1.grid(row=4, column=0, columnspan=4)
selection_sort_button.grid(row=5,column=1)
output_label2.grid(row=6,columnspan=4)

mainloop()