export default function getStudentIdsSum(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  return array.reduce((sum, student) => sum + student.id, 0);
}
