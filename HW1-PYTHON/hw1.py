###########   define matrix   ############
def createMatrix(matrix): 
    R = 21 # 11 x grid and 10 spaces for roads
    C = 21 # 11 y grid and 10 spaces for roads
    for i in range(R):          # A for loop for row 
        a =[]
        for j in range(C):      # A for loop for column 
            if j % 2 == 0 and i % 2 == 0:
                a.append(".")
            elif j % 2 != 0 and i % 2 == 0:
                a.append(" ")
            else:
                a.append(" ")
        matrix.append(a)

def printMatrix(matrix):
    R = 21 # 11 x grid and 10 spaces for roads
    C = 21 # 11 y grid and 10 spaces for roads
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end = "")
        print("")

###########   enter input  (LOGO ,ENGRAVE,SAME ) ############
logosNames = {}
while(True):

    stringInput = input("Enter:")
    arrInput = stringInput.split()

    ## LOGO logoName ROTATION(Example:DDRRUL)
    if arrInput[0] == "LOGO":
        if  arrInput[1] not in logosNames: # is logoName defined before?
            logosNames[arrInput[1]] = arrInput[2]
            print("{} defined".format(arrInput[1]))

    ## ENGRAVE logoName Xcordinate YCordinate
    elif arrInput[0] == "ENGRAVE":
         matrix = []
         createMatrix(matrix)
         if  arrInput[1] in logosNames: # is input valid? Does logoname exist?
            rotation = logosNames[arrInput[1]]  #finds rotation of logo1 in dictionary
            givenX = int(arrInput[2])    # 3
            givenY = int(arrInput[3])    # 8            
            currentXinGrid = (givenX - 1) * 2
            currentYinGrid = (givenY - 1) * 2 # 1 eksiğinin iki katı !!
            for movement in rotation:
                if movement.upper() == "U":
                    currentXinGrid-=1
                    matrix[currentXinGrid][currentYinGrid] = "|"
                    currentXinGrid-=1
                elif movement.upper() == "D":
                    currentXinGrid+=1
                    matrix[currentXinGrid][currentYinGrid] = "|"
                    currentXinGrid+=1
                elif movement.upper() == "L":
                    currentYinGrid-=1
                    matrix[currentXinGrid][currentYinGrid] = "-"
                    currentYinGrid-=1
                elif movement.upper() == "R":
                    currentYinGrid+=1
                    matrix[currentXinGrid][currentYinGrid] = "-"
                    currentYinGrid+=1
            
            printMatrix(matrix)
