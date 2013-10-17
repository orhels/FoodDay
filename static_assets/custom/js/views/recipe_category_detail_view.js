/**
 * Created by orjan on 15/10/13.
 */

app.RecipeCategoryDetailView = Backbone.View.extend({

    events:{
        "click a.recipe-link": "loadRecipe"
    },

    initialize: function(options){
        this.rcid = options.rcid;
        this.router = options.router;
        return this;
    },

    render: function(){
        var that = this;
        $.get("/recipe-category/" + that.rcid, function(data){
            that.$el.html(data);
        });
        return this;
    },

    remove: function(){
        this.undelegateEvents();
        this.$el.empty();
    },

    loadRecipe: function(event){
        rid = event.currentTarget.dataset.recipe_id;
        this.router.navigate('//recipe/'+rid);
    }


});