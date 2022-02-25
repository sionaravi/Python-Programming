# Siona Ravi
# CSCI 236
# Sep 5, 2020
# Program 01 - Steps
# Status: It compiles very well

def main():
   if len(sys.argv)!=2: #check if command line argument is given
       print("Enter python step.py filename")
       sys.exit()

   steps = []
   myfile = open(sys.argv[1], 'r')           #read input file
   for line in myfile:                       #read each line
       line = line.strip("\n")               #strip newline char from line
       if line != "":
           steps.append(int(line))           #append integer to steps list
   myfile.close()                           #close the file
   average_steps(steps)                   #compute and print average


def average_steps(steps):
   #(month, days) List of tuples
   #Feb has 28 days
   NonLeap_months = [("January", 31), ("February", 28), ("March", 31), ("April", 30),
   ("May", 31), ("June", 30), ("July", 31), ("August", 31),
   ("September", 30), ("October", 31), ("November", 30), ("December", 31)]

   #feb has 29 days
   Leap_months = [("January", 31), ("February", 29), ("March", 31), ("April", 30),
   ("May", 31), ("June", 30), ("July", 31), ("August", 31),
   ("September", 30), ("October", 31), ("November", 30), ("December", 31)]

   months = []
   if len(steps) == 365:   #according to number of days set months
       months = NonLeap_months
   else:
       months = Leap_months

   start = 0           #start at index start
   for month in months:   #for every month in list
       totalSteps = 0       #count totalSteps
       i = start           #from index start to start + number of days in that month
       while i < (start + month[1]):
           totalSteps = totalSteps + steps[i]   #add steps to total
           i = i + 1
       avgSteps = totalSteps/month[1]   #compute average
       print("The average steps taken in " + month[0] + " was " + str(round(avgSteps, 1)))
       start = start + month[1]   #update start for next month
