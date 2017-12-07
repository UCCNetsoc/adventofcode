import re



class TreeNode(object):
    def __init__(self, node):
        self.node = node
        self.weight = None
        self.parent = None


    def __str__(self):
        return "<N:{n}->P:{p}>".format(n=self.node, p=self.parent)


def part1():
    all_nodes = {} # maps node names to pointers to their object
    with open("d7.in") as f:
        for l in f:
            m = re.match("([a-z]+) \(([0-9]+)\)( -> ([a-z]+,? ?)+)?", l.strip())
            node = m.group(1)
            weight = m.group(2)
            
            if node not in all_nodes:
                # if this is the first time we see this name, we add it
                all_nodes[node] = TreeNode(node)
            all_nodes[node].weight = weight

            if not m.group(3):
                # we are given no child information, so we are done
                continue
            
            for c in m.group(3).strip(" -> ").split(", "):
                if c not in all_nodes:
                    all_nodes[c] = TreeNode(c)
                # we set the parent of c to be node
                all_nodes[c].parent = all_nodes[node]
    
    n = list(all_nodes.values())[0]
    while n.parent:
        n = n.parent
    print(n.node)

if __name__ == "__main__":
    part1()