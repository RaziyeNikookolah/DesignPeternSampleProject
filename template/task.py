from abc import ABC, abstractmethod

from audit_trail import AuditTrail


class Task(ABC):
    def __init__(self):
        self.audit_trail = AuditTrail()

    @abstractmethod
    def _do_execute(self):
        ...

    def execut(self):
        self._do_execute()
        self.audit_trail.record()
