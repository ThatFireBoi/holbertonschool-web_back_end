export default function getStudentsByLocation(array, location) {
  return array.filter((student) => student.location === location);
}
