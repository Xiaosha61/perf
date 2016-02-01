import os

def readFiles():
    results = os.listdir("CounterOutputs")
    fileNo=0
    for result in results:
        if result.__contains__("4"):
            fr = open("CounterOutputs/"+result,'r')
            lines = fr.readlines()
            fr.close()
            parseFile(lines,fileNo)
        else:
            print "Here is " + result
        fileNo=fileNo + 1

# parse to read counters and output what you read into StatOut.csv
def parseFile(lines,fileNo):

    #you can decide whatever events that is a subset of what you get from bash script you need here.!!!
    # MUST be the same order , otherwise not enough outputs :( coupled with RunScript.sh :(
    searchEvents = ["instructions","LLC-loads","LLC-load-misses","LLC-stores","LLC-store-misses","LLC-prefetches","LLC-prefetch-misses","cpu-cycles","page-faults"]

    # StatOut.csv to hold what you will read
    if fileNo is 1:
        fw = open("StatOut.csv",'w')
        fw.write("Workloads," + ",".join(searchEvents) + "\n")
    else:
        fw = open("StatOut.csv",'a')

    #gather counters
    for line in lines:
        searchWord = "Performance counter stats for "
        if line.find(searchWord) != -1:
            app=line[line.index(searchWord)+len(searchWord):len(line)]

            if app.index("benchspec/CPU2006") != -1:
                #app=app.split("/")[7]
                app=app.split("/")[7] + "_" + app.split("/")[9].split("_")[1] + "_" + app.split("/")[9].split("_")[2]

            fw.write(app)

        # here are all the counters I need.
        for event in searchEvents:
            if line.find(event) != -1:
                counterValue = line[0:line.find(event)-1].replace(" ","")
                fw.write(",")
                fw.write(counterValue)
                if event is searchEvents[len(searchEvents)-1]:
                    fw.write("\n")

    fw.close()

readFiles()

