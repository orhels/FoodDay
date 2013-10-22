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
        app.cartView.addToCart();
    }
});