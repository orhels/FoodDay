var Sidebar = {

    init:   function(){
        this.makeSidebarClickable();
    },

    makeSidebarClickable: function(){
        var menuHeader = $('div#sidebar').find('div.panel-heading');
        $.each(menuHeader, this.addMenuHeaderListener);
        var menuSubcat = $('div#sidebar').find('div.sidebar-subcat');
        $.each(menuSubcat, this.addMenuSubcatListener);
    },

    addMenuHeaderListener: function(index, element){
        //console.log(element);
        $(element).on('click', function(){
            //console.log($(element).find('a.sidebar-toggle')[0])
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

};