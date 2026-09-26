import time
import asyncio

# def task1():
#     print("Task 1 started")
#     time.sleep(3)
#     print("Task 1 finished")

# print(task1())

# async def task1():
#     print("Task 1 started")
#     time.sleep(3)
#     return "Task 1 finished"

# print(task1())

# result = asyncio.run(task1())
#
# print(result)

# async def task1():
#     print("Task 1 started")
#     await asyncio.sleep(3)
#     print("Task 1 finished")
#
# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(2)
#     print("Task 2 finished")
#
# async def main():
#     start_time = time.perf_counter()
#
#     t1 = asyncio.create_task(task1())
#     t2 = asyncio.create_task(task2())
#     t3 = asyncio.create_task(task2())
#
#     await t1
#     await t2
#     await t3
#
#     print(f"Total time: {time.perf_counter() - start_time:.2f}")
#
# asyncio.run(main())


# async def task1():
#     print("Task 1 started")
#     await asyncio.sleep(3)
#     return "Task 1 finished"
#
# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(2)
#     return "Task 2 finished"
#
# async def main():
#     start_time = time.perf_counter()
#
#     result = await asyncio.gather(task1(), task2(), task2())
#
#     print(f"Total time: {time.perf_counter() - start_time:.2f}")
#     print(result)
#
# asyncio.run(main())


async def davaleba(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    print(f"Task {name} finished")

async def main():
    start_time = time.perf_counter()

    # tasks = []

    # for i in range(1, 6):
    #     tasks.append(asyncio.create_task(davaleba(i)))

    # for task in tasks:
    #     await task

    tasks = [davaleba(i) for i in range(1, 6)]

    await asyncio.gather(*tasks)

    end_time = time.perf_counter()

    print(f"Total time: {end_time - start_time:.2f}")

asyncio.run(main())

















 