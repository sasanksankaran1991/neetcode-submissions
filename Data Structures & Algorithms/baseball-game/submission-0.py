class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []

        for i in range(len(operations)):
            if operations[i] == '+':
                val = record[-1]+record[-2]
                record.append(val)
            elif operations[i] == 'D':
                val = record[-1]*2
                record.append(val)
            elif operations[i] == 'C':
                record.pop()
            else:
                record.append(int(operations[i]))
        
        return sum(record)