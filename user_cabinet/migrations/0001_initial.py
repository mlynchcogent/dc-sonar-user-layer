# Generated by Django 4.0.5 on 2022-06-22 15:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fqdn', models.CharField(max_length=255, unique=True)),
                ('ntlm_status', models.PositiveSmallIntegerField(choices=[('WAIT_SOFT_ADDING', 'Wait Soft Adding'), ('INIT', 'Init'), ('WAIT_PERFORMING', 'Wait Performing'), ('PERFORMING', 'Performing'), ('BRUTED', 'Bruted'), ('ERROR', 'Error')], default='WAIT_SOFT_ADDING')),
                ('ntlm_progress', models.PositiveSmallIntegerField(default=0)),
                ('ntlm_status_update', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('ntlm_error_desc', models.TextField(null=True)),
                ('no_exp_pass_status', models.PositiveSmallIntegerField(choices=[('WAIT_SOFT_ADDING', 'Wait Soft Adding'), ('INIT', 'Init'), ('WAIT_PERFORMING', 'Wait Performing'), ('PERFORMING', 'Performing'), ('BRUTED', 'Bruted'), ('ERROR', 'Error')], default='WAIT_SOFT_ADDING')),
                ('no_exp_pass_status_update', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('no_exp_pass_err_desc', models.TextField(null=True)),
                ('reused_pass_status', models.PositiveSmallIntegerField(choices=[('WAIT_SOFT_ADDING', 'Wait Soft Adding'), ('INIT', 'Init'), ('WAIT_PERFORMING', 'Wait Performing'), ('PERFORMING', 'Performing'), ('BRUTED', 'Bruted'), ('ERROR', 'Error')], default='WAIT_SOFT_ADDING')),
                ('reused_pass_status_update', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('reused_pass_err_desc', models.TextField(null=True)),
                ('acc_login', models.CharField(max_length=15, null=True)),
                ('acc_password', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReusedPassAccs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sam_acc_name', models.CharField(max_length=15)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_cabinet.domain')),
            ],
        ),
        migrations.CreateModel(
            name='NoExpPassAccs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sam_acc_name', models.CharField(max_length=15)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_cabinet.domain')),
            ],
        ),
        migrations.CreateModel(
            name='BrutedNTLMAccs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sam_acc_name', models.CharField(max_length=15)),
                ('acc_password', models.CharField(max_length=128)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_cabinet.domain')),
            ],
        ),
    ]