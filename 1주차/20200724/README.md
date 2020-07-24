# README

> project01을 하면서 알게 된점



## 1. 알게 된 점

- 파일을 입력 받는 `open` 함수를 알게됨
  - filename : 열고자 하는 파일
  - mode : 기본값은 `r`(읽기 전용), 다른 값들로 수정도 가능 ex) `w` 쓰기 전용
  - encoding : `UTF8` 이 없으면 한글 때문에 파일이 정상적으로 변환 되지 않음 

```python
open(filename, mode, encoding = 'UTF8')
```

- json
  - 아직 자세하게는 배우지 않음 `dict`과 매우 유사하게 생겨먹음

```python
import json
dict_data = json.load(json_data) #=> json 데이터를 파이썬에서 사용할수 있는 dict으로 변환 해줌
```

