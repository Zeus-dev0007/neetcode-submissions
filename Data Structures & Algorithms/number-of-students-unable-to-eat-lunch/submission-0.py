class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = Counter(students)

        for sandwich in sandwiches:
            if student_count[sandwich] > 0:
                student_count[sandwich] -= 1
            
            else:
                break

        return student_count[0] + student_count[1]
