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
    job_graph = JobGraph(jobs, deps)    
    return get_jobs_order(job_graph)
    
def get_jobs_order(job_graph):
    jobs_order = []
    for job in job_graph.nodes:
        cycle_found = dfs_traverse(job_graph, job, jobs_order)
        if cycle_found:
            return []
    
    return jobs_order

def dfs_traverse(job_graph, job, jobs_order):    
    if job.visited:
        return False
    if job.visiting:
        return True
    job.visiting = True
    for req in job.prereq:
        cycle_found = dfs_traverse(job_graph, req, jobs_order)
        if cycle_found:
            return True
    jobs_order.append(job.name)
    job.visited = True
    job.visiting = False
    return False


class JobGraph:

    def __init__(self, jobs, deps):
        self.graph = {}
        self.nodes = []
        for job in jobs:
            self.add_node(job)
        self.add_dependencies(deps)
    
    def add_dependencies(self, deps):
        for prereq, job in deps:
            job_node = self.get_node(job)
            prereq_node = self.get_node(prereq)
            job_node.prereq.append(prereq_node)
        
    def get_node(self, job):
        if job not in self.graph:
            self.add_node(job)
        return self.graph[job]
        
    def add_node(self, job):
        node = Job(job)
        self.nodes.append(node)
        self.graph[job] = node
                
        
class Job:

    def __init__(self, job):
        self.name = job
        self.prereq = []
        self.visited = False
        self.visiting = False

# test

jobs = [1, 2, 3, 4]
deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]

result = topological_sort(jobs, deps)
assert result == [1, 4, 3, 2] or result == [4, 1, 3, 2]
print("Ok")


