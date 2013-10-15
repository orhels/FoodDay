/**
 * Created by orjan on 15/10/13.
 */

app.ProductCategoryDetailView = Backbone.View.extend({

    events:{
        "click a.product-link": "loadProduct"
    },

    initialize: function(options){
        console.log(options);
        this.pcid = options.pcid;
        return this;
    },

    render: function(){
        var that = this;
        $.get("/product-category/" + that.pcid, function(data){
            that.$el.html(data);
        });
        return this;
    },

    remove: function(){
        $('body').trigger('destroy_view');
        this.$el.empty();
    },

    loadProduct: function(event){
        console.log(event);
        this.undelegateEvents();
        this.remove();

    }


});