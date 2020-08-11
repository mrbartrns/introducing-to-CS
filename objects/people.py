import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        return self.lastName
    
    def setBirthday(self, year, month, day):
        self.birthday = datetime.date(year, month, day)
    
    def getAge(self):
        try:
            return (datetime.date.today() - self.birthday).days
        except ValueError:
            print("There is no value in the birthday")
        
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

class MITPerson(Person):
    #global var in class
    nextIdNum = 0

    #객체가 생성될 때마다 nextIdNum이 1씩 증가
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
    
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return f"{self.getLastName()} says: {utterance}"

    def __repr__(self):
        return self.name


m3 = MITPerson('Mark Zuckerberg')
#class이름을 사용시, self에 instance이름을 넣어야 함
Person.setBirthday(m3,84,5,14)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2,83,3,4)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1,55,10,28)

MITPersonList = [m1, m2, m3]
#sorted by iD number
MITPersonList.sort()

print(MITPersonList)
print(m3.getIdNum(), m2.getIdNum(), m1.getIdNum())

a = ['a', 'b', 'd', 'c']
a.sort()
print(a)