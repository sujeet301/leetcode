class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter_id = [[-1] * n for _ in range(m)]

        sr = 0
        sc = 0
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr = r
                    sc = c
                elif classroom[r][c] == 'L':
                    litter_id[r][c] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        target = (1 << litter_count) - 1

        # best[cell][mask] = maximum energy reached
        # at this cell with this collected-litter mask
        best = [[-1] * (1 << litter_count) for _ in range(m * n)]

        start = sr * n + sc

        best[start][0] = energy

        # (cell, current_energy, mask)
        queue = [(start, energy, 0)]

        head = 0
        moves = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while head < len(queue):

            # Process one BFS level
            end = len(queue)

            while head < end:

                cell, current_energy, mask = queue[head]
                head += 1

                r = cell // n
                c = cell % n

                if mask == target:
                    return moves

                if current_energy == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    new_energy = current_energy - 1
                    new_mask = mask

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # Collect litter
                    elif classroom[nr][nc] == 'L':
                        bit = litter_id[nr][nc]
                        new_mask = mask | (1 << bit)

                    new_cell = nr * n + nc

                    # If we have already reached this state
                    # with equal or greater energy, this state
                    # can never be better.
                    if new_energy <= best[new_cell][new_mask]:
                        continue

                    best[new_cell][new_mask] = new_energy

                    queue.append(
                        (new_cell, new_energy, new_mask)
                    )

            moves += 1

        return -1