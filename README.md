# Graphs

Written originally with the intention of implementing graph mathching methods, but has grown into a larger library of graph algorithms.

In the course of my research, I regularly need to compute shortest paths on the brain surface (or in sub-graphs thereof) and apply label matching methods to match cortical regions across subjects.  While packages like **networkx** are already highly optimized for these problems, I thought it fruitful to begin implementing these methods on my own so that I can learn more about effective code optimization and general concepts in developing Python packages.

So far, contains classes and methods for:

-- **Breadth First Search** (bfs.py)

-- **Edmonds-Karp** (EdmondsKarp.py): algorithm for finding the maximum flow of a directed network by computing augmenting paths using Breadth First Search.

-- **Gale-Shapley** (GS.py): In this problem, we match *N* men to *N* women, optimizing for male preferences (technically, we optimize for preferences of the left-hand-side of our bipartite graph -- the male-female categorization is a historical artifact), such that, at completion, each man is matched to one woman, and each woman to one man, with no two or more men or women mapping to the same parter.

-- **National Resident Matching** (NM.py): Variant of Gale-Shapley algorithm, viewed from the perspective of matching hospitals to residents.  We are matching *H* hospitals to *R* medical residents, where each hospital also has a limited number of positions available to be filled.  We optimize for the rankings of the left-hand-side of our bipartite graph, meaning that hospitals will fare better than residents.
 
 To implement:
 
 -- **Hungarian Algorithm (Kuhn-Munkres)**: maximum-weighted bipartite matching algorithm
 
 -- **Blossom Algorithm**: generalized version of maximum-weighted matching of a graph, when the graph is not bipartite
