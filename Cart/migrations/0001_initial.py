# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration

import datetime


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cart'
        db.create_table(u'Cart_cart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'Cart', ['Cart'])

        # Adding model 'CartItem'
        db.create_table(u'Cart_cartitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['Cart.Cart'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Products.Product'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'Cart', ['CartItem'])


    def backwards(self, orm):
        # Deleting model 'Cart'
        db.delete_table(u'Cart_cart')

        # Deleting model 'CartItem'
        db.delete_table(u'Cart_cartitem')


    models = {
        u'Cart.cart': {
            'Meta': {'object_name': 'Cart'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'Cart.cartitem': {
            'Meta': {'object_name': 'CartItem'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['Cart.Cart']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Products.Product']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
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
            'quantityType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IngredientProductMapping.QuantityType']"})
        },
        u'Products.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['Products.ProductCategory']"})
        }
    }

    complete_apps = ['Cart']