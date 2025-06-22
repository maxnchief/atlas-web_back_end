const request = require('supertest');
const app = require('./api');

describe('Index page', () => {
  it('GET / should return status code 200', (done) => {
    request(app)
      .get('/')
      .expect(200, done);
  });

  it('GET / should return "Welcome to the payment system"', (done) => {
    request(app)
      .get('/')
      .expect('Welcome to the payment system', done);
  });
});