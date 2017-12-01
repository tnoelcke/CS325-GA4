from cnf2sat import satisfiable
# import 2 SAT solver

def printSAT(cfnArr):
    outfile = open("output.txt","w+")
    if satisfiable(cfnArr) == True:
        print("True")
        outfile.write("yes")
    else:
        outfile.write("no")
        print("False")
    outfile.close()

# Toggling a switch changes the on/off state of every
# light that is connected to the switch.
# so if a light is on the switches can be (x1 OR x2) AND (not x1 OR not x2)
# if a light is off it means that one switch must be off and the other on
# so the switches can be (x1 OR not x2) AND (not x1 or x2)
#with input = [1,2]
#            [2,3]
#            [1,3]
# in the form switch = [[1,1,0]
#                       [0,1,1]
#                       [1,0,1]]
# we have switch 1 = ((-1, 3), (1, -3),
#          switch 2 = (-1, 2), (1, -2)
#          switch 3 =  (2, 3), (-2, -3)
def convertCircuitTo2SAT(lightState,lights):
    cfnArr = []
    for i in range(0, lights):
        lightVals = []
        for index,switch in enumerate(switchVals[i]):
            if switch == 1:
                lightVals.append(index + 1)
            print("light values", lightVals)
        if lightState[i] == 1:
            #light is on
            cfnArr.append((lightVals[0] ,lightVals[1]))
            cfnArr.append((lightVals[0]*-1 ,lightVals[1]*-1)) 
        else:
             #light is off
            cfnArr.append((lightVals[0]*-1 ,lightVals[1]))
            cfnArr.append((lightVals[0] ,lightVals[1]*-1))
    printSAT(cfnArr)


file = open("input.txt","r")
# get number of switches n and lights m
arraySize = list(map(int,file.readline().split(',')))
switches, lights = arraySize[0], arraySize[1]
print("switches: ",switches,"lights:",lights)
# get the list of m binary values specifying the initial state of the
# lights, 1 is on, and 0 is off.
# store in lightState
lightState = list(map(int,file.readline().strip('\n').split(',')))
print("Initial light states:," lightState)
##The following n lines specify the set of lights connected to each switch.
##Specifically, line i contains a list of all lights connected to the ith switch
# create matrix/graph of which light is connected to which switch based off light index
# with input = [1,2]
#            [2,3]
#            [1,3]
# in the form switch = [[1,1,0]
#                       [0,1,1]
#                       [1,0,1]]
switchVals = [[0]*switches for i in range(lights)]
for switch in range(0,switches):
    for light in file.readline().strip('\n').split(','):
        switchVals[int(light)-1][switch] = 1
print("matrix of switches with connected lights as index:",switchVals)

convertCircuitTo2SAT(lightState,lights)

