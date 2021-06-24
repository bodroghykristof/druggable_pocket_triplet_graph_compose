from model.triplet import Triplet


def read_triplets():
    triplets = []
    file = open("resources/triplets100.txt", "r")
    while True:
        try:
            line = file.readline()
            if not line:
                break
            segments = line.split("|")
            triplet_name = segments[0].strip()
            occurrences = int(segments[1].strip())
            timestamp_list = [int(number) for number in segments[2].strip()[1:-1].split(",")]
            triplets.append(Triplet(triplet_name, occurrences, timestamp_list))
        except (IndexError, ValueError):
            pass
    return triplets
