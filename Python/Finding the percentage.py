


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = 0
    for item in student_marks[query_name] :
        result  += item 
    avg = result / len(student_marks[query_name]) 
    print("%0.2f" % avg)
    
    
    
