from unittest.mock import mock_open, patch
from task1 import add_student, remove_student, import_students, export_students, students_list, \
    check_students, edit_students

class TestImportStudents:
    def test_import_students(self):
        file_content = "Jan Kowalski,Anna Nowak"

        with patch("builtins.open", mock_open(read_data=file_content)):
            result = import_students("students.txt")

        assert len(result) == 2
        for student_id, student_data in result.items():
            assert "name" in student_data and "attendance" in student_data
            assert isinstance(student_data["name"], str)
            assert student_data["attendance"] is False

    def test_import_empty_file(self):
        with patch("builtins.open", mock_open(read_data="")):
            result = import_students("students.txt")
        assert result == {}

    def test_import_nonexistent_file(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = import_students("students.txt")
        assert result == {}

    def test_import_invalid_format(self):
        invalid_data = "JanKowalski AnnaNowak"
        with patch("builtins.open", mock_open(read_data=invalid_data)):
            result = import_students("students.txt")
            assert result == {}, "Invalid format data should return an empty dictionary"


class TestStudentsOperations:
    def test_add_student(self):
        students_list = {}
        name = "Jan Kowalski"
        result = add_student(students_list, name)
        assert len(result) == 1
        student_id = list(result.keys())[0]
        assert result[student_id]["name"] == name
        assert result[student_id]["attendance"] is False

    def test_remove_existing_student(self):
        students_list = {"1234": {"name": "Jan Kowalski", "attendance": True}}
        result = remove_student(students_list, "1234")
        assert "1234" not in result
        assert len(result) == 0

    def test_remove_nonexistent_student(self):
        students_list = {"1234": {"name": "Jan Kowalski", "attendance": True}}
        result = remove_student(students_list, "5678")
        assert "1234" in result
        assert len(result) == 1

class TestExportStudents:
    @patch("builtins.open", new_callable=mock_open)
    def test_export_students(self, mock_file):
        students_list = {
            "1234": {"name": "Jan Kowalski", "attendance": True},
            "5678": {"name": "Anna Nowak", "attendance": False},
        }
        export_students("studentsAttendance.txt", students_list)
        mock_file.assert_called_once_with("studentsAttendance.txt", "a")
        handle = mock_file()
        handle.write.assert_any_call("Jan Kowalski (ID: 1234) - present\n")
        handle.write.assert_any_call("Anna Nowak (ID: 5678) - absent\n")


class TestAttendance:
    def test_check_students(self):
        students_list = {
            "1234": {"name": "Jan Kowalski", "attendance": False},
            "5678": {"name": "Anna Nowak", "attendance": False},
        }
        with patch("builtins.input", side_effect=["Y", "N"]):
            result = check_students(students_list)
        assert result["1234"]["attendance"] is True
        assert result["5678"]["attendance"] is False

    def test_edit_existing_student_attendance(self):
        students_list = {"1234": {"name": "Jan Kowalski", "attendance": False}}
        result = edit_students(students_list, "1234", "Y")
        assert result["1234"]["attendance"] is True

    def test_edit_nonexistent_student(self):
        students_list = {"1234": {"name": "Jan Kowalski", "attendance": False}}
        result = edit_students(students_list, "5678", "Y")
        assert "5678" not in result
        assert result["1234"]["attendance"] is False

