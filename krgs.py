import fop2 as f

def build_profile(first,last,**user_info):
    user_info['first']=first
    user_info['last']=last
    return user_info

user=build_profile('john','snow',age=24,height=6,show="GOT")
print(user)

f.toppings(2,'chocoloate')
f.toppings(3,'chocolate','friuts&nuts','butterscotch')

def name1(
    ffff,ssss,ssssss,asdasdasd,asdsad,asdasd
):
    pass