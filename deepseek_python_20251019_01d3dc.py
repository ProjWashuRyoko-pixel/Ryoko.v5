# core/memory_system.py
from typing import Dict, List, Any
import numpy as np
from datetime import datetime, timedelta

class MemoryConsolidationEngine:
    """Sophisticated memory formation and pruning system"""
    
    def __init__(self, max_memories: int = 100):
        self.max_memories = max_memories
        self.memory_network = {}  # Graph of connected memories
        self.consolidation_threshold = 0.7
        
    def calculate_memory_strength(self, experience: Dict, emotional_impact: float) -> float:
        """Calculate memory strength using multiple factors"""
        recency = self._calculate_recency_factor(experience['timestamp'])
        emotional_intensity = emotional_impact
        novelty = experience.get('novelty', 0.5)
        coherence = self._calculate_narrative_coherence(experience)
        
        strength = (
            recency * 0.3 +
            emotional_intensity * 0.4 + 
            novelty * 0.2 +
            coherence * 0.1
        )
        return min(1.0, strength)
    
    def form_associative_links(self, new_memory: Dict, existing_memories: List[Dict]):
        """Create associative links between related memories"""
        for memory in existing_memories:
            similarity = self._calculate_memory_similarity(new_memory, memory)
            if similarity > 0.6:
                self._create_associative_link(new_memory['id'], memory['id'], similarity)
    
    def consolidate_memories(self, memories: List[Dict]) -> List[Dict]:
        """Prune and consolidate memories based on importance"""
        if len(memories) <= self.max_memories:
            return memories
            
        # Calculate importance scores
        memory_scores = []
        for memory in memories:
            score = self.calculate_memory_importance(memory)
            memory_scores.append((memory, score))
        
        # Keep most important memories
        memory_scores.sort(key=lambda x: x[1], reverse=True)
        return [mem for mem, score in memory_scores[:self.max_memories]]
    
    def _calculate_memory_importance(self, memory: Dict) -> float:
        """Calculate overall memory importance"""
        base_strength = memory.get('strength', 0.5)
        network_centrality = self._calculate_network_centrality(memory['id'])
        emotional_weight = memory.get('emotional_weight', 0.5)
        
        return (base_strength * 0.4 + 
                network_centrality * 0.3 + 
                emotional_weight * 0.3)