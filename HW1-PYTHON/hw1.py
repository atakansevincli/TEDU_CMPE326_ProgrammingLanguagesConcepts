

###########   define matrix   ############
matrix = []  
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
         if  arrInput[1] in logosNames: # is input valid? Does logoname exist?
            rotation = logosNames[arrInput[1]]  #finds rotation of logo1 in dictionary
            givenX = int(arrInput[2])    # 3
            givenY = int(arrInput[3])    # 8
            print(f"rotation = {rotation} , givenX = {givenX} , givenY {givenY} ")
            currentXinGrid = (givenX - 1) * 2
            currentYinGrid = (givenY - 1) * 2 # 1 eksiğinin iki katı !!
            for movement in rotation:
                if movement.upper() == "U":
                    pass
                elif movement.upper() == "D":
                    pass
                elif movement.upper() == "L":
                    pass
                elif movement.upper() == "R":
                    pass
                print(movement)
            
            matrix[currentXinGrid][currentYinGrid] = "$"
            #printing the matrix
            for i in range(R):
                for j in range(C):
                    print(matrix[i][j], end = "")
                print("")


# 1,1 den başla ve ddru çizdir.  -->  x 1 den 2 ye gitmesi için matrix de | 0,0 | *1,0* | 2,0  a çizgi çek
# 2,1
# 3,1
# 3,2
# 2,2 

## x,y verilen formatta -> aşağı git



# matrix[1][0] = "|"
# matrix[3][0] = "|"
# matrix[4][1] = "-"
# matrix[3][2] = "|"
