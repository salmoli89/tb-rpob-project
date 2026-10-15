import csv
import requests
import networkx as nx

genes = ["rpoB", "katG", "inhA", "gyrA", "gyrB", "embB", "pncA", "rpsL"]

# STRING database theke interaction anbe (83332 = M. tuberculosis H37Rv)
url = "https://string-db.org/api/tsv/network"
data = {"identifiers": "\r".join(genes), "species": 83332}
response = requests.post(url, data=data)

rows = csv.DictReader(response.text.splitlines(), delimiter="\t")
G = nx.Graph()
for row in rows:
    G.add_edge(row["preferredName_A"], row["preferredName_B"])

print("Nodes:", G.number_of_nodes(), "Edges:", G.number_of_edges())

# Degree centrality diye hub protein rank
centrality = nx.degree_centrality(G)
ranking = sorted(centrality.items(), key=lambda x: x[1], reverse=True)

for gene, score in ranking:
    print(gene, round(score, 3))

with open("hub_ranking.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["gene", "degree_centrality"])
    writer.writerows(ranking)
