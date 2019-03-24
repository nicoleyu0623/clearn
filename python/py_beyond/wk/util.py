
def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def starprint(message,stars=2):
        mstars = '*' * stars
        ending = ''
        if stars == 4:
                ending = '!'
        newline = ''
        if stars == 2:
                newline='\n'
        print(newline,mstars,message,ending)