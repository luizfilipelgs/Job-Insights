from src.pre_built.brazilian_jobs import read_brazilian_file

mock_en = {"title": "Maquinista", "salary": "2000", "type": "trainee"}
PATH = 'tests/mocks/brazilians_jobs.csv'


def test_brazilian_jobs():
    assert read_brazilian_file(PATH)[0] == mock_en
