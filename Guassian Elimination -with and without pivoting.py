'''
----------------------------------------------------------------
Title: Gauss Elimination Method
Name: Vineeth Pachava
--------------------------------
'''
def Guassian_nonpivot(D,E,n):									#A is assigned to D,B is assigned to E
        for k in range(n):                            
                        for j in range(k+1,n):                  #elimination part
                                if D[k][k]==0:                  #making sure that zero does not end up in denominator
                                        raise ValueError('element is zero')
                                l =D[j][k]/D[k][k]              #the lambda/multiplication factor
                                for m in range(k,n):
                                        D[j][m]=D[j][m]-l*D[k][m]  #performing row subtractions
                                E[j] =E[j] -l*E[k]                 #performing row subtractions on B vector
        #displaying the values
        print(" ")
        print ('Vector after guassian elimination without pivoting:')				
        print (E)
        print("")
        print ('matrix A after guassian Elimination without pivoting:')
        print (D)
        x = [0 for i in range(n)]    											#intialising solution matrix
        for i in range(n-1,-1,-1):
                sum=0.0
                for j in range(i+1,n):
                        sum+=D[i][j]*x[j]
                x[i]=(E[i]-sum)/D[i][i]
        print("=============================================================== ")
        print ('Solution without pivoting')
        print (x)

def Guassian(A,B,n):
        for k in range(n):                              #partial pivoting
                maxi=k
                for i in range(k+1,n):
                        if abs(A[i][k])>abs(A[maxi][k]):        #Choose largest pivot element
                               maxi=i;     
                        if maxi !=k:
                                A[k],A[maxi]=A[maxi],A[k]         #row swaping
                                B[k],B[maxi]=B[maxi],B[k]
        print("==================================================")
        print("matrix A after pivoting")
        print(A)
        for k in range(n):                              #partial pivoting
                        for j in range(k+1,n):                  #elimination part
                                if A[k][k]==0:                  #making sure that zero does not end up in denominator
                                        raise ValueError('element is zero',k)
                                l =A[j][k]/A[k][k]              #the lambda/multiplication factor
                                for m in range(k,n):
                                        A[j][m]=A[j][m]-l*A[k][m]  #performing row subtractions
                                B[j] =B[j] -l*B[k]                 #performing row subtractions on B vector
        print("========================================================== ")
        print ('Vector after guassian elimination with pivoting:')
        print (B)
        print("===========================================================")
        print ('matrix A after guassian Elimination with pivoting:')
        print (A)

        x = [0 for i in range(n)] 								#back substitution
        for i in range(n-1,-1,-1):
                sum=0.0
                for j in range(i+1,n):
                        sum+=A[i][j]*x[j]
                x[i]=(B[i]-sum)/A[i][i]
        print(" ===========================================================")
        print ('Solution with pivoting:')
        print (x)
#end of guassian function

#inputting values
print("choose 1->guassian elimination without pivoting:")
print("2->with pivoting")
a= input()
print(a)
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
print("================================================")

if a=='1':
	Guassian_nonpivot(A,B,n)
if a=='2':
	Guassian(A,B,n)
               
        
