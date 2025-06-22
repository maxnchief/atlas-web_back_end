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

describe('Cart page', () => {
  it('GET /cart/:id should return status 200 when id is a number', (done) => {
    request(app)
      .get('/cart/123')
      .expect(200, done);
  });

  it('GET /cart/:id should return correct message when id is a number', (done) => {
    request(app)
      .get('/cart/42')
      .expect('Payment methods for cart 42', done);
  });

  it('GET /cart/:id should return 404 when id is NOT a number', (done) => {
    request(app)
      .get('/cart/abc')
      .expect(404, done);
  });

  it('GET /cart/:id should return 404 when id is alphanumeric', (done) => {
    request(app)
      .get('/cart/123abc')
      .expect(404, done);
  });
});