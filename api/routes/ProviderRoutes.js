'use strict';
module.exports = function(app) {
    var provider = require('../controllers/ProviderController');


    // todoList Routes
    app.route('/provider')
        .get(provider.list_all_providers)
        .post(provider.create_a_provider);


    app.route('/provider/:providerId')
        .get(provider.read_a_provider)
        .put(provider.update_a_provider)
        .delete(provider.delete_a_provider);
};