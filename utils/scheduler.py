"""
Task Scheduling Module

Provides asynchronous task scheduling and execution with support for
recurring tasks, retries, and execution history.
"""

from typing import Callable, Optional, Dict, Any, List
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import uuid


class TaskStatus(Enum):
    """Status of scheduled task."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class TaskFrequency(Enum):
    """Frequency of recurring tasks."""
    ONCE = "once"
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


@dataclass
class TaskExecution:
    """Record of task execution."""
    task_id: str
    execution_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: TaskStatus = TaskStatus.PENDING
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None
    result: Optional[Any] = None
    retry_count: int = 0
    
    def duration_seconds(self) -> Optional[float]:
        """Get execution duration in seconds."""
        if self.started_at and self.completed_at:
            return (self.completed_at - self.started_at).total_seconds()
        return None


@dataclass
class ScheduledTask:
    """Definition of a scheduled task."""
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    description: str = ""
    func: Optional[Callable] = None
    args: tuple = ()
    kwargs: Dict[str, Any] = field(default_factory=dict)
    frequency: TaskFrequency = TaskFrequency.ONCE
    next_run: Optional[datetime] = None
    enabled: bool = True
    max_retries: int = 3
    timeout_seconds: int = 300
    executions: List[TaskExecution] = field(default_factory=list)
    
    def should_run(self) -> bool:
        """Check if task should run now."""
        if not self.enabled:
            return False
        if not self.next_run:
            return False
        return datetime.utcnow() >= self.next_run
        
    def mark_executed(self, status: TaskStatus, result: Any = None, error: str = None) -> None:
        """Mark task as executed."""
        execution = TaskExecution(
            task_id=self.task_id,
            status=status,
            completed_at=datetime.utcnow(),
            result=result,
            error=error
        )
        self.executions.append(execution)
        self._schedule_next_run()
        
    def _schedule_next_run(self) -> None:
        """Schedule next run based on frequency."""
        now = datetime.utcnow()
        
        if self.frequency == TaskFrequency.ONCE:
            self.enabled = False
        elif self.frequency == TaskFrequency.HOURLY:
            self.next_run = now + timedelta(hours=1)
        elif self.frequency == TaskFrequency.DAILY:
            self.next_run = now + timedelta(days=1)
        elif self.frequency == TaskFrequency.WEEKLY:
            self.next_run = now + timedelta(weeks=1)
        elif self.frequency == TaskFrequency.MONTHLY:
            self.next_run = now + timedelta(days=30)


class TaskScheduler:
    """Schedule and manage asynchronous tasks."""
    
    def __init__(self):
        self.tasks: Dict[str, ScheduledTask] = {}
        self.execution_history: List[TaskExecution] = []
        
    def add_task(
        self,
        name: str,
        func: Callable,
        frequency: TaskFrequency = TaskFrequency.ONCE,
        args: tuple = (),
        kwargs: Optional[Dict[str, Any]] = None,
        description: str = ""
    ) -> str:
        """Add a new scheduled task."""
        task = ScheduledTask(
            name=name,
            func=func,
            frequency=frequency,
            args=args,
            kwargs=kwargs or {},
            description=description,
            next_run=datetime.utcnow()
        )
        self.tasks[task.task_id] = task
        return task.task_id
        
    def get_pending_tasks(self) -> List[ScheduledTask]:
        """Get tasks that should run now."""
        return [task for task in self.tasks.values() if task.should_run()]
        
    def get_task(self, task_id: str) -> Optional[ScheduledTask]:
        """Get task by ID."""
        return self.tasks.get(task_id)
        
    def get_execution_history(
        self,
        task_id: Optional[str] = None,
        limit: int = 100
    ) -> List[TaskExecution]:
        """Get execution history."""
        if task_id:
            return [e for e in self.execution_history if e.task_id == task_id][-limit:]
        return self.execution_history[-limit:]
        
    def cancel_task(self, task_id: str) -> bool:
        """Cancel a scheduled task."""
        if task_id in self.tasks:
            self.tasks[task_id].enabled = False
            return True
        return False
