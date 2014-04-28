'''
Created on Apr 28, 2014

@author: Albert Haque
'''

class User:
    name = None
    # Number of messages aligned with #1,2,3 goal
    feature1 = 0
    feature2 = 0
    feature3 = 0
    # Number of spam messages
    feature4 = 0
    # Number of messages sent during anarchy mode
    feature5 = 0
    # Number of times pushed start
    feature6 = 0
    # Number of times voted anarchy
    feature7 = 0
    # Number of messages that are least important goal
    feature8 = 0
    # Totals for different inputs
    total_mode = 0
    total_button = 0

    def __init__(self, name):
        self.name = name
    
    def processMessage(self, context, message):
        msg = message.lower()
        if msg == "up" or msg == "down" or msg == "left" or msg == "right" or msg == "select" or msg == "a" or msg == "b":
            self.total_button += 1
            if msg in context.getTopNGoals(3):
                self.feature3 += 1
            if msg in context.getTopNGoals(2):
                self.feature2 += 1
            if msg in context.getTopNGoals(1):
                self.feature1 += 1
            if msg in context.getLastNGoals(1):
                self.feature8 += 1
        elif msg == "start":
            self.total_button += 1
            self.feature6 += 1
        elif msg == "anarchy":
            self.total_mode += 1
            self.feature7 += 1
        elif msg == "democracy":
            self.total_mode += 1
        # Else, spam
        else:
            self.feature4 += 1
        
        
        