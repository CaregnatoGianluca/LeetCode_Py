from typing import List
class twoSum:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            j = i + 1
            while n + numbers[j] < target:
                j += 1
            if n + numbers[j] == target:
                return [i+1 , j+1]