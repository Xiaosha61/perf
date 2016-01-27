# parse to read counters and output what you read into StatOut.csv
def parseFile():

    #you can decide whatever events that is a subset of what you get from bash script you need here.!!!
    # MUST be the same order , otherwise not enough outputs :( coupled with RunScript.sh :(
    searchEvents = ["instructions","LLC-loads","LLC-load-misses","LLC-stores","LLC-store-misses","LLC-prefetches","LLC-prefetch-misses","cpu-cycles","page-faults"]

    # StatOut.csv to hold what you will read
    with open("StatOut.csv",'w') as fw, open("CtOutput.txt",'r') as fr:
        fw.write("Workloads," + ",".join(searchEvents) + "\n")

        #read file CtOutput.txt
        lines = fr.readlines()

        #gather counters
        for line in lines:
            searchWord = "Performance counter stats for "
            if line.find(searchWord) != -1:
                app=line[line.index(searchWord)+len(searchWord):len(line)]
                if app.index("benchspec/CPU2006") != -1:
                    app=app.split("/")[7]
                fw.write(app)

            # here are all the counters I need.
            for event in searchEvents:
                if line.find(event) != -1:
                    counterValue = line[0:line.find(event)-1].replace(" ","")
                    fw.write(",")
                    fw.write(counterValue)
                    if event is searchEvents[len(searchEvents)-1]:
                        fw.write("\n")

parseFile()
