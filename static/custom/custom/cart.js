var cartApp = function () {


    var updateCartWidget = function () {
        $.get(cartWidgetUrl, function (data) {
            $('#cart-widget-container').html(data);
        })
    }

    var addToCart = function (event) {
        event.preventDefault();
        data = {'product_id': $('input[name=id]').val(),
            'quantity': 1 };
        $.post(cartAddUrl, data, updateCartWidget);
    }


    // Add event listener to "kjøp"-knapp (if it exists)
    $('#buy-product-btn').on('click', addToCart);

    // Load cart widget
    updateCartWidget();

}
cartApp();
