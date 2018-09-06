"""
# 定义一个队列的进一步学习

"""
import multiprocessing

queue = multiprocessing.Queue(3)

queue.put("123")
queue.put(345)
print(queue.full())  # False
queue.put(345)

print(queue.get())
print(queue.get())
print("queue 个数为 ", queue.qsize())
