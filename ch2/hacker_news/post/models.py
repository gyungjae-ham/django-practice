from django.db import models

# Create your models here.
# 게시물
# - 제목, 본문, 작성자 이름, 좋아요 개수, 게시물 생성시간
# Django ORM은 기본적으로 Lazy Loading으로 동작한다
# 실제 정보가 필요할 때 쿼리를 실행한다

class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    author_name = models.CharField(max_length=32)
    points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}, {self.title}"