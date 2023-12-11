# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PokedexappPokedex(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    num = models.CharField(db_column='Num', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='Img', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=100, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'pokedex'
        db_table = 'PokedexApp_pokedex'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        app_label = 'pokedex'
        db_table = 'django_migrations'
