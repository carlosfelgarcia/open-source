'''
Created on 02/05/2013

@author: carlosfelgarcia
'''
temp = []
i=0



def test(x,y,temp):
    if temp[x].count(y) != 0:
    
        print temp[x-1], "temp"
        #print " x " , x, " y ", y
for x in range(0,256):
    for y in range(0,256):
        if y%5==0:
            temp.insert(x,"")

for x in range(0,256):
    temp2=[]
    for y in range(0,256):
        i=i+1
        temp2.append(y)
        if y%5==0:
            temp.insert(x,temp2)
        #test(x,y,temp)
            temp.remove("")


    
print len(temp), " Temp ", i, " total** "