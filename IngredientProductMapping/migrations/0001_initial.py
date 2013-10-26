# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration

import datetime


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IngredientProductMapping'
        db.create_table(u'IngredientProductMapping_ingredientproductmapping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'IngredientProductMapping', ['IngredientProductMapping'])

        # Adding model 'QuantityType'
        db.create_table(u'IngredientProductMapping_quantitytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'IngredientProductMapping', ['QuantityType'])


    def backwards(self, orm):
        # Deleting model 'IngredientProductMapping'
        db.delete_table(u'IngredientProductMapping_ingredientproductmapping')

        # Deleting model 'QuantityType'
        db.delete_table(u'IngredientProductMapping_quantitytype')


    models = {
        u'IngredientProductMapping.ingredientproductmapping': {
            'Meta': {'object_name': 'IngredientProductMapping'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'IngredientProductMapping.quantitytype': {
            'Meta': {'object_name': 'QuantityType'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['IngredientProductMapping']