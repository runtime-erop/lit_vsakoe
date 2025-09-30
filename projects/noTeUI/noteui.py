def interface():
    while True:
        print('''
                 1. +n
                 2. -n 
                 3. /s
                 4. *n
                 5. /e
                 ''')
        a = input()
        match a:
            case '1':
                create()
            case '2':
                delete()
            case '3':
                search()
            case '4':
                view()
            case '5':
                close()

def create():
    note = input()
    with open("notes.nt", "a") as f:
        f.write(note + "\n")

def delete():
    num = int(input())
    with open("notes.nt", "r") as f:
        notes = f.readlines()
    if 1 <= num <= len(notes):
        del notes[num-1]
        with open("notes.nt", "w") as f:
            f.writelines(notes)

def search():
    find = input()
    with open("notes.nt", "r") as f:
        notes = f.readlines()
    for i, n in enumerate(notes):
        if find in n:
            print(f"{i}. {n.strip()}")

def close():
    exit()

def view():
    with open("notes.nt", "r") as f:
        notes = f.readlines()
    for i, n in enumerate(notes, 1):
        print(f"{i}. {n.strip()}")

with open("notes.nt", "w") as init:
    ...
interface()
