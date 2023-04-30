# This sys library is used for importing runtime python libs
import sys
"""
It lets us access system-specific parameters and functions.
This function provides the name of the existing python modules
which have been imported.
"""
def HeuristicFileInfo(file):## we define heuristic file
    for h in file:
        if h.lower() == "end of input":
            break ##we break the function if the h.lower is equal to end of input.
        else:
            record = h.split(" ")
            Heury[CityList.index(record[0])] = float(record[1])
    return

def CheckVisited(ExistingNode, VistedList):## we will check the visited node and exixting node
    for node in VistedList:## we check if the node is present in visitedlist or not.
        if ExistingNode == node["slave"]:##we made slave if the node is in existing node.
            return True## if present then its true.
    return False## if no then return false.

"""
pathfinding algorithm uses a heuristic to find the shortest path in a graph.
"""

def findingHeuristic(FinalNode, VisitedList):## we define the  finindingheurictic with finalnode and visitednode.

    route = []## the route is the path way that we are connecting cities from one city to  another.

    def tracing(FinalNode, VisitedList):##tracing the path between the destination city and already visited city.
        if FinalNode is None:## check if there is any finalnode.if not it will return
            return
        else:
            for visited_node in VisitedList:## if a  visited node  is present in  visitedlist.
                if visited_node["slave"] == FinalNode:##slave is the child node to visited from  previous city.
                    route.append(FinalNode)##it neeed to append the finalnode for continue path.
                    tracing(visited_node["master"], VisitedList)"""it  will trace the visitednode
                     of masternode='which is the  previous NodesExpanded """

    if FinalNode:## if  it the final node .
        print ("distance: " + str(FinalNode["Karchu"]) + " km")## it need to print the distance + coast + miles or km.
        print ("route:")## print the route between the starting node and destination node or city.
        tracing(FinalNode["Youngster"], VisitedList)## it need to  trace t he path between the visitedcity  and final city.
        route.reverse()## once  it visited the city and also need to check the reverse  coast form a to b  and b to a.
        for i in range(0, len(route) - 1):## lets  take the range.
            print (CityList[route[i]] + " to " + CityList[route[i+1]] + ", " + str(GivenGraph[route[i]][route[i+1]]) + " km")
        print("\n")
    else:
        print ("distance: infinity")## will print the distance,infinity,route.
        print ("route:")
        print ("No route found \n" )
    return## will return untill  it  reach the lastnode.

def generatingMap(file):##definig  the generatingMap og the graph.
    for line in file:## will start the with first node of the list .
        if line.lower() == "end of input":## it should be  starting value if less than starting value
            break## it should be break.
        else:
            curr_line = line.strip().split(" ")##curr_line is the present value.
            source_city = curr_line[0]##source_city is the starting city.
            destination_city = curr_line[1]##is to reach the destination_city
            if source_city not in CityList :
                CityList.append(source_city)## if not in the list we need to append the city
            if destination_city not in CityList:## if there is no destination_city then it need to append the list.
                CityList.append(destination_city)

    CityList.sort()## it  is the list with city names.
    for _ in range(len(CityList)):## we take the length of the city .
        GivenGraph.append([])## so we need to append the given graph.
        for __ in range(len(CityList)):## to know the range and length of the city.
            GivenGraph[_].append(-1) ## it should be less than the range.
        GivenGraph[_][_] = 0

    for line in file:##is given input file.
        if line.lower() == "end of input":## it should be the starting city.
            break
        else:
            curr_line = line.strip().split(" ")## curr_line is the current line.
            source_city = curr_line[0]## the curr_line is the source_city.
            destination_city = curr_line[1]## is the final destination city.
            distance = curr_line[2] ## it is the distanve between the source_city and destination_city.
            GivenGraph[CityList.index(source_city)][CityList.index(destination_city)] = float(distance)
            GivenGraph[CityList.index(destination_city)][CityList.index(source_city)] = float(distance)

    return


def TripInfo():##the info is  about the trip  between the  source_city and destination_city.
    BeginCity = CityList.index(destination)## is the begin city.
    Heuristic = []## the list  with  visited city  to the list.
    VistedList = []## is the list with already visitedcity
    FinalNode = False## is the finalnode.
    NodesGenerated = 0
    NodesExpanded = 0
    Heuristic.append({
        "Youngster"      : CityList.index(source),##  is
        "Karchu"  : 0,## the coast that spent for the grph
        "Gangster"           : None ## it  is the parentnode to the Youngster.
    })
    NodesGenerated +=1## incrementing the NodesGenerated

    while(len(Heuristic) > 0):##the length of the heuristic list should be less than heuristic.
        NodesExpanded = NodesExpanded + 1## NodesExpanded in increment
        if Heuristic[0]["Youngster"] == BeginCity:##  the Youngster should be BeginCity.
            VistedList.append({
                "slave"  : Heuristic[0]["Youngster"],
                "master": Heuristic[0]["Gangster"]
            })
            FinalNode = Heuristic[0]
            break
        elif CheckVisited(Heuristic[0]["Youngster"], VistedList):## the heuristic is* Youngster.
            del Heuristic[0]
            continue## it need to continue.
        else:
            VistedList.append({
                "slave"  : Heuristic[0]["Youngster"],
                "master": Heuristic[0]["Gangster"]
            })
            for i in range(len(GivenGraph[Heuristic[0]["Youngster"]])):## the i in range of heuristic.
                if GivenGraph[Heuristic[0]["Youngster"]][i] > 0:
                    Heuristic.append({
                        "Youngster": i,##  i in the Youngster
                        "Karchu": Heuristic[0]["Karchu"]+GivenGraph[Heuristic[0]["Youngster"]][i],
                        "Gangster": Heuristic[0]["Youngster"]
                    })## it checks the  city.
                    NodesGenerated += 1
            del Heuristic[0]## it delete the heuristic[0] if it greater than 1.
            if(len(Heuristic) > 1):
                Heuristic.sort(key=lambda x: x.get('Karchu'))


    print("Nodes Expanded: " + str(NodesExpanded)) ## it should be added the NodesExpanded +str(NodesExpanded)
    print("Nodes Generated: " + str(NodesGenerated))
    findingHeuristic(FinalNode, VistedList)## this is the finalnode and the visitednode.
    return
def GraphProcess():## it defining the GraphProcess
    BeginCity = CityList.index(destination) ##it is the starting city
    Heuristic = [] ## it adds the  city to  heuristic list
    VistedList = [] ##  the list the visited city.
    FinalNode = False ## it is the finalnode of the city.
    NodesGenerated = 0## the generated nodes
    NodesExpanded = 0## the expanded nodes
    Heuristic.append({
        "Youngster"      : CityList.index(source),
        "Karchu"  : 0,## it is the coast of the  distance between the city  from one city to another.
        "HeuristicCost"    : Heury[CityList.index(source)],
        "Gangster"            : None
    })
    NodesGenerated +=1
    while(len(Heuristic) > 0):## the length of the heuristic is >0.
        NodesExpanded = NodesExpanded + 1## it is to increament  the NodesExpanded list.
        if Heuristic[0]["Youngster"] == BeginCity:## the begincity = heuristic[0] value and the Youngster.
            VistedList.append({
                "slave"  : Heuristic[0]["Youngster"],
                "master": Heuristic[0]["Gangster"]
            })
            FinalNode = Heuristic[0]
            break ## it break  if the finalnode is equal to heuristic.
        elif CheckVisited(Heuristic[0]["Youngster"], VistedList):
            del Heuristic[0]##del if the heuristic value is 0.
            continue
        else:
            VistedList.append({
                "slave"  : Heuristic[0]["Youngster"],
                "master": Heuristic[0]["Gangster"]## it is  to append the  slavevalue and mastervalue.
            })
            for i in range(len(GivenGraph[Heuristic[0]["Youngster"]])):
                if GivenGraph[Heuristic[0]["Youngster"]][i] > 0:
                    Heuristic.append({
                        "Youngster": i,
                        "Karchu": Heuristic[0]["Karchu"]+GivenGraph[Heuristic[0]["Youngster"]][i],
                        "HeuristicCost": Heury[i],
                        "Gangster": Heuristic[0]["Youngster"]
                    })## the heuristic value  append the Youngster,karchu,heuristic and Gangster.
                    NodesGenerated += 1## it is to increament NodesGenerated
            del Heuristic[0]## it del the heuristic[0]
            if(len(Heuristic) > 1):
                Heuristic.sort(key=lambda x: (x.get('Karchu')+ x.get('HeuristicCost')))
    print("Nodes Expanded: " + str(NodesExpanded))## it prints the value .
    print("Nodes Generated: " + str(NodesGenerated))
    findingHeuristic(FinalNode, VistedList)## the finalnode and visitedlist.
    return

if len(sys.argv) >= 4:
    GivenGraph = []## it is the GivenGraph
    CityList = []## citylist
    generatingMap(open(sys.argv[1], "r").read().split("\n"))
    source= sys.argv[2]
    destination= sys.argv[3]
    if len(sys.argv) == 4:
        TripInfo()## it is the list containing the trip info.
    elif len(sys.argv) == 5:
            Heury = [0] * len(CityList)## the  length of the CityList *0.
            HeuristicFileInfo(open(sys.argv[4], "r").read().split("\n"))## it is the HeuristicFileInfo.
            GraphProcess()
    else:
        print ("Input is not matching with requirements.")## print not matching with requirements.
else:
    print ("Input is not matching with requirements.")## print the not matching with expression as target:
        pass
