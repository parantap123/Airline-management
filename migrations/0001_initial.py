# Generated by Django 2.0.2 on 2018-03-18 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airhostess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_flight_id', models.CharField(max_length=20)),
                ('next_date_and_time', models.DateTimeField()),
                ('flight_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('flight_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('flight_type', models.CharField(max_length=50)),
                ('no_of_seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('street_details', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_mobile_no',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Desk_Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_name', models.CharField(max_length=100)),
                ('desk_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('street_details', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_mobile_no',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=10)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_flight_id', models.CharField(max_length=20)),
                ('next_date_and_time', models.DateTimeField()),
                ('flight_id', models.CharField(max_length=20)),
                ('emp_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='airline.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Seat_Allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.IntegerField()),
                ('baggage_weight', models.IntegerField()),
                ('food_preference', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticket_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('flight_id', models.CharField(max_length=20)),
                ('date_and_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField()),
                ('fromLocation', models.CharField(max_length=200)),
                ('toLocation', models.CharField(max_length=200)),
                ('sche_dept', models.DateTimeField()),
                ('sche_arrival', models.DateTimeField()),
                ('actual_dept', models.DateTimeField()),
                ('actual_arrival', models.DateTimeField()),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Airplane')),
            ],
        ),
        migrations.AddField(
            model_name='tickets',
            name='flight_date_time_combo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Traffic'),
        ),
        migrations.AddField(
            model_name='tickets',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Customer'),
        ),
        migrations.AddField(
            model_name='seat_allocation',
            name='ticket_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='airline.Tickets'),
        ),
        migrations.AddField(
            model_name='pilot',
            name='flight_date_time_combo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Traffic'),
        ),
        migrations.AddField(
            model_name='desk_workers',
            name='emp_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='airline.Employee'),
        ),
        migrations.AddField(
            model_name='airhostess',
            name='emp_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='airline.Employee'),
        ),
        migrations.AddField(
            model_name='airhostess',
            name='flight_date_time_combo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Traffic'),
        ),
        migrations.AlterUniqueTogether(
            name='traffic',
            unique_together={('flight_id', 'date_and_time')},
        ),
        migrations.AlterUniqueTogether(
            name='employee_mobile_no',
            unique_together={('mobile_no', 'emp_id')},
        ),
        migrations.AlterUniqueTogether(
            name='customer_mobile_no',
            unique_together={('mobile_no', 'username')},
        ),
    ]
