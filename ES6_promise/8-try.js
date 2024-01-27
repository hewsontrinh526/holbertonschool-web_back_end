export default function divideFunction(numerator, demoninator) {
  if (demoninator === 0) {
    throw new Error('Cannot divide by 0');
  }

  try {
    return numerator / demoninator;
  } catch (error) {
    console.error(error);
    return error;
  }
}
