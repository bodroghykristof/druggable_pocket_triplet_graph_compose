import file_reader
from model import graph_plotter


def main():
    triplets = file_reader.read_triplets()
    graph_plotter.scatter_graph(triplets)


if __name__ == '__main__':
    main()
