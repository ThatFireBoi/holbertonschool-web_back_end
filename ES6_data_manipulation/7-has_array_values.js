export default function hasValuesFromArray(array, values) {
  return values.every((value) => array.includes(value));
}
