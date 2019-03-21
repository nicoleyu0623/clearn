"""small tests for apprentice chapter 4  , plural chap5 """


count = 0 #global var


def show_count():
    print(count)


def set_count(c):
    global count  #make sure a global variable will be used
    count = c



