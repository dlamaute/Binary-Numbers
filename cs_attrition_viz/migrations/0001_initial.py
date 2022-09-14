# Generated by Django 4.1.1 on 2022-09-13 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsWomen',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
                ('num_employees_bls', models.IntegerField(blank=True, null=True)),
                ('num_employees_nsf', models.IntegerField(blank=True, null=True)),
                ('salary_bls', models.IntegerField(blank=True, null=True)),
                ('salary_nsf', models.IntegerField(blank=True, null=True)),
                ('num_recent_grad_employees', models.IntegerField(blank=True, null=True)),
                ('num_recent_grad_nonstem', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cs_women',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecentGradYears',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
                ('grad_years', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'recent_grad_years',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
                ('num_employees_bls_source', models.CharField(blank=True, max_length=255, null=True)),
                ('num_employees_nsf_source', models.CharField(blank=True, max_length=255, null=True)),
                ('salary_bls_source', models.CharField(blank=True, max_length=255, null=True)),
                ('salary_nsf_source', models.CharField(blank=True, max_length=255, null=True)),
                ('num_recent_grad_employees_source', models.CharField(blank=True, max_length=255, null=True)),
                ('num_recent_grad_nonstem_source', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sources',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CsMen',
            fields=[
                ('year', models.OneToOneField(db_column='year', on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='cs_attrition_viz.cswomen')),
                ('num_employees_bls', models.IntegerField(blank=True, null=True)),
                ('num_employees_nsf', models.IntegerField(blank=True, null=True)),
                ('salary_bls', models.IntegerField(blank=True, null=True)),
                ('salary_nsf', models.IntegerField(blank=True, null=True)),
                ('num_recent_grad_employees', models.IntegerField(blank=True, null=True)),
                ('num_recent_grad_nonstem', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cs_men',
                'managed': False,
            },
        ),
    ]