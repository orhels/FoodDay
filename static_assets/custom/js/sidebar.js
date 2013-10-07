var Sidebar = {

    init:   function(){
        this.makeSidebarClickable();
    },

    makeSidebarClickable: function(){
        var menuItems = $('div#sidebar').find('div.panel-heading');
        $.each(menuItems, this.addMenuItemListener);
    },

    addMenuItemListener: function(index, element){
        $(element).on('click', this.menuItemEventHandler);
    },

    menuItemEventHandler: function(event){
        console.log(event.targetElement);
    }


};