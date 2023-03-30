from src.pre_built.sorting import sort_by

jobs = [
    {"max_salary": 2500, "min_salary": 500, "date_posted": "2023-03-01"},
    {"max_salary": 5000, "min_salary": 2000, "date_posted": "2023-03-02"},
    {"max_salary": 10000, "min_salary": 5000, "date_posted": "2023-03-03"},
    {"max_salary": 20000, "min_salary": 7000, "date_posted": "2023-03-04"}
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == [
        {"max_salary": 2500, "min_salary": 500, "date_posted": "2023-03-01"},
        {"max_salary": 5000, "min_salary": 2000, "date_posted": "2023-03-02"},
        {"max_salary": 10000, "min_salary": 5000, "date_posted": "2023-03-03"},
        {"max_salary": 20000, "min_salary": 7000, "date_posted": "2023-03-04"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"max_salary": 20000, "min_salary": 7000, "date_posted": "2023-03-04"},
        {"max_salary": 10000, "min_salary": 5000, "date_posted": "2023-03-03"},
        {"max_salary": 5000, "min_salary": 2000, "date_posted": "2023-03-02"},
        {"max_salary": 2500, "min_salary": 500, "date_posted": "2023-03-01"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"max_salary": 20000, "min_salary": 7000, "date_posted": "2023-03-04"},
        {"max_salary": 10000, "min_salary": 5000, "date_posted": "2023-03-03"},
        {"max_salary": 5000, "min_salary": 2000, "date_posted": "2023-03-02"},
        {"max_salary": 2500, "min_salary": 500, "date_posted": "2023-03-01"},
    ]
