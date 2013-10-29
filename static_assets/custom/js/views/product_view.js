/**
 * Created by orjan on 15/10/13.
 */
app.ProductView = Backbone.View.extend({

    events: {
        'click .buy-product-btn': 'addToCart'
    },

    initialize: function(options){
        this.pid = options.pid;
    },

    render: function(){
        var that = this;
        $.get("/product/" + that.pid, function(data){
            that.$el.html(data);
        });
        return this;
    },

    remove: function(){
        this.undelegateEvents();
        this.$el.empty();
    },

    addToCart: function(evt){
        var data = [{'product_id': evt.currentTarget.dataset.product_id,
            'quantity': 1 }];
        app.cartView.addToCart(data);
    }
});