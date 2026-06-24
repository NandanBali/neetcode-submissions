class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        size = [1] * n

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if size[pb] > size[pa]:
                pa, pb = pb, pa
            parent[pb] = pa
            size[pa] += size[pb]

        owner = {}                       # email -> account index
        for i, acct in enumerate(accounts):
            for email in acct[1:]:
                if email in owner:
                    union(i, owner[email])
                else:
                    owner[email] = i

        groups = defaultdict(list)
        for email, i in owner.items():
            groups[find(i)].append(email)

        return [[accounts[root][0]] + emails
                for root, emails in groups.items()]