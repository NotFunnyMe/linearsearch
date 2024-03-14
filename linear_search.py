def linear_serach(n,x):
    element = []
    for i in range(1,n):
        element.append(i)

    count = 0
    flag = 0
    for i in element:
        count+=1
        if i == x:
            print("Element found at index: ",str(i))
            flag = 1
            break
    
    if flag == 0:
        print("Element not found")

    print("number of iterations: ",str(count))

linear_serach(1001,10)