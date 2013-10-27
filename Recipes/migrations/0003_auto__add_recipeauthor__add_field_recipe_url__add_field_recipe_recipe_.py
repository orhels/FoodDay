# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RecipeAuthor'
        db.create_table(u'Recipes_recipeauthor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('attribution_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'Recipes', ['RecipeAuthor'])

        # Adding field 'Recipe.url'
        db.add_column(u'Recipes_recipe', 'url',
                      self.gf('django.db.models.fields.URLField')(default='matprat.no', max_length=400),
                      keep_default=False)

        # Adding field 'Recipe.recipe_author'
        db.add_column(u'Recipes_recipe', 'recipe_author',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='recipes', null=True, to=orm['Recipes.RecipeAuthor']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'RecipeAuthor'
        db.delete_table(u'Recipes_recipeauthor')

        # Deleting field 'Recipe.url'
        db.delete_column(u'Recipes_recipe', 'url')

        # Deleting field 'Recipe.recipe_author'
        db.delete_column(u'Recipes_recipe', 'recipe_author_id')


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
            'is_added_by_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'recipe_author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'recipes'", 'null': 'True', 'to': u"orm['Recipes.RecipeAuthor']"}),
            'recipe_categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recipes'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['Recipes.RecipeCategory']"}),
            'servings': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400'})
        },
        u'Recipes.recipeauthor': {
            'Meta': {'object_name': 'RecipeAuthor'},
            'attribution_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'Recipes.recipecategory': {
            'Meta': {'object_name': 'RecipeCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['Recipes.RecipeCategory']"})
        }
    }

    complete_apps = ['Recipes']