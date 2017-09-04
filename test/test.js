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

var superagent = require('superagent');
var expect = require('expect.js');


var chai = require('chai');
var chaiHttp = require('chai-http');
var should = chai.should();

chai.use(chaiHttp);


describe('Blobs', function() {
    it('should list ALL blobs on /blobs GET');
    it('should list a SINGLE blob on /blob/<id> GET');
    it('should add a SINGLE blob on /blobs POST');
    it('should update a SINGLE blob on /blob/<id> PUT');
    it('should delete a SINGLE blob on /blob/<id> DELETE');
});


describe('express rest api server', function(){
    var id;

    it('post object', function(done){
        superagent.post('http://localhost:3000/providers/')
            .send({ name: 'John'
                , email: 'john@rpjs.co'
            })
            .end(function(e,res){
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(res.body.length).to.eql(1);
                expect(res.body[0]._id.length).to.eql(24);
                id = res.body[0]._id;
                done()
            })
    });

    it('retrieves an object', function(done){
        superagent.get('http://localhost:3000/providers/'+id)
            .end(function(e, res){
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(typeof res.body).to.eql('object');
                expect(res.body._id.length).to.eql(24);
                expect(res.body._id).to.eql(id);
                done()
            })
    });

    it('retrieves a collection', function(done){
        superagent.get('http://localhost:3000/providers/')
            .end(function(e, res){
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(res.body.length).to.be.above(0);
                expect(res.body.map(function (item){return item._id})).to.contain(id);
                done()
            })
    });

    it('updates an object', function(done){
        superagent.put('http://localhost:3000/providers/'+id)
            .send({name: 'Peter'
                , email: 'peter@yahoo.com'})
            .end(function(e, res){
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(typeof res.body).to.eql('object');
                expect(res.body.msg).to.eql('success');
                done()
            })
    });
    it('checks an updated object', function(done){
        superagent.get('http://localhost:3000/providers/'+id)
            .end(function(e, res){
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(typeof res.body).to.eql('object');
                expect(res.body._id.length).to.eql(24);
                expect(res.body._id).to.eql(id);
                expect(res.body.name).to.eql('Peter');
                done()
            })
    });

    it('removes an object', function(done){
        superagent.del('http://localhost:3000/providers/'+id)
            .end(function(e, res){
                // console.log(res.body)
                expect(e).to.eql(null);
                expect(typeof res.body).to.eql('object');
                expect(res.body.msg).to.eql('success');
                done()
            })
    })
});
