# Leletu Ngalo 
# NGLLEL001
from random import *
from sys import argv

def fifo(size,pages):
    memory = []
    hit = 0
    oldest = 0
    for i in range(0,len(pages)):
        if (len(memory)) < 3:
            
            if len(memory) == 0:
                memory.append(pages[i])

            else:
                curhit = 0
                for r in range(0,len(memory)):
                    if memory[r] == pages[i]:
                        curhit += 1

                if curhit == 0:
                    memory.append(pages[i]) 

                hit += curhit       

        else:
            curhit2 = 0
            for j in range(0,len(memory)):
                if memory[j] == pages[i]:
                    curhit2 += 1
            
            if curhit2 == 0:
                memory.append(pages[i])
                memory.pop(0)
            hit += curhit2
    return size - hit

def lru(size,pages):
    memory = []
    hit = 0
    for i in range(0,len(pages)):
        if len(memory) ==0:
            memory.insert(0,pages[i])
        else:
            if len(memory) < 3:
                curhit = 0
                for j in range(0,len(memory)):
                    if memory[j] == pages[i]:
                        curhit +=1
            
                if curhit == 0:
                    memory.insert(0,pages[i])
                else:
                    memory.remove(pages[i])
                    memory.insert(0,pages[i])
                hit += curhit

            else:
                curhit = 0
                for j in range(0,len(memory)):
                    if memory[j] == pages[i]:
                        curhit +=1
            
                if curhit == 0:
                    memory.insert(0,pages[i])
                    memory.pop(len(memory) -1)
                else:
                    memory.remove(pages[i])
                    memory.insert(0,pages[i])
                    memory.pop(len(memory) -1)
                hit += curhit
    return size - hit

def OPT(size,pages):
    memory = []
    hit = 0
    for i in range(0,len(pages)):
        if len(memory) == 0:
            memory.append(pages[i])

        else:
            if len(memory) < 3:
                curhit = 0
                for j in range(0,len(memory)):
                    if memory[j] == pages[i]:
                        curhit += 1

                if curhit == 0:
                    memory.append(pages[i])

                else:
                    counters = []
                    con = 0
                    distance = 0
                    m = i
                    for r in range(0,len(memory)):
                        curElement = memory[r]
                        for x in range(m,len(pages)):
                            print(pages[x])
                            if (curElement != pages[x]):
                                distance += 1
                            else:
                                break
                        
                        print("ljikoj",m)
                        counters.append(distance)
                        distance = 0
                    print(counters)
                hit = curhit
    



def main():
    #items = []
    items = [8, 5, 5, 2, 5, 3, 5, 4]
    size = int(argv[1])
    #for i in range(0,size):
     #  element = randint(1,9)
     #  items.append(element)
    # may print 
    #print("FIFO ",fifo(size,items)," page faults.")
    #print ("LRU ",lru(size,items), "page faults.")
    OPT(size,items)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python paging.py [number of pages]")
    else:
        main()