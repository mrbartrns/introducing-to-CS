list1 = []
for i in range(15):
    if i % 2 == 0:
        list1.append(i)

print(list1)

# or 
list2 = [i for i in range(15) if i % 2 == 0]
print(list2)

#[<value_to_include> for <elem> in <sequence> if <condition>]
#example
namesDict = {"Nora": 90, "Lulu": 15, "Gino": 60}
doubleGrades = {key: value*2 for (key, value) in namesDict.items() if value % 2 == 0}
print(doubleGrades)
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
len(animals)