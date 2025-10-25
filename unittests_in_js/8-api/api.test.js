const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const url = 'http://localhost:7865/';

  it('Correct status code?', (done) => {
    request.get(url, (err, res, _body) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', (done) => {
    request.get(url, (err, _res, body) => {
      expect(err).to.be.null;
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Other?', (done) => {
    request.get(url, (err, res, _body) => {
      expect(err).to.be.null;
      expect(res.headers['content-type']).to.match(/text\/html/);
      done();
    });
  });
});