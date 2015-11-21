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
    epsilon = 30 # seconds
    
    loadAll(allRaces)
    print "Done loading"
    userName = raw_input("Enter name (e.g. John Doe): ")
    runnerTime = findRunner(userName, allRaces)
    findCloseRunners(runnerTime, closeRunners, epsilon, allRaces, closeRunnerTimes)

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
        #if runner.getTime() == None:
        #    print runner.getName()
        if abs(runner.getTime() - runnerTime) < epsilon:
            closeRunners.append(runner)
    for runner in closeRunners:
        print runner.getName()
main()