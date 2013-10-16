/**
 * Created by orjan on 15/10/13.
 */

app.ProductCategoryDetailView = Backbone.View.extend({

    events:{
        "click a.product-link": "loadProduct"
    },

    initialize: function(options){
        this.pcid = options.pcid;
        this.router = options.router;
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
        this.undelegateEvents();
        this.$el.empty();
    },

    loadProduct: function(event){
        pid = event.currentTarget.dataset.product_id;
        this.router.navigate('//product/'+pid);
    }


});