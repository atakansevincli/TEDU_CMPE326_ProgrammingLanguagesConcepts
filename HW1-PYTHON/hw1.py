from sys import stdin
###########   define matrix   ############
def createMatrix(arr): 
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
        arr.append(a)
def createLargeMatrix(arr): 
    R = 100 # 11 x grid and 10 spaces for roads
    C = 100 # 11 y grid and 10 spaces for roads
    for i in range(R):          # A for loop for row 
        a =[]
        for j in range(C):      # A for loop for column 
            if j % 2 == 0 and i % 2 == 0:
                a.append(".")
            elif j % 2 != 0 and i % 2 == 0:
                a.append(" ")
            else:
                a.append(" ")
        arr.append(a)
def reverseColumns(arr):
    R = 21 # 11 x grid and 10 spaces for roads
    C = 21 # 11 y grid and 10 spaces for roads
    for i in range(C):
        j = 0
        k = C-1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1

# Function for do transpose of matrix
def transpose(arr):
    R = 21 # 11 x grid and 10 spaces for roads
    C = 21 # 11 y grid and 10 spaces for roads
    for i in range(R):
        for j in range(i, C):
            
            t = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = t
            
def printMatrix(matrix):
    R = 21 # 11 x grid and 10 spaces for roads
    C = 21 # 11 y grid and 10 spaces for roads
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end = "")
        print("")

def rotate90(arr):
    R = 21 # 11 x grid and 10 spaces for roads
    C = 21 # 11 y grid and 10 spaces for roads
    for i in range(R):
        for j in range(C):
            if "|" == arr[i][j]:
                arr[i][j] = "-"
            elif "-" == arr[i][j]:
                arr[i][j] = "|"
    transpose(arr)
    reverseColumns(arr)
def addToArr(matrix):
    bosArr = []
    for i in range(21):
        for j in range(21):
            if "|" == matrix[i][j]:
                bosArr.append(1)
            elif "-" == matrix[i][j]:
                bosArr.append(0)
    return bosArr
    

###########   enter input  (LOGO ,ENGRAVE,SAME ) ############
logosNames = {}

allInputsArr = []
for line in stdin:
    arr = line.split()
    allInputsArr.append(arr)
for i in range(len(allInputsArr)):

    arrInput = allInputsArr[i]

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
            currentYinGrid = (givenY - 1) * 2 # 1 eksiÄŸinin iki katÄ± !!
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
            
    elif arrInput[0] == "SAME":
        #compareDic = {"Ä°lk":[],"Ä°lkAnti90":[],"Ä°lkAnti180":[],"Ä°lkAnti270":[],"Ä°kinci":[]}
        compareArr = []
        if  arrInput[1] in logosNames and arrInput[2] in logosNames: # is input valid? Does logoname exist?
            for i in range(1,3):
                matrix = []
                createMatrix(matrix)
                rotation = logosNames[arrInput[i]]  #finds rotation of logo1 in dictionary
                givenX = 5    # 3
                givenY = 5    # 8            
                currentXinGrid = (givenX - 1) * 2
                currentYinGrid = (givenY - 1) * 2 # 1 eksiÄŸinin iki katÄ± !!
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
                if i == 1:
                    compareArr.append(addToArr(matrix)) # 0 firstLogoName
                    rotate90(matrix) #anti 90
                    compareArr.append(addToArr(matrix)) # 90Ä± append et
                    rotate90(matrix) #anti 180
                    compareArr.append(addToArr(matrix)) # 180Ä± append et
                    rotate90(matrix) #anti 270
                    compareArr.append(addToArr(matrix)) # 270Ä± append et
                else:
                    compareArr.append(addToArr(matrix))# second logoName
        if compareArr[0] == compareArr[4] or compareArr[1] == compareArr[4] or compareArr[2] == compareArr[4] or compareArr[3] == compareArr[4]:
            print("Yes")
        else:
            print("No")
