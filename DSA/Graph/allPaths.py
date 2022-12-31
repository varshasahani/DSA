

class Solution:
    def allPathsSourceTarget(graph):
        res=[]
        source=len(graph)-1
        que=[[0]]
        while que:
            temp=[]
            node=que.pop()
            cur=node[-1]
            for i in graph[cur]:
                x=node.copy()
                x.append(i)
                if i==source:
                    res.append(x)
                else:
                    temp.append(x)
            que.extend(temp)
        return res
    
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(allPathsSourceTarget(graph))