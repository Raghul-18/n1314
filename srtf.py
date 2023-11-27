class Process():
    def __init__(self,no,at,bt):
        self.p_no=no
        self.at=at
        self.bt=bt
        self.rt=bt
        self.start=None
        self.exit=None
        self.tat=None
        self.wt=None
    def TAT(self,exit):
        self.exit=exit
        self.tat=self.exit-self.at
        return self.tat
    def WT(self):
        self.wt=self.tat-self.bt
        return self.wt
def srtf():
    process=[]
    for i in range(4):
        at=int(input(f"Enter Arrival time of P{i}: "))
        bt=int(input(f"Enter Burst time of P{i}: "))
        process.append(Process(i,at,bt))
    process=sorted(process,key=lambda x:x.at)
    completed=[]
    queue=[]
    current_time=0
    out=[]
    while queue or process:
        if process and process[0].at<=current_time:
            queue.append(process.pop(0))
        if queue!=[]:
            queue=sorted(queue,key=lambda x:x.rt)
            p=queue.pop(0)
            p.start=current_time
            p.rt-=1
            if p.rt==0:
                p.exit=current_time+1
                p.tat=p.TAT(p.exit)
                p.wt=p.WT()
                out.append(p)
                completed.append((p.p_no,p.start,p.exit,p.wt,p.tat))
            else:
                if completed==[]:
                    completed.append((p.p_no,p.start,current_time+1,None,None))
                elif p.p_no!=completed[-1][0]:
                    completed.append((p.p_no,p.start,current_time+1,None,None))
                queue.append(p)
        current_time+=1
    return completed,out
def main():
    com,process=srtf()
    process=sorted(process,key=lambda x:x.p_no)
    awt=0
    print("Process_no","\t","Arrival_time","\t","Burst_time","\t","TAT","\t\t","WT")
    for i in range(len(process)):
        print(process[i].p_no,"\t\t",process[i].at,"\t\t",process[i].bt,"\t\t",process[i].tat,"\t\t",process[i].wt)
        awt+=process[i].wt
    print("Average_wt: ",awt/len(process))
    gant_chart=""
    for i in range(len(com)):
        if i!=0:
            if com[i-1][0]==com[i][0]:
                gant_chart+=str(com[i][2])+'|'
            else:
                gant_chart+=str(com[i][1])+" "+"P"+str(com[i][0])+" "
        else:
            gant_chart+=str(com[i][1])+" "+"P"+str(com[i][0])+" "+str(com[i][2])+'|'
    print(gant_chart)
main()



