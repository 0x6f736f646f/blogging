# Generated by Django 2.0 on 2018-05-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourblog', '0003_auto_20180528_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.TextField(choices=[('Travelling', 'Travelling'), ('Work', 'Work'), ('Lifestyle', 'Lifestyle'), ('Photography', 'Photography'), ('Finance', 'Finance'), ('Programming', 'Programming'), ('Food & Drinks', 'Food & Drinks'), ('Technology', 'Technology'), ('Engineering', 'Engineering'), ('Science', 'Science'), ('Law', 'Law'), ('Health', 'Health'), ('Agriculture', 'Agriculture'), ('Enterprenuership', 'Enterprenuership'), ('Cars', 'Cars')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='place_from',
            field=models.CharField(blank=True, choices=[('Juja', 'Juja'), ('Nairobi', 'Nairobi'), ('Kahawa', 'Kahawa'), ('Madaraka', 'Madaraka'), ('Athi-River', 'Athi-River'), ('Karen', 'Karen')], max_length=1, verbose_name='Place from'),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='university_name',
            field=models.CharField(blank=True, choices=[('JKUAT', 'Jommo Kenyatta University of Agriculture and technology'), ('UON', 'University of Nairobi'), ('KU', 'Kenyatta University'), ('STRATH', 'Strathmore'), ('DAYSTAR', 'Daystat University'), ('CUEA', 'Cooperative University of East Africa')], max_length=1, null=True, verbose_name='University from'),
        ),
    ]