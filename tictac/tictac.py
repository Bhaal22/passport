import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Compute the remaining times for your objectives')
    parser.add_argument('objectives', type=str,
                   help='an integer for the accumulator')

    args = parser.parse_args()

def main():
    parse_arguments()


if __name__ == "__main__":
    main()
