import argparse
import time


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--db",
        help="Path to the SQLite database file",
        type=str,
        required=True
    )

    parser.add_argument(
        "--host",
        help="Host address for the server",
        type=str,
        default="127.0.0.1"
    )

    parser.add_argument(
        "--port",
        help="Port number for the server",
        type=int,
        default=8080
    )
    return parser.parse_args()
