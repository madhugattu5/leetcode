class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        barriers = SortedList()  
        barriers.add(0)  

        for query in queries:
            if query[0] == 1:
                it = query[1]
                barriers.add(it)

        holes = SortedList()  
        holes.add(float('inf'))  
        hole2start = {float('inf'): barriers[-1]}

        for pos in range(len(barriers) - 1):
            start = barriers[pos]
            end = barriers[pos + 1]
            size = end - start
            if size:
                pos = holes.bisect_left(size)
                hole_size = holes[pos]
                if hole2start[hole_size] > start:
                    if hole_size > size:
                        holes.add(size)
                    hole2start[size] = start

        barriers.add(float('inf'))  
        result = []
        
        for query in reversed(queries):
            if query[0] == 1:  
                it = query[1]
                pos = barriers.bisect_left(it)
                left = barriers[pos - 1]
                right = barriers[pos + 1]
                size = right - left

                hole_pos = holes.bisect_left(size)
                if hole2start[holes[hole_pos]] > left:
                    while hole_pos > 0 and hole2start[holes[hole_pos - 1]] > left:
                        del hole2start[holes[hole_pos - 1]]
                        del holes[hole_pos - 1]
                        hole_pos -= 1

                    hole2start[size] = left
                    if holes[hole_pos] != size:
                        holes.add(size)

                barriers.remove(it)
            else:  
                _, start, size = query
                hole_pos = holes.bisect_left(size)
                hole = holes[hole_pos]
                result.append(hole2start[hole] <= start - size)

        result.reverse()  

        return result