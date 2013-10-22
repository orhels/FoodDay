app.CartView = Backbone.View.extend({

    events: {
        'click .cart-remove-btn': 'removeItem'
    },

    initialize: function(){

    },

    render: function(){
        $.get("cart/widget/", function (data) {
            $('#cart-widget-container').html(data);
        })
    },

    remove: function(){
        this.$el.empty();
    },

    addToCart: function (data) {
        var carttext = $('#carttext');
        var productImg = $('.productimg').eq(0);
        if(productImg){
            var imgClone = productImg.clone().offset({
                top: productImg.offset().top,
                left: productImg.offset().left
            }).css({
                'opacity': '0.5',
                    'position': 'absolute',
                    'height': '150px',
                    'width': '100px',
                    'z-index': '100'
            }).appendTo(
                $('body')
            ).animate({
                'top': carttext.offset().top + 10,
                'left': carttext.offset().left + 210,
                'width': 1,
                'height': 1
            }, 1000, 'easeOutCubic');

            var that = this;
            $.post("cart/add/", JSON.stringify(data), function(){
                setTimeout(function(){
                    that.render();
                }, 500); // this number should be tweaked when in prod.
            });

            imgClone.animate({
                'width': 0,
                'height': 0
            }, function() {
                $(this).detach()
            });
        }
    },

    editQuantity: function(){

    },

    removeItem: function(event) {
        var product_id = $(event.currentTarget).data('id');
        var data = {'product_id': product_id, 'quantity': 0};
        var that = this;
        $.post('cart/update/', data, function(){
            setTimeout(function(){
                that.render();
            }, 100)
        });
    }

});



