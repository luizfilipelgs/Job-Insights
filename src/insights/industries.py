from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    unique_industries = []

    for ind in data:
        if "" != ind["industry"] not in unique_industries:
            unique_industries.append(ind["industry"])
    print(unique_industries)
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_filtered = [job for job in jobs if job['industry'] == industry]
    return jobs_filtered
