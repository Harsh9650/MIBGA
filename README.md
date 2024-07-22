# MIBGA
MultiPath Island Based Genetic Algorithm

This repository provides the results that we used to formulate the experimental analysis section in our study. Each directory consists

1) sp.xlsx providing the length of the shortest path achieved using Dijkstra's algorithm, GA by C.ahn, and MIBGA for all test case (50 on each network).
2) state_gap.xlsx providing Gap (%) for both GAs were calcuated using the length of the shortest path from the Dijkstra's algorithm.
3) state_eva.xlsx, providing the total, and unique evaluations performed by MIBGA and the GA by C.ahn.
4) state_cd.xlsx, providing the convergence achieved by MIBGA and the GA by C.ahn on each test case. It is provided as percentage (%) and calculated as ((X-Y)/Y)*100 where X and Y are the length of the shortest path in the first generation and the final generation of the GA, respectively. Convergence distance (%) of 0 and -ve value, show the shortest path was found in the first generation and the shortest path in the final generation was longer than the shortest path in the first generation, respectively.
5) state_time.xlsx providing the computation time on each test case by Dijkstra's algorithm, GA by C.ahn, and MIBGA.
