from common import *

class sender:
    ACK = 0
    RTT = 20
    #currentSeqNum
    #currentPacket
    
    def isCorrupted (self, packet):
        #  Check if a received packet (ACK) has been corrupted during transmission.
        #similar to the corresponding function in receiver side
        #3 points
        return

    def isDuplicate(self, packet):
        # checks if an ACK is duplicate or not
        #similar to the corresponding function in receiver side
        #2 points
        return
         
    def getNextSeqNum(self):
        #generate the next sequence number to be used
        #similar to the corresponding function in receiver side
        #2 points
        return

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing sender: A: "+str(self.entity))

    def init(self):
        #initialize the currentSeqNum  and currentPacket
        #4 points
        return

    def timerInterrupt(self):
        #what the sender does in case of timer interrupt?
        #It sends the packet again. 
        #It starts the timer, sets the timeout value to be twice the RTT
        #6 points
        return

    def output(self, message):
        #if current packet is not transmitted ignore the message
        #else prepare a packet and send it through the network layer
        #call utdSend
        #start the timer
        #12 points
        return
    
    def input(self, packet):

        #If ACK isn't corrupted or duplicate, transmission complete.
        #so the currentPacket should be set to None
        #You do not need to do anythin else.
        #In the case of duplicate ACK the packet will be sent again.
        #since you do not change the current packet in that case 
        #8 points 
        return