"""
Ask user for input, get initial time, and then go through other races
and compare times

11/21 MA wrote it
11/30 MA added comments
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

    # assuming runner ran in first race
    runnerTime = findRunner(userName, allRaces[0]) 
    findCloseRunners(userName, closeRunners, epsilon, allRaces[0])
    findCloseRunnerTimes(allRaces, closeRunners, closeRunnerTimes)
    calcDiffTimes(diffsInTimes, closeRunnerTimes)
    
    for race in diffsInTimes:
        print findMedian(race)

def loadAll(allRaces):
    """
    Given a parent list, loadAll will create child lists for each race
    where each child list contains all the runners from the specific race
    """
    for race in raceFilePaths:
        runnersInRace = []
        allRaces.append(runnersInRace)
        loadTxt(race, runnersInRace)

def findRunner(userName, race):
    """
    Given a race and a runner's name, get the time of the runner in that race.
    The assumption is that no two different people of the same name are in the
    race. This can be strengthened by getting school.
    """
    for runner in race:
        if runner.getName() == userName:
            return runner.getTime()

def findCloseRunners(baseRunner, closeRunners, epsilon, race):
    """
    Given a race and some epsilon time, the program will add to a list
    called closeRunners all the runners within epsilon time of the given
    runner
    """
    runnerTime = findRunner(baseRunner, race)
    for runner in race:
        if abs(runner.getTime() - runnerTime) <= epsilon:
            closeRunners.append(runner)

def findCloseRunnerTimes(allRaces, closeRunners, closeRunnerTimes):
    """
    findCloseRunnerTimes goes through all the races and finds all the runners
    in the list closeRunners. Each race has its own list in closeRunnerTimes 
    If the closeRunner is found, the sublist of closeRunnerTimes corresponding 
    to the race will append that runner's time. Otherwise, if the runner didn't
    compete it in the race, they will have a time of None.
    """
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
    """
    Using the times from closeRunnerTimes, calcDiffTimes will find the
    differences of each runner's time through each race. The resulting
    list that stores all this is diffsInTimes
    """
    for race in closeRunnerTimes[1:]:
        runnerDifferences = []
        diffsInTimes.append(runnerDifferences)
        for index in range(len(race)):
            if (race[index] != None) & (closeRunnerTimes[0][index] != None):
                # i.e. runner competed in both races
                runnerDifferences.append(race[index] - closeRunnerTimes[0][index]) # append difference
            else:
                runnerDifferences.append(None)

def findMedian(lst):
    """
    Given a list return the median
    """
    lst = [x for x in lst if x is not None] # get rid of None values
    if (len(lst) % 2) == 1:
        return sorted(lst)[(len(lst)+1)/2]
    else:
        return avg(sorted(lst)[len(lst)/2], sorted(lst)[len(lst)/2-1])

def avg(a, b):
    """
    Return the mean of two numbers
    """
    return (a + b)/2


main()