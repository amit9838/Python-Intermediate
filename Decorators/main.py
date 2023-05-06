from decorators_new import do_thrice

@do_thrice
def say_hi(name):
    print(f"hi {name}")

x = say_hi("amit")
print(x)




