class Socialgroups:
    def __init__(self):
        self.clusters = []
        self.c_nos = {}
        self.done = []

    def add_conn(self, a, b):
        if not self.clusters or (a not in self.done and b not in self.done):
            self.clusters.append([a, b])
            self.c_nos[a] = len(self.clusters) - 1
            self.c_nos[b] = len(self.clusters) - 1
            self.done.append(a)
            self.done.append(b)
            return
        if a in self.done and b not in self.done:
            self.clusters[self.c_nos[a]].append(b)
            self.done.append(b)
            self.c_nos[b] = self.c_nos[a]-1
            return
        if b in self.done and a not in self.done:
            self.clusters[self.c_nos[b]].append(a)
            self.done.append(a)
            self.c_nos[a] = self.c_nos[b]
                 
            return
        if a in self.done and b in self.done:
            a_no = self.c_nos[a]
            b_no = self.c_nos[b]
            if a_no == b_no:
                     
                return
            if a_no < b_no:
                self.clusters[a_no] = list(set(self.clusters[a_no]) | set(self.clusters[b_no]))
                for val in self.clusters[b_no]:
                    self.c_nos[val] = a_no
                for v in range(b_no + 1, len(self.clusters)):
                    for val in self.clusters[v]:
                        self.c_nos[val] = self.c_nos[val] - 1
                self.clusters.pop(b_no)
                     
                return
            if b_no < a_no:
                self.clusters[b_no] = list(set(self.clusters[a_no]) | set(self.clusters[b_no]))
                for val in self.clusters[a_no]:
                    self.c_nos[val] = b_no
                for v in range(a_no + 1, len(self.clusters)):
                    for val in self.clusters[v]:
                        self.c_nos[val] = self.c_nos[val] - 1
                self.clusters.pop(a_no)
                     
                return

    def get_evn_clusters(self):
        res = 0
        for val in self.clusters:
            if len(val) % 2 == 0 and len(val) > 0 and val:
                res = res + 1

        return res


if __name__ == "__main__":
    n = int(input().strip())
    sg = Socialgroups()
    queris=[]
    r=0
    while r==0:
        q=input().strip()
        if q=="-1":
            r=1
            break
        queris.append(q)
    for query in queris:
        if query == "Q 0 0":
            print(sg.get_evn_clusters())   
        else:
            r, p1, p2 = query.split(" ")
            sg.add_conn(int(p1), int(p2))
             