"""
Ask user for input, get initial time, and then go through other races
and compare times

11/21 MA wrote it
"""

from loadData import *

raceFilePaths = ["mPaulShort.txt", 
                    "mRowan.txt", 
                    "mCentennialConferences.txt",
                    "mRegionals.txt"]

def main():

    allRaces = []
    closeRunners = []
    closeRunnerTimes = []
    diffsInTimes = []
    epsilon = 30 # seconds

    loadAll(allRaces)
    print "Done loading"
    userName = raw_input("Enter name (e.g. John Doe): ")
    runnerTime = findRunner(userName, allRaces)
    findCloseRunners(runnerTime, closeRunners, epsilon, allRaces)
    findCloseRunnerTimes(allRaces, closeRunners, closeRunnerTimes)
    calcDiffTimes(diffsInTimes, closeRunnerTimes)
    for race in diffsInTimes:
        print findMedian(race)

def loadAll(allRaces):

    for race in raceFilePaths:
        runnersInRace = []
        allRaces.append(runnersInRace)
        loadTxt(race, runnersInRace)

def findRunner(userName, allRaces):
    #for race in allRaces:
    for runner in allRaces[0]:
        if runner.getName() == userName:
            return runner.getTime()

def findCloseRunners(runnerTime, closeRunners, epsilon, allRaces):
    for runner in allRaces[0]:
        if abs(runner.getTime() - runnerTime) <= epsilon:
            closeRunners.append(runner)

def findCloseRunnerTimes(allRaces, closeRunners, closeRunnerTimes):
    for race in allRaces:
        raceTimes = []
        closeRunnerTimes.append(raceTimes)
        for runner in closeRunners:
            found = False
            for otherRunner in race:
                if runner.getName() == otherRunner.getName():
                    raceTimes.append(otherRunner.getTime())
                    found = True
                    break
            if found == False:
                raceTimes.append(None)


def calcDiffTimes(diffsInTimes, closeRunnerTimes):
    for race in closeRunnerTimes[1:]:
        runnerDifferences = []
        diffsInTimes.append(runnerDifferences)
        for index in range(len(race)):
            if (race[index] != None) & (closeRunnerTimes[0][index] != None):
                runnerDifferences.append(race[index] - closeRunnerTimes[0][index])
            else:
                runnerDifferences.append(None)

def findMedian(lst):
    lst = [x for x in lst if x is not None]
    if (len(lst) % 2) == 1:
        return sorted(lst)[(len(lst)+1)/2]
    else:
        return avg(sorted(lst)[len(lst)/2], sorted(lst)[len(lst)/2-1])

def avg(a, b):
    return (a + b)/2


main()