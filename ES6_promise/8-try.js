export default function divideFunction(numerator, demoninator) {
  if (demoninator === 0) {
    throw Error('Cannot divide by 0');
  }
  return numerator / demoninator;
}
