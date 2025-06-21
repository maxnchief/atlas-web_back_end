const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {
  describe('type=SUM', function () {
    it('should return the sum of rounded numbers', function () {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
      expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
      expect(calculateNumber('SUM', -1.2, -3.7)).to.equal(-5);
      expect(calculateNumber('SUM', -1.5, -3.7)).to.equal(-5);
    });
  });

  describe('type=SUBTRACT', function () {
    it('should return the difference of rounded numbers', function () {
      expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
      expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
      expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
      expect(calculateNumber('SUBTRACT', -1.2, -3.7)).to.equal(3);
      expect(calculateNumber('SUBTRACT', -1.5, -3.7)).to.equal(3);
    });
  });

  describe('type=DIVIDE', function () {
    it('should return the division of rounded numbers', function () {
      expect(calculateNumber('DIVIDE', 8, 2)).to.equal(4);
      expect(calculateNumber('DIVIDE', 7.5, 2.1)).to.equal(4);
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
      expect(calculateNumber('DIVIDE', -4.5, 2)).to.equal(-2);
    });
  });

  describe('type=DIVIDE and return error', function () {
    it('should return "Error" when dividing by zero', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 1.4, -0.2)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');