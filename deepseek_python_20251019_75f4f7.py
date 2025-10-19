# core/experience.py
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from enum import Enum
import uuid
from datetime import datetime

class ExperienceType(Enum):
    """Enhanced experience types with subcategories"""
    TRAUMATIC = "traumatic"
    POSITIVE = "positive" 
    RELATIONAL = "relational"
    SELF_DISCOVERY = "self_discovery"
    CREATIVE = "creative"
    CHALLENGE = "challenge"
    NEUTRAL = "neutral"
    TRANSFORMATIVE = "transformative"
    SPIRITUAL = "spiritual"
    PHYSICAL = "physical"

@dataclass
class Experience:
    """Enhanced experience representation"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: ExperienceType
    description: str
    base_intensity: float  # 0.0 to 1.0
    emotional_valence: float  # -1.0 to +1.0
    growth_potential: float  # 0.0 to 1.0
    duration: float = 1.0  # Relative duration factor
    complexity: float = 0.5  # 0.0 to 1.0
    novelty: float = 0.5  # 0.0 to 1.0
    context: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        if self.context is None:
            self.context = {}
        
        # Validate ranges
        self.base_intensity = max(0.0, min(1.0, self.base_intensity))
        self.emotional_valence = max(-1.0, min(1.0, self.emotional_valence))
        self.growth_potential = max(0.0, min(1.0, self.growth_potential))
        self.duration = max(0.1, self.duration)
        self.complexity = max(0.0, min(1.0, self.complexity))
        self.novelty = max(0.0, min(1.0, self.novelty))
        
        # Auto-generate some tags based on type and intensity
        if not self.tags:
            self._generate_tags()
    
    def _generate_tags(self):
        """Generate relevant tags based on experience properties"""
        # Intensity tags
        if self.base_intensity > 0.8:
            self.tags.append("intense")
        elif self.base_intensity < 0.3:
            self.tags.append("mild")
        
        # Valence tags
        if self.emotional_valence > 0.6:
            self.tags.append("positive")
        elif self.emotional_valence < -0.6:
            self.tags.append("negative")
        else:
            self.tags.append("neutral-valence")
        
        # Type-specific tags
        self.tags.append(f"type:{self.type.value}")
        
        # Growth potential tags
        if self.growth_potential > 0.7:
            self.tags.append("transformative-potential")
    
    @classmethod
    def create_traumatic(cls, description: str, intensity: float, 
                        recovery_potential: float = 0.3, **kwargs) -> 'Experience':
        """Factory method for traumatic experiences"""
        return cls(
            type=ExperienceType.TRAUMATIC,
            description=description,
            base_intensity=intensity,
            emotional_valence=-0.8,
            growth_potential=recovery_potential,
            tags=["traumatic", "challenging"] + kwargs.pop('tags', []),
            **kwargs
        )
    
    @classmethod
    def create_breakthrough(cls, description: str, insight_level: float = 0.8, **kwargs) -> 'Experience':
        """Factory method for breakthrough experiences"""
        return cls(
            type=ExperienceType.SELF_DISCOVERY,
            description=description,
            base_intensity=0.7,
            emotional_valence=0.9,
            growth_potential=insight_level,
            tags=["breakthrough", "insightful"] + kwargs.pop('tags', []),
            **kwargs
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            "id": self.id,
            "type": self.type.value,
            "description": self.description,
            "base_intensity": self.base_intensity,
            "emotional_valence": self.emotional_valence,
            "growth_potential": self.growth_potential,
            "duration": self.duration,
            "complexity": self.complexity,
            "novelty": self.novelty,
            "context": self.context,
            "tags": self.tags,
            "timestamp": self.timestamp.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Experience':
        """Create from dictionary"""
        data = data.copy()
        data['type'] = ExperienceType(data['type'])
        data['timestamp'] = datetime.fromisoformat(data['timestamp'])
        return cls(**data)