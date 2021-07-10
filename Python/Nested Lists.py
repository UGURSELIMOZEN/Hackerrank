


if __name__ == '__main__':
    grade = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
    
        grade.append([name , score])
        
    second_highest = sorted(set([score for name, score in grade]))[1]
    print('\n'.join(sorted([name for name, score in grade if score == second_highest])))
    
    
    
