from src.pre_built.counter import count_ocurrences
PATH = 'data/jobs.csv'


def test_counter():
    jobs_javascript = count_ocurrences(PATH, 'Javascript')
    jobs_typescript = count_ocurrences(PATH, 'Typescript')
    jobs_python = count_ocurrences(PATH, 'Python')
    jobs_java = count_ocurrences(PATH, 'Java')

    assert jobs_javascript == 122
    assert jobs_typescript == 4
    assert jobs_python == 1639
    assert jobs_java == 676
