# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.delivery_time'
        db.add_column(u'Order_order', 'delivery_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 3, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.delivery_time'
        db.delete_column(u'Order_order', 'delivery_time')


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
            'delivery_time': ('django.db.models.fields.DateTimeField', [], {}),
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