def main()
# Những cách cải thiện tốc độ chương trình
import timeit
# 3
def ko_nen_3():
    string_interrupt=["chào ","ban ","xin ","tự ","giới ","thiệu ","tôi là Nguyễn Văn Thiện"]
    new_str=[]
    for i in string_interrupt:
        new_str.append(i.upper())
    return new_str


def in_hoa(x):
    return x.upper()
def nen_3():
    string_interrupt=["chào ","ban ","xin ","tự ","giới ","thiệu ","tôi là Nguyễn Văn Thiện"]
    new_str=map(in_hoa,string_interrupt)
    return new_str
nen_3()    

    
# 2
def ko_nen_2():
    string_interrupt=["chào ","ban ","xin ","tự ","giới ","thiệu ","tôi tên là Nguyễn Văn Thiện"]
    string=""
    for i in string_interrupt:
       string+= i
    return string

def nen_2():
    string_interrupt=["chào ","ban ","xin ","tự ","giới ","thiệu ","tôi tên là Nguyễn Văn Thiện"]
    string="".join(string_interrupt)
    return string


# 1 
def ko_nen():
    array=[]
    for i in range(100):
        array.append(i)
    return array   
  
def nen():
    array=[i for i in range(100) ]
    return array
# 2 kiểm tra tóc độ đoạn code nên_n và ko_nen_n n=(1,2,3,4....)

t=timeit.Timer(setup="from __main__ import ko_nen_3",stmt="ko_nen_3()")
print("không nên: ",t.timeit())

t=timeit.Timer(setup="from __main__ import nen_3",stmt="nen_3()")
print("nên: ",t.timeit())