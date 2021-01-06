def extract_names(i):
    file =i
    index=0
    c=0
    for i in range(0, len(file)): 
        if file[i]=='_':
            c=c+1
        if c==2:
            index=i
            break

    name =file[0:index]
    return name