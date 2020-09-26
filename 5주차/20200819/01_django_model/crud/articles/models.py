from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) #길이의 제한이 있는 문자열을 넣을때 사용,max_length가 필수인자
    content = models.TextField() #글자의 수가 많을 때 사용
    created_at = models.DateTimeField(auto_now_add=True) #최초 생성 일자: (auto_now_add=True) django ORM이 최초 데이터 입력시에만 현재 날짜와 시간으로 갱신
    updated_at = models.DateTimeField(auto_now=True) #최초 수정일자: (auto_now=True) django ORM이 save 할 때마다 현재 날짜와 시간으로 갱신

    def __str__(self):
        return self.title    