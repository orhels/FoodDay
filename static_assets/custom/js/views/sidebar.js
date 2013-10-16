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
    },

    addMenuHeaderListener: function(index, element){
        $(element).on('click', function(){
            $(element).find('a.sidebar-toggle')[0].click();
        });
    }
});