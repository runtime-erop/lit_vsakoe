def interface():
    while True:
        print('''What do you want me to do?
                 1. Create a new note
                 2. Delete your note
                 3. Search for a note
                 4. View notes
                 5. Exit''')
        act = input()
        match act:
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
            case _:
                print('err: invalid action')
                continue

def create():
    note = input('Enter note: ')
    with open('notes.ntui', 'a') as f:
        f.write(note + '\n')
    print('Note saved.')

def delete():
    view()
    try:
        num = int(input('Note to delete: '))
        with open('notes.ntui', 'r') as f:
            notes = f.readlines()
        if 1 <= num <= len(notes):
            del notes[num-1]
            with open('notes.ntui', 'w') as f:
                f.writelines(notes)
            print('Note deleted.')
        else:
            print('err: invalid number')
    except:
        print('err: unknown')

def search():
    s = input('Search: ')
    with open('notes.ntui', 'r') as f:
        notes = f.readlines()
    for i, n in enumerate(notes, 1):
        if s in n:
            print(f'{i}. {n.strip()}')

def close():
    print('Program terminated, have a nice day!' + '\n' + '>_<')
    exit()

def view():
    with open('notes.ntui', 'r') as f:
        notes = f.readlines()
    for i, note in enumerate(notes, 1):
        print(f'{i}. {note.strip()}')

print('\n' + "'interafce()' by Chevy-SS-1970 on github" + '\n')
print('Greetings, my Lord! We praise thee.')
interface()
