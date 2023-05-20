# Implement 2 classes, the first one is the Boss and the second one is the Worker.
#
# Worker has a property 'boss', and its value must be an instance of Boss.
#
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute,
# use getters and setters instead!
#

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)

    @property
    def workers(self):
        return self._workers
    def get_workers(self):
        return self._workers

    def set_workers(self, workers):
        if isinstance(workers, list):
            self._workers = workers

    workers = property(get_workers, set_workers)

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: "Boss"):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            if self._boss:
                self._boss.workers.remove(self)
            self._boss = boss
            boss.add_worker(self)


boss1 = Boss(1, "Alice", "Company A")
boss2 = Boss(2, "Bob", "Company B")

worker1 = Worker(1, "John", "Company A", boss1)
worker2 = Worker(2, "Mary", "Company B", boss2)
worker3 = Worker(3, "Peter", "Company A", boss1)

worker1.boss = boss2

print("Boss:", boss1.id, boss1.name, boss1.company)
print("Boss workers:", [worker.name for worker in boss1.workers])
print("Worker 1:", worker1.id, worker1.name, worker1.company, worker1.boss.name)
print("Worker 2:", worker2.id, worker2.name, worker2.company, worker2.boss.name)
print("New Boss workers:", [worker.name for worker in boss2.workers])
