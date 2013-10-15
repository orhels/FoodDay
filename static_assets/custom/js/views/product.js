/**
 * Created by orjan on 15/10/13.
 */
app.ProductView = Backbone.View.extend({

    events: {
        'click $buy-product-button': 'addToCart'
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

    addToCart: function(){
        app.cartView.addToCart();
    }
});