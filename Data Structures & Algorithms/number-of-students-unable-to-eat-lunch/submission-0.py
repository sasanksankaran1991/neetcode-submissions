class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        attempts = 0
        while len(students) > 0 and attempts < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                attempts = 0
            else:
                val = students.pop(0)
                students.append(val)
                attempts += 1
            print(students, sandwiches, attempts)
        
        return len(students)