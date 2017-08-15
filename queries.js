var promise = require('bluebird');

var options = {
  // Initialization Options
  promiseLib: promise
};

var pgp = require('pg-promise')(options);
var connectionString = 'postgres://postgres:postgres@localhost:5432/providers';
var db = pgp(connectionString);

// add query functions

module.exports = {
  getAllProviders: getAllProviders,
  getSingleProvider: getSingleProvider,
  createProvider: createProvider,
  updateProvider: updateProvider,
  removeProvider: removeProvider
};

function getAllProviders(req, res, next) {
  db.any('select * from providers')
    .then(function (data) {
      res.status(200)
        .json({
          status: 'success',
          data: data,
          message: 'Retrieved ALL providers'
        });
    })
    .catch(function (err) {
      return next(err);
    });
}

function getSingleProvider(req, res, next) {
  db.any('select * from providers')
    .then(function (data) {
      res.status(200)
        .json({
          status: 'success',
          data: data,
          message: 'Retrieved ALL providers'
        });
    })
    .catch(function (err) {
      return next(err);
    });
}

function createProvider(req, res, next) {
  db.any('select * from providers')
    .then(function (data) {
      res.status(200)
        .json({
          status: 'success',
          data: data,
          message: 'Retrieved ALL providers'
        });
    })
    .catch(function (err) {
      return next(err);
    });
}

function updateProvider(req, res, next) {
  db.any('select * from providers')
    .then(function (data) {
      res.status(200)
        .json({
          status: 'success',
          data: data,
          message: 'Retrieved ALL providers'
        });
    })
    .catch(function (err) {
      return next(err);
    });
}

function removeProvider(req, res, next) {
  db.any('select * from providers')
    .then(function (data) {
      res.status(200)
        .json({
          status: 'success',
          data: data,
          message: 'Retrieved ALL providers'
        });
    })
    .catch(function (err) {
      return next(err);
    });
}