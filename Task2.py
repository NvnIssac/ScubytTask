def reverse_lis(lis,n):
    if n==1:
        return lis
    for i in range(0,len(lis),n):
        lis[i:i+n]=reversed(lis[i:i+n])
    return lis

if __name__=="__main__":
    print("Enter number of elements to be reversed in groups")
    k = int(input())
    print("Enter list of array elements separated by space")
    inp=list(map(int,input().split()))
    print("Reversed List by {} group subset is {}".format(k,reverse_lis(inp,k)))