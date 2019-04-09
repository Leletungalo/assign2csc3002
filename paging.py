# Leletu Ngalo 
# NGLLEL001
from random import *
from sys import argv

def fifo(size,pages):
    print(pages)
    memory = []
    hit = 0
    for i in range(0,len(pages)):
        if (len(memory)) < 4:
            if len(memory) == 0:
                memory.append(pages[i])

            else:
                for r in range(0,len(memory)):
                    if memory[r] == pages[i]:
                        hit += 1

                    else:
                        memory.append(pages[i])

        else:
            print(memory)
            for j in range(0,len(memory)):
                x = 10



def main():
    items = [9, 4, 6, 9, 3, 8, 7, 1, 8, 3]
    #for i in range(0,10):
     #  element = randint(1,9)
     #  items.append(element)

    size = int(argv[1])
    fifo(size,items)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python paging.py [number of pages]")
    else:
        main()