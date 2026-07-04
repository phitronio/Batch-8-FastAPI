def insert_student(name : str, math : int , eng : int):
    
    if type(math) == int and type(eng) == int:
        total = math + eng
        print("Total Marks:", total)
        print(type(math))
    else:
        print("Wrong Data Type")



insert_student('Sakib',34,70)