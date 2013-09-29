var cartApp = function () {
    $.get(cartWidgetUrl, function(data){
        $('#cart-widget-container').html(data)
    })
}
cartApp();
