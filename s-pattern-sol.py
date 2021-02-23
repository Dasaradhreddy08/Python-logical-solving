n=int(input().strip())


l=1

arrt=[]
val=1

arrty=[]
arrti=[]
arrto=[]
for val in range(1,2*n):
    arrty.append(val)

for valk in arrty:
    if valk%2==1:arrto.append(valk)
arrto.append(0)

t=n
while t>=0:
    arrti.append(t)
    t=t-1
    
while val<2*n:
    arrt.append(val)
    val=val+2
i=0
    
while i<n:
    k=i+1
    s=arrty[i:k+i]
    ln=1
    st=""
    p=0
    while p<k:
        
        st+=str(s[p])
        
        p=p+1
    print(" "*(n-i-1)+str("*")*(i+1)+" "+st)
    i=i+1
j=0    
while j<n:
    s=arrti[0:-j-1]
    y=arrto[j:-1]
    
    sy=""
    p=0
    while p<n-j:
        sy+=str(s[p])
        p=p+1
        
    sy+=" "
    p=0
    
    while p<n-j:
        sy+=str(y[p])
        p=p+1
    print(" "*j+str(sy))
    j=j+1
        
    
    
