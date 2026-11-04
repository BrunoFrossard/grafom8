import networkx as nx

arestas = [
    (0, 1, 10), (0, 2, 17), (1, 2, 10), (1, 3, 12),
    (2, 4, 15), (2, 5, 14), (3, 4, 11), (3, 6, 16),
    (4, 5, 8), (4, 7, 17), (5, 7, 24), (6, 7, 13), (1, 4, 20)
]

G = nx.Graph()
G.add_weighted_edges_from(arestas)

matriz = nx.to_numpy_array(G, nodelist=range(8))
print(matriz)

rota = nx.dijkstra_path(G, 0, 7)
custo = nx.dijkstra_path_length(G, 0, 7)

print("Rota:", rota)
print("Custo:", custo, "km")

G.remove_edge(2, 4)

nova_rota = nx.dijkstra_path(G, 0, 7)
novo_custo = nx.dijkstra_path_length(G, 0, 7)

print("Nova rota:", nova_rota)
print("Novo custo:", novo_custo, "km")
print("Aumento:", novo_custo - custo, "km")

G.add_edge(2, 4, weight=15)

mst = nx.minimum_spanning_tree(G, algorithm="prim")
custo_mst = mst.size(weight="weight")

distancias = nx.single_source_dijkstra_path_length(G, 0)
soma_distancias = sum(distancias.values())

print("Custo MST:", custo_mst, "km")
print("Soma Dijkstra:", soma_distancias, "km")