import networkx as nx
from edge_betweenness__girvan_newman import edge_betweenness
from load_custom_graph import load_custom_graph


def girvan_newman_algorithm(G):
    # Khởi tạo danh sách các cạnh và betweenness centrality của chúng
    edges = list(G.edges())
    betweenness = edge_betweenness(G)

    # Khởi tạo danh sách các cụm (cluster) ban đầu
    clusters = list(nx.connected_components(G))

    # Duyệt qua các cạnh trong đồ thị theo thứ tự giảm dần của betweenness centrality
    while edges:
        edges.sort(key=lambda e: betweenness[e], reverse=True)
        e = edges.pop(0)

        # Xóa cạnh vừa tìm được
        G.remove_edge(*e)

        # Tính lại danh sách các cụm (cluster)
        new_clusters = list(nx.connected_components(G))

        # Kiểm tra xem số lượng cụm (cluster) có thay đổi hay không
        if len(new_clusters) > len(clusters):
            clusters = new_clusters
        else:
            break

    return clusters


if __name__ == "__main__":
  # G = nx.barbell_graph(5, 0)
  G = load_custom_graph(2)
  print(girvan_newman_algorithm(G))
  print(*[community for community in nx.community.girvan_newman(G)])

# import networkx as nx
  
  
# def edge_to_remove(g):
    
#   d1 = nx.edge_betweenness_centrality(g)
#   list_of_tuples = list(d1.items())
    
#   sorted(list_of_tuples, key = lambda x:x[1], reverse = True)
    
#   # Will return in the form (a,b)
#   return list_of_tuples[0][0]
  
# def girvan(g):
#   a = nx.connected_components(g)
#   lena = len(list(a))
#   print (' The number of connected components are ', lena)
#   while (lena == 1):
  
#     # We need (a,b) instead of ((a,b))
#     u, v = edge_to_remove(g)
#     g.remove_edge(u, v) 
      
#     a = nx.connected_components(g)
#     lena=len(list(a))
#     print (' The number of connected components are ', lena)
  
#   return a
  
# # Driver Code
# g = nx.barbell_graph(5,0)
# a = girvan(g)
# print ('Barbell Graph')
  
# for i in a:
#   print (i.nodes())
#   print ('.............')
  
# g1 = nx.karate_club_graph()
# a1 = girvan(g1)
  
# print ('Karate Club Graph')
# for i in a1:
#   print (i.nodes())
#   print ('.............')


# if __name__ == "__main__":
#   from visualize_graph import visualize_graph
#   # visualize_graph(g)
#   visualize_graph(g1)