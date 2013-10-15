var app = {
    collections: {},
    models: {},
    views: {},

    initialize: function(){
        app.router = new app.Router();
        Backbone.history.start();
    }
}

$(document).ready(function(){
    app.initialize();
})


var csrftoken = $.cookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
