const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
  it('should resolve with the correct object when success is true', async function () {
    const result = await getPaymentTokenFromAPI(true);
    expect(result).to.deep.equal({ data: 'Successful response from the API' });
  });

  it('should return undefined when success is false', function () {
    const result = getPaymentTokenFromAPI(false);
    expect(result).to.be.undefined;
  });
});