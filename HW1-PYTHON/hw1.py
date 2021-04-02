from sys import stdin
def createMatrix(arr,R,C): 
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
def reverseColumns(arr,R,C):
    for i in range(C):
        j = 0
        k = C-1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1
def movement(matrix,rotation,givenX,givenY):          
    currentXinGrid = (givenX - 1) * 2
    currentYinGrid = (givenY - 1) * 2 
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
    return matrix
# Function for do transpose of matrix
def transpose(arr,R,C):
    for i in range(R):
        for j in range(i, C):
            
            t = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = t
            
def printMatrix(matrix,R,C):
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end = "")
        print("")

def rotate90(arr,R,C):
    for i in range(R):
        for j in range(C):
            if "|" == arr[i][j]:
                arr[i][j] = "-"
            elif "-" == arr[i][j]:
                arr[i][j] = "|"
    transpose(arr,R,C)
    reverseColumns(arr,R,C)
def ArrForComparing(matrix,R,C):
    bosArr = []
    for i in range(R):
        for j in range(C):
            if "|" == matrix[i][j]:
                bosArr.append(1)
            elif "-" == matrix[i][j]:
                bosArr.append(0)
    return bosArr


logosNames = {} #handle logosnames and their rotation

allInputsArr = []
for line in stdin:
    arr = line.split()
    allInputsArr.append(arr)
for i in range(len(allInputsArr)):

    arrInput = allInputsArr[i]

    if arrInput[0] == "LOGO":
        if  arrInput[1] not in logosNames: # is logoName defined before?
            logosNames[arrInput[1]] = arrInput[2]
            print("{} defined".format(arrInput[1]))

    elif arrInput[0] == "ENGRAVE":
         matrix = []
         createMatrix(matrix,21,21)
         if  arrInput[1] in logosNames: #Does logoname exist?
            rotation = logosNames[arrInput[1]]  #finds rotation of logo1 in dictionary
            movement(matrix,rotation,int(arrInput[2]),int(arrInput[3]))
            printMatrix(matrix,21,21)
            
    elif arrInput[0] == "SAME":
        compareArr = []
        if  arrInput[1] in logosNames and arrInput[2] in logosNames: # is input valid? Does logoname exist?
            for i in range(1,3): # SAME logo1 logo2 -> for iterate 2 times because get 2 logo
                matrix = []
                R = 401 # for big inputs
                C = 401 # for big inputs
                createMatrix(matrix,R,C)
                rotation = logosNames[arrInput[i]]
                movement(matrix,rotation,100,100)
                if i == 1:
                    compareArr.append(ArrForComparing(matrix,R,C)) # 0 LogoName2
                    for i in range(3):
                        rotate90(matrix,R,C) # anti 90 180 270 rotate and append to compare arr for logoName1
                        compareArr.append(ArrForComparing(matrix,R,C))

                elif i == 2:
                    compareArr.append(ArrForComparing(matrix,R,C))# 0 LogoName2
        
        check = False
        for i in range(len(compareArr)-1):
            if compareArr[i] == compareArr[4]:
                check = True
        if check:
            print("Yes")
        else:
            print("No")
