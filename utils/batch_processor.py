"""
Batch Processing Module

Provides utilities for processing large amounts of data in batches
with progress tracking, error handling, and retry logic.
"""

from typing import List, Callable, Any, Optional, Dict
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class BatchStatus(Enum):
    """Status of batch processing."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"


@dataclass
class BatchResult:
    """Result of batch processing."""
    batch_id: str
    status: BatchStatus
    total_items: int
    processed: int
    failed: int
    skipped: int
    errors: List[str]
    started_at: datetime
    completed_at: Optional[datetime] = None
    
    def success_rate(self) -> float:
        """Calculate success rate as percentage."""
        if self.total_items == 0:
            return 0.0
        return (self.processed / self.total_items) * 100


class BatchProcessor:
    """Process items in batches with progress tracking."""
    
    def __init__(
        self,
        batch_size: int = 100,
        max_retries: int = 3,
        batch_id: Optional[str] = None
    ):
        self.batch_size = batch_size
        self.max_retries = max_retries
        self.batch_id = batch_id or self._generate_batch_id()
        self.results: List[Any] = []
        self.errors: List[str] = []
        
    def _generate_batch_id(self) -> str:
        """Generate unique batch ID."""
        return f"batch_{int(datetime.utcnow().timestamp() * 1000)}"
        
    def process(
        self,
        items: List[Any],
        processor_func: Callable,
        skip_on_error: bool = True
    ) -> BatchResult:
        """Process items in batches."""
        start_time = datetime.utcnow()
        total = len(items)
        processed = 0
        failed = 0
        skipped = 0
        
        for i in range(0, total, self.batch_size):
            batch = items[i:i + self.batch_size]
            
            for item in batch:
                try:
                    result = self._process_item_with_retry(item, processor_func)
                    self.results.append(result)
                    processed += 1
                except Exception as e:
                    error_msg = f"Failed to process item {i}: {str(e)}"
                    self.errors.append(error_msg)
                    
                    if skip_on_error:
                        skipped += 1
                    else:
                        failed += 1
                        raise
                        
        return BatchResult(
            batch_id=self.batch_id,
            status=BatchStatus.COMPLETED if not failed else BatchStatus.FAILED,
            total_items=total,
            processed=processed,
            failed=failed,
            skipped=skipped,
            errors=self.errors,
            started_at=start_time,
            completed_at=datetime.utcnow()
        )
        
    def _process_item_with_retry(
        self,
        item: Any,
        processor_func: Callable
    ) -> Any:
        """Process item with retry logic."""
        last_exception = None
        
        for attempt in range(self.max_retries):
            try:
                return processor_func(item)
            except Exception as e:
                last_exception = e
                if attempt < self.max_retries - 1:
                    continue
                    
        raise last_exception or Exception("Processing failed")
        
    def get_progress(self) -> Dict[str, Any]:
        """Get current processing progress."""
        return {
            'batch_id': self.batch_id,
            'processed': len(self.results),
            'errors': len(self.errors),
            'total_results': len(self.results),
        }
