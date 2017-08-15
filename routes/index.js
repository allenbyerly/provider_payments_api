var express = require('express');
var router = express.Router();

var db = require('../queries');


router.get('/api/providers', db.getAllProviders);
router.get('/api/providers/:id', db.getSingleProvider);
router.post('/api/providers', db.createProvider);
router.put('/api/providers/:id', db.updateProvider);
router.delete('/api/providers/:id', db.removeProvider);


module.exports = router;