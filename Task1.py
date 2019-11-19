def leader_lis(lis):
    maxi=lis[-1]
    l=[maxi]
    for i in range(len(lis)-2,-1,-1):
        if lis[i]>=maxi:
            maxi=lis[i]
            l.append(maxi)
    return l

if __name__=="__main__":
    print("Enter list of array elements separated by space")
    inp=list(map(int,input().split()))
    print("Leaders in the list are {}" .format(leader_lis(inp)))