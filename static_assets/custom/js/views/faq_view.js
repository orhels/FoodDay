/**
 * Created by orjan on 28/10/13.
 */
app.FaqView = Backbone.View.extend({

    initialize: function(options){

    },

    render: function(){
        var that = this;
        $.get("/faq/", function(data){
            that.$el.html(data);
        });
        return this;
    },

    remove: function(){
        this.$el.empty();
    }
});