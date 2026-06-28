import pytest

from src.decorators import log


def test_log(capsys):
    """Тест декоратора на удачное выполнение без ошибок"""

    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    out, err = capsys.readouterr()
    assert result == 5
    assert "Ошибок нет" in out


def test_log_error(capsys):
    """Тест декоратора на ошибку"""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    out, err = capsys.readouterr()
    assert "Ошибка" in out


def test_log_to_file(tmp_path):
    """Тест декоратора на запись файла"""
    log_file = tmp_path / "test.log"
    filename = str(log_file)

    @log(filename=filename)
    def multiply(a, b):
        return a * b

    multiply(3, 4)
    content = log_file.read_text()
    assert "Ошибок нет" in content
