var cartApp = function () {

    // Load cart widget
    $.get(cartWidgetUrl, function(data){
        $('#cart-widget-container').html(data)
    })

    var addToCart = function(event){

    }

    // Add event listener to "kjøp"-knapp (if it exists)
    $('#buy-product-btn').on('click', addToCart);

}
cartApp();
