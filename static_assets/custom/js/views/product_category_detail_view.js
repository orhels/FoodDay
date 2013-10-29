/**
 * Created by orjan on 15/10/13.
 */

app.ProductCategoryDetailView = Backbone.View.extend({

    events:{
        'click .buy-product-btn': 'addToCart'
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
            var panel = $('.productpanel');
            //console.log(panel)
            $.each(panel, function(index, element){
                $(element).on('click', function(event){
                    if (event.target.nodeName != 'BUTTON'){
                        that.loadProduct($(element).data('product_id'))

                    };
                });
            });
        });
        return this;
    },

    remove: function(){
        this.undelegateEvents();
        this.$el.empty();
    },

    loadProduct: function(pid){
        this.router.navigate('//product/'+pid);
    },

    addToCart: function(evt){
        var data = [{'product_id': evt.currentTarget.dataset.product_id,
            'quantity': 1 }];
        app.cartView.addToCart(data);
    }

});