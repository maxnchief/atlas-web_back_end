class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this._validateString(name, 'Name');
    this._length = this._validateNumber(length, 'Length');
    his._students = this._validateArrayOfStrings(students, 'Students');
  }

  _validateString(value, attributeName) {
    if (typeof value !== 'string') {
      throw new TypeError(`${attributeName} must be a string`);
    }
      return value;
  }

  _validateNumber(value, attributeName) {
    if (typeof value !== 'number') {
      throw new TypeError(`${attributeName} must be a number`);
    }
      return value;
  }

  _validateArrayOfStrings(value, attributeName) {
    if (!Array.isArray(value) || !value.every(item => typeof item === 'string')) {
      throw new TypeError(`${attributeName} must be an array of strings`);
    }
      return value;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this._validateString(value, 'Name');
  }

  get length() {
    return this._length;
  }

  set length(value) {
    this._length = this._validateNumber(value, 'Length');
  }

  get students() {
    return this._students;
  }

  set students(value) {
    this._students = this._validateArrayOfStrings(value, 'Students');
  }
}

export default HolbertonCourse;
