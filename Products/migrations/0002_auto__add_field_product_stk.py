# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.stk'
        db.add_column(u'Products_product', 'stk',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.stk'
        db.delete_column(u'Products_product', 'stk')


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
        u'Products.producer': {
            'Meta': {'object_name': 'Producer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'Products.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'product_images/product_images_placeholder.png'", 'max_length': '100', 'blank': 'True'}),
            'ingredientMapping': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'products'", 'null': 'True', 'to': u"orm['IngredientProductMapping.IngredientProductMapping']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Products.Producer']"}),
            'productCategories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'products'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['Products.ProductCategory']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'quantityType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IngredientProductMapping.QuantityType']"}),
            'stk': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'Products.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['Products.ProductCategory']"})
        }
    }

    complete_apps = ['Products']