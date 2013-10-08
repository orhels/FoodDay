var cartApp = function () {


    var updateCartWidget = function () {
        $.get(cartWidgetUrl, function (data) {
            $('#cart-widget-container').html(data);
        })
    }

    var addToCart = function (event) {
        data = {'product_id': $('input[name=id]').val(),
            'quantity': 1 };
        $.post(cartAddUrl, data);
        event.preventDefault();
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

            setTimeout(function(){
                updateCartWidget();
            }, 1100);

            imgClone.animate({
                'width': 0,
                'height': 0
            }, function() {
                $(this).detach()
            });
        }
    }


    // Add event listener to "kjøp"-knapp (if it exists)
    $('#buy-product-btn').on('click', addToCart);

    // Load cart widget
    updateCartWidget();

}
cartApp();
