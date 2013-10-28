/**
 * Created by orjan on 28/10/13.
 */
app.FooterView = Backbone.View.extend({

    initialize: function(options){

    },

    render: function(){
        var that = this;
        $.get("/footer/", function(data){
            that.$el.html(data);
        });
        return this;
    },

    remove: function(){
        this.$el.empty();
    }
});