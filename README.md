# Provider Payments -- Queryable API

## Overview
A API server for a national healthcare provider that has queriable endpoints for inpatient prospective payment systems providers and summary data for the top 100 diagnosis related provider groups throughout the country.   

## Design Choice: MEAN Stack - Angular + Mocha Chai Testing Frameworks

Core Stack
Node - Node was used for this project as the primary stack with the intention of stayng as close to a MEAN stack as possible (MongoExpressAngularNode) 
Express - to implement the REST API Server
Mongo - No-SQL datastore exposed to the rest of the stack using Mongoose
Mocha & Chai - Testing frameworks.

## Design Choices

1. The solution can be implemented repeatable and rapidly (2 hours or less).
2. The solution is simple to implement and hs minimal dependencies or unnecessary complications.
3. The solution is designed for the stack to scale vertically (Front-Ends & Deep-Backends)
4. The solution is designed for the stack to scale horizontally (Additional Features, Data-Sets, Functionalities, Capabilities)
5. The Solution has a good test framework options that can be used as the "Defention of Done".
6. Technology stack must be able to scale using generaly available cloud services.
7. The solution must be able to support Health Care HIPAA/HITECH/PCI/OAUTH/FHIR requirements. 
8.  The intent is to make a project that can be reused to expand from with very little rework and has maximum flexibility so that if an additional dataset was to be added to the project then it would require at least 50% less time to implment than the inital project. 

The challenge is a two-fold challenge: 
1.  Carefuly consider various implementation methods, architectures, designs, and technologies (known and unknown), experment, and ultimately decide how to implement the solution.
2.  Complete the challenge with a solution that fullfills all requirements. 

I took the first part very seriously and took some time to implement the same project using multiple different technology stacks including python, ruby, java, and node based options.  I initially started with a node project and was able to get quite far very quickly and then decided to try a few other stacks and options to compare the tradeoffs from one to another including node stacks with Postgres Datastoresm.  I found Django to be my preference until I ran into unecessary complexities and to many additional functions that were unecessary for the requirements.

In the end I chose the method that would make it as easy as possible to complete the chalenge, meet the requirements and nothing more.  The stack I chose allowed me to define the work, do the work, check the work, document the work, and complete the work without anything unecessarily added either.  Furthermore, this implementation is made to be easily reviewed and repeated by almost any software developer to determine what it does and how it does it.  



## Deliverables - (Self-Test)
- An API endpoint that implements the url ending with `/providers` (COMPLETED)
- Every possible combination of query string parameters works (COMPLETED)
- Some datastore is used (COMPLETED)
- Your API returns valid JSON (COMPLETED)
- Automated tests (i.e. tests that can be run from command line) (COMPLETED)
- A writeup/README describing your architecture, solutions, and assumptions made.  Be as thorough as possible with your explination.  (COMPLETED)





## 


## Instructions
You have been asked to assist in the creation of an internal API for a national healthcare provider.  This provider has a set of inpatient prospective payment systems providers.  This dataset can be found here: https://s3-us-west-2.amazonaws.com/bain-coding-challenge/Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv.  We want to implement an API that allows for various methods of querying this data.  

#### API:

```
GET /providers?max_discharges=5&min_discharges=6&max_average_covered_charges=50000
&min_average_covered_charges=40000&min_average_medicare_payments=6000
&max_average_medicare_payments=10000&state=GA
```
**NOTE the line breaks are there just for readability.  In reality this is one long querystring**

| Parameter                       | Description                               |
|---------------------------------|-------------------------------------------|
| `max_discharges`                | The maximum number of Total Discharges    |
| `min_discharges`                | The minimum number of Total Discharges    |
| `max_average_covered_charges`   | The maximum Average Covered Charges       | 
| `min_average_covered_charges`   | The minimum Average Covered Charges       |
| `max_average_medicare_payments` | The maximum Average Medicare Payment      |
| `min_average_medicare_payments` | The minimum Average Medicare Payment      |
| `state`                         | The exact state that the provider is from |

#### The expected response is a JSON blob containing the list of providers meeting the criteria.  All query parameters are optional.  Min and Max fields are inclusive

```json
[
	{
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
	
]

```


Once complete, please send a copy of all of your code to [ronald.brown@bain.com](mailto:ronald.brown@bain.com) as well as deploy your solution somewhere (Heroku is perfect if you want to go that route) and include a link to it in your email.

Good luck, if you have any questions please mail [ronald.brown@bain.com](mailto:ronald.brown@bain.com)

If you're having problems with database size on Heroku, use a smaller subset of the data and indicate it in your writeup.  Also provide example queries to this