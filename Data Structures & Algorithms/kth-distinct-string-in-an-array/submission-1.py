class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        disti_count = 0

        for i in range(len(arr)):
            match_count = 0

            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    match_count += 1

            if match_count == 1:
                disti_count += 1

                if disti_count == k:
                    return arr[i]

        return ""