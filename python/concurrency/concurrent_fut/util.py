
def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def starprint(message, nstars=2, starchar='*'):
        mstars = starchar * nstars
        ending = ''
        if nstars == 4:
                ending = '!'
        newline = ''
        if nstars == 2:
                newline='\n'
        print(newline,mstars,message,ending)