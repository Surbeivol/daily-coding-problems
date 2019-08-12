"""
You are given a list of arbitrary jobs that need to be completed; these jobs
are represented by integers. You are also given a list of dependecies. A
dependecy is represented as a pair of jobs where the first job is prerequisite
of the second one. In other words, the second job depends on the first one; it
can only be completed once the first job is completed. Write a function that
takes in a list of jobs and a list of dependencies and returns  a list
containing a valid order in which the given jobs can be completed. If no such
order exists, the function should return an empty list.
"""


def topological_sort(jobs, deps):
    pass


# test

jobs = [1, 2, 3, 4]
deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]

result = topological_sort(jobs, deps)
assert result == [1, 4, 3, 2] or result == [4, 1, 3, 2]
print("Ok")


