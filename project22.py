import atexit


students=["zion","james","nicole","kemi","clinton","timi","temi","mimi","tolu"]

checker = input("check student: ")

def attendace(checker):
    if(checker in students):
        print("he attended class")
    else:
        print("he did not attend class")
        
attendace(checker)
