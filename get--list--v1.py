import pyfiglet

art = pyfiglet.figlet_format("Hello!")
print(art)

get_things = [
    {
        'title': 'Minecraft',
        'Platform': 'PC',
        'Year': 2011,
    },
]


name = input("What is your name?") # variable

art_name = pyfiglet.figlet_format(name + "!" + "Got it!")
print(art_name)

if name == "Nick":
    get_list = input("Would you like to see your list?")

else: 
    get_list = input("Would you like to see your list?")


if get_list == ("yes"):
    art_if_yes = pyfiglet.figlet_format("Here is your list!")
    print(art_if_yes)
    print(get_things)




    