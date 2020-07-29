# OOP 2

- 인스턴스 & 클래스 변수
- 인스턴스 & 클래스간의 이름공간
- 인스턴스 & 클래스 메서드(+ 스태틱 메서드)



## 1. 인스턴스 & 클래스 변수

### 1.1 인스턴스 변수

- 메서드 정의에서 `self.변수명`로 정의
- 인스턴스가 생성된 이후 `인스턴스.변수명`로 접근 및 할당
- 각 인스턴스들의 고유한 변수(데이터)

```python
class Person:
    def __init__(self, name):    # 인스턴스 메서드 (생성자) 
        self.name = name         # 인스턴스 변수
        
john = Person('john')
eric = Person('eric')

print(john.name)
print(eric.name)
```

```python
john
eric
```



### 1.2 클래스 변수

- 해당 클래스의 모든 인스턴스가 공유
- 클래스 정의 내부에서 선언
- `클래스.변수명` 또는 `인스턴스.변수명`으로 접근(할당)

```python
class Person:
    species = 'human'
    
    def __init__(self, name):
        self.name = name
        
john = Person('john')
eric = Person('eric')
print(Person.species)
print(john.species)
print(eric.species)
```

```python
human
human
human
```



- 클래스 변수를 한번 바꿔보자

```python
class Person:
    species = 'human'
    
    def __init__(self, name):
        self.name = name
john = Person('john')
eric = Person('eric')
print(john.species)
print(eric.species)
john.species = 'developer'
print(john.species)
print(eric.species)
```

```python
human
human
developer
human
```

- 다른 인스턴스는 수정 못했음
- 각자 인스턴스가 임시로 불러와 저장된 값에만 덮여진다.



## 2. 인스턴스 & 클래스간의 이름 공간

### 2.1 이름 탐색 순서

- 인스턴스와 클래스 모두에서 같은 속성 이름이 등장하면, 인스턴스를 우선

```python
class Person:
    name = '김싸피'

    def __init__(self, name='ssafy'):
        self.name = name
    
    def talk(self):
        return f'안녕, 나는 {self.name}'
p1 = Person()
p1.talk()
Person.name
```

```python
'안녕, 나는 ssafy'
'김싸피'
```



### 2.2 이름공간 원칙

- 인스턴스에서 변수의 이름을 조회를 할 수 없다면, 클래스 객체의 데이터를 조회한다.
- 인스턴스 > 클래스 > 상위클래스 순

```python
class Person:
    name = '김싸피'

    def talk(self):
        return f'안녕, 나는 {self.name}'
p1 = Person()
p1.talk()
p1.name = 'john'
p1.talk()
p2 = Person()
p2.talk()
```

```python
'안녕, 나는 김싸피'
'안녕, 나는 john'
'안녕, 나는 김싸피'
```



## 3. 인스턴스 & 클래스 메서드

### 3.1 인스턴스 메서드

- 인스턴스가 사용하는 메서드
- 클래스 내부에 정의되는 메서드의 기본값은 인스턴스 메서드
- 호출시, 첫 인자로 인스턴스 자기자신 `self`가 전달

```python
class MyClass:
    def instance_method(self, arg1, arg2, ...):
        ...

my_instance = MyClass()
my_instance.instance_method(arg1, arg2)

# 호출시, 첫 번째 인자로 인스턴스(my_instance)가 전달됨
MyClass.instane_method(my_instance, arg1, arg2)
```



### 3.2 클래스 메서드

- 클래스가 사용할 메서드
- `@classmethod` 데코레이터를 사용하여 정의
- **호출시, 첫 번째 인자로 클래스 `cls`가 전달됨**

```python
class MyClass:
    @classmethod
    def class_method(cls, arg1, arg2, ...):
        ...

# 호출시, 첫 번째 인자로 클래스(MyClass)가 전달됨
MyClass.class_method(MyClass, arg1, arg2, ...)  
```



### 3.3 스태틱 메서드

- 클래스가 사용할 메서드
- `@staticmethod` 데코레이터를 사용하여 정의
- **호출시, 어떠한 인자도 전달되지 않음**

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2, ...):
        ...

# 호출시, 어떤 인자도 전달되지 않음
MyClass.static_method(arg1, arg2)
```



### 3.4 예제

```python
class Puppy:
    population = 0
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Puppy.population += 1
        
    def __del__(self):
        Puppy.population -= 1
    
    def bark(self):
        return f'왈왈! 나는{self.name}, {self.breed}(이)야'
    
    @classmethod
    def get_population(cls):
        return f'현재 강아지 마리수: {cls.population}'
    
p1 = Puppy('초코', '푸들')
p2 = Puppy('꽁이', '말티즈')
p3 = Puppy('별이', '시츄')
print(p1.name, p2.name, p3.name)
print(Puppy.get_population())
print(p1.get_population())
```

```python
초코 꽁이 별이
현재 강아지 마리수: 3
현재 강아지 마리수: 3
```





```python
class Puppy:
    population = 0
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Puppy.population += 1
        
    def __del__(self):
        Puppy.population -= 1
    
    def bark(self):
        return f'왈왈! 나는{self.name}, {self.breed}(이)야'
    
    @classmethod
    def get_population(cls):
        return f'현재 강아지 마리수: {cls.population}'
    
    @staticmethod
    def info():
        return '이것은 Puppy 클래스입니다!'
    
choco = Puppy('초코', '푸들')

# instance method
print(choco.bark())

# static method
print(choco.info(), Puppy.info())

# class method
print(Puppy.get_population())
```

```python
왈왈! 나는초코, 푸들(이)야
이것은 Puppy 클래스입니다! 이것은 Puppy 클래스입니다!
현재 강아지 마리수: 1
```



## 4. 정리

### 인스턴스와 메서드

- 인스턴스는, 3가지 종류의 메서드 모두에 접근할 수 있다.
- 하지만 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않아야 한다. (가능하다 != 사용한다)
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계한다.

### 클래스와 메서드

- 클래스 또한 3가지 종류의 메서드 모두에 접근할 수 있다.
- 하지만 클래스에서 인스턴스 메서드는 호출하지 않는다. (가능하다 != 사용한다)
- 클래스가 할 행동은 다음 원칙에 따라 설계한다. (클래스 메서드와 정적 메서드)
  - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 **클래스 메서드**로 정의한다.
  - 클래스와 클래스 속성에 접근할 필요가 없다면 **정적 메서드**로 정의한다.

### 클래스메서드와 정적메서드

- 클래스 메서드와 정적 메서드는 인스턴스 없이 호출할 수 있다는 점은 같다.
- 하지만 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용하며 그렇지 않을 경우 정적 메서드를 사용한다.