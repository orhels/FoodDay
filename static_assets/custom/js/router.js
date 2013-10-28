/**
 * Created by orjan on 14/10/13.
 */

app.Router = Backbone.Router.extend({
   routes:{
       "" : "frontpage",
       "about": "about",
       "faq": 'faq',
       "footer": 'footer',
       "products" : "products",
       "recipes" : "recipes",
       "product-category/:pcid" : "product_category",
       "product/:pid" : "product_detail",
       "recipe-category/:rcid" : "recipe_category",
       "recipe/:rid" : "recipe_detail"
   },

   initialize: function(){

   },

   frontpage: function(){
       //this.footer();
       if (this.activeView) this.activeView.remove();
       if (this.sidebarView) this.sidebarView.remove();
       if (this.cartView) this.cartView.remove();
       this.fullpageView = new app.FrontpageView({
           el: "#fullpage",
           router: this
       })
       this.fullpageView.render();
   },

   about: function(){
       //this.footer();
       if (this.activeView) this.activeView.remove();
       if (this.sidebarView) this.sidebarView.remove();
       if (this.cartView) this.cartView.remove();
       this.fullpageView = new app.AboutView({
           el: "#fullpage",
           router: this
       })
       this.fullpageView.render();
   },

   faq: function(){
       //this.footer();
       if (this.activeView) this.activeView.remove();
       if (this.sidebarView) this.sidebarView.remove();
       if (this.cartView) this.cartView.remove();
       this.fullpageView = new app.FaqView({
           el: "#fullpage",
           router: this
       })
       this.fullpageView.render();
   },

   footer: function(){
       if (this.footerView) return;
       this.footerView = new app.FooterView({
           el: "#footer",
           router: this
       });
       this.footerView.render();
   },

   products: function()
   {
       if (this.fullpageView) this.fullpageView.remove();
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
       if (this.fullpageView) this.fullpageView.remove();
       if (this.sidebarView) this.sidebarView.remove();

       this.sidebarView = new app.RecipeSidebarView({
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

   product_category: function(pcid){
       console.log("router -> product_category")
       if (this.activeView) this.activeView.remove();
       if (!(this.sidebarView || this.cartView)) this.products();
       this.activeView = new app.ProductCategoryDetailView({
           el: "#main-content",
           router: this,
           pcid: pcid
       });
       this.activeView.render();

   },

   product_detail: function(pid){
       if (this.activeView) this.activeView.remove();
       if (!(this.sidebarView || this.cartView)) this.products();

       this.activeView = new app.ProductView({
           el: "#main-content",
           router: this,
           pid: pid
       });
       this.activeView.render();
   },

   recipe_category: function(rcid){
       console.log("router -> recipe_category")
       if (this.activeView) this.activeView.remove();
       if (!(this.sidebarView || this.cartView)) this.recipes();

       this.activeView = new app.RecipeCategoryDetailView({
           el: "#main-content",
           router: this,
           rcid: rcid
       });
       this.activeView.render();
   },

   recipe_detail: function(rid){
       console.log("router -> recipe_detail");
       if (this.activeView) this.activeView.remove();
       if (!(this.sidebarView || this.cartView)) this.recipes();

       this.activeView = new app.RecipeView({
           el: "#main-content",
           router: this,
           rid: rid
       });
       this.activeView.render();
   }
});