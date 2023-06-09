# Generated by Django 4.1.7 on 2023-03-19 11:31

from django.db import migrations, models
import django.db.models.deletion
import software_design.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_id', models.CharField(max_length=15)),
                ('student_point', models.IntegerField(null=True)),
                ('student_passport', models.CharField(max_length=10)),
                ('student_participation_status', models.CharField(max_length=50)),
                ('student_mac_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trash_type', models.CharField(max_length=50)),
                ('trash_point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_Trash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software_design.student')),
                ('trash_id', models.ForeignKey(on_delete=software_design.models.Trash, to='software_design.trash')),
            ],
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_point', models.IntegerField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software_design.student')),
            ],
        ),
        migrations.CreateModel(
            name='Reward_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_amount', models.IntegerField()),
                ('date_earned', models.DateField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software_design.student')),
            ],
        ),
        migrations.CreateModel(
            name='Reciever',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_point', models.IntegerField()),
                ('sender_if', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software_design.sender')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software_design.student')),
            ],
        ),
        migrations.CreateModel(
            name='Case_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=50)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software_design.staff')),
                ('student_trash_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software_design.student_trash')),
            ],
        ),
    ]
