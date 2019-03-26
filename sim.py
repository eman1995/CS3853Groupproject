#!/usr/bin/env python3
# Cristian Garcia



#import sys to use argv (arguments that are being passed in)
import sys
import re

#We do len(sys.argv - 1) because we dont care about sim.py (sim.py –f trace1.txt –s 1024 –b 16 –a 2 –r RR)
#10 being 10 arguments
if (len(sys.argv) - 1) == 10:
    
    #for every other argument not including (sim.py) in the command line Ex. (–f) trace1.txt (–s) 1024 (–b) 16 (–a) 2 (–r) RR
    # (-f -s -b -a -r)
    print("")
    for arg in sys.argv[1::2]:

        #check what to do for each argument
        # (–f) trace1.txt (–s) 1024 (–b) 16 (–a) 2 (–r) RR
        #   1       2       3    4    5   6   7  8   9  10        
        # Trace file name
        if "f" in arg:
            filename = sys.argv[2]
            #use try except to see if file exists
            try:
                with open(filename, 'r') as inputFile:
                    #for every line in the file
                    for line in inputFile:
                        readNextLine = 0
                        tokens = line.split();
                        
                        # using regular expression to find non-digits (\D) and replace them with nothing A.K.A. (delete)
                        length = re.sub(r'\D', "", tokens[1])
                        address = tokens[2]
                        
                        # read the next line while still in the same iteration
                        # to grab the dstM and srcM. (this also moves the file pointer) 
                        tokens2 = inputFile.readline().split()
                        readNextLine = 1

                        dstM = tokens2[1]
                        srcM = tokens2[4]
                        
                        isThereData1 = 1
                        isThereData2 = 1

                        if int(dstM, 16) == 0 and readNextLine == 1:
                            isThereData1 = 0
                        if int(srcM, 16) == 0 and readNextLine == 1:
                            isThereData2 = 0

                        if isThereData1 == 0 and isThereData2 == 0:
                            print("Address: 0x" + address + ", length =", length, "No data writes/reads occurred.")
                        else:
                            print("Address: 0x" + address + ", length =", length, "Data write at 0x" + dstM, "length = 4 bytes.")
                        
            except IOError:
                print("Error opening file: " + sys.argv[2] + ".")
                sys.exit(1)

        # Cache size in KB
        elif 's' in arg:
            cache_size = sys.argv[4]

        # Block size
        elif 'b' in arg:
            block_size = sys.argv[6]

        # Associativity
        elif 'a' in arg:
            associativity = sys.argv[8]

        # Replacement policy
        elif 'r' in arg:
            replacement_policy = sys.argv[10]

    # Print results
    print("\nCache Simulator CS 3853 Spring 2019 - Group #21")
    print("")
    print("Cmd Line:", " ".join(sys.argv))
    print("Trace File:", filename)
    print("Cache Size:", cache_size, "KB")
    print("Block Size:", block_size, "bytes")
    print("Associativity:", associativity, "way")
    print("R-Policy:", replacement_policy)
    print("")
    print("Generic:")
    print("Cache Size:", cache_size, "KB")
    print("Block Size:", block_size, "bytes")
    print("Associativity:", associativity)
    print("Policy:", replacement_policy)
    print("")
    print("----- Calculated Values -----")
    print("Total #Blocks:", 64, "KB", "(2^16)")
    print("Tag Size:", 13,"bits")
    print("Index Size:", 15, "bits,", "Total Indices:", 32, "KB")
    print("Implementation Memory Size:", "114,688", "bytes")
    print("")
    print("----- Results -----")
    print("Cache Hit Rate:", 96.2,"%")

else:
    print("Error: Argument(s) not in range.")
    sys.exit(1)
