inf=9999
def printsolution(vertices,distance):
    for i in range(vertices):
        for j in range(vertices):
            if distance[i][j]==inf:
                print(inf,end=" ")
            else:
                print(distance[i][j],end=" ")    
        print()

def floydwarshalls(vertices,g):
    distance=g
    for k in range(vertices):   #d**0,d**1,d**2,d**3
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
            


    printsolution(vertices,distance)        


g=[[0,8,inf,1],              # this is actually d**0 
   [inf,0,1,inf],
   [4,inf,0,inf] ,
   [inf,2,9,1]
    ]        
floydwarshalls(4,g)