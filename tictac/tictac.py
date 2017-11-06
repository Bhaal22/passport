import argparse
import os
import json
from datetime import date, datetime
from pprint import pprint


def parse_arguments():
    parser = argparse.ArgumentParser(description='Compute the remaining times for your objectives')
    parser.add_argument('--profile', type=str,
                   help='profile path')

    args = parser.parse_args()
    return args


def handle_objectives(data):
    objectives_data = data['objectives']

    today = datetime.now()
    for objective in objectives_data:
        objective_date = datetime.strptime(objective['date'], '%Y-%m-%d')
        dt = objective_date - today
        pprint(dt)


def main():
    args = parse_arguments()

    profile = args.profile
    objectives = os.path.join(profile, 'objectives.json')

    with open(objectives) as data_file:
        data = json.load(data_file)
        handle_objectives(data)


if __name__ == "__main__":
    main()
