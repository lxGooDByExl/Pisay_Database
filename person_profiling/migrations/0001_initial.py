# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('student_number', models.IntegerField()),
                ('section', models.CharField(choices=[('1', '7-Diamond'), ('2', '7-Gold'), ('3', '7-Pearl'), ('4', '8-Dahlia'), ('5', '8-Kamia'), ('6', '8-Rosal'), ('7', '9-Calcium'), ('8', '9-Lithium'), ('9', '9-Sodium'), ('10', '10-Electron'), ('11', '10-Neutron'), ('12', '10-Proton'), ('13', '11-Curie'), ('14', '11-Darwin'), ('15', '11-Einstein'), ('16', '11-Franklin'), ('17', '11-Newton'), ('18', '12-Farad'), ('19', '12-Hertz'), ('20', '12-Kelvin'), ('21', '12-Pascal'), ('22', '12-Tesla')], default=None, max_length=13)),
                ('balance', models.IntegerField(blank=0)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_profiling.Student')),
            ],
            options={
                'verbose_name_plural': 'Student Attendance',
            },
        ),
        migrations.CreateModel(
            name='StudentInfractions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('infractions', models.CharField(choices=[('A', 'Absent'), ('L', 'Late'), ('CC', 'Cutting Class')], max_length=13)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_profiling.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('teacher_number', models.IntegerField()),
                ('advisory', models.CharField(choices=[('1', '7-Diamond'), ('2', '7-Gold'), ('3', '7-Pearl'), ('4', '8-Dahlia'), ('5', '8-Kamia'), ('6', '8-Rosal'), ('7', '9-Calcium'), ('8', '9-Lithium'), ('9', '9-Sodium'), ('10', '10-Electron'), ('11', '10-Neutron'), ('12', '10-Proton'), ('13', '11-Curie'), ('14', '11-Darwin'), ('15', '11-Einstein'), ('16', '11-Franklin'), ('17', '11-Newton'), ('18', '12-Farad'), ('19', '12-Hertz'), ('20', '12-Kelvin'), ('21', '12-Pascal'), ('22', '12-Tesla')], max_length=13, null='')),
                ('balance', models.IntegerField(blank=0)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(blank=True, null=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_profiling.Teacher')),
            ],
            options={
                'verbose_name_plural': 'Teacher Attendance',
            },
        ),
        migrations.CreateModel(
            name='TeacherInfractions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('infractions', models.CharField(choices=[('A', 'Absent'), ('L', 'Late'), ('CC', 'Cutting Class')], max_length=13)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_profiling.Teacher')),
            ],
        ),
    ]
