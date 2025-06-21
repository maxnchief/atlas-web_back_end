const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
  it('should stub Utils.calculateNumber and log the correct message', function () {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnceWithExactly(stub, 'SUM', 100, 20);
    sinon.assert.calledOnceWithExactly(consoleSpy, 'The total is: 10');

    stub.restore();
    consoleSpy.restore();
  });
});