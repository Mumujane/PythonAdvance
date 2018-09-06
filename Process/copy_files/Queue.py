"""
队列
    队列的作用是存取数据
    队列中的数据取完了就没有了
    队列是现存先取(先进 先出)

"""
import multiprocessing

queue = multiprocessing.Queue(3)

# 存数据
queue.put("!234")
queue.put((1,2))
queue.put({"age":19})
# queue.put({"age":20}) # 队列如果满了,再放会等待

# 取数据
# print(queue.get())
# print(queue.get())
# print(queue.get())
print(queue.get()) # 队列如果空的,那么再取会等待

print("取完了")


