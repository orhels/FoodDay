/**
 * Created by orjan on 28/10/13.
 */
app.AboutView = Backbone.View.extend({

    initialize: function(options){

    },

    render: function(){
        var that = this;
        $.get("/about/", function(data){
            that.$el.html(data);
        });
        return this;
    },

    remove: function(){
        this.$el.empty();
    }
});