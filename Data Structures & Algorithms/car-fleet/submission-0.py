class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a hashset arrival
        arrival = set()

        # get length of positions
        # for car in range(len(position))
        for car in range(len(position)):
            # get position of car
            pos = position[car]
            # get speed of car
            spd = speed[car]

            # arrival.add((target -position)//speed)
            value = (pos/spd)
            arrival.add((target-position[car])//speed[car])
        # return len(arrival)
        print(arrival)
        return len(arrival)
