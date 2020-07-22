# 함수(Function) II

- 함수와 스코프
- 재귀함수



## 1. 함수와 스코프

> 함수는 코드 내부에 공간을 생성하고 이 공간을 지역 스코프라고 부른다. 그 외의 공간은 전역 스코프라고 부른다.

- 전역 스코프 : 코드 어디서든 참조 가능
- 지역 스코프 : 함수가 만든 스코프로 함수 내부에서만 참조 가능
- 전역 변수 : 전역 스코프에 정의된 변수
- 지역 변수 : 지역 스코프에 정의된 변수



### 1.1 이름 검색 규칙

> 파이썬에서 사용되는 식별자들은 이름 공간에 저장되어 있으며 아래의 순서로 이름을 찾아간다.

함수 내부에서 점점 밖으로 나가며 큰 범위를 탐색한다고 생각하면 된다.

- Local scope : 정의된 함수
- Enclosed scope : 상위 함수
- Global scope : 함수 밖의 변수 혹은 import된 모듈
- Built-in scope : 파이썬안에 내장되어 있는 함수 또는 속성

밖에서는 안을 못보고 안에서는 밖을 보고 참조 할 수 있다.

```python
global_num = 3
def local_scope():
    global_num = 5
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num)
```

```python
#실행 결과
global_num이 5으로 설정되었습니다.
global_num: 3 #함수 안을 참조 못하고 전역 스코프를 참조하기 때문
```



```python
global_num = 3
def local_scope():
    global global_num
    global_num = 5
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num)
```

```python
global_num이 5으로 설정되었습니다.
global_num: 5 #함수 안에서 전역 스코프 값 자체를 끌고와서 수정했기 때문
```





### 1.2 변수의 수명주기

> 변수의 이름은 각자의 수명주기가 존재

- 빌트인 스코프 : 파이썬이 실행되있는 동안 계속
- 전역 스코프 : 모듈이 호출된 시점 이후 또는 이름이 선언된 이후부터 인터프리터가 끝날때 까지
- 지역 스코프 : 함수가 돌아 가는 동안





## 2. 재귀 함수

> 함수 내부에서 자기 자신을 호출하는 함수

### 2.1 팩토리얼 계산

#### 2.1.1 반복문을 이용한 팩토리얼 계산

```python
def fact(num):
  ans = 1
  for i in range(1,num+1):
    ans *= i
  return ans
```

#### 2.1.2 재귀를 이용한 팩토리얼 계산

```python
def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num-1)
```



### 2.2 반복문과 재귀함수

- 재귀함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제를 푼다.
- 재귀함수를 작성시에는 반드시, `base case`가 존재 하여야 한다.
- `base case`는 점점 범위가 줄어들어 반복되지 않는 최종 위치



#### 2.2.1 최대 재귀 깊이

- 파이썬은 최대 재귀 깊이가 정해져있다.



### 2.3 피보나치 수열

#### 2.3.1 재귀를 이용한 피보나치 수열

```python
def fib(num):
  if num < 3:
    return 1
  return fib(num-1)+fib(num-2)
```

#### 2.3.2 반복문을 이용한 피보나치 수열

```python
def fib_loop(n):
  if n < 3:
    return 1
  n1 = n2 = 1
  ret = 0
  for i in range(3,n+1):
    ret = n1 + n2
    if i % 2:
      n1 = ret
    else:
      n2 = ret
  return ret
```



### 2.4 반복문과 재귀 함수의 차이

- 알고리즘이 재귀적 표현이 자연스러울 경우 재귀 함수 사용
- 재귀 호출은 변수 사용을 줄여줌