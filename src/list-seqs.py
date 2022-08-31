import sys

def list_seqs():

    inFile = sys.argv[1]  
    with open(inFile,'r') as j:
        lines = j.readlines()

    record_list = []
    header = ''
    sequence = ''
    for line in lines:
        line = line.strip()
        if line.startswith('@'):
            if header != "":
                record_list.append([header, sequence])
                sequence = ""
            header = line[1:]
        else:
            sequence = sequence + line
    record_list.append([header, sequence])   

    for i in record_list:
        print(i[1]) 
    
    return ''
list_seqs()
