import asyncio
import time

tasks = [
    ("Downloading data", 3),
    ("Processing data", 2),
    ("Sending notification", 1),
    ("Saving results", 4),
]


async def do_task(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")
    return f"{name} completed"



async def sequential_tasks():
    results = []

    for name, seconds in tasks:
        result = await do_task(name, seconds)
        results.append(result)

    return results


async def concurrent_tasks():
    coroutines = []

    for name, seconds in tasks:
        coroutines.append(do_task(name, seconds))

    results = await asyncio.gather(*coroutines)
    return results


async def main():
    
    start = time.perf_counter()
    await sequential_tasks()
    end = time.perf_counter()

    sequential_time = end - start

    print("-" * 40)

    start = time.perf_counter()
    await concurrent_tasks()
    end = time.perf_counter()

    concurrent_time = end - start

    print("-" * 40)

    print(f"Sequential execution time: {sequential_time:.2f} seconds")
    print(f"Concurrent execution time: {concurrent_time:.2f} seconds")


asyncio.run(main())