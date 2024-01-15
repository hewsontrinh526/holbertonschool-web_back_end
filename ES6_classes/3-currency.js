export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }

    this._code = code;
    this._name = name;
  }

  set code(newCode) {
    this._code = newCode;
  }

  get code() {
    return this._code;
  }

  set name(newName) {
    this._name = newName;
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this._name} (${this.code})`;
  }
}
