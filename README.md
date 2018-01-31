# GraphMatchings

**GS** contains class to apply Gale-Shapley to the Stable Marriage problem.  In this problem, we match *N* men to *N* women, optimizing for male preferences (technically, we optimize for preferences of the left-hand-side of our bipartite graph -- the male-female categorization is a historical artifact), such that, at completion, each man is matched to one woman, and each woman to one man, with no two or more men or women mapping to the same parter.

**NRM**  contains class to apply variant of the Gale-Shapley algorithm to the National Resident Matching problem.  In this problem, we are matching *H* hospitals to *R* medical residents, where each hospital also has a limited number of positions available.  Again, we optimize for the rankings of the left-hand-side of our bipartite graph, meaning that hospitals will fare better than residents.

**In the works:**

 -- **Ford-Fulkerson**
 
 -- **Edmonds-Karp** -- the distinction between Ford-Fulkerson and Edmonds-Karp being that Edmonds-Karp is actually an algorithm in that it specifies *how* (via Breadth First Search) to find augmenting paths, while the means of finding augmenting paths in Ford-Fulkerson is left unspecified -- so, the Edmonds-Karp algorithm is a special instance of the Ford-Fulkerson method.
 
 -- **Hungarian Method**
 
I regularly use the **scipy.optimize.linear_sum_assignment** method for the purpose of cortical parcellation label matchings, where the cost matrix is defined by some measure of similarity.  While I could theoretically use my own future implementation to do this, I doubt  that my code will be as efficient as the scipy version.  This repository will probably only be used for learning purposes.
