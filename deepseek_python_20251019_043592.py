# monitoring/performance_tracking.py
import prometheus_client
from prometheus_client import Counter, Histogram, Gauge

class RyokoMetrics:
    """Comprehensive metrics collection for production monitoring"""
    
    def __init__(self):
        self.experiences_processed = Counter(
            'ryoko_experiences_processed_total',
            'Total experiences processed'
        )
        self.processing_time = Histogram(
            'ryoko_processing_time_seconds',
            'Experience processing time'
        )
        self.entity_growth = Gauge(
            'ryoko_entity_growth_stage',
            'Current growth stage of entity'
        )
    
    def record_experience_processing(self, processing_time: float):
        self.experiences_processed.inc()
        self.processing_time.observe(processing_time)