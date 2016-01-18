
# parse to read counters and output what you read into StatOut.csv
def parseFile():

    #you can decide whatever events that is a subset of what you get from bash script you need here.!!!
    # MUST be the same order , otherwise not enough outputs
    searchEvents = ["instructions","LLC-loads","LLC-load-misses","LLC-stores","LLC-store-misses","LLC-prefetches","LLC-prefetch-misses","cpu-cycles","page-faults"]
    #searchEvents = ["context-switches","cpu-migrations","page-faults","instructions"]

    #create StatOut.csv to hold what you will read
    fw = open("StatOut.csv",'w')
    # note that: the events'order should be same with CtOutput.txt, because it's searched line by line.
    fw.write("Workloads")
    fw.close()

    fw = open("StatOut.csv",'a')
    for event in searchEvents:
        fw.write(","),
        fw.write(event),

    #read file CtOutput.txt
    fr = open("CtOutput.txt",'r')
    lines = fr.readlines()
    fr.close()

    #gather counters

    fw = open("StatOut.csv",'a')
    fw.write("\n")

    for line in lines:
        line = line.strip() # get rid of double \n
        searchWord = "Performance counter stats for "
        if line.find(searchWord) != -1:
            fw.write(line[line.index(searchWord)+len(searchWord):len(line)])

        # here are all the counters I need.

        for event in searchEvents:
            if line.find(event) != -1:
                pageFaults = line[0:line.find(event)-1]
                fw.write(",")
                fw.write(pageFaults)
                if event is searchEvents[len(searchEvents)-1]:
                    fw.write("\n")

    fw.close()

parseFile()
