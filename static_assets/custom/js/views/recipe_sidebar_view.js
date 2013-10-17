app.RecipeSidebarView = Backbone.View.extend({

    initialize: function(options){

    },

    render: function(){
        var that = this;
        $.get("/recipe-category-sidebar/", function(data){
            that.$el.html(data);
            //that.makeSidebarClickable();
        });
        return this;
    },

    remove:function(){
        var menuHeader = $('div#sidebar').find('div.panel-heading');
        $.each(menuHeader, function(index, element){
            $(element).off('click');
        })
        this.$el.empty();
    },

    makeSidebarClickable: function(){
        var menuHeader = $('div#sidebar').find('div.panel-heading');
        $.each(menuHeader, function(index, element){
            $(element).on('click', function(){
                $(element).find('a.sidebar-toggle')[0].click();
            });
        });
    }
});