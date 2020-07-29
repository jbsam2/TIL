# OOP 1

- 객체(Object)
- 객체지향프로그래밍(Object Oriented Programming)
- 클래스(Class)와 객체(Object)



## 1. 객체

> 파이썬에서 모든 것은 객체
>
> 모든 객체는 타입, 속성, 조작법을 가진다



### 1.1 객체의 특징

- 타입 : 어떤 연산자와 조작이 가능한가?
- 속성 : 어떤 상태를 가지는가?
- 조작법 : 어떤 행위를 할 수 있는가?



### 1.2 타입과 인스턴스

| type | instance           |
| ---- | ------------------ |
| int  | 0,1,2              |
| str  | '', '123'          |
| list | [],[1,2,3]         |
| dict | {},{'key':'value'} |

#### 1.2.1 타입

- 공통된 속성과 조작법을 가진 객체들의 분류

#### 1.2.2 인스턴스

- 특정 타입의 실제 데이터 예시
- 파이썬에서 모든 것은 객체, 모든 객체는 특정 타입의 인스턴스

```python
a = int(10)
b = int(20)
# a, b는 객체
# a, b는 int 타입의 인스턴스
```

```python
a = int(10)
isinstance(a,int) #isinstance(데이터, 타입)
True
```



### 1.3 속성과 메서드

| type      | 속성             | 메서드                                 |
| --------- | ---------------- | -------------------------------------- |
| `complex` | `.real`, `.imag` |                                        |
| `str`     | -                | `.capitalize()`, `.join()`, `.split()` |
| `list`    | -                | `.append()`, `.reverse()`, `.sort()`   |
| `dict`    | -                | `.keys()`, `.values()`, `.items()`     |



#### 1.3.1 속성

- 속성은 객체의 상태/데이터를 의미
- 활용법 : <객체>.<속성>

```python
a = 3+4j
print(a.real)
print(a.imag)

3.0
4.0
```



#### 1.3.2 메서드

- 특정 객체에 적용할 수 있는 행위
- 활용법 : <객체>.<조작법>()

```python
a = [3, 2, 1]
a.sort()
print(a)

[1,2,3]
```



## 2. 객체 지향 프로그래밍

> 객체가 중심이 되는 프로그래밍
>
> 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다.



### 2.1 절차 중심 vs 객체 중심

> 프로그래밍 패러다임: 어떻게 프로그램을 정돈(organize)할 것인가



### 2.2 객체 중심의 장점

> 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용된다.
>
> 또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며,
>
> 보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있다.

- 코드의 직관성
- 활용의 용이성
- 변경의 유연성



## 3. 클래스와 객체

> `type`: 공통 속성을 가진 객체들의 분류(class)
>
> `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드



### 3.1 클래스 생성

- 클래스 생성은 `class` 키워드와 정의하고자 하는 `<클래스의 이름>`으로 가능
- `<클래스의 이름>`은 `PascalCase`로 정의한다.
- 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 정의된 함수는 **메서드(method)**로 불린다.

```python
class <클래스이름>:
    <메소드>
class ClassName:
    methods
```

```python
class Person:
    pass
print(type(Person))
<class 'type'>
```



### 3.2 인스턴스 생성

- 정의된 클래스에 속하는 객체를 해당 클래스의 인스턴스라고 한다.

```python
# 인스턴스 = 클래스()
person1 = Person()
```

- person1은 사용자가 정의한 Person이라는 데이터 타입의 인스턴스

```python
class Person:
    """
    이것은 Person 클래스(class)입니다.
    """
person1 = Person()
person2 = Person()
print(type(person1))
print(type(person2))
print(person1.__doc__)
print(person2.__doc__)


<class '__main__.Person'>
<class '__main__.Person'>

    이것은 Person 클래스(class)입니다.
    

    이것은 Person 클래스(class)입니다.
```



### 3.3 메서드 정의

> 특정 데이터 타입의 객체에 공통적으로 적용 가능한 행위들

```python
class Person:
    # 메서드(method)
    def talk(self):    # 인자로 self를 붙여줍니다.
        return '안녕'
    
p1 = Person()
p1.talk()
```

```python
'안녕'
```



- 메서드도 함수이기 때문에 추가적인 인자를 받을 수 있다.

```python
class Person:
    def talk(self):
        return '안녕'
    
    def eat(self, food):
        return f'냠냠 {food}'
    
p1 = Person()
p1.eat('hamburger')
```

```python
'냠냠 hamburger'
```



- 기본 인자, 가변 인자 리스트 등 함수의 인자와 동일하게 매개변수를 정의할 수 있다.

```python
class Person:
    def talk(self):
        return '안녕'
    
    def eat(self, food="(먹을거줘)"):
        return f'{food} 냠냠'
p1 = Person()
p1.eat()
```

```python
'(먹을거줘) 냠냠'
```



#### 3.3.1 생성자 메서드

> 인스턴스 객체가 생성될 때 호출되는 함수

```python
def __init__(self):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
```

- 생성자를 활용하면 인스턴스가 생성될 때 인스턴스의 속성을 정의 할 수 있다.



#### 3.3.2 소멸자 메서드

> 인스턴스 객체가 소멸되기 직전에 호출되는 함수

```python
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
```



- 생성자와 소멸자 활용 예시

```python
class Person:
    def __init__(self):
        print('응애!')
        
    def __del__(self):
        print('갈게..')
        
p1 = Person()
del p1
```

```python
응애!
갈게..
```



```python
p1 = Person()
p1 = 'hello'
```

```python
응애!
갈게..
```

- 처음에는 클래스를 생성 했지만 p1이 새로운 값을 지정하면서 클래스가 사라지는 것과 같은 효과를 보여준다.



### 3.4 속성 정의

> 특정 데이터 타입의 객체들이 가지게 될 상태/데이터를 의미

```python
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return f'안녕, 나는 {self.name}'

me = Person('홍길동')
print(me.name)
```

```python
홍길동
```



- 인스턴스 변수의 값은 변경도 가능

```python
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return f'안녕, 나는 {self.name}'

me = Person('홍길동')
print(me.name)
me = Person('홍싸피')
print(me.name)
```

```python
홍길동
홍싸피
```



### 3.5 매직메서드

- 더블언더스코어(`__`)가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드이기 때문에 매직 메서드라고 부른다



예시)

```python
class Person:
    def __init__(self, name):
        self.name = name
p1 = Person('john')
print(p1)
```

```python
<__main__.Person object at 0x000002512A7F53C8>
```

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'나는 {self.name}'
p1 = Person('john')
print(p1)
```

```python
나는 john
```



#### 3.5.1 `self`: 인스턴스 자신

- Python에서 메서드는 **호출 시 첫번째 인자로 인스턴스 자신이 전달**되게 설계되었다.

- 보통 매개변수명으로 `self`를 첫번째 인자로 설정(다른 이름도 가능)

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        return f'안녕, 나는 {self.name}'
john = Person('john')
john.talk()

Person.talk(john)
```

```python
'안녕, 나는 john'
'안녕, 나는 john'
```





## 4. 정리

### 객체(Object)

- 객체는 자신 고유의 **속성(attribute)**을 가지며 클래스에서 정의한 **행위(behavior)**를 수행할 수 있다.

### 클래스(Class)

- 공통된 속성(attribute)과 행위(behavior)를 정의한 것으로 객체지향 프로그램의 기본적인 **사용자 정의 데이터형(user-defined data type)**

### 인스턴스(Instance)

- 특정 `class`로부터 생성된 해당 클래스의 예시(instance)

### 속성(Attribute)

- 클래스/인스턴스가 가지는 속성(값/데이터)

### 메서드(Method)

- 클래스/인스턴스에 적용 가능한 조작법(method) & 클래스/인스턴스가 할 수 있는 행위(함수)