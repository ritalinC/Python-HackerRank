if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

#solution 1
    
    list_1 = [];
    list_2 = [];
    
    for A in range(x+1):
        for B in range(y+1):
           for C in range(z+1):
                if A+B+C != n:
                    list_2 = [A,B,C];
                    list_1.append(list_2);
                    
print(list_1);


#Solution 2

list_1 = [[A,B,C] for A in range(x+1) for B in range(y+1) for C in range(z+1) if A+B+C != n ]

print(list_1)