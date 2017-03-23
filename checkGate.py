import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

OutputList=[7,11]
GPIO.setup(OutputList, GPIO.OUT)
InputPos=13
GPIO.setup(InputPos, GPIO.IN)
print("GateChecker")
print("Pin connections:")
print("5V (Power)     2   1 on the right")
print("- (Ground)     6   3 on the right")
print("A (Gate Input) 7   4 on the left")
print("B (Gate Input) 11  6 on the left")
print("O (Gate Output)13  7 on the left")
input("Press enter to continue")

time.sleep(.1)

## get gate input
def reliableInput(pin):
        amountTrue=0
        amountFalse=0
        testCount=100
        for num in range(0,testCount):
                if(GPIO.input(pin)):
                        amountTrue = amountTrue+1
                else:
                        amountFalse= amountFalse+1
                time.sleep(0.01)
        if(amountTrue>(.3*testCount)and amountFalse>(.3*testCount) ):
                print ("Insufficient: %True=" + str(100*amountTrue/testCount)+"  %False="+str(100*amountFalse/testCount)+"   Continuing anyway...")
        if(amountTrue>=amountFalse):
                return True
        else :
                return False

##Main Checker

GPIOoutputList = []

print("A     B        O")
GPIO.output(7, False)
GPIO.output(11, False)
time.sleep(0.1)
valueNow=reliableInput(InputPos)
time.sleep(0.1)
valueNow=reliableInput(InputPos)

GPIOoutputList.append(valueNow)
print("False False -> "+str(valueNow))
GPIO.output(7, True)
GPIO.output(11, False)
time.sleep(0.1)
valueNow=reliableInput(InputPos)
GPIOoutputList.append(valueNow)
print("True  False -> "+str(valueNow))
GPIO.output(7, False)
GPIO.output(11, True)
time.sleep(0.1)
valueNow=reliableInput(InputPos)
GPIOoutputList.append(valueNow)
print("False True  -> "+str(valueNow))
GPIO.output(7, True)
GPIO.output(11, True)
time.sleep(0.1)
valueNow=reliableInput(InputPos)
GPIOoutputList.append(valueNow)
print("True  True  -> "+str(valueNow))

gate= False

if(GPIOoutputList[0]==False
and GPIOoutputList[1]==False
and GPIOoutputList[2]==False
and GPIOoutputList[3]==True ):
        gate=True
        print("---------------")
        print("")
        print("AND GATE")
        print("")
        print("----------------")
if(GPIOoutputList[0]==True
and GPIOoutputList[1]==True
and GPIOoutputList[2]==True
and GPIOoutputList[3]==False ):
        gate=True
        print("---------------")
        print("")
        print("NAND GATE")
        print("")
        print("----------------")
if(GPIOoutputList[0]==False
and GPIOoutputList[1]==True

if(GPIOoutputList[0]==False
and GPIOoutputList[1]==True
and GPIOoutputList[2]==True
and GPIOoutputList[3]==True ):
        gate=True
        print("---------------")
        print("")
        print("OR GATE")
        print("")
        print("----------------")
if(GPIOoutputList[0]==True
and GPIOoutputList[1]==False
and GPIOoutputList[2]==False
and GPIOoutputList[3]==False ):
        gate=True
        print("---------------")
        print("")
        print("NOR GATE")
        print("")
        print("----------------")
if(GPIOoutputList[0]==False
and GPIOoutputList[1]==True
and GPIOoutputList[2]==True
and GPIOoutputList[3]==False ):
        gate=True
        print("---------------")
        print("")
        print("XOR GATE")
        print("")
        print("----------------")
if(GPIOoutputList[0]==True
and GPIOoutputList[1]==False
and GPIOoutputList[2]==False
and GPIOoutputList[3]==True ):
        gate=True
        print("---------------")
        print("")
        print("XNOR GATE")
        print("")
        print("----------------")
if(not gate):
        print("-------ERROR--------")
        print("")
        print("ERROR:    -----NOT A GATE-----     ERROR")
        print("")
        print("-------ERROR---------")
       
GPIO.cleanup()
