#Import json class library
import json

data = {
    
    'name': 'Ronin Davis',
    'age': 18,
    'city': 'Tacoma, WA',
    'interests': ['Poems', 'Board Games', 'Martial Arts', 'Gaming'],
    'is_student': True
}

#Create json file in folder
with open('data.json','w') as json_file:

#Place data in json file
    json.dump(data,json_file,indent=4)

#Print when data has been placed
print("Data has been written to data.json")


#Open json and read
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

#Print when data has been read and print data in json file
print("Succesfully able to read data.json")
print(loaded_data)

#Changes to json file
loaded_data ['age'] = 20
loaded_data ['interests'].append('Cooking History')

#Rewrite changes to json file
with open('data.json','w') as json_file:

    json.dump(loaded_data,json_file,indent=4)

print("Data has succesfully been rewritten to data.json")
