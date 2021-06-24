import matplotlib.pyplot as plt


def scatter_graph(triplets):
    sublist_size = 20
    image_count = len(triplets) // 20 + 1
    for i in range(image_count):
        x, y = [], []
        lower = i * 20
        upper = min(sublist_size * (i+1), len(triplets))
        for index, triplet in enumerate(triplets[lower:upper]):
            x.extend(triplet.timestamp_list)
            y.extend([triplet.name + " - " + str(triplet.occurrence) for _ in range(len(triplet.timestamp_list))])
        plt.figure(figsize=(12, 12), dpi=240)
        plt.scatter(x, y, marker=".", s=0.5)
        plt.savefig('result/scatter_' + str(lower + 1) + '_' + str(upper))
        plt.close()
