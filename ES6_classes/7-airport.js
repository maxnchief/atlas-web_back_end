class Airport {
    constructor(name, code) {
        this._name = name;
        this._code = code;
    }

    toString() {
        return this._code;
    }
}

export default Airport;