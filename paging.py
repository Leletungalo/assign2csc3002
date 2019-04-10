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
    print("faults: " , size - hit)
    print("pages in memory: " , memory)
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
                else:
                    memory.remove(pages[i])
                    memory.insert(0,pages[i])
                hit += curhit

    print(memory)
    print(hit)
            

def main():
    items = [8, 5, 6, 2, 5, 3, 5, 4]
    size = int(argv[1])
    #for i in range(0,size):
    #   element = randint(1,9)
    #   items.append(element)
    #print(fifo(size,items))
    lru(size,items)
    

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python paging.py [number of pages]")
    else:
        main()