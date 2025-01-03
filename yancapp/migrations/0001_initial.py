# Generated by Django 5.1.1 on 2024-12-05 11:30

import django.db.models.deletion
import django.utils.timezone
import yancapp.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlertType',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.alerttype')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationCategory',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CohortRole',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CohortMemberRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.cohortrole')),
            ],
        ),
        migrations.CreateModel(
            name='CohortRoleAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('assignment', models.ManyToManyField(to='yancapp.cohortmemberrole')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.cohort')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CohortScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.cohort')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CohortScoreCard',
            fields=[
                ('activity', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('rename_continent', 'Can rename the continent'), ('update_code_continent', 'Can update code for a continent')],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.continent')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CountryCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.country')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.eventtype')),
            ],
        ),
        migrations.CreateModel(
            name='ContinentCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('continent', models.ForeignKey(on_delete=yancapp.models.Continent, to='yancapp.continent')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.eventtype')),
            ],
        ),
        migrations.CreateModel(
            name='CohortCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.cohort')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.eventtype')),
            ],
        ),
        migrations.CreateModel(
            name='CityCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.city')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.eventtype')),
            ],
        ),
        migrations.CreateModel(
            name='InvitationCategory',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipApplication',
            fields=[
                ('applied_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='yancapp.invitee')),
                ('info', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.applicationcategory')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='invitee',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.invitationcategory'),
        ),
        migrations.AddField(
            model_name='invitee',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('hobbies', models.CharField(blank=True, max_length=255, null=True)),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.cohort')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('referred_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referred_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='invitee',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.member'),
        ),
        migrations.AddField(
            model_name='cohortmemberrole',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.member'),
        ),
        migrations.CreateModel(
            name='CohortInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.cohort')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.cohortcalendar')),
                ('Invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.invitee')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='yancapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberScoreCard',
            fields=[
                ('activity', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberStatus',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberStatusTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.member')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.memberstatus')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.city')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cohort',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.region'),
        ),
        migrations.CreateModel(
            name='RegionCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.eventtype')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.region')),
            ],
        ),
        migrations.CreateModel(
            name='RegionInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.regioncalendar')),
                ('invitee', models.ManyToManyField(to='yancapp.invitee')),
                ('referred_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.member')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.region')),
            ],
        ),
        migrations.CreateModel(
            name='RegionRole',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegionRoleAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.member')),
                ('role', models.ManyToManyField(to='yancapp.regionrole')),
            ],
        ),
        migrations.CreateModel(
            name='RegionScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.region')),
            ],
        ),
        migrations.CreateModel(
            name='RegionScoreCard',
            fields=[
                ('activity', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.member')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.reward')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoleAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('access', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.access')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.role')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('duration', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='eventtype',
            name='session',
            field=models.ManyToManyField(to='yancapp.session'),
        ),
        migrations.CreateModel(
            name='SessionAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('invitee', models.ManyToManyField(to='yancapp.invitee')),
                ('member', models.ManyToManyField(to='yancapp.member')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.session')),
            ],
        ),
        migrations.CreateModel(
            name='RegionAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.region')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.regioncalendar')),
                ('attendance', models.ManyToManyField(to='yancapp.sessionattendance')),
            ],
        ),
        migrations.CreateModel(
            name='CohortAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.cohort')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.cohortcalendar')),
                ('attendance', models.ManyToManyField(to='yancapp.sessionattendance')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.country')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.state'),
        ),
        migrations.CreateModel(
            name='StateCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.eventtype')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.state')),
            ],
        ),
        migrations.CreateModel(
            name='SupportCategory',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.supportcategory')),
            ],
        ),
        migrations.CreateModel(
            name='SupportTicketStatus',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupportStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.support')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.supportticketstatus')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.JSONField()),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.transactiontype')),
            ],
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('name', models.CharField(max_length=15)),
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('fee', models.FloatField()),
                ('discount', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('discount', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.invitee')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.paymentmode')),
                ('payfor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.tribe')),
            ],
        ),
        migrations.CreateModel(
            name='MemberTribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.member')),
                ('tribe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yancapp.tribe')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipApplicationStatus',
            fields=[
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='yancapp.membershipapplication')),
                ('status', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
