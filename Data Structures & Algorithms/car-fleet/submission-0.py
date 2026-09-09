class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [] # [position, speed]
        for i in range(n):
            cars.append([position[i], speed[i]])
        
        cars = sorted(cars, reverse=True)

        res = n
        pret = 0
        for i in range(n):
            t = float(target - cars[i][0]) / float(cars[i][1])
            if t <= pret:
                res -= 1
            else:
                pret = t
                
        return res