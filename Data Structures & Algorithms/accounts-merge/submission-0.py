class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(0, len(accounts)))
        size = [1] * len(accounts)

        def find(a):
            if parent[a] == a:
                return a
            parent[a] = find(parent[a])
            return parent[a]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if size[pb] > size[pa]:
                pa, pb = pb, pa
            parent[pb] = pa
            size[pa] += size[pb]
        
        emails = {}
        for index, lst in enumerate(accounts):
            for email in lst[1:]:
                if email not in emails:
                    emails[email] = index
                else:
                    union(index, emails[email])

        results = [[] for _ in range(0, len(parent))] 
        for email, idx in emails.items():
            pa = find(idx)
            if len(results[pa]) == 0:
                results[pa].append(accounts[pa][0]) 
            results[pa].append(email)

        return [x for x in results if len(x) > 0]             
