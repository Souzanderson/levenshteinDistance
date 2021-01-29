
class Levenshtein():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
    def distance(self):
        m = [[(i if j==0 else (j if i==0 else 0)) for i in range(len(self.p1)+1)] for j in range(len(self.p2)+1)]
        for i in range(1,len(self.p1)+1):
            for j in range(1,len(self.p2)+1):
                m[j][i] = min(m[j-1][i-1]+int(not(self.p1[i-1] == self.p2[j-1])),m[j][i-1]+1,m[j-1][i]+1)

        return m[-1][-1]
    