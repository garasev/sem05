"use strict";

class ServerA {
	static fs = require("fs");
	static express = require("express");

	constructor(port) {
		this.app = ServerA.express();
		this.port = port;

		try {
			this.app.listen(this.port);
			console.log(` Starting server on port ${this.port}... `);
		} catch (error) {
			console.log(" Failure while starting server!");
			throw new Error(' Port is unavalible!');
		}
		
		this.app.use(this.getHeaders);
		this.app.use(ServerA.express.static(__dirname + '/static'));
		this.app.post('/insert/record', this.insertRecord);
		this.app.post('/select/record', this.selectRecord);
		console.log(" Server started succesfully!");
	}

	getHeaders(request, response, next) {
		response.header("Cache-Control", "no-cache, no-store, must-revalidate");
    	response.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    	response.header("Access-Control-Allow-Origin", "*");
    	next();
	}

	insertRecord(request, response) {
		function loadBody(request, callback) {
			let body = [];
			request.on('data', (chunk) => {
				body.push(chunk);
			}).on('end', () => {
				body = Buffer.concat(body).toString();
				callback(body);
			});
		}

		loadBody(request, function(body) {
			const obj = JSON.parse(body);
			const name = obj.name;
			const price = obj.price;

			const storage_path = "data/cars.json";
			const fd = ServerA.fs.readFileSync(storage_path, "utf8")
			let storage = fd.length ? new Map(JSON.parse(fd)) : new Map();

			const name_exists = storage.has(name);

			let added = false;

			if (!name_exists) {
				added = true;
				storage.set(name, price);
				ServerA.fs.writeFileSync(storage_path, JSON.stringify([...storage]));
			}

			response.end(JSON.stringify({answer: added}));
		});
	}

	selectRecord(request, response) {
		function loadBody(request, callback) {
			let body = [];
			request.on('data', (chunk) => {
				body.push(chunk);
			}).on('end', () => {
				body = Buffer.concat(body).toString();
				callback(body);
			});
		}

		loadBody(request, function(body) {
			const obj = JSON.parse(body);
			const name = obj.name;

			const storage_path = "data/cars.json";
			const fd = ServerA.fs.readFileSync(storage_path, "utf8")
			let storage = fd.length ? new Map(JSON.parse(fd)) : new Map();

			let found = false;
			let price;

			if (storage.has(name)) {
				found = true;
				price = storage.get(name);
			}

			response.end(JSON.stringify({answer: found,
										 price: price}));
		});
	}
}

class ServerB {
	static fs = require("fs");
	static express = require("express");

	constructor(port) {
		this.app = ServerB.express();
		this.port = port;

		try {
			this.app.listen(this);
			console.log(` Starting server on port ${this.port}... `);
		} catch (error) {
			console.log(" Failure while starting server!");
			throw new Error(' Port is unavalible!');
		}
		
		this.app.use(this.getHeaders);
		this.app.use(ServerB.express.static(__dirname + '/static'));
		this.app.post('/insert/record' , this.insertRecord);
		this.app.post('/select/record', this.selectRecord);
		console.log(" Server started succesfully!");
	}

	getHeaders(request, response, next) {
		response.header("Cache-Control", "no-cache, no-store, must-revalidate");
    	response.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    	response.header("Access-Control-Allow-Origin", "*");
    	next();
	}

	loadBody(request, callback) {
		let body = [];
		request.on('data', (chunk) => {
			body.push(chunk);
		}).on('end', () => {
			body = Buffer.concat(body).toString();
			callback(body);
		});
	}

	insertRecord(request, response) {
		function loadBody(request, callback) {
			let body = [];
			request.on('data', (chunk) => {
				body.push(chunk);
			}).on('end', () => {
				body = Buffer.concat(body).toString();
				callback(body);
			});
		}

		console.log(1);
		loadBody(request, function(body) {
			const obj = JSON.parse(body);
			const name = obj.name;
			const cars = obj.cars;

			const storage_path = "data/storage.json";
			const fd = ServerB.fs.readFileSync(storage_path, "utf8")
			let storage = fd.length ? new Map(JSON.parse(fd)) : new Map();

			console.log(name, cars);
			console.log(storage);

			const name_exists = storage.has(name);

			let added = false;

			if (!name_exists) {
				added = true;
				storage.set(name, cars);
				ServerB.fs.writeFileSync(storage_path, JSON.stringify([...storage]));
			}

			response.end(JSON.stringify({answer: added}));
		});
	}

	selectRecord(request, response) {
		function loadBody(request, callback) {
			let body = [];
			request.on('data', (chunk) => {
				body.push(chunk);
			}).on('end', () => {
				body = Buffer.concat(body).toString();
				callback(body);
			});
		}

		loadBody(request, function(body) {
			const obj = JSON.parse(body);
			const name = obj.name;

			const storage_path = "data/storage.json";
			const fd = ServerB.fs.readFileSync(storage_path, "utf8")
			let storage = fd.length ? new Map(JSON.parse(fd)) : new Map();

			let found = false;
			let cars;

			if (storage.has(name)) {
				found = true;
				cars = storage.get(name);
			}

			response.end(JSON.stringify({answer: found,
										 cars: cars}));
		});
	}
}

class ServerC {
	static fs = require("fs");
	static express = require("express");

	constructor(port) {
		this.app = ServerC.express();
		this.port = port;

		try {
			this.app.listen(this.port);
			console.log(` Starting server on port ${this.port}... `);
		} catch (error) {
			console.log(" Failure while starting server!");
			throw new Error(' Port is unavalible!');
		}
		
		this.app.use(this.getHeaders);
		this.app.use(ServerC.express.static(__dirname + '/static'));
		this.app.post('/add_car', this.addCar);
		this.app.get('/get_car', this.getCar);
		this.app.post('/add_storage', this.addStorage);
		this.app.get('/get_storage', this.getStorage);
		console.log(" Server started succesfully!");
	}

	getHeaders(request, response, next) {
		response.header("Cache-Control", "no-cache, no-store, must-revalidate");
    	response.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    	response.header("Access-Control-Allow-Origin", "*");
    	next();
	}

	addCar(request, response) {
		const name = request.query.name;
		const price = request.query.price;

		function sendPost(url, body, callback) {
			const headers = {};
			const requests = require("request");

			headers["Cache-Control"] = "no-cache, no-store, must-revalidate";
			headers["Connection"] = "close";

			requests.post({
				url: url,
				body: body,
				headers: headers
			}, function(error, response, body) {
				if (error) {
					callback(null);
				} else {
					callback(body);
				}
			});
		}

		sendPost("http://localhost:5001/insert/record",
				  JSON.stringify({name: name,
				  				  price: price
	}), function(answerString) {
			response.end(answerString);
		});
	}

	getCar(request, response) {
		const name = request.query.name;

		function sendPost(url, body, callback) {
			const headers = {};
			const requests = require("request");

			headers["Cache-Control"] = "no-cache, no-store, must-revalidate";
			headers["Connection"] = "close";

			requests.post({
				url: url,
				body: body,
				headers: headers
			}, function(error, response, body) {
				if (error) {
					callback(null);
				} else {
					callback(body);
				}
			});
		}

		sendPost("http://localhost:5001/select/record",
				  JSON.stringify({name: name}),
		function(answerString) {
			response.end(answerString);
		});
	}

	addStorage(request, response) {
		const name = request.query.name;
		const cars = request.query.cars;

		function sendPost(url, body, callback) {
			const headers = {};
			const requests = require("request");
			headers["Cache-Control"] = "no-cache, no-store, must-revalidate";
			headers["Connection"] = "close";

			requests.post({
				url: url,
				body: body,
				headers: headers
			}, function(error, response, body) {
				if (error) {
					callback(null);
				} else {
					callback(body);
				}
			});
		}

		sendPost("http://localhost:5002/insert/record",
				  JSON.stringify({name: name,
				  				  cars: cars}),
		function(answerString) {
			response.end(answerString);
		});
	}

	getStorage(request, response) {
		const name = request.query.name;
		const requests = require("request");

		function sendPost(url, body, callback) {
			const headers = {};
			headers["Cache-Control"] = "no-cache, no-store, must-revalidate";
			headers["Connection"] = "close";

			requests.post({
				url: url,
				body: body,
				headers: headers
			}, function(error, response, body) {
				if (error) {
					callback(null);
				} else {
					callback(body);
				}
			});
		}

		sendPost("http://localhost:5002/select/record",
				  JSON.stringify({name: name}),
		function(answerString) {
			response.end(answerString);
		});
	}
}

let serverA = new ServerA(5001);
let serverB = new ServerB(5002);
let serverC = new ServerC(5003);