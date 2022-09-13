# Generated by Django 4.0.4 on 2022-06-06 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Modality', '0001_initial'),
        ('Course', '0001_initial'),
        ('UserAuthentication', '0001_initial'),
        ('Session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_requesters', models.IntegerField(default=1)),
                ('state', models.CharField(choices=[('PN', 'Pendiente'), ('AP', 'Aprobada'), ('DD', 'Rechazada'), ('DN', 'Realizada')], default='PN', max_length=2)),
                ('meeting_type', models.CharField(choices=[('ZO', 'Zoom'), ('DI', 'Discord'), ('ME', 'Meetup'), ('MT', 'Microsoft Teams'), ('PL', 'Lugar físico')], default='ZO', max_length=2)),
                ('tutor_comment', models.TextField(null=True)),
                ('student_comment', models.TextField(null=True)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('date_request', models.DateTimeField(auto_now_add=True)),
                ('date_resolution', models.DateTimeField(null=True)),
                ('course_requested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_requested', to='Course.course')),
                ('modality_requested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modality_requested', to='Modality.modality')),
                ('session_requested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_requested', to='Session.session')),
                ('tutor_requested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_requested', to='UserAuthentication.user')),
                ('user_requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_requester', to='UserAuthentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='Requesters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.request')),
                ('user_requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserAuthentication.user')),
            ],
        ),
    ]