l=['123','456','789']
def board():
    global l
    print('\n')
    for i in range(len(l)):
        row=''
        for j in range(len(l[i])-1):
            row+=l[i][j]+' | '
        row+=l[i][2]
        if i !=0 and i !=len(l):
            print('__________\n')
        print(row)

def check_input(p,s,i):
    global l
    ic='123456789'
    f,r=False,False
    while f != True or r != True:
        if p.isdigit():
            f=True
        else:
            print('Enter a digit')
            
        if f == True and p in ic:
            if i % 2 == 0:
                for i in range(len(l)):
                    if p in l[i]:
                        l[i]=l[i].replace(p,s[0])
                r = True
            else:
                for i in range(len(l)):
                    if p in l[i]:
                        l[i]=l[i].replace(p,s[1])
                r = True
        else:
            print('Enter within range 1-9 ')

def check_win():
    global l
    if (l[0] == 'XXX') or (l[1] == 'XXX') or (l[2] == 'XXX') or (l[0][0] == l[1][0] == l[2][0] == 'X') or (l[0][1] == l[1][1] == l[2][1] == 'X') or (l[0][2] == l[1][2] == l[2][2] == 'X') or (l[0][0] == l[1][1] == l[2][2] == 'X') or (l[0][2] == l[1][1] == l[2][0] == 'X'):
        return 'X'
    elif (l[0] == 'OOO') or (l[1] == 'OOO') or (l[2] == 'OOO') or (l[0][0] == l[1][0] == l[2][0] == 'O') or (l[0][1] == l[1][1] == l[2][1] == 'O') or (l[0][2] == l[1][2] == l[2][2] == 'O') or (l[0][0] == l[1][1] == l[2][2] == 'O') or (l[0][2] == l[1][1] == l[2][0] == 'O'):
        return 'O'
    else:
        return 'C'
        
ch= input('Player 1 choose X or O: ')
f=False
if ch.upper() == 'X':
    s='XO'
else:
    s='OX'
for i in range(9):
    p=input('\nEnter position: ')
    check_input(p,s,i)
    print('\n'*10)
    board()
    c=check_win()
    if c == 'X' or c == 'O':
        print(f'{c} wins')
        f=True
        break
if f == False:
    print('Draw')
