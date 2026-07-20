class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        indices = []
        for index, triplet in enumerate(triplets):
            valid = True
            for i in range(0, 3):
                if triplet[i] > target[i]:
                    valid = False
                    break
            if valid:
                indices.append(index)
        
        flts = [False, False, False]
        for index in indices:
            for i in range(0, 3):
                if triplets[index][i] == target[i] and not flts[i]:
                    flts[i] = True
        
        for f in flts:
            if not f:
                return False
        
        return True