"""
From a .txt file that was copied manually, parse through the data and load
into the runner class

11/21 MA wrote it
11/30 MA added comments
"""

class Runner(object):

    def __init__(self, name, school, time):
        self.name = name
        self.school = school
        self.time = time

    def getName(self):
        return self.name

    def getSchool(self):
        return self.school

    def getTime(self):
        return self.time


def convertName(name):
    """
    Input Name: Doe, John
    Output: John Doe

    """
    commaIndex = name.find(",")
    if commaIndex < 0:
        return name # couldn't find comma
    firstName = name[commaIndex+2:len(name)]
    lastName = name[:commaIndex]

    # fix cases
    firstName = firstName[0].upper() + firstName[1:].lower()
    lastName = lastName[0].upper() + lastName[1:].lower()  
    
    return firstName + " " + lastName


def convertTime(minSecs):
    """
    Input Time: 5:23.7
    Output: 323 (60*5 + 23)
    """
    minSecs = minSecs[:-2] # take off ms
    secs = int(minSecs[-2:]) 
    mins = int(minSecs[0:-3])
    return mins*60 + secs

def loadTxt(filepath, lstRunners):
    """
    Given a text file, parse through the text file and add each runner to
    the list of runners
    """
    f = open(filepath)
    nextLine = f.readline()
    while nextLine != (""):
        name = convertName(f.readline().strip())
        f.readline()
        school = f.readline().strip()
        f.readline()
        time = convertTime(f.readline().strip())
        f.readline()
        lstRunners.append(Runner(name, school, time))
        nextLine = f.readline()

    f.close()



