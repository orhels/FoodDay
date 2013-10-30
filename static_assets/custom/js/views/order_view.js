
app.OrderView = Backbone.View.extend({

    initialize: function(options){

    },

    render: function(){
        var that = this;
        $.get("/order/", function(data){
            that.$el.html(data);
        });
        return this;
    },

    remove: function(){
        this.undelegateEvents();
        this.$el.empty();
    }
});