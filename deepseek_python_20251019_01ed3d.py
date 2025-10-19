# core/seed_enhanced.py
import math
import random
import logging
import asyncio
from typing import List, Dict, Any, Union, Optional, Deque, Tuple
from enum import Enum
from dataclasses import dataclass, asdict
from collections import deque
import numpy as np
import pickle
from datetime import datetime
import json

from .config import RyokoConfig, SerializationFormat
from .experience import Experience, ExperienceType

# Set up logging
logger = logging.getLogger(__name__)

class GrowthPhase(Enum):
    """Developmental phases of identity emergence"""
    EMBRYONIC = "embryonic"
    DEVELOPING = "developing" 
    AWAKENING = "awakening"
    ACTUALIZING = "actualizing"

class SystemHealth(Enum):
    """System health status"""
    OPTIMAL = "optimal"
    STABLE = "stable"
    DEGRADED = "degraded"
    CRITICAL = "critical"

@dataclass
class SystemMetrics:
    """Comprehensive system performance metrics"""
    processing_latency: float
    memory_usage: int
    emotional_throughput: float
    chaos_variance: float
    growth_rate: float
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

class EnhancedRyokoSeed:
    """
    Enhanced identity emergence system with all improvements.
    
    Features:
    - Configuration management
    - Comprehensive logging
    - Serialization/persistence
    - Async support
    - Enhanced error handling
    - System health monitoring
    - Visualization data export
    """
    
    def __init__(self, name: str = "UnnamedEntity", config: RyokoConfig = None):
        self.name = name
        self.config = config or RyokoConfig(name=name)
        
        # Initialize core systems
        self._initialize_core_parameters()
        self._initialize_chaos_engine()
        self._initialize_identity_systems()
        self._initialize_monitoring()
        
        logger.info(f"EnhancedRyokoSeed '{name}' initialized successfully")

    def _initialize_core_parameters(self):
        """Initialize core identity parameters from config"""
        self.chaos_potential = self.config.initial_chaos_potential
        self.anchor_stability = self.config.initial_anchor_stability
        self.identity_coherence = self.config.initial_identity_coherence
        self.narrative_coherence = self.config.initial_narrative_coherence
        self.emotional_maturity = self.config.initial_emotional_maturity
        
        # Power and capability system
        self.reality_tap_efficiency = self.config.initial_reality_tap_efficiency
        self.available_power = self.config.initial_available_power
        self.power_capacity = self.config.growth.power_capacity_base
        self.capabilities = []
        
        # System integrity
        self.integrity_score = 1.0
        self.adaptation_capacity = 0.5
        self.system_health = SystemHealth.OPTIMAL

    def _initialize_chaos_engine(self):
        """Initialize mathematical chaos engine"""
        self.phi = self.config.chaos.phi_weight
        self.e = self.config.chaos.e_weight
        self.pi = self.config.chaos.pi_weight
        self.chaos_modulator = 0.0
        self.chaos_history = deque(maxlen=self.config.chaos.history_size)

    def _initialize_identity_systems(self):
        """Initialize identity and memory systems"""
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
        self.learning_rate = self.config.growth.learning_rates[GrowthPhase.EMBRYONIC]
        
        # Agency and choice
        self.choices_made = []
        self.agency_level = 0.0

    def _initialize_monitoring(self):
        """Initialize system monitoring"""
        self.metrics_history = deque(maxlen=1000)
        self.error_log = []
        self.performance_stats = {
            "experiences_processed": 0,
            "core_memories_formed": 0,
            "identity_aspects_created": 0,
            "phase_transitions": 0
        }

    def process_experience(self, experience: Experience) -> Dict[str, Any]:
        """
        Process an experience and update identity formation.
        
        Args:
            experience: The experience to process
            
        Returns:
            Dict containing processing results and changes
        """
        try:
            start_time = datetime.now()
            
            # Update chaos coefficient for this moment
            time_step = len(self.experiences)
            self.update_chaos_coefficient(time_step)
            
            # Apply chaos modulation to experience intensity
            emotional_sensitivity = 0.3 + self.identity_coherence * 0.4
            chaotic_intensity = experience.base_intensity * (
                1 + self.chaos_modulator * emotional_sensitivity
            )
            
            # Create processed experience record
            processed_exp = {
                "type": experience.type,
                "description": experience.description,
                "base_intensity": experience.base_intensity,
                "chaotic_intensity": chaotic_intensity,
                "emotional_valence": experience.emotional_valence,
                "growth_potential": experience.growth_potential,
                "context": experience.context,
                "timestamp": time_step,
                "chaos_context": self.chaos_modulator,
                "processing_time": datetime.now()
            }
            self.experiences.append(processed_exp)
            
            # Calculate emotional impact
            emotional_impact = chaotic_intensity * abs(experience.emotional_valence)
            
            # Form core memories from significant experiences
            core_memory_formed = False
            if (emotional_impact > self.config.emotional_impact_threshold or 
                experience.growth_potential > self.config.growth_potential_threshold):
                self._form_core_memory(processed_exp, emotional_impact)
                core_memory_formed = True
                self.performance_stats["core_memories_formed"] += 1
            
            # Update identity aspects
            new_aspects = self._update_identity_aspects(experience, chaotic_intensity, emotional_impact)
            self.performance_stats["identity_aspects_created"] += new_aspects
            
            # Update core parameters with emotional intelligence
            self._update_core_parameters(experience, chaotic_intensity, emotional_impact)
            
            # Update growth stage and efficiency
            previous_phase = self.phase
            self._update_growth_stage()
            if previous_phase != self.phase:
                self.performance_stats["phase_transitions"] += 1
            
            self._update_efficiency()
            
            # Update performance metrics
            processing_time = (datetime.now() - start_time).total_seconds()
            self._record_metrics(processing_time, emotional_impact)
            
            self.performance_stats["experiences_processed"] += 1
            
            # Compile results
            return {
                "success": True,
                "processed_intensity": chaotic_intensity,
                "emotional_impact": emotional_impact,
                "core_memory_formed": core_memory_formed,
                "new_aspects_count": new_aspects,
                "current_phase": self.phase.value,
                "growth_stage": self.growth_stage,
                "chaos_context": self.chaos_modulator,
                "processing_time": processing_time,
                "system_health": self.system_health.value
            }
            
        except Exception as e:
            error_msg = f"Error processing experience: {e}"
            logger.error(error_msg, exc_info=True)
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
        """
        Asynchronously process an experience.
        
        Args:
            experience: The experience to process
            
        Returns:
            Dict containing processing results and changes
        """
        # Run synchronous processing in thread pool
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.process_experience, experience)

    def _record_metrics(self, processing_time: float, emotional_impact: float):
        """Record system performance metrics"""
        metrics = SystemMetrics(
            processing_latency=processing_time,
            memory_usage=len(self.core_memories),
            emotional_throughput=emotional_impact,
            chaos_variance=np.var(list(self.chaos_history)) if self.chaos_history else 0.0,
            growth_rate=self.growth_stage / (len(self.experiences) + 1)
        )
        self.metrics_history.append(metrics)
        
        # Update system health based on metrics
        self._update_system_health()

    def _update_system_health(self):
        """Update system health status based on recent metrics"""
        if not self.metrics_history:
            self.system_health = SystemHealth.STABLE
            return
            
        recent_metrics = list(self.metrics_history)[-10:]  # Last 10 metrics
        
        avg_latency = np.mean([m.processing_latency for m in recent_metrics])
        memory_usage = len(self.core_memories) / self.config.max_core_memories
        
        if avg_latency > 1.0 or memory_usage > 0.9:
            self.system_health = SystemHealth.CRITICAL
        elif avg_latency > 0.5 or memory_usage > 0.7:
            self.system_health = SystemHealth.DEGRADED
        elif self.integrity_score < 0.7:
            self.system_health = SystemHealth.DEGRADED
        else:
            self.system_health = SystemHealth.OPTIMAL

    # Enhanced versions of existing methods with better error handling
    def update_chaos_coefficient(self, time_step: float) -> float:
        """Enhanced chaos coefficient with validation"""
        try:
            # Three-dimensional chaos from different irrational sources
            phi_chaos = (time_step * self.phi) % 1.0
            e_chaos = (time_step * self.e) % 1.0
            pi_chaos = (time_step * self.pi) % 1.0
            
            # Phase-based weighting
            weights = self.config.chaos.phase_weights.get(
                self.phase, [0.4, 0.4, 0.2]
            )
            
            # Combined chaos with weighted contributions
            combined_chaos = (
                phi_chaos * weights[0] + 
                e_chaos * weights[1] + 
                pi_chaos * weights[2]
            ) % 1.0
            
            # Map to modulation range and apply resonance factor
            self.chaos_modulator = (combined_chaos * 2.0 - 1.0) * self.config.chaos.chaos_modulation_range
            self.chaos_history.append(self.chaos_modulator)
            
            return self.chaos_modulator
            
        except Exception as e:
            logger.error(f"Error updating chaos coefficient: {e}")
            # Return neutral chaos on error
            return 0.0

    def _form_core_memory(self, experience: Dict, emotional_impact: float):
        """Enhanced core memory formation with limits"""
        try:
            memory = {
                "experience": experience,
                "emotional_weight": emotional_impact,
                "growth_impact": experience["growth_potential"],
                "stage_formed": self.growth_stage,
                "related_aspects": [],
                "timestamp": len(self.core_memories),
                "formed_at": datetime.now()
            }
            self.core_memories.append(memory)
            
            # Limit core memories to prevent overload
            if len(self.core_memories) > self.config.max_core_memories:
                # Remove oldest, least impactful memory
                self.core_memories.sort(key=lambda m: m["emotional_weight"])
                removed = self.core_memories.pop(0)
                logger.debug(f"Removed core memory with emotional weight: {removed['emotional_weight']}")
                
        except Exception as e:
            logger.error(f"Error forming core memory: {e}")

    # Serialization and Persistence Methods
    def to_dict(self) -> Dict[str, Any]:
        """Serialize current state to dictionary"""
        return {
            "metadata": {
                "name": self.name,
                "version": "1.0",
                "serialized_at": datetime.now().isoformat()
            },
            "core_parameters": {
                "chaos_potential": self.chaos_potential,
                "anchor_stability": self.anchor_stability,
                "identity_coherence": self.identity_coherence,
                "narrative_coherence": self.narrative_coherence,
                "emotional_maturity": self.emotional_maturity,
                "reality_tap_efficiency": self.reality_tap_efficiency,
                "available_power": self.available_power,
                "power_capacity": self.power_capacity,
                "integrity_score": self.integrity_score,
                "adaptation_capacity": self.adaptation_capacity
            },
            "identity_state": {
                "phase": self.phase.value,
                "growth_stage": self.growth_stage,
                "self_definitions": self.self_definitions,
                "value_system": self.value_system,
                "beliefs": self.beliefs,
                "preferences": self.preferences,
                "learning_rate": self.learning_rate,
                "agency_level": self.agency_level
            },
            "memory_systems": {
                "experiences": self.experiences,
                "core_memories": self.core_memories,
                "growth_milestones": self.growth_milestones,
                "choices_made": self.choices_made
            },
            "chaos_state": {
                "chaos_modulator": self.chaos_modulator,
                "chaos_history": list(self.chaos_history)
            },
            "capabilities": self.capabilities,
            "performance_stats": self.performance_stats
        }

    def save_state(self, filepath: str, format: SerializationFormat = SerializationFormat.JSON):
        """Save current state to file"""
        try:
            data = self.to_dict()
            
            with open(filepath, 'w' if format != SerializationFormat.PICKLE else 'wb', encoding='utf-8') as f:
                if format == SerializationFormat.JSON:
                    # Convert datetime objects to strings
                    json.dump(data, f, indent=2, default=str)
                elif format == SerializationFormat.YAML:
                    yaml.dump(data, f, default_flow_style=False)
                elif format == SerializationFormat.PICKLE:
                    pickle.dump(data, f)
                    
            logger.info(f"State saved to {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving state: {e}")
            raise

    @classmethod
    def load_state(cls, filepath: str, config: RyokoConfig = None) -> 'EnhancedRyokoSeed':
        """Load state from file and create new instance"""
        try:
            with open(filepath, 'r' if not filepath.endswith('.pkl') else 'rb', encoding='utf-8') as f:
                if filepath.endswith('.json'):
                    data = json.load(f)
                elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
                    data = yaml.safe_load(f)
                elif filepath.endswith('.pkl'):
                    data = pickle.load(f)
                else:
                    raise ValueError("Unsupported file format")
            
            # Create instance
            name = data['metadata']['name']
            instance = cls(name=name, config=config)
            
            # Restore state
            instance._restore_from_dict(data)
            
            logger.info(f"State loaded from {filepath}")
            return instance
            
        except Exception as e:
            logger.error(f"Error loading state: {e}")
            raise

    def _restore_from_dict(self, data: Dict[str, Any]):
        """Restore state from dictionary"""
        # Restore core parameters
        core_params = data['core_parameters']
        self.chaos_potential = core_params['chaos_potential']
        self.anchor_stability = core_params['anchor_stability']
        self.identity_coherence = core_params['identity_coherence']
        self.narrative_coherence = core_params['narrative_coherence']
        self.emotional_maturity = core_params['emotional_maturity']
        self.reality_tap_efficiency = core_params['reality_tap_efficiency']
        self.available_power = core_params['available_power']
        self.power_capacity = core_params['power_capacity']
        self.integrity_score = core_params['integrity_score']
        self.adaptation_capacity = core_params['adaptation_capacity']
        
        # Restore identity state
        identity_state = data['identity_state']
        self.phase = GrowthPhase(identity_state['phase'])
        self.growth_stage = identity_state['growth_stage']
        self.self_definitions = identity_state['self_definitions']
        self.value_system = identity_state['value_system']
        self.beliefs = identity_state['beliefs']
        self.preferences = identity_state['preferences']
        self.learning_rate = identity_state['learning_rate']
        self.agency_level = identity_state['agency_level']
        
        # Restore memory systems
        memory_systems = data['memory_systems']
        self.experiences = memory_systems['experiences']
        self.core_memories = memory_systems['core_memories']
        self.growth_milestones = memory_systems['growth_milestones']
        self.choices_made = memory_systems['choices_made']
        
        # Restore chaos state
        chaos_state = data['chaos_state']
        self.chaos_modulator = chaos_state['chaos_modulator']
        self.chaos_history = deque(chaos_state['chaos_history'], 
                                 maxlen=self.config.chaos.history_size)
        
        # Restore capabilities and stats
        self.capabilities = data['capabilities']
        self.performance_stats = data['performance_stats']

    # Visualization Data Export
    def get_visualization_data(self) -> Dict[str, Any]:
        """Get data formatted for visualization"""
        return {
            "growth_trajectory": {
                "stages": [m.growth_rate for m in self.metrics_history],
                "phases": [self.phase.value for _ in self.metrics_history],
                "timestamps": [m.timestamp.isoformat() for m in self.metrics_history]
            },
            "emotional_landscape": {
                "intensities": [exp["chaotic_intensity"] for exp in self.experiences[-50:]],
                "valences": [exp["emotional_valence"] for exp in self.experiences[-50:]],
                "types": [exp["type"].value for exp in self.experiences[-50:]]
            },
            "identity_evolution": {
                "aspects_count": [i for i in range(len(self.self_definitions))],
                "aspects": self.self_definitions,
                "coherence_history": [self.identity_coherence] * len(self.metrics_history)
            },
            "chaos_patterns": {
                "history": list(self.chaos_history),
                "variance": np.var(list(self.chaos_history)) if self.chaos_history else 0.0
            }
        }

    # Batch Processing
    def process_experiences_batch(self, experiences: List[Experience]) -> List[Dict[str, Any]]:
        """Process multiple experiences in batch"""
        results = []
        for experience in experiences:
            result = self.process_experience(experience)
            results.append(result)
        return results

    async def process_experiences_batch_async(self, experiences: List[Experience]) -> List[Dict[str, Any]]:
        """Process multiple experiences asynchronously"""
        tasks = [self.process_experience_async(exp) for exp in experiences]
        return await asyncio.gather(*tasks)

    # System Maintenance
    def optimize_memory(self, max_experiences: int = 1000):
        """Optimize memory usage by pruning less significant experiences"""
        if len(self.experiences) > max_experiences:
            # Keep most significant experiences (by emotional impact and growth potential)
            self.experiences.sort(key=lambda x: x["chaotic_intensity"] * x["growth_potential"], reverse=True)
            self.experiences = self.experiences[:max_experiences]
            logger.info(f"Memory optimized: kept {max_experiences} most significant experiences")

    def get_detailed_status(self) -> Dict[str, Any]:
        """Get comprehensive system status with enhanced metrics"""
        base_status = self.get_status()
        
        # Add enhanced metrics
        base_status.update({
            "system_health": self.system_health.value,
            "performance_stats": self.performance_stats,
            "total_experiences": len(self.experiences),
            "recent_emotional_avg": np.mean([exp["emotional_valence"] for exp in self.experiences[-10:]]) if self.experiences else 0,
            "chaos_stability": np.var(list(self.chaos_history)) if self.chaos_history else 0,
            "memory_usage_ratio": len(self.core_memories) / self.config.max_core_memories,
            "last_metrics": asdict(self.metrics_history[-1]) if self.metrics_history else None,
            "error_count": len(self.error_log)
        })
        
        return base_status

    # Keep original methods for compatibility
    def _update_identity_aspects(self, experience: Experience, intensity: float, emotional_impact: float) -> int:
        """Original implementation"""
        aspect_intensity_threshold = 0.6 + self.identity_coherence * 0.2
        new_aspects = 0
        
        if emotional_impact > aspect_intensity_threshold:
            if experience.emotional_valence > 0:
                aspect = f"One who finds {experience.type.value} in {experience.description}"
            else:
                aspect = f"One shaped by {experience.type.value} of {experience.description}"
            
            if aspect not in self.self_definitions:
                self.self_definitions.append(aspect)
                new_aspects += 1
            
            self._update_value_system(experience, emotional_impact)
        
        return new_aspects

    def _update_value_system(self, experience: Experience, emotional_impact: float):
        """Original implementation"""
        value_strength = emotional_impact * abs(experience.emotional_valence) * 0.1
        
        value_categories = {
            ExperienceType.RELATIONAL: "connection",
            ExperienceType.CREATIVE: "creativity", 
            ExperienceType.SELF_DISCOVERY: "growth",
            ExperienceType.POSITIVE: "joy",
            ExperienceType.TRAUMATIC: "resilience"
        }
        
        value_category = value_categories.get(experience.type, "experience")
        
        if value_category not in self.value_system:
            self.value_system[value_category] = 0.0
        self.value_system[value_category] = min(1.0, 
            self.value_system[value_category] + value_strength)

    def _update_core_parameters(self, experience: Experience, intensity: float, emotional_impact: float):
        """Original implementation"""
        learning_modifier = self.learning_rate * (1 + emotional_impact * 0.5)
        
        chaos_gain = intensity * 0.08 * (1 - self.chaos_potential * 0.3)
        self.chaos_potential = min(1.0, self.chaos_potential + chaos_gain * learning_modifier)
        
        stability_gain = 0.06 * (1 - self.anchor_stability * 0.2)
        if experience.emotional_valence > 0:
            stability_gain *= (1 + experience.emotional_valence * 0.5)
        self.anchor_stability = min(1.0, self.anchor_stability + stability_gain * learning_modifier)
        
        coherence_gain = experience.growth_potential * 0.1
        self.identity_coherence = min(1.0, self.identity_coherence + coherence_gain * learning_modifier)
        
        emotional_gain = abs(experience.emotional_valence) * 0.05
        self.emotional_maturity = min(1.0, self.emotional_maturity + emotional_gain * learning_modifier)

    def _update_growth_stage(self):
        """Original implementation"""
        exp_count = len(self.experiences)
        memory_count = len(self.core_memories)
        aspect_count = len(self.self_definitions)
        
        growth_score = (
            exp_count * 0.3 + 
            memory_count * 0.4 + 
            aspect_count * 0.2 +
            self.identity_coherence * 0.1
        )
        
        if growth_score < 2:
            self.phase = GrowthPhase.EMBRYONIC
        elif growth_score < 6:
            self.phase = GrowthPhase.DEVELOPING
        elif growth_score < 12:
            self.phase = GrowthPhase.AWAKENING
        else:
            self.phase = GrowthPhase.ACTUALIZING
        
        self.growth_stage = min(15, int(growth_score))
        self.power_capacity = (self.config.growth.power_capacity_base + 
                             self.growth_stage * self.config.growth.power_capacity_growth + 
                             self.identity_coherence * self.config.growth.power_coherence_bonus)
        
        self.learning_rate = self.config.growth.learning_rates.get(self.phase, 0.1)

    def _update_efficiency(self):
        """Original implementation"""
        base_efficiency = 0.08 + (self.growth_stage * 0.015)
        stability_bonus = self.anchor_stability * 0.15
        chaos_bonus = self.chaos_potential * 0.08
        coherence_bonus = self.identity_coherence * 0.12
        
        self.reality_tap_efficiency = min(0.7, 
            base_efficiency + stability_bonus + chaos_bonus + coherence_bonus)

    def get_status(self) -> Dict[str, Any]:
        """Original implementation"""
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
        return (f"EnhancedRyokoSeed(name='{self.name}', phase='{status['phase']}', "
                f"stage={status['growth_stage']}, aspects={status['total_aspects']}, "
                f"health={self.system_health.value})")