'use strict';
module.exports = function(app) {
    var providers = require('../controllers/ProviderController');


    // todoList Routes
    app.route('/providers')
        .get(providers.list_all_providers)
        .post(providers.create_a_provider);


    app.route('/providers/:providerId')
        .get(todoList.read_a_provider)
        .put(todoList.update_a_provider)
        .delete(todoList.delete_a_provider);
};