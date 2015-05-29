import itertools

def medium215(network_file="C:\Users\Will\Documents\Python Practice\Daily Programmer\sorter input.txt"):
    intext = open(network_file)
    networkParams=[int (x) for x in intext.readline().split()]
    
    tests=list(itertools.product([0,1],repeat=networkParams[0]))

    network=[]
    for line in intext:
        network.append(line)
        
    for test in tests:
        test=list(test) #Itertools gives tuples, change test from tuple to list
        for junction in network:
            cands=[int (x) for x in junction.split()]
            if test[cands[0]] > test[cands[1]]: #If they're out of order, swap
                test[cands[0]],test[cands[1]] = test[cands[1]], test[cands[0]]
        
        if not isSorted(test):
            print "Failure.  Returned: ",test
            return False
    return True

def isSorted(test):
    for i in range(len(test)-1):
        if test[i]>test[i+1]:
            return False
    return True

def medium214():
    print "Enter data"
    inData = list(iter(raw_input, ""))
    print "------------------\n"

    dims=[int(x) for x in inData[0].split()]
    cards=[]
    for line in inData[1:]:
        cards.append([int(x) for x in line.split()])
        
    Image=[[0 for x in range(dims[0])] for x in range(dims[1])]    
    
    for x in range(dims[0]):
        for y in range(dims[1]):
            for card in cards:
                if fallsIn([x,y],card):
                    Image[y][x]=card[0]
    for line in Image:
        print line

    #Generate a list of n zeros where n is the number of colours
    count=[0]
    for card in cards:
        count.append(0)

    for line in Image:
        for item in line:
            count[item]+=1 #This assumes the colors are numbered sequentially

    return count

def fallsIn(loc,card):
    #Determine if a coordinate falls in the rectangle bounded by a card
    if loc[0]>=card[1] and loc[0]<card[1]+card[3]:
        if loc[1]>=card[2] and loc[1]<card[2]+card[4]:
            return True
    return False



def easy214(inString):
    nums=[int(x) for x in inString.split()]
    mean=sum(nums)/float(len(nums))

    dev=0
    for num in nums:
        dev+=(num-mean)**2
    return round((dev/float(len(nums)))**0.5,4)

def easy210(a,b,bits=32):
    res=bin(a^b)[2:].zfill(bits)

    matches=0
    for dig in res:
        if dig=='0':
            matches+=1

    
    print matches*100.0/bits,"% Compatability"

    print a," should avoid ", a^(2**bits-1) 
    print b," should avoid ", b^(2**bits-1)

def easy211(name="Nick!"):
    name=name[:-1]
    f=name[0]
    vowels={'A','E','I','O','U'}
    
    l1=name+", "+name
    if f=='B':
        l1+=" Bo-"+name[1:]
    elif f in vowels:
        l1+=" bo B"+f.lower()+name[1:]
    else:
        l1+=" bo " +'B'+name[1:]
    print l1

    l2 ="Bonana fanna"
    if f=='F':
        l2+=" Fo-"+name[1:]
    elif f in vowels:
        l2+=" fo F"+f.lower()+name[1:]
    else:
        l2+=" fo "+'F'+name[1:]
    print l2
    
    l3="Fee fy"
    if f=='M':
        l3+=" Mo-"+name[1:]
    elif f in vowels:
        l3+=" mo M"+f.lower()+name[1:]
    else:
        l3+=" mo "+'M'+name[1:]
    print l3

    print name+"!"

    
def easy212(quote="I'm speaking Robber's language!"):
    cons={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z'}

    trans=""
    for letter in quote:
        trans+=letter
        if letter in cons:
            trans+='o'+letter.lower()
    return trans

from operator import itemgetter
def easy209():
    print "Enter button press data:"
    inData = list(iter(raw_input, ""))
    print "------------------\n"
    
    data=[]
    for line in inData:
        x=line.split(": ")
        data.append([x[0],float(x[1])])

    data=sorted(data,key=itemgetter(1))
    
    lasttime=0.0
    for user in data:
        print user[0]+": "+str(int(60+lasttime-user[1]))
        lasttime=user[1]

from PIL import Image
def medium210(width=1000,height=100,c2=[204,119,34],c1=[1,66,37]):

    im=Image.new("RGB",(width,height),"white")    
    
    for w in range(width):
        for h in range(height):
            px=[]
            for i in range(3):
                px.append((w*c1[i]+(width-w)*c2[i])/width)
            im.putpixel((w,h),tuple(px))
    im.save("C:/Users/Will/Desktop/test.jpg")
    
        
        

