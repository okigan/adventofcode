#! env python

from itertools import *
from functools import *
from collections import *

from collections import defaultdict
from heapq import * 

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def dijkstra(graph, source):
  # create a distance dictionary and set the distance to the source to 0
  dist = {source: 0}
  
  # create a priority queue for storing the unvisited vertices
  pq = []
  # add the source vertex to the priority queue with distance 0
  heappush(pq, (source, 0))
  
  # while the priority queue is not empty
  while pq:
    # select the unvisited vertex with the smallest distance
    current = heappop(pq)[0]
    
    # loop through each neighbor of the current vertex
    r, c = current
    children = set([(r + 1, c + 0), (r - 1, c + 0), (r + 0, c + 1), (r + 0, c - 1)])
    for neighbor in children.intersection(graph):

      # calculate the distance to the neighbor through the current vertex
      new_dist = dist[current] + 1
      
      # update the distance to the neighbor if it is smaller than the previous distance
      if neighbor not in dist or new_dist < dist[neighbor]:
        dist[neighbor] = new_dist
        # add the neighbor to the priority queue with its updated distance
        heappush(pq, (neighbor, new_dist))
        
  # return the calculated distances
  return dist


    

def main():
    aaa = []

    starts = []
    start = None
    end = None
    maze = {}
    with open(dir_path + "/input.txt") as f:
        count = 0
        for line in f.readlines():
            line = line.strip()
            for idx, c in enumerate(line):
                maze[(count, idx)] = c
                if c == 'S':
                    start = (count, idx)
                    maze[(count, idx)] = 'a'
                    starts += [((count, idx))]
                elif c == 'E':
                    end = (count, idx)
                    maze[(count, idx)] = 'z'
                elif c == 'a':
                    starts += [((count, idx))]


            count += 1

    # print(maze)

    q = []
    visited = {}
    heappush(q, (0, start))
    while q:
        depth, current = heappop(q)
        if current == end:
            # print("found", current, depth)
            print(depth)
            break

        visited[current] = depth

        r, c = current
        children = [(r + 1, c + 0), (r - 1, c + 0), (r + 0, c + 1), (r + 0, c - 1)]
        for child in children:
            if child in maze:
                if child not in visited or visited[child] > depth:
                    if ord(maze[child]) - ord(maze[current]) < 7:
                        heappush(q, (depth + 1, child))




if __name__ == "__main__":
    main()