from unittest.mock import mock_open, patch
from task1 import add_student, file_lista_studentow, remove_student, import_students, export_students, students_list, \
    check_students, edit_students


class TestImportStudents:
    def test_import_students(self):
        #given
        file_content="Jan Kowalski, Anna Nowak,"
        #when
        with patch('builtins.open', mock_open(read_data=file_content)):
            result=import_students(file_lista_studentow)
        #then
        assert result=={'Jan Kowalski': True, ' Anna Nowak': True}

class TestStudentsOperations:
    def test_add_student(self):
        # Given
        imie = "Jan Kowalski"
        students_list = {}

        # When
        with patch("builtins.open", mock_open()):
            result = add_student(students_list, imie)

        # Then
        expected = {"Jan Kowalski": True}
        assert result == expected

    def test_remove_student(self):
        #given
        file_lista_studentow = "students.txt"
        students_list = {"Jan Kowalski": True, "Damian Szymczyk":True}
        imie = "Damian Szymczyk"

        #when
        with patch("builtins.open", mock_open()):
            remove_student(file_lista_studentow,students_list,imie)

        #then
        assert "Damian Szymczyk" not in students_list

class TestExportStudents:
    @patch("builtins.open", new_callable=mock_open)
    def test_export_students(self, mock_file):
        # Given
        file_path2 = "studentsAttendance.txt"
        students_list = {"Jan Kowalski": True, "Anna Nowak": False}
        test_date = "2024-11-24"

        # When
        export_students(file_path2, students_list)

        # Then
        mock_file().write.assert_any_call(str(test_date) + "\n")
        mock_file().write.assert_any_call("Jan Kowalski - obecny\n")
        mock_file().write.assert_any_call("Anna Nowak - nieobecny\n")

class TestAttendance:
    def test_check_students(self):
        #given
        students_list={"Jan Kowalski": None, "Anna Nowak": None}

        #when
        with patch("builtins.input", side_effect=["T","N"]):
            check_students(students_list)
        #then
        assert students_list["Jan Kowalski"] == True
        assert students_list["Anna Nowak"] == False

    def test_edit_students_to_present(self):
        #given
        students_list={}
        imie="Jan Kowalski"
        obecnosc="T"

        #when
        edit_students(students_list,imie,obecnosc)

        #then
        assert students_list["Jan Kowalski"] == True

    def test_edit_students_add_to_absent(self):
        #given
        students_list={}
        imie="Anna Nowak"
        obecnosc="N"

        #when
        edit_students(students_list,imie,obecnosc)

        #then
        assert students_list["Anna Nowak"] == False

