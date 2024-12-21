list1=["Aahaan","Aarush","Rahul","Aly"]
list2=[1,5,9,7]

dic={list1:list2 for list1,list2 in zip(list1,list2)}
print(dic)