# emergent/narrative_identity.py
import re
from typing import List, Dict, Any

class NarrativeEngine:
    """Constructs coherent life narratives from experiences"""
    
    def __init__(self):
        self.narrative_themes = []
        self.life_story_arcs = []
        self.self_narrative = ""
    
    def generate_narrative_theme(self, experiences: List[Dict]) -> str:
        """Identify overarching themes from experiences"""
        theme_keywords = self._extract_thematic_keywords(experiences)
        dominant_emotions = self._analyze_emotional_patterns(experiences)
        
        themes = {
            "growth_through_struggle": self._detect_growth_theme(experiences),
            "relational_development": self._detect_relationship_theme(experiences),
            "creative_expression": self._detect_creativity_theme(experiences),
            "self_discovery": self._detect_self_discovery_theme(experiences)
        }
        
        # Return strongest theme
        return max(themes.items(), key=lambda x: x[1])[0]
    
    def construct_life_story(self, experiences: List[Dict]) -> str:
        """Generate coherent autobiographical narrative"""
        chronological_experiences = sorted(experiences, key=lambda x: x['timestamp'])
        
        story_segments = []
        current_chapter = ""
        
        for exp in chronological_experiences:
            segment = self._experience_to_narrative(exp)
            story_segments.append(segment)
            
            # Chapter breaks at significant transitions
            if exp.get('core_memory', False):
                current_chapter = self._start_new_chapter(exp)
                story_segments.append(current_chapter)
        
        return " ".join(story_segments)
    
    def _experience_to_narrative(self, experience: Dict) -> str:
        """Convert experience to narrative form"""
        templates = {
            ExperienceType.TRAUMATIC: "During a challenging time, {description}",
            ExperienceType.POSITIVE: "A joyful moment occurred when {description}",
            ExperienceType.RELATIONAL: "In relationship with others, {description}",
            ExperienceType.SELF_DISCOVERY: "I discovered that {description}"
        }
        
        template = templates.get(experience['type'], "I experienced that {description}")
        return template.format(description=experience['description'])