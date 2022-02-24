dataset=[["Whih of the following is the correct identifier?","Which of the following is the address operator?","Which of the following features must be supported by any programming language to become a pure object-oriented programming language?","Which of the following refers to characteristics of an array?","If we stored five elements or data items in an array, what will be the index address or the index number of the array\"s last data item?","Which of the following is the correct syntax for declaring the array?","Which of the following is the correct syntax for accessing the first element?","Which of the following gives the 4th element of the array?","Which type of memory is used by an Array in C++ programming language?","Which one of the following is the correct definition of the \"is_array();\" function in C++?"],
    ["$var_name","@","Encapsulation","An array is a set of similar data items","2","int array{};","array[2];","array[2];","Contiguous","It checks that the specified variable is of the array or not"],
    ["VAR_123","#","Inheritance","An array is a set of distinct data items","3","int array [5];","array[0]","array[3]","None-contiguous","It checks that the specified array of single dimension or not"],
    ["varname@","&","Polymorphism","An array can hold different types of data types","4","Array[5];","Array[5];","Array[5];","Both A and B","It checks that the array specified of multi-dimension or not"],
    ["None of the above","%","All of the above","None of the above","5","None of the above","array[1]","array[1]","Not mentioned","Both B and C"],
    ["B","C","D","A","C","B","B","B","A","A"]]


count=0
fail_count=0
score=0
while(count!=10):
        print("Question ",count+1)
        print(dataset[0][count])
        print("A. ", dataset[1][count])
        print("B. ", dataset[2][count],"\n")
        print("C. ", dataset[3][count])
        print("D. ", dataset[4][count])
        check = input("What is your answer(CAPS): ")
        if(check!=dataset[5][count] and fail_count!=2):
            count
            fail_count+=1
            print("Answer is wrong, you have ",3-fail_count," more tries")
        elif(check==dataset[5][count]):
            count+=1
            score+=1
        elif(fail_count==2):
            count+=1
            fail_count=0
            
print("Your score is ",score)
   
    
    
    
    
