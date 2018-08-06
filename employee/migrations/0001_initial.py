# Generated by Django 2.0 on 2018-08-01 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptNo', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100, unique=True)),
                ('loc', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'db_table': 'dept',
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empNo', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=50)),
                ('hireDate', models.DateField()),
                ('sal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comm', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('gender', models.IntegerField(choices=[(1, '男'), (0, '女')], null=True)),
                ('isValid', models.IntegerField(choices=[(1, '有效'), (0, '无效')], db_column='is_valid')),
                ('dept', models.ForeignKey(db_column='deptNo', on_delete=django.db.models.deletion.CASCADE, to='employee.Dept')),
                ('mgr', models.ForeignKey(db_column='mgr', db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Emp')),
            ],
            options={
                'db_table': 'emp',
            },
        ),
        migrations.CreateModel(
            name='SaleGrade',
            fields=[
                ('grade', models.AutoField(primary_key=True, serialize=False)),
                ('lowsal', models.IntegerField()),
                ('higsal', models.IntegerField()),
            ],
            options={
                'db_table': 'salegrade',
            },
        ),
    ]
