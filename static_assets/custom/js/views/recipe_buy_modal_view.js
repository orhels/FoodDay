/**
 * Created by orjan on 22/10/13.
 */
app.RecipeBuyModalView = Backbone.View.extend({

    events: {
        'click #buy-recipe-modal-btn': 'addToCart'
    },

    initialize: function(options){
        this.rid = options.rid;
    },

    render: function(){

    },

    remove: function(){
        this.undelegateEvents();
        this.$el.empty();
    },

    addToCart: function(){
        console.log("Modal adding to cart");
        data = [];
        _.each($('tr.product'), function(tr){
            if ($(tr).find('input').first().is(':checked')){
                var obj={};
                obj['product_id'] = $(tr).data('product_id')
                obj['quantity'] = $(tr).data('quantity');
                data.push(obj);
            }
        });
        app.cartView.addToCart(data);
    }
});