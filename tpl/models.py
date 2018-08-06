from django.db import models
from uuslug.uuslug import slugify

"""定义UserInfo表"""


class UserInfo(models.Model):
    userName = models.CharField(max_length=20, unique=True, db_column="user_name")
    password = models.CharField(max_length=50)
    slugUrl = models.SlugField(default='', db_column='slug_url')
    header = models.CharField(max_length=255)
    age = models.IntegerField(default=0, db_column='age')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slugUrl = slugify(self.userName) # 生成一个slug值
        super().save(force_insert, force_update, using, update_fields)

    def show(self):
        return "%s-%s" % (self.id, self.userName)

    def age(self):
        return "年龄：19"


"""定义UserContact表跟UserInfo表时一对一"""
class UserContact(models.Model):
    userInfo = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    phone = models.CharField(max_length=18)
    email = models.EmailField(max_length=50)
