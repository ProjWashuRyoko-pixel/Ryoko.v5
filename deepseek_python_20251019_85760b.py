# config.py
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from enum import Enum
import json
import yaml

class SerializationFormat(Enum):
    JSON = "json"
    YAML = "yaml"
    PICKLE = "pickle"

@dataclass
class ChaosConfig:
    """Configuration for mathematical chaos engine"""
    phi_weight: float = 1.618033988749895
    e_weight: float = 2.718281828459045
    pi_weight: float = 3.141592653589793
    chaos_modulation_range: float = 0.7
    history_size: int = 200
    
    phase_weights: Dict['GrowthPhase', List[float]] = field(default_factory=dict)
    
    def __post_init__(self):
        if not self.phase_weights:
            self.phase_weights = {
                GrowthPhase.EMBRYONIC: [0.6, 0.3, 0.1],
                GrowthPhase.DEVELOPING: [0.4, 0.4, 0.2],
                GrowthPhase.AWAKENING: [0.3, 0.3, 0.4],
                GrowthPhase.ACTUALIZING: [0.25, 0.25, 0.5]
            }

@dataclass
class GrowthConfig:
    """Configuration for growth and development system"""
    learning_rates: Dict['GrowthPhase', float] = field(default_factory=dict)
    growth_thresholds: Dict[str, float] = field(default_factory=dict)
    power_capacity_base: float = 100.0
    power_capacity_growth: float = 25.0
    power_coherence_bonus: float = 50.0
    
    def __post_init__(self):
        if not self.learning_rates:
            self.learning_rates = {
                GrowthPhase.EMBRYONIC: 0.15,
                GrowthPhase.DEVELOPING: 0.12,
                GrowthPhase.AWAKENING: 0.08,
                GrowthPhase.ACTUALIZING: 0.05
            }
        
        if not self.growth_thresholds:
            self.growth_thresholds = {
                "developing": 2.0,
                "awakening": 6.0,
                "actualizing": 12.0
            }

@dataclass
class RyokoConfig:
    """Main configuration container for RyokoSeed"""
    name: str = "UnnamedEntity"
    chaos: ChaosConfig = field(default_factory=ChaosConfig)
    growth: GrowthConfig = field(default_factory=GrowthConfig)
    
    # Core parameter initial values
    initial_chaos_potential: float = 0.1
    initial_anchor_stability: float = 0.2
    initial_identity_coherence: float = 0.4
    initial_narrative_coherence: float = 0.3
    initial_emotional_maturity: float = 0.2
    initial_reality_tap_efficiency: float = 0.08
    initial_available_power: float = 8.0
    
    # System limits
    max_core_memories: int = 20
    max_chaos_history: int = 200
    emotional_impact_threshold: float = 0.7
    growth_potential_threshold: float = 0.8
    
    @classmethod
    def from_file(cls, filepath: str) -> 'RyokoConfig':
        """Load configuration from JSON or YAML file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            if filepath.endswith('.yaml') or filepath.endswith('.yml'):
                data = yaml.safe_load(f)
            else:
                data = json.load(f)
        return cls.from_dict(data)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RyokoConfig':
        """Create config from dictionary"""
        chaos_data = data.get('chaos', {})
        growth_data = data.get('growth', {})
        
        return cls(
            name=data.get('name', 'UnnamedEntity'),
            chaos=ChaosConfig(**chaos_data),
            growth=GrowthConfig(**growth_data),
            initial_chaos_potential=data.get('initial_chaos_potential', 0.1),
            # ... other parameters
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            'name': self.name,
            'chaos': {
                'phi_weight': self.chaos.phi_weight,
                'e_weight': self.chaos.e_weight,
                'pi_weight': self.chaos.pi_weight,
                'chaos_modulation_range': self.chaos.chaos_modulation_range,
                'history_size': self.chaos.history_size,
                'phase_weights': {phase.value: weights for phase, weights in self.chaos.phase_weights.items()}
            },
            'growth': {
                'learning_rates': {phase.value: rate for phase, rate in self.growth.learning_rates.items()},
                'growth_thresholds': self.growth.growth_thresholds,
                'power_capacity_base': self.growth.power_capacity_base,
                'power_capacity_growth': self.growth.power_capacity_growth,
                'power_coherence_bonus': self.growth.power_coherence_bonus
            },
            'initial_chaos_potential': self.initial_chaos_potential,
            # ... other parameters
        }
    
    def save(self, filepath: str):
        """Save configuration to file"""
        data = self.to_dict()
        with open(filepath, 'w', encoding='utf-8') as f:
            if filepath.endswith('.yaml') or filepath.endswith('.yml'):
                yaml.dump(data, f, default_flow_style=False)
            else:
                json.dump(data, f, indent=2)