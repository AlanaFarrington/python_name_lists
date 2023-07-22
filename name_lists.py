name_list = ['Alana', 'Will', 'Rachel', 'Sam', 'Robbie', 'Ash', 'Ruth', 'Shadi','Mum','Dad']
sex = ['female','male','female','male','male','male','male','female','female','female','male']
age_list = [36,37,32,38,38,34,34,38,67,73]
index = 0
for age in age_list:
    print(f"{name_list[index]} is {age} and {sex[index]}.")
    index +=1

print(f"Hello, {name_list[3]} and {name_list[7]}!")
print(f"Hello, {name_list[4]} and {name_list[6]}!")

print(name_list)

family_details = {'Name':['Alana', 'Will', 'Rachel', 'Sam', 'Robbie', 'Ash', 'Ruth', 'Shadi','Mum','Dad'], 
                  'Age':[36,37,32,38,38,34,34,38,67,73],
                  'Sex':['female','male','female','male','male','male','male','female','female','female','male'],}
print(family_details['Name'])

print(f"Did you know that {family_details['Name'][1]} is {family_details['Age'][1]} and is {family_details['Sex'][1]}?")

name = input('What is your name? ')
age = input ('How old are you? ')
location = input('Where do you live? ')
print('Hello, {}. You are {} years old. What is the weather like in {} today? '.format(name, age, location))


