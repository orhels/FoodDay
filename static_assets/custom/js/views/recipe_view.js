/**
 * Created by orjan on 17/10/13.
 */
app.RecipeView = Backbone.View.extend({

    events: {
        'click #buy-recipe-btn': 'addToCart'
    },

    initialize: function(options){
        this.rid = options.rid;
    },

    render: function(){
        var that = this;
        $.get("/recipe/" + that.rid, function(data){
            that.$el.html(data);
        });
        return this;
    },

    remove: function(){
        this.undelegateEvents();
        this.$el.empty();
    },

    addToCart: function(){
        app.cartView.addToCart();
    }
});