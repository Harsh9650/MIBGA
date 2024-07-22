import networkx as nx
import matplotlib.pyplot as plt


# This is the file to create a graph from the dataset created using an ESRI shapefile.

def creating_graph(nodes, edges):
    """
    This is a simple function that takes 2 lists:
    1) nodes: list of nodes and that can be with or without positions.
    2) edges: List of connections and with their respective weights.
    """
    a = nx.Graph()
    a.add_nodes_from(nodes)
    a.add_edges_from(edges)
    return a


def uniquenodes(dataset):
    nodes = []
    hashNodes = {}
    intCounter = 0
    intNodeCounter = 0
    uniqueNodes = []
    for index, row in dataset.iterrows():
        start_point = (intCounter, {'pos':(row["startnode_x"], row["startnode_y"])})
        strKey = str(row["startnode_x"]) + "|" + str(row["startnode_y"])
        if strKey not in hashNodes:
            hashNodes[strKey]  = (intNodeCounter, {'pos':(row["startnode_x"], row["startnode_y"])})
            intNodeCounter += 1
            uniqueNodes.append(hashNodes[strKey])
        nodes.append(start_point)
        intCounter += 1
        end_point = (intCounter, {'pos':(row["endnode_x"], row["endnode_y"])})
        strKey = str(row["endnode_x"]) + "|" + str(row["endnode_y"])
        
        if strKey not in hashNodes:
            hashNodes[strKey]  = (intNodeCounter, {'pos':(row["endnode_x"], row["endnode_y"])})
            intNodeCounter += 1
            uniqueNodes.append(hashNodes[strKey])
            #hashNodes[strKey] += 1

        nodes.append(end_point)
        intCounter += 1
    return uniqueNodes, hashNodes


def edges(dataset, hashNodes):
    edges_in_graph = []
    for index, row in dataset.iterrows():
        start_point = str(row["startnode_x"]) + "|" + str(row["startnode_y"])
        end_point = str(row["endnode_x"]) + "|" + str(row["endnode_y"])
        if start_point != end_point:
            connection = (hashNodes[start_point][0], hashNodes[end_point][0], {"weight": row["distance"] })
            edges_in_graph.append(connection)
    return edges_in_graph


def topological_database(graph):
    nodes_with_connection = {}
    total_number_nodes = nx.Graph.number_of_nodes(graph)
    connection_nodes = list(nx.get_edge_attributes(graph, 'weight').keys())
    for i in range(total_number_nodes):
        connections = list(graph.adj[i])
        details = {}
        for j in connections:
            if (i,j) in connection_nodes:
                details[j] = nx.get_edge_attributes(graph, 'weight')[(i,j)]
            else:
                details[j] = nx.get_edge_attributes(graph, 'weight')[(j,i)]
        nodes_with_connection[i] = details
    return nodes_with_connection


def graph_networkx(dataset, plt_size, node_size):
    uniqueNodes, hashNodes = uniquenodes(dataset)
    edges_in_graph = edges(dataset, hashNodes)
    graph_network = creating_graph(uniqueNodes, edges_in_graph)
    plt.figure(figsize= plt_size)
    nx.draw(graph_network, nx.get_node_attributes(graph_network, 'pos') , with_labels = False, node_size = node_size)
    plt.show()
    return graph_network
