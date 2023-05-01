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

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, newWorker):
        if newWorker not in self._workers:
            self._workers.append(newWorker)

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company

        self._boss = boss
        boss.workers = self

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, newBoss):
        if self._boss.id != newBoss.id:
            self._boss.workers.remove(self)
            newBoss.workers = self
            self._boss = newBoss


boss1 = Boss(1, "Alice", "Company A")
boss2 = Boss(2, "Bob", "Company B")

worker1 = Worker(1, "John", "Company A", boss1)
worker2 = Worker(2, "Mary", "Company B", boss2)
worker3 = Worker(3, "Peter", "Company A", boss1)

print('workers')
print(worker1)
print(worker2)
print('boss')
print(boss1.workers)
print(boss2.workers)

print('func')
worker2.boss = boss1
print(boss1.workers)
print(boss2.workers)
