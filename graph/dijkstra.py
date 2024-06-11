# Dijkstra 算法模板
# 返回从 start 到每个点的最短路
def dijkstra(self, graph: List[Tuple[int]], start: int) -> List[int]:
        dist = [inf] * len(graph)
        dist[start] = 0
        h = [(0, start)]
        while h:
            d, x = heappop(h)
            if d > dist[x]:
                continue
            for y, wt in graph[x]:
                new_d = d + wt
                if new_d < dist[y]:
                    dist[y] = new_d
                    heappush(h, (new_d, y))
        return dist
