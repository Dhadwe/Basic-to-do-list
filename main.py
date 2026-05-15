
to_do_list = []

def display_list():
    print("-" * 60)    
    for i, v in enumerate(to_do_list):
        print(f"{i}: {v}") 

def choose_function():
    print("-" * 60)    
    print("1 = add to list")
    print("2 = mark as done")
    print("3 = show to do list")
    print("4 = Quit")

    function = int(input("Choose 1, 2, 3 or 4 "))
    if function == 1:
        add_to_list()
    elif function == 2:
        mark_as_done()
    elif function == 3:
        display_list()
        choose_function()
    elif function == 4:
        quit()
    else: 
        print("please enter either 1,2,3 or 4 ")

def add_to_list():
    print("-" * 60)    
    to_do = input("enter the task(type END to quit and SHOW to see list): ")
    if to_do ==  "END":
        choose_function()
    elif to_do == "SHOW":
        display_list()
        add_to_list()
    else:    
        to_do_list.append(to_do)
        add_to_list()



def mark_as_done():
    print("-" * 60)    
    done = input("Type the number corresponding to the task u want to mark as done(type END to exit and SHOW to see list): ")
    if done == "END":
        choose_function()
    elif done == "SHOW":
        display_list()
        mark_as_done()
    else:
        del to_do_list[int(done)]
        mark_as_done()

choose_function()
