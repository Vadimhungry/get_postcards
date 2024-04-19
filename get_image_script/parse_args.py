import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='The script retrieves scans of postcards '
                    'from the provided HTML page.'
                    'Supported file extensions: html'
    )
    parser.add_argument('page', type=str, help='Path to HTML page.')
    parser.add_argument(
        'results',
        type=str,
        help='The path to the folder '
             'where the scans of postcards will be saved.'
    )
    args = parser.parse_args()

    return args.page, args.results
