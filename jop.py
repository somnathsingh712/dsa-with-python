name="somnath singh"
print(name.title())     #print in capital case
print(name.upper())     #print in upper case
print(name.lower())     #print in lower case

first="Johny"
last="Sins"
full=f"{first} {last}"      #print string with space between
print(full)
full_name=first+last        #print string without space between
print(full_name)


str1="      this is for lstrip     "
print(str1)
print(str1.lstrip())        #removes whitespaces from left of the string

str2="this is for r strip          "
print(str2)
length=len(str2)
print(length)
print(len(str2.rstrip()))



print("he is somnath friend")


student=["som","nath","singh","yadav"]
# # print(student[4])
# student[4]="ravi"
# print(student[4])
print(student[-1::-1])



# unprinted_designs=['phone case','robot pendant','dodecahedra']
# completed_models=[]

# while unprinted_designs:
#     current_design=unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)



def print_models(unprinted, completed):
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}")
        completed.append(current_design)


def show_completed_models(completed):
    print("\nThe following models have been printed:")
    for model in completed:
        print(model)


# Main Program
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedra']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)