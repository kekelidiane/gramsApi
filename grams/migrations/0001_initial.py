# Generated by Django 5.0.2 on 2024-06-25 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('codeDep', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=25)),
                ('contact', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('disponibilite', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], default='oui', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Parcours',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('codePar', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('codeSalle', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=50)),
                ('capacite', models.IntegerField()),
                ('localisation', models.CharField(max_length=100)),
                ('disponibilite', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], default='oui')),
                ('etat', models.CharField(choices=[('lib', 'Libre'), ('occ', 'Occupée'), ('res', 'Reservée')], default='lib')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('codeSem', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('codeUe', models.CharField(max_length=10)),
                ('intitule', models.CharField(max_length=50)),
                ('prerequis', models.CharField(blank=True, max_length=150)),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grams.enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('codeFiliere', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=100)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departement', to='grams.departement')),
                ('parcours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcours', to='grams.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('codeExam', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('debut', models.DateTimeField(auto_now=True, verbose_name='')),
                ('fin', models.DateTimeField(auto_now=True, verbose_name='')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grams.cours')),
                ('filiere', models.ManyToManyField(to='grams.filiere')),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='option',
            field=models.ManyToManyField(to='grams.filiere'),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=25)),
                ('date', models.DateField()),
                ('duree', models.IntegerField()),
                ('debut', models.DateTimeField(auto_now=True, verbose_name='')),
                ('fin', models.DateTimeField(auto_now=True, verbose_name='')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grams.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('numCarte', models.IntegerField()),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=25)),
                ('date_naissance', models.DateField()),
                ('contact', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grams.semestre')),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='semestre_etude',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semestre_etude', to='grams.semestre'),
        ),
        migrations.AddField(
            model_name='cours',
            name='semestre_evolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semestre_evolution', to='grams.semestre'),
        ),
    ]
