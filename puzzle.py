
import random

class Puzzle:
    boxs = None
    rows = None
    colums = None
    squares = None
    debug = True


    def __init__(self):
        self.boxs = []
        self.rows = []
        self.colums = []
        self.squares = []


        for i in range(9):
            self.rows.append(group(0))
            self.colums.append(group(1))
            self.squares.append(group(2))


        for i in range(9): # rows
            for j in range(9): # colum
                val = 0
                if self.debug:
                    val = 'x'
                else:
                    while (val is 0) or not ((val in range(9)) or val == 'x'):
                        val = input("what is the value of row: " + str(i) + "colum: " + str(j))
                self.boxs.append(Box(i, j, 3*(i//3) + j//3,  val, self))
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

    def solve(self):
        for b in self.boxs:
            if b.colum == 8 and b.row == 0:
                x = 1
            for i in range(9):
                b.possibleValues[i] = b.groups[0].valuesOpen[i] * b.groups[1].valuesOpen[i] * b.groups[2].valuesOpen[i]
            if ((sum(b.possibleValues) == 1) or b.value != 'x') and not b.fullyChecked:
                if(b.value == 'x'):
                    b.guess(b.possibleValues.index(1) + 1)
                b.accountFor()
            x = 1
        for r in self.rows:
            r.evaluate()
        for c in self.colums:
            c.evaluate()
        for s in self.squares:
            s.evaluate()



    def toString(self):
        myString = ""
        for r in self.rows:
            myString += r.toString() + "\n"
        return myString



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
#        for i in range(9):
 #           self.possibleValues.append(1)


        self.groups = []
        self.accountedFor = [0,0,0]

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


    def setVal(self, val):
        if val == 'x' :
            self.value = 'x'
        else:
            self.value = int(val)
            self.possibleValues[int(val)-1] = 0

    def accountFor(self):

        for g in self.groups:
            g.valuesOpen[self.value-1] = 0
            self.accountedFor[g.type] = 1

        self.fullyChecked = True

    def upadate(self):
        for i in range(9):
            for g in self.groups:
                self.possibleValues[i] *= g.valuesOpen[i]


    def guess(self, val):
        self.upadate()
        if(self.possibleValues[val-1] == 1 and self.value != 'x'):
            self.value = val
        else:
            print('error')






def sum(arr):
    sum = 0
    for i in arr:
        sum += arr[i]
    return sum





class group:
    boxs = None
    type = None
    valuesOpen = None


    def __init__(self, type):
        self.type = type
        self.boxs = []
        self.valuesOpen = []
        for i in range(9):
            self.valuesOpen.append(1)



    def addBox(self, b):
        self.boxs.append(b)
        if b.value != 'x':
            self.valuesOpen[b.value-1] = 0
            b.accountedFor[type] = 1

    def toString(self):
        myString = ""
        for b in self.boxs:
            myString += ' | ' + str(b.value)
        return myString

    def evaluate(self):
        for b in self.boxs:
            if(b.row == 4 and b.colum == 8 ):
                temp =1
            b.upadate()
        for i in range(9):
            while(self.valuesOpen[i] == 0):
                i += 1
                if(i > 8):
                    break
            if (i > 8):
                break
            boxToSet = -1
            set = True
            for b in self.boxs:
                if(boxToSet != -1) and b.possibleValues[i] and b.value == 'x':
                    set = False
                    break
                elif b.possibleValues[i] and b.value == 'x':
                    boxToSet = b
            if set and b.value != 'x':
                b.guess( i + 1)










myPuzzle = Puzzle()

print(myPuzzle.toString())

myPuzzle.solve()
myPuzzle.solve()


# it needs to get to here before anything happens
myPuzzle.solve()
myPuzzle.solve()
myPuzzle.solve()
myPuzzle.solve()
myPuzzle.solve()
myPuzzle.solve()
myPuzzle.solve()
myPuzzle.solve()
myPuzzle.solve()
myPuzzle.solve()



print(myPuzzle.toString())


#for i in range(81):
#    print(' self.boxs[' + str(i) + '] =  "x"   # value for row ' + str(i//9) + ' and colum ' + str(i%9))


