
var chai = require('chai');
var chaiHttp = require('chai-http');


chai.use(chaiHttp);

var should = require('chai').should();
expext = require('chai').expext,
supertest = require('supertest'),
api = supertest('http://localhost:3000');

var superagent = require('superagent');

var express = require('express'),
    app = express(),
    port = process.env.PORT || 3000,
    mongoose = require('mongoose'),
    Provider = require('../api/models/providerModel'),
    bodyParser = require('body-parser');


mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/Providerdb');


app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


var routes = require('../api/routes/providerRoutes');

routes(app);

app.listen(port);



//describe('Refresh Providers', () => {
//        beforeEach((done) => { //Before each test we empty the database
//        Provider.remove({}, (err) => {
//            done();
//        })
//    })
//})

describe('Tests', function() {
    it('should use automated tests that can be ran from the command line');
});

describe('API', function() {
    it('Uses a datastore for querying data');
    it('should returns valid JSON');
});

describe('Providers', function() {
    it('An API endpoint that implements the url ending with `/providers`');

    it('The expected response is a JSON blob containing the list of providers.');
});

describe('Query', function() {
    it('should list ALL providers on /providers GET', (done) => {
        chai.request(app)
            .get('/providers')
            .end((err, res) => {
            res.should.have.status(200);
        res.body.should.be.a('array');
        res.body.length.should.be.eql(0);
        done();
})
})
    it('should list a SET of providers on /providers GET with parameters');
    it('finds results that have a maximum number of total discharges with no more than the value of the max_discharges parameter');
    it('finds results that have a minimum number of total discharges with no less than the value of the min_discharges parameter');
    it('finds results that have a maximum average covered chages of no more than the value of the max_average_covered_charges parameter');
    it('finds results that have a minimum average covered chages of no less than the value of the min_average_covered_charges parameter');     
    it('finds results that have a maximum average medicare payments of no more than the value of the max_average_medicare_payments parameter');
    it('finds results that have a minimum average medicare payments of no less than the value of the min_average_medicare_payments parameter');
    it('finds results that have a state that matches the state parameter');
    it('Should work with every possible combination of query strings parameters');
});

describe('Documentation', function() {
    it('Should include a writeup/README file');
    it('Should describe the architecture, solutions, and assumptions made');
});



/*
  * Test the /GET route
  */
describe('/GET providers', () => {
    it('it should GET all the providers', (done) =;> {
        chai.request(app)
            .get('/providers')
            .end((err, res) => {
            res.should.have.status(200);
        res.body.should.be.a('array');
        res.body.length.should.be.eql(0);
        done();
})
}
)
})
describe('express rest api server', function() {
    var id;
    it('post object', function (done) {
        superagent.post('http://localhost:3000/providers/')
            .send({
                name: 'John'
                , email: 'john@rpjs.co'
            })
            .end(function (e, res) {
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(res.body.length).to.eql(1);
                expect(res.body[0]._id.length).to.eql(24);
                id = res.body[0]._id;
                done();
            });
    });

    it('retrieves an object', function (done) {
        superagent.get('http://localhost:3000/providers/' + id)
            .end(function (e, res) {
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(typeof res.body).to.eql('object');
                expect(res.body._id.length).to.eql(24);
                expect(res.body._id).to.eql(id);
                done();
            });
    });

    it('retrieves a collection', function (done) {
        superagent.get('http://localhost:3000/providers/')
            .end(function (e, res) {
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(res.body.length).to.be.above(0);
                expect(res.body.map(function (item) {
                    return item._id
                })).to.contain(id);
                done();
            });
    });

    it('updates an object', function (done) {
        superagent.put('http://localhost:3000/providers/' + id)
            .send({
                name: 'Peter'
                , email: 'peter@yahoo.com'
            })
            .end(function (e, res) {
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(typeof res.body).to.eql('object');
                expect(res.body.msg).to.eql('success');
                done();
            });
    });
    it('checks an updated object', function (done) {
        superagent.get('http://localhost:3000/providers/' + id)
            .end(function (e, res) {
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(typeof res.body).to.eql('object');
                expect(res.body._id.length).to.eql(24);
                expect(res.body._id).to.eql(id);
                expect(res.body.name).to.eql('Peter');
                done();
            });
    });

//    it('removes an object', function (done) {
//        superagent.del('http://localhost:3000/providers/' + id)
//            .end(function (e, res) {
//                // console.log(res.body)
//                expect(e).to.eql(null);
//                expect(typeof res.body).to.eql('object');
//                expect(res.body.msg).to.eql('success');
//                done();
//            });
//    });
});