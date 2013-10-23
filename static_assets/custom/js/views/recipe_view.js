/**
 * Created by orjan on 17/10/13.
 */
app.RecipeView = Backbone.View.extend({

    events: {
        'click #buy-recipe-btn': 'openBuyModal'
    },

    initialize: function(options){
        this.rid = options.rid;
    },

    render: function(){
        var that = this;
        $.get("/recipe/" + that.rid, function(data){
            that.$el.html(data);
            $('#servings').on('change', function(){
                if ($('#servings').val() <= 0){
                    $('#servings').val(1);
                }
                _.each($('.ingredient-quantity'), function(quantity){
                    var base_quantity = $(quantity).data("base-quantity");
                    $(quantity).html(base_quantity*$('#servings').val())
                })
            });
        });
        return this;
    },

    remove: function(){
        this.undelegateEvents();
        this.$el.empty();
    },

    openBuyModal: function(){
        $.get("/buy-recipe-modal/"+this.rid+"/"+ $('#servings').val(), function(data){
            var modal = {};
            $('#buy-recipe-modal').html(data);
            $('.modal').modal();
            $('.modal').on('shown.bs.modal', function(){
                modal = new app.RecipeBuyModalView({
                    el: $('#buy-recipe-modal'),
                    rid: this.rid
                });
            })
            $('.modal').on('hidden.bs.modal', function(){
                modal.remove();
            })
        });
    }
});