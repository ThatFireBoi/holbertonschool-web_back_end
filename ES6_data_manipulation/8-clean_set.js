export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  const str = [];
  set.forEach((element) => {
    if (element && element.startsWith(startString)) {
      str.push(element.slice(startString.length));
    }
  });
  return str.join('-');
}
