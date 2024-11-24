from unittest.mock import mock_open, patch
from task1 import add_student, file_lista_studentow, remove_student, import_students, export_students, students_list


class TestImportStudents:
    def test_import_students(self):
        #given
        file_content="Jan Kowalski, Anna Nowak,"
        #when
        with patch('builtins.open', mock_open(read_data=file_content)):
            result=import_students(file_lista_studentow)
        #then
        assert result=={'Jan Kowalski': True, ' Anna Nowak': True}

    def test_import_students_fail(self):
        pass
class TestStudentsOperations:
    def test_add_student(self):
        # Given
        imie = "Jan Kowalski"
        students_list = {}

        # mockowanie funkcji open
        with patch("builtins.open", mock_open()) as mocked_file:
            # When
            result = add_student(students_list, imie)

        # Then
        expected = {"Jan Kowalski": True}
        assert result == expected
        # mocked_file.assert_called_once_with(file_lista_studentow, "a")  # Sprawdzenie, czy plik został otwarty w trybie dopisania

    def test_remove_student(self):
        #given
        file_lista_studentow = "students.txt"
        students_list = {"Jan Kowalski": True, "Damian Szymczyk":True}
        imie = "Damian Szymczyk"

        #when
        with patch("builtins.open", mock_open()) as mocked_file:
            remove_student(file_lista_studentow,students_list,imie)

        #then
        assert "Damian Szymczyk" not in students_list
class TestExportStudents:
    def test_export_students_with_mock(self):
        # Mockowanie otwierania pliku w trybie zapisu
        students_list = {"Jan Kowalski - obecny\n", "Anna Nowak - nieobecny\n"}
        with patch("builtins.open", mock_open()) as mock_file:
            # Eksportowanie studentów do pliku
            export_students("studentsAttendance.txt",students_list)

        # Sprawdzenie, czy plik został otwarty w trybie zapisu
        mock_file.assert_called_once_with("studentsAttendance.txt", "a")

        # Sprawdzenie, czy zawartość została zapisana poprawnie
        handle = mock_file()
        handle.write.assert_any_call("Jan Kowalski - obecny\n")
        handle.write.assert_any_call("Anna Nowak - nieobecny\n")



