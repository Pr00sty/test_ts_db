from uuid import uuid1
from random import random
from datetime import datetime, timedelta
from logging import INFO, getLogger, basicConfig

LOGGER = getLogger()
basicConfig(level=INFO)


def writer(filename: str, line: str):
    with open(filename, 'a+') as file:
        file.write(line)


def main():
    points_count = 100000
    networks_count = 2
    points = []

    network_id_list = [uuid1().hex for i in range(networks_count)]
    for network_id in network_id_list:
        for point_no in range(points_count):
            if point_no % 1000 == 0:
                LOGGER.info(point_no)
            project_id = network_id[:20]
            time = datetime(2020, 3, 7, 21, 0, 0) + timedelta(seconds=point_no)
            csv_line = "{time},{network_id},{project_id},{area_id},{zone_id},{uuid},{energy},{reliability}\n".format(
                time=time.strftime("%Y-%m-%d %H:%M:%S"),
                network_id=network_id,
                project_id=project_id,
                area_id=uuid1().hex,
                zone_id=uuid1().hex,
                uuid=uuid1().hex,
                energy=random()*10,
                reliability=random()*100,
            )
            points.append(csv_line)
        writer("data/{}.csv".format(network_id), "".join(points))
        points.clear()


if __name__ == '__main__':
    main()
