const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return the sum of rounded numbers', function () {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
      assert.strictEqual(calculateNumber('SUM', -1.2, -3.7), -5);
      assert.strictEqual(calculateNumber('SUM', -1.5, -3.7), -5);
    });
  });

  describe('SUBTRACT', function () {
    it('should return the difference of rounded numbers', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5, 3), 2);
      assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
      assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
      assert.strictEqual(calculateNumber('SUBTRACT', -1.2, -3.7), 3);
      assert.strictEqual(calculateNumber('SUBTRACT', -1.5, -3.7), 2);
    });
  });

  describe('DIVIDE', function () {
    it('should return the division of rounded numbers', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 8, 2), 4);
      assert.strictEqual(calculateNumber('DIVIDE', 7.5, 2.1), 4);
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
      assert.strictEqual(calculateNumber('DIVIDE', -4.5, 2), -2);
    });

    it('should return "Error" when dividing by zero', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, -0.2), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
    });
  });
});