class Solution:
    def countPrimes(self, n: int) -> int:
        prime =[1]*n
        for i in range(2,n):
            if(prime[i]==1):
                for j in range(2*i,n,i):
                    prime[j]=0
        count = 0
        for i in range(2,n):
            if(prime[i]==1):
                count+=1
        return count        






                   

        