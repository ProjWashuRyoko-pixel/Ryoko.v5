# applications/therapeutic_enhanced.py
class TraumaRecoveryAssistant:
    """Enhanced therapeutic application for trauma recovery"""
    
    def assess_recovery_progress(self, entity) -> Dict:
        """Assess recovery progress from traumatic experiences"""
        trauma_experiences = [
            exp for exp in entity.experiences 
            if exp['type'] == ExperienceType.TRAUMATIC
        ]
        
        recovery_indicators = {
            'trauma_integration': self._calculate_integration_score(trauma_experiences),
            'emotional_regulation': entity.emotional_maturity,
            'post_traumatic_growth': self._calculate_ptg_score(entity),
            'narrative_coherence': self._assess_trauma_narrative(entity)
        }
        
        return recovery_indicators
    
    def generate_recovery_plan(self, entity) -> List[Dict]:
        """Generate personalized recovery plan"""
        plan = []
        
        # Based on recovery stage
        if entity.growth_stage < 5:
            plan.append({
                'type': 'stabilization',
                'activities': ['grounding_exercises', 'safety_planning'],
                'goals': ['emotional_regulation', 'basic_trust']
            })
        else:
            plan.append({
                'type': 'integration', 
                'activities': ['narrative_work', 'meaning_making'],
                'goals': ['coherent_identity', 'future_oriented']
            })
        
        return plan