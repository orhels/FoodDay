# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Order'
        db.create_table(u'Order_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('phone_number_extra', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('shipping_address', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shippingaddress', to=orm['Order.Address'])),
            ('email_has_been_sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('shipping_cost', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=2)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(related_name='order', to=orm['Cart.Cart'])),
        ))
        db.send_create_signal(u'Order', ['Order'])

        # Adding model 'Address'
        db.create_table(u'Order_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('postal_place', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'Order', ['Address'])


    def backwards(self, orm):
        # Deleting model 'Order'
        db.delete_table(u'Order_order')

        # Deleting model 'Address'
        db.delete_table(u'Order_address')


    models = {
        u'Cart.cart': {
            'Meta': {'object_name': 'Cart'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'Order.address': {
            'Meta': {'object_name': 'Address'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'postal_place': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'Order.order': {
            'Meta': {'object_name': 'Order'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'order'", 'to': u"orm['Cart.Cart']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'email_has_been_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'phone_number_extra': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'shipping_address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shippingaddress'", 'to': u"orm['Order.Address']"}),
            'shipping_cost': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2'})
        }
    }

    complete_apps = ['Order']