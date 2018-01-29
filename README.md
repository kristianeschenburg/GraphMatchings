# StableMarriage

**GS** contains class to apply Gale-Shapley to the Stable Marriage problem.  In this problem, we match *N* men to *N* women, optimizing for male preferences (nominally -- technically we optimize for preferences of the left-hand-side of our bipartite graph), such that, at completion, each man is matched to one woman, and each woman to one man, and no two men or women can map to the same partner.

**NRM**  contains class to apply variant of the Gale-Shapley algorithm to the National Resident Matching problem.  In this problem, we are matching *H* hospitals to *R* medical residents, where each hospital also has a limited number of positions available.  Again, we optimize for the rankings of the left-hand-side of our graph, which in this case can be non-bipartite if each hospital has more than 1 position available.
