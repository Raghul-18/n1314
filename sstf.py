def calculate_diff(queue,head,diff):
    for i in range(len(diff)):
        diff[i][0]=abs(queue[i]-head)
def find_min(diff):
    ind=-1
    minim=999999
    for i in range(len(diff)):
        if (not diff[i][1] and diff[i][0]<minim):
            minim=diff[i][0]
            ind=i
    return ind
def sstf(request,head):
    if len(request)==0:
        return
    l=len(request)
    diff=[0]*l
    for i in range(len(diff)):
        diff[i]=[0,0]
    seek_count=0
    seek_sequence=[0]*(l+1)
    for i in range(l):
        seek_sequence[i]=head
        calculate_diff(request,head,diff)
        ind=find_min(diff)
        diff[ind][1]=True
        seek_count+=diff[ind][0]
        head=request[ind]
    seek_sequence[len(seek_sequence)-1]=head
    for i in range(len(seek_sequence)):
        print(seek_sequence[i])
    return seek_count
proc = [93,176,42,148,27,14,180]
seek=sstf(proc,55)
print("Seek_count: ",seek)

