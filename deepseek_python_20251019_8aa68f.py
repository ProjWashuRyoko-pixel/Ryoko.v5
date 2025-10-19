# applications/educational_enhanced.py
class AdaptiveLearningCoach:
    """AI learning coach using Ryoko identity model"""
    
    def __init__(self):
        self.learning_styles = {}
        self.knowledge_gaps = set()
        self.motivation_factors = {}
    
    def analyze_learning_style(self, entity) -> str:
        """Analyze preferred learning style based on experiences"""
        creative_exps = len([e for e in entity.experiences 
                           if e['type'] == ExperienceType.CREATIVE])
        relational_exps = len([e for e in entity.experiences 
                             if e['type'] == ExperienceType.RELATIONAL])
        
        if creative_exps > relational_exps:
            return "creative_explorer"
        elif relational_exps > creative_exps:
            return "social_learner" 
        else:
            return "balanced_learner"
    
    def recommend_learning_path(self, entity, subject: str) -> List[Dict]:
        """Generate personalized learning path"""
        learning_style = self.analyze_learning_style(entity)
        
        recommendations = {
            "creative_explorer": [
                {"type": "project_based", "description": "Create a project about..."},
                {"type": "visual_learning", "description": "Use diagrams and mind maps"}
            ],
            "social_learner": [
                {"type": "group_study", "description": "Join study group on..."},
                {"type": "teaching_others", "description": "Explain concept to peers"}
            ]
        }
        
        return recommendations.get(learning_style, [])