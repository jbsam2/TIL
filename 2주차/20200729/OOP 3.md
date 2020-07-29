# OOP 3

- 상속(Inheritance)
- 메서드 오버라이딩(Method Overriding)
- 다중 상속(Multiple Inheritance)



## 1. 상속

### 1.1 상속이란?

> 부모 클래스의 모든 속성이 자식 클래스에게 그대로 적용되는 것



```python
class ChildClass(ParentClass):
    <code block>
```



```python
class Person:
    population = 0
    
    def __init__(self, name='사람'):
        self.name = name
        Person.population += 1
        
    def greeting(self):
        print(f'반갑습니다. {self.name}입니다.')
p = Person()
p.greeting()
```

```python
반갑습니다. 사람입니다.
```



클래스를 상속 시켜보자

```python
class Student(Person):
    def __init__(self, student_id, name='학생'):
        self.name = name
        self.student_id = student_id  
        Person.population += 1
s = Student(1)
s.name
s.student_id
s.greeting()
```

```python
'학생'
1
반갑습니다. 학생입니다. # 부모 클래스에 정의된 메서드도 호출 ㅆㄱㄴ
```

### 1.2 상속의 이점

> 코드를 중복하여 정의하지 않아도 됨
>
> 공통된 속성이나 메서드를 부모 클래스에 정의하고 상속함으로써, 적은 코드를 사용해도 다양한 형태의 객체를 생성 가능



```python
issubclass(Student, Person) #True
print(isinstance(s, Student), isinstance(s, Person)) #True True
print(issubclass(bool, int)) # True
print(issubclass(float, int))# False
```



### 1.3 `super()`

- 자식 클래스에 메서드를 추가로 구현가능
- 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용

```python
class Child(Parent):
    def method(self, arg):
        super().method(arg)
```



ex)

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
      
    
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        self.student_id = student_id
    
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('김싸피', 20, '12312312', 'student@naver.com', '190000')
p1.greeting()
s1.greeting()
```

```python
안녕, 홍길동
안녕, 김싸피
```

뭔가 지저분해보이니 수정을 해본다.

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        self.student_id = student_id
        
p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
s1 = Student('김싸피', 20, '12312312', 'student@naver.com', '190000')
p1.greeting()
s1.greeting()
```

```python
안녕, 홍길동
안녕, 김싸피
```



### 예제

>  직사각형 클래스를 만들고 이를 활용하여 정사각형 클래스를 만들어보자

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2* (self.length + self.width)

class Square(Rectangle):
    def __init__(self, length):
        super.__init__(length, length)
squ = Square(4)
print(squ.area())
print(squ.perimeter())
```

```python
16
16
```



## 2. 메서드 오버라이딩

> 자식 클래스에서 부모 클래스의 메서드를 재정의 하는 것

- 상속 받은 메서드도 ㅆㄱㄴ
- 상속 받은 클래스에서 같은 이름의 메서드로 덮어쓴다.

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Soldier(Person):
    def __init__(self, name, age, number, email, rank):
        super().__init__(name, age, number, email)
        self.rank = rank
        
    def greeting(self):
        print(f'충성! {self.rank} {self.name}')

s = Soldier('굳건이', 25, '0101234', 'soldier@roka.kr', '하사')
s.greeting()
```

```python
충성! 하사 굳건이
```



## 3. 상속관계에서의 이름공간

- 인스턴스 -> 자식클래스 -> 부모 클래스 순으로 탐색

```python
class Animal:
    def __init__(self, life=True):
        self.life = life
    
    def eat(self):
        if self.life:
            print('쩝쩝')
            

class Person(Animal):
    def __init__(self, name, life=True):
        super().__init__(life)
        self.name = name
    
    def eat(self):
        if self.life:
            print('냠냠')
            

animal = Animal(True)
animal.eat()

person = Person('ssafy', True)
person.eat()
```

```python
쩝쩝
냠냠
```



## 4. 다중 상속

> 두개 이상의 클래스를 상속받으면 다중 상속이 된다.



```python
class Person:
    def __init__(self, name):
        self.name = name
    
    
    def breath(self):
        return '날숨'
    
    
    def greeting(self):
        return f'hi, {self.name}'
    

class Mom(Person):
    gene = 'XX'
    
    def swim(self):
        return '첨벙첨벙'
    
    
class Dad(Person):
    gene = 'XY'
    
    def walk(self):
        return '성큼성큼'
    
    
class FirstChild(Dad, Mom):
    def swim(self):
        return '챱챱'
    
    def cry(self):
        return '응애'
    
    
baby = FirstChild('아가')
baby.cry()
baby.swim()
baby.walk()
baby.gene
```

```python
'응애' #최종 상속 클래스의 값
'챱챱' #상속 해준 클래스중 swim 메서드를 가진 mom 클래스 값을 받아옴
'성큼성큼' #상속 해준 클래스중 walk 메서드를 가진 dad 클래스 값을 받아옴
'XY' # 먼저 상속해준 dad 클래스 값을 받아옴
```



상속 순서를 바꿔줘보면

```python
class SecondChild(Mom, Dad):  
    def walk(self):  # Dad 의 walk 메서드를 override 합니다.
        return '아장아장'
    
    def cry(self):  
        return '응애'
    
brother = SecondChild('애기')
brother.cry()
brother.walk()
brother.swim()
brother.gene
```

```python
'응애'
'아장아장'
'첨벙첨벙'
'XX' # 상속 순서가 바뀌었기 때문에 받아온 값이 달라짐
```

