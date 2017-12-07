import re
from collections import Counter



class TreeNode(object):
    def __init__(self, node):
        self.node = node
        self.weight = None
        self.parent = None
        self.children = []


    def __str__(self):
        return "<N:{n}->P:{p}>".format(n=self.node, p=self.parent)


    def tower_weight(self):
        return self.weight + sum(c.tower_weight() for c in self.children)


    def towers_balanced(self):
        weights = [c.tower_weight() for c in self.children]
        if len(set(weights)) <= 1:
            # if all weights are equal or we have no children
            return

        # otherwise, we find the culprit child
        weight_bag = Counter(weights)
        bad_weight = weight_bag.most_common()[-1][0]
        bad_child = self.children[weights.index(bad_weight)]
        
        bad_child.towers_balanced()
        
        should_have = weight_bag.most_common(1)[0][0]
        difference = bad_weight - should_have
        raise SolutionFound("Child %s should have weight %s"%(
            bad_child.node, bad_child.weight-difference))




class SolutionFound(Exception):
    """Rasied when a solution to part2 is found"""


def main():
    all_nodes = {} # maps node names to pointers to their object
    with open("d7.in") as f:
        for l in f:
            m = re.match("([a-z]+) \(([0-9]+)\)( -> ([a-z]+,? ?)+)?", l.strip())
            node = m.group(1)
            weight = m.group(2)
            
            if node not in all_nodes:
                # if this is the first time we see this name, we add it
                all_nodes[node] = TreeNode(node)
            all_nodes[node].weight = int(weight)

            if not m.group(3):
                # we are given no child information, so we are done
                continue
            
            for c in m.group(3).strip(" -> ").split(", "):
                if c not in all_nodes:
                    all_nodes[c] = TreeNode(c)
                # we set the parent of c to be node
                all_nodes[c].parent = all_nodes[node]

                # we c to be one of nodes children
                all_nodes[node].children.append(all_nodes[c])
    
    n = list(all_nodes.values())[0]
    while n.parent:
        n = n.parent
    print("Part1:", n.node)

    try: print(n.towers_balanced())
    except SolutionFound as s: print("Part2", s)

if __name__ == "__main__":
    main()