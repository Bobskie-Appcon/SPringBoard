# Generated by Django 4.2.4 on 2023-12-07 08:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(default=None, max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(default='0000-00-00 00:00:00')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=6)),
                ('class_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(default='0000-00-00 00:00:00')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(default='0000-00-00 00:00:00')),
                ('classroom_fk', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='springboard_api.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(default='')),
                ('isActive', models.BooleanField(default=False)),
                ('score', models.FloatField(default=0)),
                ('reason', models.TextField(default='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('group_fk', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='springboard_api.group')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(default=None, max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(default='0000-00-00 00:00:00')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('rules', models.TextField()),
                ('description', models.TextField()),
                ('isActive', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardId', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=50)),
                ('templateId', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('novelty', models.IntegerField()),
                ('capability', models.IntegerField()),
                ('technical_feasibility', models.IntegerField()),
                ('feedback', models.TextField(default='')),
                ('recommendation', models.TextField(default='')),
                ('references', models.TextField(default='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('project_fk', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='springboard_api.project')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='springboard_api.teacher'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(default=None, max_length=254, unique=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(default='0000-00-00 00:00:00')),
                ('group_fk', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='springboard_api.group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]