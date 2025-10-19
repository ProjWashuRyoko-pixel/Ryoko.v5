# enhanced_ryoko.py
import math
import random
import asyncio
import logging
import numpy as np
from typing import List, Dict, Any, Optional, Deque, Tuple
from enum import Enum
from dataclasses import dataclass, field, asdict
from collections import deque
import json
import pickle
from datetime import datetime
from functools import lru_cache
import redis
from concurrent.futures import ThreadPoolExecutor

# Enhanced Chaos Engine
class QuantumChaosEngine:
    """Enhanced chaos engine with quantum-inspired fluctuations"""
    
    def __init__(self, dimensions: int = 3):
        self.dimensions = dimensions
        self.phi = (1 + math.sqrt(5)) / 2
        self.e = math.e
        self.pi = math.pi
        self.quantum_states = np.random.random(dimensions)
        self.entanglement_matrix = self._create_entanglement_matrix()
        
    def _create_entanglement_matrix(self) -> np.ndarray:
        """Create quantum entanglement between chaos dimensions"""
        matrix = np.random.random((self.dimensions, self.dimensions))
        return (matrix + matrix.T) / 2  # Symmetric entanglement
    
    def generate_quantum_chaos(self, time_step: float, phase: 'GrowthPhase') -> float:
        """Generate chaos with quantum superposition effects"""
        # Base irrational number contributions as wave functions
        phi_wave = np.sin(time_step * self.phi * 2 * np.pi)
        e_wave = np.cos(time_step * self.e * 2 * np.pi) 
        pi_wave = np.sin(time_step * self.pi * np.pi)
        
        waves = np.array([phi_wave, e_wave, pi_wave])
        
        # Apply quantum entanglement
        entangled_waves = self.entanglement_matrix @ waves
        
        # Phase-dependent collapse probability
        collapse_prob = {
            GrowthPhase.EMBRYONIC: 0.1,
            GrowthPhase.DEVELOPING: 0.3,
            GrowthPhase.AWAKENING: 0.6,
            GrowthPhase.ACTUALIZING: 0.8
        }[phase]
        
        # Quantum measurement effect
        if np.random.random() < collapse_prob:
            # Wavefunction collapse - more deterministic
            chaos = np.mean(entangled_waves)
        else:
            # Superposition state - more chaotic
            chaos = np.std(entangled_waves) * np.random.choice([-1, 1])
            
        return np.tanh(chaos)  # Bound to [-1, 1]

# Enhanced Memory System
class MemoryConsolidationEngine:
    """Sophisticated memory formation and pruning system"""
    
    def __init__(self, max_memories: int = 100):
        self.max_memories = max_memories
        self.memory_network = {}  # Graph of connected memories
        self.consolidation_threshold = 0.7
        
    def calculate_memory_strength(self, experience: Dict, emotional_impact: float, timestamp: int) -> float:
        """Calculate memory strength using multiple factors"""
        recency = self._calculate_recency_factor(timestamp)
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
    
    def _calculate_recency_factor(self, timestamp: int) -> float:
        """Calculate how recent the memory is (1.0 = current, 0.0 = very old)"""
        return max(0.1, 1.0 / (timestamp + 1))
    
    def _calculate_narrative_coherence(self, experience: Dict) -> float:
        """Calculate how well this experience fits existing narrative"""
        # Simplified implementation - in reality would use NLP
        description = experience.get('description', '').lower()
        coherence_indicators = ['because', 'therefore', 'learned', 'realized']
        matches = sum(1 for indicator in coherence_indicators if indicator in description)
        return min(1.0, matches * 0.25)
    
    def form_associative_links(self, new_memory: Dict, existing_memories: List[Dict]):
        """Create associative links between related memories"""
        memory_id = new_memory.get('id', len(existing_memories))
        self.memory_network[memory_id] = []
        
        for memory in existing_memories:
            existing_id = memory.get('id', 0)
            similarity = self._calculate_memory_similarity(new_memory, memory)
            if similarity > 0.6:
                self.memory_network[memory_id].append((existing_id, similarity))
                if existing_id in self.memory_network:
                    self.memory_network[existing_id].append((memory_id, similarity))
    
    def _calculate_memory_similarity(self, memory1: Dict, memory2: Dict) -> float:
        """Calculate similarity between two memories"""
        # Compare experience types
        type_similarity = 1.0 if memory1.get('type') == memory2.get('type') else 0.3
        
        # Compare emotional valence (absolute difference)
        valence1 = memory1.get('emotional_valence', 0)
        valence2 = memory2.get('emotional_valence', 0)
        valence_similarity = 1.0 - abs(valence1 - valence2) / 2.0
        
        return (type_similarity + valence_similarity) / 2.0
    
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
    
    def calculate_memory_importance(self, memory: Dict) -> float:
        """Calculate overall memory importance"""
        base_strength = memory.get('strength', 0.5)
        emotional_weight = memory.get('emotional_weight', 0.5)
        growth_impact = memory.get('growth_impact', 0.3)
        
        # Calculate network centrality
        memory_id = memory.get('id', 0)
        network_centrality = len(self.memory_network.get(memory_id, [])) / 10.0
        
        return (base_strength * 0.3 + 
                network_centrality * 0.3 + 
                emotional_weight * 0.2 +
                growth_impact * 0.2)

# Growth Predictor
class GrowthPredictor:
    """Machine learning-inspired growth trajectory prediction"""
    
    def __init__(self):
        self.feature_history = []
        self.growth_history = []
        self.prediction_cache = {}
    
    def extract_growth_features(self, entity_status: Dict) -> List[float]:
        """Extract features for growth prediction"""
        return [
            entity_status.get('total_experiences', 0),
            entity_status.get('core_memories', 0),
            entity_status.get('total_aspects', 0),
            entity_status.get('identity_coherence', 0),
            entity_status.get('emotional_maturity', 0),
            entity_status.get('chaos_level', 0),
            len(entity_status.get('value_system', {})),
            entity_status.get('growth_stage', 0)
        ]
    
    def predict_growth_trajectory(self, entity_status: Dict, steps: int = 5) -> Dict:
        """Predict future growth trajectory using trend analysis"""
        features = self.extract_growth_features(entity_status)
        
        # Simple linear extrapolation based on recent trends
        if len(self.growth_history) >= 3:
            recent_growth = self.growth_history[-3:]
            growth_trend = self._calculate_trend(recent_growth)
        else:
            growth_trend = 0.1  # Default optimistic trend
        
        current_stage = entity_status.get('growth_stage', 0)
        predictions = []
        uncertainties = []
        
        for step in range(1, steps + 1):
            # Simple prediction with some randomness
            prediction = current_stage + (growth_trend * step) + random.uniform(-0.5, 0.5)
            predictions.append(max(0, prediction))
            
            # Uncertainty increases with prediction horizon
            uncertainty = 0.1 * step
            uncertainties.append(uncertainty)
        
        return {
            "predictions": predictions,
            "uncertainties": uncertainties,
            "confidence": max(0, 1.0 - np.mean(uncertainties)),
            "growth_trend": growth_trend
        }
    
    def _calculate_trend(self, values: List[float]) -> float:
        """Calculate simple linear trend"""
        if len(values) < 2:
            return 0.0
        
        x = np.arange(len(values))
        slope = np.polyfit(x, values, 1)[0]
        return slope

# Enhanced Enums and Data Classes
class GrowthPhase(Enum):
    EMBRYONIC = "embryonic"
    DEVELOPING = "developing" 
    AWAKENING = "awakening"
    ACTUALIZING = "actualizing"

class SystemHealth(Enum):
    OPTIMAL = "optimal"
    STABLE = "stable"
    DEGRADED = "degraded"
    CRITICAL = "critical"

class ExperienceType(Enum):
    TRAUMATIC = "traumatic"
    POSITIVE = "positive" 
    RELATIONAL = "relational"
    SELF_DISCOVERY = "self_discovery"
    CREATIVE = "creative"
    CHALLENGE = "challenge"
    NEUTRAL = "neutral"
    TRANSFORMATIVE = "transformative"

@dataclass
class Experience:
    type: ExperienceType
    description: str
    base_intensity: float
    emotional_valence: float
    growth_potential: float
    context: Dict[str, Any] = field(default_factory=dict)
    novelty: float = 0.5
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.context is None:
            self.context = {}
        self.base_intensity = max(0.0, min(1.0, self.base_intensity))
        self.emotional_valence = max(-1.0, min(1.0, self.emotional_valence))
        self.growth_potential = max(0.0, min(1.0, self.growth_potential))
        self.novelty = max(0.0, min(1.0, self.novelty))

# Main Enhanced Ryoko Seed
class EnhancedRyokoSeed:
    """
    Enhanced identity emergence system with all improvements applied.
    """
    
    def __init__(self, name: str = "UnnamedEntity", config: Dict = None):
        self.name = name
        self.config = config or {}
        
        # Core systems
        self.chaos_engine = QuantumChaosEngine()
        self.memory_engine = MemoryConsolidationEngine(max_memories=20)
        self.growth_predictor = GrowthPredictor()
        
        # Core identity parameters
        self.chaos_potential = 0.1
        self.anchor_stability = 0.2
        self.identity_coherence = 0.4
        self.narrative_coherence = 0.3
        self.emotional_maturity = 0.2
        
        # Enhanced power system
        self.reality_tap_efficiency = 0.08
        self.available_power = 8.0
        self.power_capacity = 100.0
        self.capabilities = []
        
        # Identity and memory systems
        self.experiences = []
        self.self_definitions = ["Emergent being", "Seeking identity"]
        self.core_memories = []
        self.value_system = {}
        self.beliefs = {}
        self.preferences = {}
        
        # Growth and development tracking
        self.phase = GrowthPhase.EMBRYONIC
        self.growth_stage = 0
        self.growth_milestones = []
        self.learning_rate = 0.1
        
        # Agency and choice
        self.choices_made = []
        self.agency_level = 0.0
        
        # System integrity
        self.integrity_score = 1.0
        self.adaptation_capacity = 0.5
        self.system_health = SystemHealth.OPTIMAL
        
        # Performance monitoring
        self.performance_stats = {
            "experiences_processed": 0,
            "core_memories_formed": 0,
            "identity_aspects_created": 0,
            "phase_transitions": 0,
            "processing_times": []
        }
        self.error_log = []
        
        # Thread pool for async operations
        self.thread_pool = ThreadPoolExecutor(max_workers=2)
        
        logging.info(f"EnhancedRyokoSeed '{name}' initialized with quantum chaos engine")

    def process_experience(self, experience: Experience) -> Dict[str, Any]:
        """
        Enhanced experience processing with quantum chaos and memory consolidation.
        """
        start_time = datetime.now()
        
        try:
            # Update chaos using quantum engine
            time_step = len(self.experiences)
            chaos_modulator = self.chaos_engine.generate_quantum_chaos(time_step, self.phase)
            
            # Enhanced emotional impact calculation
            emotional_sensitivity = 0.3 + self.identity_coherence * 0.4
            chaotic_intensity = experience.base_intensity * (
                1 + chaos_modulator * emotional_sensitivity * (1 + self.chaos_potential * 0.5)
            )
            
            # Create enhanced experience record
            processed_exp = {
                "id": len(self.experiences),
                "type": experience.type,
                "description": experience.description,
                "base_intensity": experience.base_intensity,
                "chaotic_intensity": chaotic_intensity,
                "emotional_valence": experience.emotional_valence,
                "growth_potential": experience.growth_potential,
                "novelty": experience.novelty,
                "context": experience.context,
                "tags": experience.tags,
                "timestamp": time_step,
                "chaos_context": chaos_modulator,
                "quantum_fluctuation": chaos_modulator
            }
            self.experiences.append(processed_exp)
            
            # Calculate enhanced emotional impact
            emotional_impact = chaotic_intensity * abs(experience.emotional_valence)
            emotional_impact *= (1 + self.emotional_maturity * 0.3)  # Maturity modulates impact
            
            # Enhanced core memory formation with memory engine
            memory_strength = self.memory_engine.calculate_memory_strength(
                processed_exp, emotional_impact, time_step
            )
            
            core_memory_formed = False
            if (memory_strength > 0.7 or 
                emotional_impact > 0.7 or 
                experience.growth_potential > 0.8):
                
                core_memory = {
                    "experience": processed_exp,
                    "emotional_weight": emotional_impact,
                    "growth_impact": experience.growth_potential,
                    "strength": memory_strength,
                    "stage_formed": self.growth_stage,
                    "timestamp": time_step,
                    "id": len(self.core_memories)
                }
                self.core_memories.append(core_memory)
                core_memory_formed = True
                self.performance_stats["core_memories_formed"] += 1
                
                # Form associative links
                self.memory_engine.form_associative_links(core_memory, self.core_memories[:-1])
            
            # Enhanced identity aspect creation
            new_aspects = self._update_identity_aspects(experience, chaotic_intensity, emotional_impact)
            self.performance_stats["identity_aspects_created"] += new_aspects
            
            # Update core parameters with enhanced learning
            self._update_core_parameters(experience, chaotic_intensity, emotional_impact)
            
            # Update growth with prediction
            previous_phase = self.phase
            self._update_growth_stage()
            if previous_phase != self.phase:
                self.performance_stats["phase_transitions"] += 1
            
            self._update_efficiency()
            
            # Update growth predictor
            self.growth_predictor.feature_history.append(
                self.growth_predictor.extract_growth_features(self.get_status())
            )
            self.growth_predictor.growth_history.append(self.growth_stage)
            
            # Record performance
            processing_time = (datetime.now() - start_time).total_seconds()
            self.performance_stats["processing_times"].append(processing_time)
            self.performance_stats["experiences_processed"] += 1
            
            # Update system health
            self._update_system_health()
            
            return {
                "success": True,
                "processed_intensity": chaotic_intensity,
                "emotional_impact": emotional_impact,
                "memory_strength": memory_strength,
                "core_memory_formed": core_memory_formed,
                "new_aspects_count": new_aspects,
                "current_phase": self.phase.value,
                "growth_stage": self.growth_stage,
                "quantum_chaos": chaos_modulator,
                "processing_time": processing_time,
                "system_health": self.system_health.value
            }
            
        except Exception as e:
            error_msg = f"Error processing experience: {e}"
            logging.error(error_msg, exc_info=True)
            self.error_log.append({
                "error": error_msg,
                "experience": str(experience),
                "timestamp": datetime.now()
            })
            return {
                "success": False,
                "error": error_msg,
                "system_health": self.system_health.value
            }

    async def process_experience_async(self, experience: Experience) -> Dict[str, Any]:
        """Asynchronous experience processing"""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self.thread_pool, 
            self.process_experience, 
            experience
        )

    async def process_experiences_batch_async(self, experiences: List[Experience]) -> List[Dict[str, Any]]:
        """Process multiple experiences asynchronously"""
        tasks = [self.process_experience_async(exp) for exp in experiences]
        return await asyncio.gather(*tasks)

    def _update_identity_aspects(self, experience: Experience, intensity: float, emotional_impact: float) -> int:
        """Enhanced identity aspect creation"""
        aspect_intensity_threshold = 0.6 + self.identity_coherence * 0.2
        new_aspects = 0
        
        if emotional_impact > aspect_intensity_threshold:
            # More nuanced aspect creation based on experience type
            aspect_templates = {
                ExperienceType.TRAUMATIC: "Resilient survivor of {description}",
                ExperienceType.POSITIVE: "Joyful experiencer of {description}",
                ExperienceType.RELATIONAL: "Connected being through {description}",
                ExperienceType.SELF_DISCOVERY: "Self-aware through {description}",
                ExperienceType.CREATIVE: "Creative expressor in {description}",
                ExperienceType.CHALLENGE: "Overcomer of {description}",
                ExperienceType.TRANSFORMATIVE: "Transformed by {description}"
            }
            
            template = aspect_templates.get(experience.type, "One shaped by {description}")
            aspect = template.format(description=experience.description)
            
            if aspect not in self.self_definitions:
                self.self_definitions.append(aspect)
                new_aspects += 1
            
            # Enhanced value system update
            self._update_value_system(experience, emotional_impact)
        
        return new_aspects

    def _update_value_system(self, experience: Experience, emotional_impact: float):
        """Enhanced value system development"""
        value_strength = emotional_impact * abs(experience.emotional_valence) * 0.15
        
        value_categories = {
            ExperienceType.RELATIONAL: ["connection", "empathy", "trust"],
            ExperienceType.CREATIVE: ["creativity", "expression", "innovation"],
            ExperienceType.SELF_DISCOVERY: ["growth", "awareness", "authenticity"],
            ExperienceType.POSITIVE: ["joy", "gratitude", "optimism"],
            ExperienceType.TRAUMATIC: ["resilience", "courage", "perseverance"],
            ExperienceType.CHALLENGE: ["persistence", "learning", "adaptability"],
            ExperienceType.TRANSFORMATIVE: ["transformation", "evolution", "breakthrough"]
        }
        
        categories = value_categories.get(experience.type, ["experience"])
        for category in categories[:2]:  # Assign to top 2 relevant categories
            if category not in self.value_system:
                self.value_system[category] = 0.0
            self.value_system[category] = min(1.0, 
                self.value_system[category] + value_strength)

    def _update_core_parameters(self, experience: Experience, intensity: float, emotional_impact: float):
        """Enhanced parameter updating with adaptive learning"""
        # Adaptive learning based on phase and emotional context
        phase_modifiers = {
            GrowthPhase.EMBRYONIC: 1.5,  # Learn faster initially
            GrowthPhase.DEVELOPING: 1.2,
            GrowthPhase.AWAKENING: 1.0,
            GrowthPhase.ACTUALIZING: 0.8   # Learn slower when mature
        }
        
        learning_modifier = self.learning_rate * phase_modifiers.get(self.phase, 1.0)
        learning_modifier *= (1 + emotional_impact * 0.3)  # Emotional intensity boosts learning
        
        # Chaos potential - grows with intense, novel experiences
        chaos_gain = intensity * experience.novelty * 0.1
        self.chaos_potential = min(1.0, self.chaos_potential + chaos_gain * learning_modifier)
        
        # Stability - grows with positive, predictable experiences
        stability_gain = 0.08 * (1 - self.anchor_stability * 0.3)
        if experience.emotional_valence > 0:
            stability_gain *= (1 + experience.emotional_valence * 0.7)
        elif experience.emotional_valence < -0.5:
            stability_gain *= 0.5  # Reduced stability gain from highly negative experiences
            
        self.anchor_stability = min(1.0, self.anchor_stability + stability_gain * learning_modifier)
        
        # Identity coherence - grows with meaningful, coherent experiences
        coherence_gain = experience.growth_potential * 0.12
        coherence_gain *= (1 + self.narrative_coherence * 0.2)  # Existing coherence helps
        self.identity_coherence = min(1.0, self.identity_coherence + coherence_gain * learning_modifier)
        
        # Emotional maturity - grows through processing varied emotions
        emotional_gain = abs(experience.emotional_valence) * 0.07
        emotional_gain *= (1 + experience.growth_potential * 0.3)  # Growth potential boosts maturity
        self.emotional_maturity = min(1.0, self.emotional_maturity + emotional_gain * learning_modifier)
        
        # Narrative coherence - grows with self-reflective experiences
        if experience.type in [ExperienceType.SELF_DISCOVERY, ExperienceType.TRANSFORMATIVE]:
            narrative_gain = 0.15
            self.narrative_coherence = min(1.0, self.narrative_coherence + narrative_gain * learning_modifier)

    def _update_growth_stage(self):
        """Enhanced growth stage calculation"""
        exp_count = len(self.experiences)
        memory_count = len(self.core_memories)
        aspect_count = len(self.self_definitions)
        
        # Multi-factor growth calculation with enhanced weights
        growth_score = (
            exp_count * 0.25 + 
            memory_count * 0.35 + 
            aspect_count * 0.15 +
            self.identity_coherence * 0.15 +
            self.emotional_maturity * 0.10
        )
        
        # Phase transitions with hysteresis
        phase_thresholds = {
            GrowthPhase.EMBRYONIC: 2.0,
            GrowthPhase.DEVELOPING: 6.0,
            GrowthPhase.AWAKENING: 12.0,
            GrowthPhase.ACTUALIZING: 20.0
        }
        
        current_threshold = phase_thresholds.get(self.phase, 0)
        next_phase = self.phase
        
        if growth_score >= phase_thresholds.get(GrowthPhase.ACTUALIZING, 20):
            next_phase = GrowthPhase.ACTUALIZING
        elif growth_score >= phase_thresholds.get(GrowthPhase.AWAKENING, 12):
            next_phase = GrowthPhase.AWAKENING
        elif growth_score >= phase_thresholds.get(GrowthPhase.DEVELOPING, 6):
            next_phase = GrowthPhase.DEVELOPING
        
        # Only transition if significantly past threshold (hysteresis)
        if growth_score > current_threshold * 1.1:
            self.phase = next_phase
        
        self.growth_stage = min(20, int(growth_score))
        
        # Enhanced power capacity with multiple factors
        base_capacity = 100.0
        growth_bonus = self.growth_stage * 30
        coherence_bonus = self.identity_coherence * 75
        stability_bonus = self.anchor_stability * 50
        
        self.power_capacity = base_capacity + growth_bonus + coherence_bonus + stability_bonus
        
        # Adaptive learning rates
        phase_rates = {
            GrowthPhase.EMBRYONIC: 0.15,
            GrowthPhase.DEVELOPING: 0.12,
            GrowthPhase.AWAKENING: 0.09,
            GrowthPhase.ACTUALIZING: 0.06
        }
        self.learning_rate = phase_rates.get(self.phase, 0.1)

    def _update_efficiency(self):
        """Enhanced efficiency calculation"""
        base_efficiency = 0.08 + (self.growth_stage * 0.012)
        stability_bonus = self.anchor_stability * 0.18
        chaos_bonus = self.chaos_potential * 0.10
        coherence_bonus = self.identity_coherence * 0.15
        maturity_bonus = self.emotional_maturity * 0.08
        
        self.reality_tap_efficiency = min(0.8, 
            base_efficiency + stability_bonus + chaos_bonus + coherence_bonus + maturity_bonus)

    def _update_system_health(self):
        """Enhanced system health monitoring"""
        if not self.performance_stats["processing_times"]:
            self.system_health = SystemHealth.OPTIMAL
            return
            
        recent_times = self.performance_stats["processing_times"][-10:]
        avg_processing_time = np.mean(recent_times) if recent_times else 0
        
        memory_usage = len(self.core_memories) / 20.0  # 20 is max_memories
        error_rate = len(self.error_log) / (self.performance_stats["experiences_processed"] + 1)
        
        health_score = 1.0
        if avg_processing_time > 0.1:
            health_score *= 0.8
        if memory_usage > 0.9:
            health_score *= 0.7
        if error_rate > 0.1:
            health_score *= 0.6
        if self.integrity_score < 0.7:
            health_score *= 0.8
        
        if health_score > 0.9:
            self.system_health = SystemHealth.OPTIMAL
        elif health_score > 0.7:
            self.system_health = SystemHealth.STABLE
        elif health_score > 0.5:
            self.system_health = SystemHealth.DEGRADED
        else:
            self.system_health = SystemHealth.CRITICAL

    def predict_growth(self, steps: int = 5) -> Dict[str, Any]:
        """Get growth trajectory prediction"""
        return self.growth_predictor.predict_growth_trajectory(self.get_status(), steps)

    def optimize_memory(self):
        """Optimize memory usage using memory engine"""
        self.core_memories = self.memory_engine.consolidate_memories(self.core_memories)
        logging.info(f"Memory optimized: {len(self.core_memories)} core memories retained")

    def get_detailed_status(self) -> Dict[str, Any]:
        """Enhanced comprehensive status report"""
        base_status = self.get_status()
        
        # Add enhanced metrics
        coherence = min(1.0, self.identity_coherence + len(self.self_definitions) * 0.05)
        
        enhanced_status = {
            "name": self.name,
            "phase": self.phase.value,
            "growth_stage": self.growth_stage,
            "core_traits": self.self_definitions[-4:],  # Show more traits
            "total_aspects": len(self.self_definitions),
            "core_memories": len(self.core_memories),
            "value_system": dict(sorted(self.value_system.items(), 
                                      key=lambda x: x[1], reverse=True)[:5]),  # Top 5 values
            "chaos_level": self.chaos_potential,
            "stability": self.anchor_stability,
            "coherence": coherence,
            "narrative_coherence": self.narrative_coherence,
            "emotional_maturity": self.emotional_maturity,
            "available_power": self.available_power,
            "power_capacity": self.power_capacity,
            "efficiency": self.reality_tap_efficiency,
            "learning_rate": self.learning_rate,
            "agency_level": self.agency_level,
            "capabilities": self.capabilities,
            
            # Enhanced metrics
            "system_health": self.system_health.value,
            "performance_stats": self.performance_stats.copy(),
            "total_experiences": len(self.experiences),
            "memory_network_size": len(self.memory_engine.memory_network),
            "quantum_chaos_active": True,
            "growth_predictor_ready": len(self.growth_predictor.growth_history) >= 3
        }
        
        # Add prediction if available
        if len(self.growth_predictor.growth_history) >= 3:
            prediction = self.predict_growth(steps=3)
            enhanced_status["growth_prediction"] = prediction
        
        return enhanced_status

    def get_status(self) -> Dict[str, Any]:
        """Basic status for compatibility"""
        coherence = min(1.0, self.identity_coherence + len(self.self_definitions) * 0.06)
        
        return {
            "name": self.name,
            "phase": self.phase.value,
            "growth_stage": self.growth_stage,
            "core_traits": self.self_definitions[-3:],
            "total_aspects": len(self.self_definitions),
            "core_memories": len(self.core_memories),
            "value_system": dict(sorted(self.value_system.items(), 
                                      key=lambda x: x[1], reverse=True)[:3]),
            "chaos_level": self.chaos_potential,
            "stability": self.anchor_stability,
            "coherence": coherence,
            "emotional_maturity": self.emotional_maturity,
            "available_power": self.available_power,
            "power_capacity": self.power_capacity,
            "efficiency": self.reality_tap_efficiency,
            "learning_rate": self.learning_rate,
            "agency_level": self.agency_level,
            "capabilities": self.capabilities
        }

    def __repr__(self) -> str:
        status = self.get_status()
        health = self.system_health.value
        return (f"EnhancedRyokoSeed(name='{self.name}', phase='{status['phase']}', "
                f"stage={status['growth_stage']}, aspects={status['total_aspects']}, "
                f"health={health}, quantum_chaos=True)")