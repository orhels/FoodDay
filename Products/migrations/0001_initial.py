# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

import datetime


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'Products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='product_images/product_images_placeholder.png', max_length=100, blank=True)),
            ('quantityType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['IngredientProductMapping.QuantityType'])),
            ('producer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Products.Producer'])),
            ('ingredientMapping', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='products', null=True, to=orm['IngredientProductMapping.IngredientProductMapping'])),
        ))
        db.send_create_signal(u'Products', ['Product'])

        # Adding M2M table for field productCategories on 'Product'
        m2m_table_name = db.shorten_name(u'Products_product_productCategories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'Products.product'], null=False)),
            ('productcategory', models.ForeignKey(orm[u'Products.productcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'productcategory_id'])

        # Adding model 'Producer'
        db.create_table(u'Products_producer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'Products', ['Producer'])

        # Adding model 'ProductCategory'
        db.create_table(u'Products_productcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'Products', ['ProductCategory'])

        # Adding M2M table for field parents on 'ProductCategory'
        m2m_table_name = db.shorten_name(u'Products_productcategory_parents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_productcategory', models.ForeignKey(orm[u'Products.productcategory'], null=False)),
            ('to_productcategory', models.ForeignKey(orm[u'Products.productcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_productcategory_id', 'to_productcategory_id'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'Products_product')

        # Removing M2M table for field productCategories on 'Product'
        db.delete_table(db.shorten_name(u'Products_product_productCategories'))

        # Deleting model 'Producer'
        db.delete_table(u'Products_producer')

        # Deleting model 'ProductCategory'
        db.delete_table(u'Products_productcategory')

        # Removing M2M table for field parents on 'ProductCategory'
        db.delete_table(db.shorten_name(u'Products_productcategory_parents'))


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
            'quantityType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['IngredientProductMapping.QuantityType']"})
        },
        u'Products.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['Products.ProductCategory']"})
        }
    }

    complete_apps = ['Products']