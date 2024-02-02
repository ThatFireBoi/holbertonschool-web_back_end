export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8View = new Int8Array(buffer, 0);
  if (position > length - 1) {
    throw Error('Position outside range');
  }
  int8View[position] = value;
  return int8View;
}
