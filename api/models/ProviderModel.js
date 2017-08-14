'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var ProviderSchema = new Schema({
    provider_name: {
        type: String,
        Required: 'Kindly enter the name of the provider'
    },
    provider_street: {
        type: String,
    },
    provider_city: {
        type: String,
    },
    provider_state: {
        type: String,
    },
    provider_zip: {
        type: Number
    },
    Created_date: {
        type: Date,
        default: Date.now
    },
    status: {
        type: [{
            type: String,
            enum: ['pending', 'ongoing', 'completed']
        }],
        default: ['pending']
    }
});

module.exports = mongoose.model('Provider', ProviderSchema);

/*  {
        "Provider Name": "SOUTHEAST ALABAMA MEDICAL CENTER",
        "Provider Street Address": "1108 ROSS CLARK CIRCLE",
        "Provider City": "DOTHAN",
        "Provider State": "AL",
        "Provider Zip Code": "36301",
        "Hospital Referral Region Description": "AL - Dothan",
        "Total Discharges": 91,
        "Average Covered Charges": "$32,963.07",
        "Average Total Payments": 	"$5,777.24",
        "Average Medicare Payments": "$4,763.73"
    },
    {
		"Provider Name": "MARSHALL MEDICAL CENTER SOUTH",
		"Provider Street Address": "2505 U S HIGHWAY 431 NORTH",
		"Provider City": "BOAZ",
		"Provider State": "AL",
		"Provider Zip Code": "35957",
		"Hospital Referral Region Description": "AL - Birmingham",
		"Total Discharges": 14,
		"Average Covered Charges": "$32,963.07",
		"Average Total Payments": 	"$5,777.24",
		"Average Medicare Payments": "$4,763.73"
	}
*/