# Generated by Django 2.2.2 on 2019-12-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myparliament', '0008_auto_20191202_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_step3_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='que4',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='application',
            name='que5',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='application',
            name='que6',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='application',
            name='que7',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
