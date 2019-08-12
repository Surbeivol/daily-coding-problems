"""
You are given three inputs, all of which are instances of a class that have an
"ancestor" property pointing to their youngest ancestor. The first input is the
top ancestor in an ancestral tree(i.e. the only instance that has no ancestor),
and the other two inputs are descendants in the ancestral tree. Write a
functions that returns the youngest common ancestor to the two descendants.

for input Node A, Node E, Node I from this ancestral
        A
      /  \
     B    C
    / \  / \
   D   EF   G
  / \
 H   I

 Returns node B
"""

def get_youngest_common_ancestor(top_ancestor, descendant_one, descendant_two):
    depth_one = get_depth(descendant_one, top_ancestor)
    depth_two = get_depth(descendant_two, top_ancestor)

    if depth_one < depth_two:
        return backtrack(descendant_two,
                         descendant_one,
                         top_ancestor,
                         depth_two - depth_one)
    else:
        return backtrack(descendant_one,
                         descendant_two,
                         top_ancestor,
                         depth_one - depth_two)

def get_depth(descendant, top_ancestor):
    depth = 0
    while descendant != top_ancestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

def backtrack(descendant_lower, descendant_higher, top_ancestor, diff):
    while diff > 0:
        descendant_lower = descendant_lower.ancestor
        diff -= 1

    while descendant_lower != descendant_higher:
        descendant_lower = descendant_lower.ancestor
        descendant_higher = descendant_higher.ancestor
        if descendant_lower == top_ancestor and descendant_lower != descendant_higher:
            return None

        return descendant_lower
