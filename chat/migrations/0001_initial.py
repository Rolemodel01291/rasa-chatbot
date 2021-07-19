# Generated by Django 2.2.3 on 2019-07-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heat_map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_db', models.CharField(max_length=80)),
                ('LINEAR_REGRESSION', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('LOGISTIC_REGRESSION', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('LSTM_1', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('LSTM_2', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('LDS_190101', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('REL_VAL_1', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('M2', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('SUMMARY_SC_SCORE', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_db', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=80)),
                ('latest_pickle_of_model', models.CharField(max_length=80)),
                ('latest_update_time', models.DateTimeField(auto_now_add=True)),
                ('standardized_conviction_score', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_db', models.CharField(max_length=50)),
                ('report_content', models.CharField(max_length=500)),
                ('latest_pickle_of_the_report', models.CharField(max_length=80)),
                ('report_generated_time', models.DateTimeField(auto_now_add=True)),
                ('phonenumber', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tickers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_db', models.CharField(max_length=80)),
                ('isin', models.CharField(max_length=80)),
                ('exchange', models.CharField(max_length=80)),
                ('bloomberg_id', models.CharField(max_length=80)),
                ('reuters_id', models.CharField(max_length=80)),
            ],
        ),
    ]