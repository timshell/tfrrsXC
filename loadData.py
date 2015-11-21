"""
From a .txt file that was copied manually, parse through the data and load
into the runner class

11/21 MA wrote it
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
        return name;
    firstName = name[commaIndex+2:len(name)]
    lastName = name[:commaIndex];
    return firstName + " " + lastName


def convertTime(minSecs):
    """
    Input Time: 5:23.7
    Output: 323 (60*5 + 23)
    """
    minSecs = minSecs[:-2]
    strlen = len(minSecs)
    secs = int(minSecs[strlen-2:strlen])
    mins = int(minSecs[0:strlen-3])
    return mins*60 + secs

def loadTxt(filepath, lstRunners):
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


"""
def main():

    listOfRunners = []
    loadTxt("mPaulShort.txt", listOfRunners)
    print listOfRunners[167].getName()

main()

"""


