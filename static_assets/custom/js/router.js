/**
 * Created by orjan on 14/10/13.
 */

app.Router = Backbone.Router.extend({
   routes:{
       "product-category/:pcid" : "product_category",
       "product/:pid" : "product_detail"
   },

   initialize: function(){
       app.sidebarView = this.sidebarView = new app.SidebarView({
           el: "#sidebar",
           router: this
       });
       app.sidebarView.render();

       app.cartView = this.cartView = new app.CartView({
           el: "#cart-widget-container",
           router: this
       });
       app.cartView.render();
   },

   product_category: function(pcid){
       if (this.activeView){
           this.activeView.remove();
       }
       app.productCategoryView = this.activeView = new app.ProductCategoryDetailView({
           el: "#main-content",
           router: this,
           pcid: pcid
       });
       app.productCategoryView.render();

   },

   product_detail: function(pid){
       if (this.activeView){
           this.activeView.remove();
       }
       app.productView = this.activeView = new app.ProductView({
           el: "#main-content",
           router: this,
           pid: pid
       });
       app.productView.render();
   }
});