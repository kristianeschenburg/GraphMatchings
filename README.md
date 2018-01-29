# GraphMatchings

**GS** contains class to apply Gale-Shapley to the Stable Marriage problem.  In this problem, we match *N* men to *N* women, optimizing for male preferences (nominally -- technically we optimize for preferences of the left-hand-side of our bipartite graph), such that, at completion, each man is matched to one woman, and each woman to one man, and no two men or women can map to the same partner.

**NRM**  contains class to apply variant of the Gale-Shapley algorithm to the National Resident Matching problem.  In this problem, we are matching *H* hospitals to *R* medical residents, where each hospital also has a limited number of positions available.  Again, we optimize for the rankings of the left-hand-side of our graph, which in this case can be non-bipartite if each hospital has more than 1 position available.

**In the works:**

 -- Ford-Fulkerson for Maximum Bipartite Matching
 
 -- Hungarian Method for Maximum-Weighted Bipartite Matching
 
I regularly use the **scipy.optimize.linear_sum_assignment** method for the purpose of cortical parcellation label matchings, where the cost matrix is defined by various metrics.  While I could theoretically use my own future implementation to do this, I don't think that my code will be as efficient as the **scipy** version.  This repository will probably only be used for learning purposes.
