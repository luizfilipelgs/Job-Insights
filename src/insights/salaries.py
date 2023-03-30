from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary_list = [int(salary['max_salary']) for salary in data
                       if salary['max_salary'].isnumeric()]
    return max(max_salary_list)


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary_list = [int(salary['min_salary']) for salary in data
                       if salary['min_salary'].isnumeric()]
    return min(min_salary_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        salary = int(salary)
    except (KeyError, TypeError, ValueError):
        raise ValueError()
    if min_salary > max_salary:
        raise ValueError()
    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    jobs_filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered.append(job)
        except ValueError:
            print('entrada invalida')
    print(jobs_filtered)
    return jobs_filtered
