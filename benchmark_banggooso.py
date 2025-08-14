import argparse
import statistics
import time
from typing import List
from urllib import request


def benchmark(url: str, runs: int) -> List[float]:
    """Benchmark a URL by making multiple GET requests.

    Args:
        url: The URL to request.
        runs: Number of requests to make.
    Returns:
        List of response times in seconds for each run.
    """
    times: List[float] = []
    for i in range(runs):
        start = time.perf_counter()
        with request.urlopen(url) as resp:
            resp.read()  # consume data to ensure full transfer
        elapsed = time.perf_counter() - start
        print(f"Run {i+1}: {elapsed:.3f}s (status {resp.status})")
        times.append(elapsed)
    return times


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark a website by measuring response times.")
    parser.add_argument(
        "url",
        nargs="?",
        default="https://www.banggooso.com/",
        help="Target URL to benchmark",
    )
    parser.add_argument("--runs", type=int, default=5, help="Number of requests to perform")
    args = parser.parse_args()

    times = benchmark(args.url, args.runs)
    print()
    print(f"Min: {min(times):.3f}s")
    print(f"Max: {max(times):.3f}s")
    print(f"Average: {statistics.mean(times):.3f}s")


if __name__ == "__main__":
    main()
