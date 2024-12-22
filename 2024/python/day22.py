from utils import *

from collections import deque

start_time: float = get_start_time()

secrets = [int(x) for x in get_input_lines("day22.txt")]

PRUNE_CONST = 16777216

def evolve(secret: int) -> int:
    secret = (secret ^ (secret * 64)) % PRUNE_CONST
    secret = (secret ^ (secret // 32)) % PRUNE_CONST
    secret = (secret ^ (secret * 2048)) % PRUNE_CONST
    return secret

def evaluate_buyer(init_secret: int, iterations: int) -> tuple[int, dict[tuple, int]]:
    sells: dict[tuple, int] = {}
    price_changes = deque(maxlen=4)
    secret = init_secret
    for _ in range(iterations):
        next_secret = evolve(secret)
        next_price = next_secret % 10
        price_changes.append(next_price - secret % 10)
        if len(price_changes) == 4:
            key = tuple(price_changes)
            if key not in sells:
                sells[key] = next_price
        secret = next_secret
    return secret, sells

sum_secrets = 0
total_sells: dict[tuple, int] = {}
for secret in secrets:
    new_secret, sells = evaluate_buyer(secret, 2000)
    for key, sell in sells.items():
        total_sells[key] = total_sells.get(key, 0) + sell
    sum_secrets += new_secret
print(sum_secrets)

best_profit = max(total_sells.values())
print(best_profit)

print_time_elapsed(start_time)
