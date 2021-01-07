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

    
    name =file[:index+1]
    first=0
    last=0
    c1=0
    for i in range(0, len(name)): 
        if name[i]=='_':
            first=i
            c1=c1+1
            break
        if c1==2:
            last=i-1
            break
    ct=first+1
    last=len(name)-1
    s= name[ct:last]
    f= name[0:first]
    return f,s