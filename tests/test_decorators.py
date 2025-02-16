from src.decorators import log


def test_decorators_1(capsys):

    @log(filename=None)
    def my_function(x, y):
        return x / y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok" + "\n"


def test_decorators_2(capsys):
    @log(filename=None)
    def my_function(x, y):
        return x / y

    my_function(1, 0)
    out, err = capsys.readouterr()
    assert "my_function error: division by zero. Inputs: (1, 0), {}\n" == out
