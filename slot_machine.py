import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3

symbol_counts={
    'A':2,
    'B':3,
    'c':4,
    'D':5
}

symbol_value={
    'A':10,
    'B':8,
    'c':6,
    'D':4
}

def bet_winnings(columns,lines,bet,values):
    won=0
    wonlines=[]
    for line in range(lines):
        symbol=columns[0][lines]
        for col in columns:
            check=col[line]
            if symbol!=check:
                break
        else:
            won+=values[symbol]*bet
            wonlines.append(line+1)
    return won,wonlines





def slotmachine(row,col,symbolcount):
    symbols=[]
    for symbol,symbcnt in symbolcount.items():
        for i in range(symbcnt):
            symbols.append(symbol)
    slot_lines=[]
    for i in range(col):
        line=[]
        current_lines=symbols.copy()
        for j in range(row):
            v=random.choice(current_lines)
            current_lines.remove(v)
            line.append(v)
        slot_lines.append(line)
    return slot_lines

def print_slots(st):
    for i in range(len(st[0])):
        for a in st:
            print('|',a[i],end=' | ')
        print()

def deposit():
    while True:
        amount=input('Enter the amount you want to deposit: $')
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print('Amount must be greater than Zero')
        else:
            print('Enter amount in digits')
    return amount

def no_of_lines():
    while True:
        lines=input("Enter number of lines you want to bet on (1-"+ str(MAX_LINES) +"): ")
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <=MAX_LINES:
                break
            else:
                print('lines should be less than or equal to Three.')
        else:
            print('Enter lines in digits.')
    return lines

def bet():
    while True:
        amount=input('Enter the amount you want to bet on line: $')
        if amount.isdigit():
            amount=int(amount)
            if 0<amount<=MAX_BET:
                break
            else:
                print('Amount must be in '+'($1-$'+str(MAX_BET)+')')
        else:
            print('Enter amount in digits')
    return amount

def slotspin(balance):
    lines=no_of_lines()
    while True:
        bet_on_line=bet()
        total_bet=bet_on_line*lines
        if total_bet>balance:
            print('Insufficient balance select bet within your balance')
        else:
            break
    print(f"your bet is ${bet_on_line} on {lines} lines \nyour total bet is : ${total_bet} ")
    slots=slotmachine(ROWS,COLS,symbol_counts)
    print_slots(slots)
    winnings,winning_lines=bet_winnings(slots,lines,bet_on_line,symbol_value)
    print(f'you won ${winnings}')
    print(f'your winning lines: ',*winning_lines)
    return winnings-total_bet

def slotbetting():
    balance=deposit()
    while True:
        print(f'your balance is ${balance}')
        spin=input('press enter to spin or q to quit')
        if spin=='q':
            break
        else:
            balance+=slotspin(balance)
    print(f'you left with ${balance}')

slotbetting()





