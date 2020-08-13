#클래스를 정의 할 때 큰 클래스부터 차례대로 정의해 나간다
# class Person(object):
# class MITPerson(Person):
# class Student(MITPerson): 등 순서대로
import datetime

# 일반적인 객체의 형태
class Person(object):
    # 첫줄에 속성인__init__을 정의
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1] # 빈칸부터 마지막까지
    
    # 둘째줄부터 class method정의. 클래스 내부 함수는 setter와 getter로 구성되어 있다.
    # getter는 어떠한 외부로 부터 받는 변수가 없는 반면, setter는 외부로부터 값을 받는다.
    # getter는 return값이 있으나, setter는 return값이 없다.
    # 항상 getter와 setter로 이루어져 있는 것은 아니다.
    def getLastName(self):
        return self.lastName
    
    def setBirthday(self, year, month, day):
        self.birthday = datetime.date(year, month, day)
    
    def getAge(self):
        try:
            return (datetime.date.today() - self.birthday).days
        except ValueError:
            print("There is no value in the birthday")
    
    # 자기자신 instance와 other instance를 비교하는 함수정의 => 무엇을 비교할 것인가?
    def __lt__(self, other):
        """ 
        assume that other is instance of Person 
        return True if other.lastname is bigger than self, otherwise return False
        """
        #3 object가 무엇인지에 대해 작성(assume을 docstring으로 작성해도 무방)
        if self.lastName == other.lastName:
            return self.name < other.name #2 성이 같을 경우 어떻게 처리할 것인지에 대해 작성
        return self.lastName < other.lastName #1 먼저 무엇을 비교할 것인지에 대해 정의

    # instance를 print했을때 어떤식으로 보여지게 할것인지에 대해 정의. type: string
    def __repr__(self):
        return self.name

# MITPerson은 Person클래스의 자식클래스이다.
class MITPerson(Person):
    # 클래스 내부에서 글로벌 변수의 역할을 한다. 함수랑 비슷한 성격
    # 외부에서 값을 받지 않아도 될경우, __init__에서 바로 정의할 수 있다. 대신 값이 있어야 함
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name) # Person 클래스의 속성을 모두 상속한다. 만약 MIT Person에 없다면, 부모클래스의 속성 참조
        self.idNum = MITPerson.nextIdNum #클래스의 글로벌 변수를 참조하기 위한 형식(클래스명.변수이름)
        MITPerson.nextIdNum += 1 #인스턴스가 생성될 때마다 __init__이 불러와지고, nextIdNum이 자동으로 1씩증가, 이는 클래스 내에 저장됨
    
    # instance.idNum으로 바로 반환할 수 있으나 get 함수를 만들어 주는것이 좋다.
    def getIdNum(self):
        return self.idNum

    def speak(self, utterance):
        return f"{self.getLastName()} says: {utterance}"
    
    # 주의해야 할 것: 속성과 달리, MITPerson클래스로 인스턴스를 만들었다면, 부모 클래스와 자식클래스 동일한 메서드가 있더라도 자식을 먼저 참조한다.
    def __lt__(self, other):
        return self.idNum < other.IdNum
    
    