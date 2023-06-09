# Generated by Django 3.2.15 on 2023-01-02 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=20)),
                ('doctorplace', models.CharField(max_length=20)),
                ('doctorpost', models.CharField(max_length=20)),
                ('doctorpin', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('pho_no', models.BigIntegerField()),
                ('qualification', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('usertype', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=20)),
                ('weight', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('userid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.login')),
            ],
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tocken_count', models.IntegerField()),
                ('schedulingtime', models.TimeField()),
                ('schedulingdate', models.DateField()),
                ('doctorid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=30)),
                ('doctorid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.doctor')),
                ('userid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.login')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctorid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.login'),
        ),
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaints', models.CharField(max_length=20)),
                ('complaint_date', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=20)),
                ('reply_date', models.CharField(max_length=20)),
                ('userid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.user')),
            ],
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=20)),
                ('doctor_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.doctor')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.user')),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('tocken_no', models.IntegerField()),
                ('schedule_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.schedule')),
                ('userid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='diabetes_moule.user')),
            ],
        ),
    ]
