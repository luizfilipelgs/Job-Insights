from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, "r") as doc_csv:
            doc_reader = list(csv.DictReader(doc_csv))
            return doc_reader
    except FileNotFoundError:
        print('Arquivo não encontrado')


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    uniques_types = []
    for job in jobs:
        if job["job_type"] not in uniques_types:
            uniques_types.append(job["job_type"])
    return uniques_types



def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
