# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

import datetime


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table(u'Recipes_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('procedure', self.gf('django.db.models.fields.TextField')()),
            ('servings', self.gf('django.db.models.fields.IntegerField')()),
            ('processing_time', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='recipe_images/recipe_images_placeholder.png', max_length=100, blank=True)),
        ))
        db.send_create_signal(u'Recipes', ['Recipe'])

        # Adding M2M table for field recipe_categories on 'Recipe'
        m2m_table_name = db.shorten_name(u'Recipes_recipe_recipe_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'Recipes.recipe'], null=False)),
            ('recipecategory', models.ForeignKey(orm[u'Recipes.recipecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'recipecategory_id'])

        # Adding model 'Ingredient'
        db.create_table(u'Recipes_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('is_main_ingredient', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ingredients', to=orm['Recipes.Recipe'])),
            ('quantityType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['IngredientProductMapping.QuantityType'])),
            ('productMapping', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ingredients', null=True, to=orm['IngredientProductMapping.IngredientProductMapping'])),
        ))
        db.send_create_signal(u'Recipes', ['Ingredient'])

        # Adding model 'RecipeCategory'
        db.create_table(u'Recipes_recipecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'Recipes', ['RecipeCategory'])

        # Adding M2M table for field parents on 'RecipeCategory'
        m2m_table_name = db.shorten_name(u'Recipes_recipecategory_parents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_recipecategory', models.ForeignKey(orm[u'Recipes.recipecategory'], null=False)),
            ('to_recipecategory', models.ForeignKey(orm[u'Recipes.recipecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_recipecategory_id', 'to_recipecategory_id'])


    def backwards(self, orm):
        # Deleting model 'Recipe'
        db.delete_table(u'Recipes_recipe')

        # Removing M2M table for field recipe_categories on 'Recipe'
        db.delete_table(db.shorten_name(u'Recipes_recipe_recipe_categories'))

        # Deleting model 'Ingredient'
        db.delete_table(u'Recipes_ingredient')

        # Deleting model 'RecipeCategory'
        db.delete_table(u'Recipes_recipecategory')

        # Removing M2M table for field parents on 'RecipeCategory'
        db.delete_table(db.shorten_name(u'Recipes_recipecategory_parents'))


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
        },
        u'Recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_main_ingredient': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'productMapping': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ingredients'", 'null': 'True', 'to': u"orm['IngredientProductMapping.IngredientProductMapping']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'quantityType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IngredientProductMapping.QuantityType']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ingredients'", 'to': u"orm['Recipes.Recipe']"})
        },
        u'Recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'recipe_images/recipe_images_placeholder.png'", 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'procedure': ('django.db.models.fields.TextField', [], {}),
            'processing_time': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recipe_categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recipes'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['Recipes.RecipeCategory']"}),
            'servings': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Recipes.recipecategory': {
            'Meta': {'object_name': 'RecipeCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['Recipes.RecipeCategory']"})
        }
    }

    complete_apps = ['Recipes']