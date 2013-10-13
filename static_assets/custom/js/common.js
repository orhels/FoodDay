var app = app || {};

app.Router = Backbone.Router.extend({
   routes:{
       "product-category/:pcid" : "product_category",
       "product/:pid" : "product"
   },

   product_category:function(pcid){
       $.get("/product-category/"+ pcid, function(data){
           $('#main-content').html(data);
       });
   },


   product:function(pid){
       $.get("/product/"+pid, function(data){
           $("#main-content").html(data);
       });
   }
});


app.router = new app.Router();
Backbone.history.start();


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


if(Sidebar !== undefined){
    Sidebar.init();
}