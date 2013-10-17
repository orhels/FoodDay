/**
 * Created by orjan on 18/10/13.
 */
app.FrontpageView = Backbone.View.extend({

    initialize: function(options){

    },

    render: function(){
        var that = this;
        $.get("/frontpage/" + that.pid, function(data){
            that.$el.html(data);
        });
        return this;
    },

    remove: function(){
        this.$el.empty();
    }
});