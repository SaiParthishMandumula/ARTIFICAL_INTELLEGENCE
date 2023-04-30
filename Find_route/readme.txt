Name: Sai Parthish Mandumula.
UTA ID: 1002022847.

Task is solved using python 3.7.9. No external is  installation required.


Construction of the code is as follow:

generatingMap -> This function will create a 2d matrix of input1.txt file where index is city name and the  coordinates are distance.

HeuristicFileInfo -> This function is used to find Uniform Cost Search(UCS) in which fringe and the closed set is created.

CheckVisited-> This function checks if the current fringe is already in closed set or not.

GraphProcess-> This function will store heuristic value provided by h_kassel.txt or any other heuristic.txt file.

 TripInfo -> This function is used for A* search in which fringe and closed set is created.

findingHeuristic-> This function returns the optimal path created by either or the method.

tracing-> This function backtrack the goal state till start state.


Instructions to run the code:-

1.Uninformed search

	>find_route.py input1.txt Berlin Kassel
OR      >find_route.py [Argument input_filename] [source_cityname] [destination_cityname]

2.Informed search

	>find_route.py input1.txt Berlin Kassel h_kassel.txt
OR      >find_route.py [Argument input_filename] [source_cityname] [destination_cityname] [heuristicValue_filename]
