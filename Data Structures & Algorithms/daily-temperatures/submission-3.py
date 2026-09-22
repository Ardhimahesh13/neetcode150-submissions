class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]* len(temperatures)
        stack = []

        for i, t in enumerate (temperatures) :
            while stack and t > temperatures[stack[-1]] :
                prev_index = stack.pop()
                result[prev_index] = i - prev_index 
            stack.append(i)
        return result