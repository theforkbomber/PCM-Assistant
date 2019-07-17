import dataStructs

choice = None
while choice != 'Quit':
    choice = input('What would you like to use:\n\tStack\n\tQueue\n\nTo quit type in \'Quit\'. ').title()
    if choice in ['Queue', 'Stack']:
        if choice == 'Queue':
            CvN = None
            while CvN not in ['Circular','Non-Circular']:
                CvN = input('Circular or Non-circular? ').title()
            SvD = None
            while SvD not in ['Static','Dynamic']:
                SvD = input('Static or Dynamic? ').title()
            if SvD == 'Static':
                lengthOfList = -1
                while lengthOfList < 0:
                    try:
                        lengthOfList = int(input('What is the capacity? '))
                    except ValueError:
                        print('Not a valid value; please enter a positive whole number.')
            Queue = dataStructs.Queue(
                lengthOfList,
                True if CvN == 'Circular' else False,
                SvD.lower()
                )
            print(Queue.contents)
            choice2 = None
            while choice2 != 'Quit':
                print(f'Head: {Queue.head}\nTail: {Queue.tail}')
                choice2 = input('Add, Remove or Quit ').title()
                if choice2 == 'Add':
                    Queue.add(input('What would you like to add? '))
                    print(Queue.contents)
                if choice2 == 'Remove':
                    Queue.remove()
                    print(Queue.contents)
        elif choice == 'Stack':
            SvD = None
            while SvD not in ['Static','Dynamic']:
                SvD = input('Static or Dynamic? ').title()
            lengthOfList = -1
            if SvD == 'Static':
                while lengthOfList < 0:
                    try:
                        lengthOfList = int(input('What is the capacity? '))
                    except ValueError:
                        print('Not a valid value; please enter a positive whole number.')
            Stack = dataStructs.Stack(
                lengthOfList,
                SvD.lower()
                )
            print(Stack.contents)
            choice2 = None
            while choice2 != 'Quit':
                print(f'Head: {Stack.head}\nTail: {Stack.tail}')
                choice2 = input('Add, Remove or Quit ').title()
                if choice2 == 'Add':
                    Stack.add(input('What would you like to add? '))
                    print(Stack.contents)
                if choice2 == 'Remove':
                    Stack.remove()
                    print(Stack.contents)


