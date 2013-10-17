/**
 * Created by orjan on 14/10/13.
 */

app.Router = Backbone.Router.extend({
   routes:{
       "" : "frontpage",
       "products" : "products",
       "recipes" : "recipes",
       "product-category/:pcid" : "product_category",
       "product/:pid" : "product_detail"
   },

   initialize: function(){

   },

   frontpage: function(){
       console.log("router -> frontpage")
       if (this.activeView) this.activeView.remove();
       if (this.sidebarView) this.sidebarView.remove();
       if (this.cartView) this.cartView.remove();

   },

   products: function()
   {
       console.log("router -> products");

       if (this.sidebarView) this.sidebarView.remove();
       this.sidebarView = new app.ProductSidebarView({
           el: "#sidebar",
           router: this
       });
       this.sidebarView.render();

       app.cartView = this.cartView = new app.CartView({
           el: "#cart-widget-container",
           router: this
       });
       app.cartView.render();
   },

   recipes: function(){
       console.log("router -> recipes")
       if (this.sidebarView) this.sidebarView.remove();

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