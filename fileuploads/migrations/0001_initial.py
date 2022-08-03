# Generated by Django 2.1.4 on 2019-02-13 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=120)),
                ('file_path', models.CharField(max_length=250)),
                ('original_name', models.CharField(max_length=120)),
                ('file_length', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('fileupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fileuploads.FileUpload')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('fileuploads.fileupload',),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('fileupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fileuploads.FileUpload')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('fileuploads.fileupload',),
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('fileupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fileuploads.FileUpload')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('fileuploads.fileupload',),
        ),
        migrations.CreateModel(
            name='TagImage',
            fields=[
                ('fileupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fileuploads.FileUpload')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tags.Tag')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('fileuploads.fileupload',),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_fileuploads.fileupload_set+', to='contenttypes.ContentType'),
        ),
    ]
