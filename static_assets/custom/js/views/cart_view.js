app.CartView = Backbone.View.extend({

    events: {
        'click .cart-remove-btn': 'removeItem',
        'click .cart-edit-btn': 'editQuantity'
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

    editQuantity: function(event){
        var product_id = $(event.currentTarget).data('id');
        var temp = $('#quantity'+product_id)[0];
        var currentQuantity = parseInt($(temp).html());
        console.log(currentQuantity);
        var that = this;
        $('#quantity'+product_id).html("<div class=\"input-group input-group-sm cart-input\"><input id=\"quantity_change"+product_id+"\" type=\"number\" class=\"input-sm form-control\" value=\""+ currentQuantity + "\"></div>");
        $('#quantity_change'+product_id).on('change', function(){
            var newQuantity = $('#quantity_change'+product_id).val();
            var data = {'product_id': product_id, 'quantity': newQuantity};
            $.post('cart/update/', data, function(){
                setTimeout(function(){
                    that.render();
                }, 10);
            });
        });
    },

    removeItem: function(event) {
        var product_id = $(event.currentTarget).data('id');
        var data = {'product_id': product_id, 'quantity': 0};
        var that = this;
        $.post('cart/update/', data, function(){
            setTimeout(function(){
                that.render();
            }, 10)
        });
    }

});



