# core/adaptive_config.py
from typing import Dict, Any
import json

class AdaptiveConfiguration:
    """Self-optimizing configuration based on entity performance"""
    
    def __init__(self, base_config: Dict):
        self.base_config = base_config
        self.performance_metrics = []
        self.adaptive_parameters = {
            'learning_rate': 0.1,
            'chaos_sensitivity': 0.5,
            'memory_retention': 0.7
        }
    
    def update_based_on_performance(self, entity_performance: Dict):
        """Adapt configuration based on entity performance"""
        growth_rate = entity_performance.get('growth_rate', 0)
        stability = entity_performance.get('stability', 0)
        coherence = entity_performance.get('coherence', 0)
        
        # Adjust learning rate based on growth
        if growth_rate < 0.1:  # Stagnant growth
            self.adaptive_parameters['learning_rate'] *= 1.2
        elif growth_rate > 0.5:  # Rapid growth
            self.adaptive_parameters['learning_rate'] *= 0.9
        
        # Adjust chaos sensitivity based on stability
        if stability < 0.3:  # Low stability
            self.adaptive_parameters['chaos_sensitivity'] *= 0.8
        elif stability > 0.8:  # High stability  
            self.adaptive_parameters['chaos_sensitivity'] *= 1.2
    
    def get_optimized_config(self) -> Dict[str, Any]:
        """Get current optimized configuration"""
        config = self.base_config.copy()
        config.update(self.adaptive_parameters)
        return config