graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : ['A', 'B'],
  'E' : ['F'],
  'F' : ['F', 'C'],
  'G' : ['C', 'E'],
  'H' : ['A', 'F']
}

visitedBFS = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
visitedDFS = set() # Set to keep track of visited nodes.


def bfs(visitedBFS, graph, node):
  visitedBFS.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visitedBFS:
        visitedBFS.append(neighbour)
        queue.append(neighbour)

def dfs(visitedDFS, graph, node):
    if node not in visitedDFS:
        print (node)
        visitedDFS.add(node)
        for neighbour in graph[node]:
            dfs(visitedDFS, graph, neighbour)


inputBFS = input("Enter a letter between A and H (BFS): \n")
bfs(visitedBFS, graph, inputBFS)

print() #only to break a line

inputDFS = input("Enter a letter between A and H (DFS): \n")
dfs(visitedDFS, graph, 'A')