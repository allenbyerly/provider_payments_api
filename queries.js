var promise = require('bluebird');

var options = {
  // Initialization Options
  promiseLib: promise
};

var pgp = require('pg-promise')(options);
var connectionString = 'postgres://localhost:5432/providers';
var db = pgp(connectionString);

// add query functions

module.exports = {
  getAllProviders: getAllProviders,
  getSingleProvider: getSingleProvider,
  createProvider: createProvider,
  updateProvider: updateProvider,
  removeProvider: removeProvider
};