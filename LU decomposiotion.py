'''
----------------------------------------------------------------
Title: LU decomposition
Name: Vineeth Pachava
----------------------------------------------------------------
'''
def inverse(A,n):
    s=[]
    for p in range(n):
        b=[]                                            #initialising B and L matrix
        L=[]
        for i in range(n):                          
            row =[]
            for j in range(n):
                if i<j:
                    y=float(0)
                elif i>=j:
                    y=float(1)
                row.append(y)
            L.append(row)
            if i==p:
                b.append(int(1))
            else:
                b.append(int(0))
        for k in range(n):                            
                        for j in range(k+1,n):                  #elimination part
                                if A[k][k]==0:                  #making sure that zero does not end up in denominator
                                        raise ValueError('element is zero',k)
                                l=A[j][k]/A[k][k]              #the lambda/multiplication factor
                                L[j][k]=l                       #assigning values to L matrix
                                for m in range(k,n):
                                        A[j][m]=A[j][m]-l*A[k][m]  #performing row subtractions to get U matrix
        

        Y = [0 for i in range(n)]                               #forward substitution
        for i in range(n):
                sum=0.0
                for j in range(0,i+1):
                        sum+=L[i][j]*Y[j]   
                Y[i]=(b[i]-sum)/L[i][i]

        x = [0 for i in range(n)]                               #back substitution
        for i in range(n-1,-1,-1):
                sum=0.0
                for j in range(i+1,n):
                        sum+=A[i][j]*x[j]
                x[i]=(Y[i]-sum)/A[i][i]
        s.append(x)
        return s
    print(s)
#end of function

    
def LU(A,B,n):
        L=[]
        for i in range(n):										#taking A matrix as input
            row =[]
            for j in range(n):
                if i<j:
                    y=float(0)
                elif i>=j:
                    y=float(1)
                row.append(y)
            L.append(row)
        for k in range(n):                              #partial pivoting
                maxi=k
                for i in range(k+1,n):
                        if abs(A[i][k])>abs(A[maxi][k]):        #Choose largest pivot element
                               maxi=i;     
                        if maxi !=k:
                                A[k],A[maxi]=A[maxi],A[k]         #row swaping
                                B[k],B[maxi]=B[maxi],B[k]
        
        for k in range(n):                              #partial pivoting
                        for j in range(k+1,n):                  #elimination part
                                if A[k][k]==0:                  #making sure that zero does not end up in denominator
                                        raise ValueError('element is zero',k)
                                l=A[j][k]/A[k][k]              #the lambda/multiplication factor
                                L[j][k]=l                       #assigning values to L matrix
                                for m in range(k,n):
                                        A[j][m]=A[j][m]-l*A[k][m]  #performing row subtractions to get U matrix
        print("========================================================== ")
        print ('matrix U')
        print (A)
        print("========================================================== ")
        print('Matrix L')
        print (L)
        Y = [0 for i in range(n)]                               #forward substitution
        for i in range(n):
                sum=0.0
                for j in range(0,i+1):
                        sum+=L[i][j]*Y[j]   
                Y[i]=(B[i]-sum)/L[i][i]
        print(" ===========================================================")
        print ('Y vector after Forward Substitution')
        print (Y)
        print(L)


        x = [0 for i in range(n)] 								#back substitution
        for i in range(n-1,-1,-1):
                sum=0.0
                for j in range(i+1,n):
                        sum+=A[i][j]*x[j]
                x[i]=(Y[i]-sum)/A[i][i]
        print(" ===========================================================")
        print ('Solution:')
        print (x)
#end of function

#inputting values
n = int(input('enter the dimensions'))
A=[]                                
for i in range(n):										#taking A matrix as input
        row =[]
        for j in range(n):
                print('Enter the Element',(i+1),(j+1))
                y=float(input())
                row.append(y)
        A.append(row)
B=[]
for i in range(n):								#taking B matrix as input
        print ('enter the b',(i+1))
        y=float(input())
        B.append(y)
print ('matrix A:') 
print (A)
print("====================================================================")
print ('Vector B')
print(B)
print('1->inverse or 2->LU decomposition ')
h=int(input())
if h==int(2):
    LU(A,B,n)
elif h==int(1):
    inverse(A,n)
        
