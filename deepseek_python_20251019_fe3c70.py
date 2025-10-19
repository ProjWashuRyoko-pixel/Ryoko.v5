# core/predictive_growth.py
import numpy as np
from sklearn.linear_model import BayesianRidge
from typing import Dict, List, Optional

class GrowthPredictor:
    """Machine learning-powered growth trajectory prediction"""
    
    def __init__(self):
        self.growth_model = BayesianRidge()
        self.is_trained = False
        self.feature_history = []
        self.growth_history = []
    
    def extract_growth_features(self, entity_status: Dict) -> List[float]:
        """Extract features for growth prediction"""
        return [
            entity_status['total_experiences'],
            entity_status['core_memories'],
            entity_status['total_aspects'],
            entity_status['identity_coherence'],
            entity_status['emotional_maturity'],
            entity_status['chaos_level'],
            len(entity_status['value_system']),
            entity_status['growth_stage']
        ]
    
    def update_model(self, entity_status: Dict):
        """Update prediction model with new data"""
        features = self.extract_growth_features(entity_status)
        target = entity_status['growth_stage']
        
        self.feature_history.append(features)
        self.growth_history.append(target)
        
        if len(self.feature_history) > 10:  # Minimum training set
            X = np.array(self.feature_history)
            y = np.array(self.growth_history)
            self.growth_model.fit(X, y)
            self.is_trained = True
    
    def predict_growth_trajectory(self, entity_status: Dict, steps: int = 5) -> Dict:
        """Predict future growth trajectory"""
        if not self.is_trained:
            return {"error": "Model not yet trained"}
        
        current_features = self.extract_growth_features(entity_status)
        predictions = []
        uncertainties = []
        
        # Multi-step prediction
        for step in range(steps):
            # Predict next state (simplified - in reality would need state transition model)
            pred, std = self.growth_model.predict(
                [current_features], return_std=True
            )
            predictions.append(float(pred[0]))
            uncertainties.append(float(std[0]))
            
            # Update features for next prediction (simulated)
            current_features[-1] = pred[0]  # Update growth stage
        
        return {
            "predictions": predictions,
            "uncertainties": uncertainties,
            "confidence": 1.0 - np.mean(uncertainties) / np.max(predictions) if predictions else 0.0
        }