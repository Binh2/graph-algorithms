import networkx as nx


def edge_betweenness(G: nx.Graph | nx.DiGraph):
  between = { edge: 0.0 for edge in G.edges }
  edges = list(G.edges)
  for u in G.nodes:
    # print(u)
    flow_tree = nx.DiGraph()
    visited_nodes = [u]
    visited_edges = []
    queue = [u]
    flow_up_stack = [u]
    flow_down_node_features = { node: 0 for node in G.nodes }
    level_features = { node: 0 for node in G.nodes}
    flow_down_node_features[u] = 1
    while len(queue) > 0:
      u = queue.pop(0)
      for v in G[u]:
        edge = (u, v)
        if edge not in edges:
          edge = (v, u)
        if edge in visited_edges:
          continue
        visited_edges.append(edge)

        if level_features[v] == 0:
          level_features[v] = level_features[u] + 1

        # print(u, v, flow_down_node_features, level_features)
        if level_features[v] != level_features[u]:
          # print(level_features[u], level_features[v])
          flow_down_node_features[v] += flow_down_node_features[u]
        if v in visited_nodes:
          continue
        level_features[v] = level_features[u] + 1
        
        flow_tree.add_edge(v, u)
        visited_nodes.append(v)
        queue.append(v)
        flow_up_stack.append(v)

    
    flow_up_edge_features = { edge: 0 for edge in G.edges }
    flow_up_node_features = { node: 0 for node in G.nodes }
    visited_edges = []
    v = flow_up_stack.pop()
    while len(flow_up_stack) > 0:
      for w in G[v]:
        if level_features[v] == level_features[w]:
          continue

        edge = (v, w)
        if edge not in edges:
          edge = (w, v)
        
        if edge in visited_edges:
          continue
        visited_edges.append(edge)

        # is_leave = True
        # for i in flow_tree.predecessors(v):
        #   is_leave = False
        #   break
        
        # print(v, w, is_leave)
        # if is_leave:
        #   flow_up_edge_features[edge] = flow_down_node_features[v] / flow_down_node_features[w]
        # else:
        #   flow_up_edge_features[edge] = (1 + flow_down_node_features[v]) / flow_down_node_features[w]
        flow_up_edge_features[edge] = (1 + flow_up_node_features[v]) * flow_down_node_features[w] / flow_down_node_features[v]
        # print(v, w, "", flow_up_node_features[v], flow_down_node_features[v], flow_down_node_features[w], flow_up_edge_features[edge])
        flow_up_node_features[w] += flow_up_edge_features[edge]
          
        
        if type(G) == nx.Graph:
          between[edge] += flow_up_edge_features[edge] / 2
        else:
          between[edge] += flow_up_edge_features[edge]
      
      v = flow_up_stack.pop()

    
  #   print(flow_down_node_features)
  #   print(flow_up_edge_features)
  # print(between)
  return between
  

if __name__ == "__main__":
  # from load_custom_graph import load_custom_graph
  # print(edge_betweenness(load_custom_graph(3)))
  from load_custom_graph import load_custom_graph
  from visualize_graph import *
  G = load_custom_graph(2)
  visualize_edge_feature_graph(G, edge_betweenness(G))
