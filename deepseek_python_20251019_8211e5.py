# Consider adding a config class
@dataclass 
class RyokoConfig:
    chaos_weights: Dict[GrowthPhase, List[float]] = None
    learning_rates: Dict[GrowthPhase, float] = None
    growth_thresholds: Dict[str, float] = None
    
    def __post_init__(self):
        if self.chaos_weights is None:
            self.chaos_weights = {
                GrowthPhase.EMBRYONIC: [0.6, 0.3, 0.1],
                GrowthPhase.DEVELOPING: [0.4, 0.4, 0.2],
                # ... etc
            }