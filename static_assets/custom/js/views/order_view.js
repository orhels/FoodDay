app.OrderView = Backbone.View.extend({

    initialize: function (options) {

    },

    render: function () {
        var that = this;
        $.get("/order/", function (data) {
            that.$el.html(data);

            $.get("/order/timeslots/0", function (data) {
                that.$el.find("#delivery-time-selector").html(data);
            })
        });
        return this;
    },

    remove: function () {
        this.undelegateEvents();
        this.$el.empty();
    }
});