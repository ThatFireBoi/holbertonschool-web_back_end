export default function updateStudentGradeByCity(array, city, newGrades) {
  return array
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.filter((grade) => grade.studentId === student.id);
      if (grade.length === 0) {
        student.grade = 'N/A';
      } else {
        student.grade = grade[0].grade;
      }
      return student;
    });
}
