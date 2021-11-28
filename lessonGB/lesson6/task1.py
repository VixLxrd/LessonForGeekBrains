import time


class TrafficLight:
    __color: dict = {"Red": 7, "Yellow": 2, "Green": 5}

    def running(self):
        while True:
            for k in self.__color.keys():
                print(f"Цвет световора : {k}")
                time.sleep(self.__color.get(k))


traffic_light = TrafficLight()
traffic_light.running()