#Created by Isak Anderson 2022

#The objective of this code is to ask a user for a promt but if they skip the awnser then use the default value which is part of the function already.

#If an option is not optional then you can insert a '*' anywhere in the value of the key value pair to make it required.

#Example function which takes arguments but has default values
from posixpath import split


def printer(age, width=4,height=3):
    print(int(age),width,height)


#This function is seperated out to show by its self.
def stringToDict(string):
    dictionary = {}
    split_string = string.split(',')
    for item in split_string:
        split_item = item.split(':',1)
        key = split_item[0]#.strip(' ')
        value = split_item[1]
        dictionary[key] = value
    return dictionary

# Main Function
def UserInput(string):
    dictionary = stringToDict(string)
    checker = {}
    for i in dictionary.copy():

        checker[i] = dictionary[i]
        dictionary[i] = input(dictionary[i])

        check = '*' in checker[i]

        if dictionary[i] == '':
            if check:
                while dictionary[i] == '':
                    dictionary[i] = input(f'{str(i).capitalize()} is required: ')
            else:
                dictionary.pop(i,None)

    return dictionary

#Example of the structure. ** are required for it to work properly    
printer(**UserInput('age:*Enter Age: ,width:*Enter width: ,height:Enter height: '))

#printer(**optionalInput({'age':'Whats yo age? '}))
