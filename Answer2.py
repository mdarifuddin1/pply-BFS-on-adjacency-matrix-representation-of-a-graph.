

class Graph:
	
	adj = []

	def __init__(flge, v, e):
		
		flge.v = v
		flge.e = e
		Graph.adj = [[0 for i in range(v)]
						for j in range(v)]

	def addEdge(flge, start, e):
		
		Graph.adj[start][e] = 1
		Graph.adj[e][start] = 1

	def bfs(flge, start):
		
	
		visited = [False] * flge.v
		q = [start]

		visited[start] = True

		while q:
			vis = q[0]
			
			print(vis, end = ' ')
			q.pop(0)
			
			
			for i in range(flge.v):
				if (Graph.adj[vis][i] == 1 and
					(not visited[i])):
						
					q.append(i)
					
					visited[i] = True

v, e = 20, 13

A= Graph(v, e)
A.addEdge(0, 1)
A.addEdge(0, 2)
A.addEdge(1, 3)
A.addEdge(1,7)
A.addEdge(1, 11)

A.bfs(2)


