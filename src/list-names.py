import sys

def list_names():
    # load input:
    inFile = sys.argv[1]
    with open(inFile,'r') as j:
        lines = j.readlines()
    
    for line in lines:
        if line.startswith('@'):
            print(line.strip('@').strip())
    
    return ''
list_names()
