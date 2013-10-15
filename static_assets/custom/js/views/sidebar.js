app.SidebarView = Backbone.View.extend({

    initialize: function(options){

    },


    render: function(){
        var that = this;
        $.get("/product-category-sidebar/", function(data){
            that.$el.html(data);
            that.makeSidebarClickable();
        });
        return this;
    },

    makeSidebarClickable: function(){
        var menuHeader = $('div#sidebar').find('div.panel-heading');
        $.each(menuHeader, this.addMenuHeaderListener);
        var menuSubcat = $('div#sidebar').find('div.sidebar-subcat');
        $.each(menuSubcat, this.addMenuSubcatListener);
    },

    addMenuHeaderListener: function(index, element){
        $(element).on('click', function(){
            $(element).find('a.sidebar-toggle')[0].click();
        });
    },

    addMenuSubcatListener: function(index, element){
        $(element).on("click", function() {
            $.get("/product-category/"+ $(element).data('product_cat_id'), function(data){
                $('#main-content').html(data);
            });
        });
    }
});