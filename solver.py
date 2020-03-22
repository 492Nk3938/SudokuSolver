import random


class Puzzle:
    boxs = None
    rows = None
    colums = None
    squares = None
    debug = False

    def __init__(self, givenPuzzle):
        self.boxs = []
        self.rows = []
        self.colums = []
        self.squares = []

        # create 9 colums rows and squares
        for i in range(9):
            self.rows.append(group(0))
            self.colums.append(group(1))
            self.squares.append(group(2))

        # populate the groups
        for i in range(9):  # rows
            for j in range(9):  # colum
                val = 'x'
                if self.debug:
                    val = 'x'
                else:
                    #while (val is 0) or not ((val in range(9)) or val == 'x'):
                        val = givenPuzzle[i][j]
                self.boxs.append(Box(i, j, 3 * (i // 3) + j // 3, val, self))

        # methiod to set a fixed puzzle in
        if self.debug:
            self.boxs[0].setVal("x")  # value for row 0 and colum 0
            self.boxs[1].setVal("x")  # value for row 0 and colum 1
            self.boxs[2].setVal(8)  # value for row 0 and colum 2
            self.boxs[3].setVal("x")  # value for row 0 and colum 3
            self.boxs[4].setVal("x")  # value for row 0 and colum 4
            self.boxs[5].setVal(6)  # value for row 0 and colum 5
            self.boxs[6].setVal("x")  # value for row 0 and colum 6
            self.boxs[7].setVal("x")  # value for row 0 and colum 7
            self.boxs[8].setVal("x")  # value for row 0 and colum 8

            self.boxs[9].setVal(9)  # value for row 1 and colum 0
            self.boxs[10].setVal("x")  # value for row 1 and colum 1
            self.boxs[11].setVal(4)  # value for row 1 and colum 2
            self.boxs[12].setVal("x")  # value for row 1 and colum 3
            self.boxs[13].setVal("x")  # value for row 1 and colum 4
            self.boxs[14].setVal(8)  # value for row 1 and colum 5
            self.boxs[15].setVal(5)  # value for row 1 and colum 6
            self.boxs[16].setVal("x")  # value for row 1 and colum 7
            self.boxs[17].setVal("x")  # value for row 1 and colum 8

            self.boxs[18].setVal("x")  # value for row 2 and colum 0
            self.boxs[19].setVal("x")  # value for row 2 and colum 1
            self.boxs[20].setVal("x")  # value for row 2 and colum 2
            self.boxs[21].setVal(9)  # value for row 2 and colum 3
            self.boxs[22].setVal("x")  # value for row 2 and colum 4
            self.boxs[23].setVal("x")  # value for row 2 and colum 5
            self.boxs[24].setVal(6)  # value for row 2 and colum 6
            self.boxs[25].setVal("x")  # value for row 2 and colum 7
            self.boxs[26].setVal("x")  # value for row 2 and colum 8

            self.boxs[27].setVal(2)  # value for row 3 and colum 0
            self.boxs[28].setVal(8)  # value for row 3 and colum 1
            self.boxs[29].setVal("x")  # value for row 3 and colum 2
            self.boxs[30].setVal("x")  # value for row 3 and colum 3
            self.boxs[31].setVal(7)  # value for row 3 and colum 4
            self.boxs[32].setVal("x")  # value for row 3 and colum 5
            self.boxs[33].setVal("x")  # value for row 3 and colum 6
            self.boxs[34].setVal("x")  # value for row 3 and colum 7
            self.boxs[35].setVal("x")  # value for row 3 and colum 8

            self.boxs[36].setVal(7)  # value for row 4 and colum 0
            self.boxs[37].setVal("x")  # value for row 4 and colum 1
            self.boxs[38].setVal(1)  # value for row 4 and colum 2
            self.boxs[39].setVal("x")  # value for row 4 and colum 3
            self.boxs[40].setVal("x")  # value for row 4 and colum 4
            self.boxs[41].setVal("x")  # value for row 4 and colum 5
            self.boxs[42].setVal(2)  # value for row 4 and colum 6
            self.boxs[43].setVal("x")  # value for row 4 and colum 7
            self.boxs[44].setVal(3)  # value for row 4 and colum 8

            self.boxs[45].setVal("x")  # value for row 5 and colum 0
            self.boxs[46].setVal("x")  # value for row 5 and colum 1
            self.boxs[47].setVal("x")  # value for row 5 and colum 2
            self.boxs[48].setVal("x")  # value for row 5 and colum 3
            self.boxs[49].setVal(8)  # value for row 5 and colum 4
            self.boxs[50].setVal("x")  # value for row 5 and colum 5
            self.boxs[51].setVal("x")  # value for row 5 and colum 6
            self.boxs[52].setVal(1)  # value for row 5 and colum 7
            self.boxs[53].setVal(4)  # value for row 5 and colum 8

            self.boxs[54].setVal("x")  # value for row 6 and colum 0
            self.boxs[55].setVal("x")  # value for row 6 and colum 1
            self.boxs[56].setVal(5)  # value for row 6 and colum 2
            self.boxs[57].setVal("x")  # value for row 6 and colum 3
            self.boxs[58].setVal("x")  # value for row 6 and colum 4
            self.boxs[59].setVal(1)  # value for row 6 and colum 5
            self.boxs[60].setVal("x")  # value for row 6 and colum 6
            self.boxs[61].setVal("x")  # value for row 6 and colum 7
            self.boxs[62].setVal("x")  # value for row 6 and colum 8

            self.boxs[63].setVal("x")  # value for row 7 and colum 0
            self.boxs[64].setVal("x")  # value for row 7 and colum 1
            self.boxs[65].setVal(9)  # value for row 7 and colum 2
            self.boxs[66].setVal(5)  # value for row 7 and colum 3
            self.boxs[67].setVal("x")  # value for row 7 and colum 4
            self.boxs[68].setVal("x")  # value for row 7 and colum 5
            self.boxs[69].setVal(4)  # value for row 7 and colum 6
            self.boxs[70].setVal("x")  # value for row 7 and colum 7
            self.boxs[71].setVal(7)  # value for row 7 and colum 8

            self.boxs[72].setVal("x")  # value for row 8 and colum 0
            self.boxs[73].setVal("x")  # value for row 8 and colum 1
            self.boxs[74].setVal("x")  # value for row 8 and colum 2
            self.boxs[75].setVal(4)  # value for row 8 and colum 3
            self.boxs[76].setVal("x")  # value for row 8 and colum 4
            self.boxs[77].setVal("x")  # value for row 8 and colum 5
            self.boxs[78].setVal(8)  # value for row 8 and colum 6
            self.boxs[79].setVal("x")  # value for row 8 and colum 7
            self.boxs[80].setVal("x")  # value for row 8 and colum 8

    # methiod to update all groups and boxes in the puzzle
    def updateAll(self):
        for b in self.boxs:
            b.update()
        for r in self.rows:
            r.update()
        for c in self.colums:
            c.update()
        for s in self.squares:
            s.update()

    def solve(self):

        i = 0
        while not self.isSolved():

            self.updateAll()  # I should attempt to make the updating recursive

            for r in self.rows:
                r.deduce()
            for c in self.colums:
                c.deduce()
            for s in self.squares:
                s.deduce()
            i += 1
            if i > 40:
                return
        print(i)

    # methiod that to check and see if there are any x's left
    def isSolved(self):
        for b in self.boxs:
            if b.value == 'x':
                return False
        return True

    # methiod to return a readble string of the whole puzzle
    def toString(self):
        myString = ""
        i = 0
        for r in self.rows:
            if i % 3 == 0:
                myString += '\n'
            myString += r.toString() + "\n"
            i += 1
        return myString


# a class used to keep track of each individual box in the puzzle
class Box:
    fullyChecked = False
    value = 'x'
    possibleValues = None
    groups = None
    accountedFor = None
    row = -1
    colum = -1

    def __init__(self, row, colum, square, value, external):
        self.row = row
        self.colum = colum
        self.possibleValues = []

        # set all varables to keep track of group info
        self.groups = []
        self.accountedFor = [0, 0, 0]

        external.rows[row].boxs.append(self)
        self.groups.append(external.rows[row])

        external.colums[colum].addBox(self)
        self.groups.append(external.colums[colum])

        external.squares[square].addBox(self)
        self.groups.append(external.squares[square])

        self.value = value
        if self.value == 'x':
            for i in range(9):
                self.possibleValues.append(1)

    # methiod used at the begining to set all the values
    def setVal(self, val):
        if val == 'x':
            self.value = 'x'
        else:
            self.value = int(val)
            self.possibleValues[int(val) - 1] = 0

    # methiod to update the possible values the box could take
    def update(self):
        # check to see if there is a possible error
        if sum(self.possibleValues) == 0 and self.value == 'x':
            print('problem: no value and no possibilities')
            return

        # check to see if a value can be assigned
        if sum(self.possibleValues) == 1 and self.value == 'x':
            self.guess(self.possibleValues.index(1) + 1)

        # go through and eliminate all the impossible values
        for i in range(9):
            for g in self.groups:
                self.possibleValues[i] *= g.valuesOpen[i]

        # redue all of the checks
        if sum(self.possibleValues) == 1 and self.value == 'x':
            self.guess(self.possibleValues.index(1) + 1)

        if sum(self.possibleValues) == 0 and self.value == 'x':
            print("problem")

    # methiod to assign a value to a box that includeds checks to make sure assigning it isn't illegal
    def guess(self, val):
        # warning if you are trying to assign a different value to the box
        if self.value != 'x' and val != self.value:
            print('trying to assign to something already taken')
        elif self.possibleValues[val - 1] == 0:
            print('trying to assign an imposible value')
        else:
            self.value = val


# methiod to sum up all the values in an array
def sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


# This is a class to represent the rows colums and squares of the puzzle
# There are practacly no differences between them so rather then using 3 sub classes
# I simply keep track of what it is in the type varable.
class group:
    # A list to hold all of the boxes in this group
    boxs = None
    # a number 1-3 that keeps track of if this is a row colum or square. 1-3 respectivly
    type = None
    # an array of size 9 which will hold a 1 if the group still needs a value for the corsponding location
    # i.e. if valuesOpen[0] == 1 then this group still needs a 1
    valuesOpen = None

    def __init__(self, type):
        # set all the varables to new arrays and fill the values open with 1's
        self.type = type
        self.boxs = []
        self.valuesOpen = []
        for i in range(9):
            self.valuesOpen.append(1)

    # methiod to check if all of the box's in the group are solved
    def solved(self):
        for b in self.boxs:
            if b.value == 'x':
                return False
        return True

    # methiod used at the begining to create the group and fill it
    def addBox(self, b):
        self.boxs.append(b)
        # check if the box is solved and account for it
        if b.value != 'x':
            self.valuesOpen[b.value - 1] = 0
            b.accountedFor[type] = 1

    # methiod to convert the group to a readabe string. It only works for rows (type 0) now
    def toString(self):
        myString = ""
        i = 0
        for b in self.boxs:
            if i != 0 and i % 3 == 0:
                myString += ' |   '
            myString += ' | ' + str(b.value)
            i += 1
        return myString

    # methiod to update the valuesOpen array to keep track of what is still needed in the group
    def update(self):
        for i in range(9):
            if (self.valuesOpen[i] == 0):
                continue
            for b in self.boxs:
                if (b.value == i + 1):
                    self.valuesOpen[i] = 0

        if sum(self.valuesOpen) == 0 and not self.solved():
            print("problem")

    def deduce(self):

        for i in range(9):
            set = True
            boxToSet = None
            for b in self.boxs:
                if not boxToSet is None and b.possibleValues[i] == 1:
                    set = False
                    break
                elif b.possibleValues[i] == 1:
                    boxToSet = b



def PuzzleToString(array):
    returnString =''
    j = 0
    for r in array:
        i = 0
        for c in r:
            if (i % 3 == 0 and i != 0):
                returnString += '\t'
            returnString += ' ' + str(c) + ' '
            i += 1


        if j % 3 == 2 and j != 0:
            returnString += '\n'
        returnString += '\n'
        j += 1
    return returnString




puzzleToSolve = [
    ['x','x','x',     'x','x','x',     'x','x','x'],
    ['x','x','x',     'x','x','x',     'x','x','x'],
    ['x','x','x',     'x','x','x',     'x','x','x'],

    ['x','x','x',     'x','x','x',     'x','x','x'],
    ['x','x','x',     'x','x','x',     'x','x','x'],
    ['x','x','x',     'x','x','x',     'x','x','x'],

    ['x','x','x',     'x','x','x',     'x','x','x'],
    ['x','x','x',     'x','x','x',     'x','x','x'],
    ['x','x','x',     'x','x','x',     'x','x','x']
]


option = None
while(True):
    option = input('type i to insert numbers into the puzzle, s to solve, or d to display the puzzle: ')

    if option == 'i':
        r = 0
        c = 0
        val = 'x'
        while(r != 'q' and c != 'q' and val != 'q'):
            print('at any point input a q to quite the inserting mode')
            r = input('input the row to change: ')
            c = input('input the colum to change: ')
            val = input('input the value to set it to, if unknown input x: ')
            if not (r.isdigit() or c.isdigit() or val.isdigit()):
                break
            puzzleToSolve[int(r)-1][int(c)-1] = val
            print(PuzzleToString(puzzleToSolve))

    elif option == 's':
        try:

            myPuzzle = Puzzle(puzzleToSolve)

            myPuzzle.solve()

            print(myPuzzle.toString())

            print("here's your puzzle " )

            break

        except Exception as e:
            print('something went wrong and we could not solve the puzzle')


    elif option == 'd':
        print(PuzzleToString(puzzleToSolve))

    else:
        print('instruction not recognised')




