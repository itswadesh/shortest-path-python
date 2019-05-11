import distBetTwoPoints as db
n=int(input("Enter Number of Sources"))
lattlong=[]#Adjacency Matrix for n no of sources and n no of destination

#Entering the values of Longitutde and Lattitude.
for i in range(2*n):
    r=[]
    if(i<n):
        strn=str(i+1)+" " 
        strn1="Enter the lattitude of the source "+strn
        r.append(float(input(strn1)));
        strn2="Enter the longitude of the source "+strn
        r.append(float(input(strn2)));
        lattlong.append(r)
    else:
        strna=str(i-n+1)+" "
        strn1="Enter the lattitude of the destination "+strna
        r.append(float(input(strn1)));
        strn2="Enter the longitude of the destination "+strna
        r.append(float(input(strn2)));
        lattlong.append(r)

dZero=[]#This is used as input for Floyd-Warshall Algorithm

#Inserting values into the dZero list
for i in range(2*n):
    r=[]
    for j in range(2*n):
        if(i==j):
            r.append(0);
        else:
            r.append(db.distance(lattlong[i][0],lattlong[i][1],lattlong[j][0],lattlong[j][1]))
    dZero.append(r)
print(dZero)

#Floyd-Warshall Function.
def floydWarshall(graph):
    dist=graph
    for k in range(2*n):
        for i in range(2*n):
            for j in range(2*n):
                dist[i][j]=min( dist[i][j] , dist[i][k] + dist[k][j] )
    print(dist)
    return dist

#Function to get the length of the List 
def len(lis):
    count=0
    for i in lis:
        count+=1
    return count

dist=floydWarshall(dZero)

frontier=[]
path=[]
frontier.append(0)
path.append(0)
currPos=0;

def findmin(i):
    min=[]
    for j in range(2*n):
        if(i==j or j in path):
            continue
        else:
            if(min.__len__()==0):
                min.append(dist[i][j])
                min.append(i)
                min.append(j)
            if(0<=j and j<n):
                if(min[0]>dist[i][j]):
                    min[0]=dist[i][j]
                    min[1]=i
                    min[2]=j
            else:
                if((j-n) in frontier):
                    if(min[0]>dist[i][j]):
                        min[0]=dist[i][j]
                        min[1]=i
                        min[2]=j
    return min
                


while(len(path)<2*n):
    arr=findmin(currPos)
    if(n<=arr[2] and arr[2]<2*n):
        frontier.remove(arr[2]-n)
    else:
        frontier.append(arr[2])
    currPos=arr[2]
    path.append(arr[2])

print(path)
