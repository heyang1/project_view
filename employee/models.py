from django.db import models

# Create your models here.


class Dept(models.Model):

    """部门实体"""
    # 编写属性 deptno -- 主键 dname, loc 三个属性
    deptNo = models.AutoField(primary_key=True) # 设置主键
    dname = models.CharField(max_length=100, unique=True)
    loc = models.CharField(max_length=100, db_index=True)
    class Meta:
        db_table = 'dept'


class Emp(models.Model):
    """员工实体"""
    empNo = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=255)
    job = models.CharField(max_length=50)
    # 上一级领导是一个自连接
    mgr = models.ForeignKey(to="self", db_column="mgr", on_delete=models.CASCADE,
                            db_constraint=False, null=True)
    hireDate = models.DateField()
    sal = models.DecimalField(max_digits=8, decimal_places=2)
    comm = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    # 关联部门
    dept = models.ForeignKey(to=Dept, on_delete=models.CASCADE,db_column='deptNo')
    choices = [
        (1, '男'),
        (0, '女'),
    ]
    gender = models.IntegerField(choices=choices, null=True)
    is_valid_choices = [
        (1, '有效'),
        (0, '无效'),
    ]
    isValid = models.IntegerField(db_column="is_valid", choices=is_valid_choices)

    class Meta:
        db_table = 'emp'


class SaleGrade(models.Model):
    grade = models.AutoField(primary_key=True)
    lowsal = models.IntegerField()
    higsal = models.IntegerField()

    class Meta:
        db_table = 'salegrade'
