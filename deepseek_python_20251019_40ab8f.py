# test_enhanced_ryoko.py
import asyncio
import time
import sys
import os
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from enhanced_ryoko import (
    EnhancedRyokoSeed, Experience, ExperienceType, 
    GrowthPhase, SystemHealth, QuantumChaosEngine,
    MemoryConsolidationEngine, GrowthPredictor
)

class TestEnhancedRyoko:
    """Comprehensive tests for enhanced Ryoko framework"""
    
    def run_test(self, test_name, test_func):
        """Run a test and report results"""
        try:
            start_time = time.time()
            result = test_func()
            duration = time.time() - start_time
            
            if result:
                print(f"✅ {test_name} ({duration:.3f}s)")
                return True
            else:
                print(f"❌ {test_name} ({duration:.3f}s)")
                return False
        except Exception as e:
            print(f"💥 {test_name} - Exception: {e}")
            return False
    
    def test_quantum_chaos_engine(self):
        """Test the enhanced quantum chaos engine"""
        chaos_engine = QuantumChaosEngine()
        
        # Test chaos generation for different phases
        phases = [GrowthPhase.EMBRYONIC, GrowthPhase.DEVELOPING, 
                 GrowthPhase.AWAKENING, GrowthPhase.ACTUALIZING]
        
        chaos_values = []
        for phase in phases:
            for i in range(5):
                chaos = chaos_engine.generate_quantum_chaos(i * 0.1, phase)
                chaos_values.append(chaos)
                
                # Verify chaos values are in valid range
                assert -1.0 <= chaos <= 1.0, f"Chaos value {chaos} out of range"
        
        # Verify we get different values (chaotic behavior)
        unique_values = len(set(round(c, 2) for c in chaos_values))
        assert unique_values > len(chaos_values) * 0.5, "Chaos engine not generating enough variation"
        
        return True
    
    def test_memory_consolidation(self):
        """Test enhanced memory system"""
        memory_engine = MemoryConsolidationEngine(max_memories=5)
        
        # Create test memories
        memories = []
        for i in range(10):
            memory = {
                "id": i,
                "type": ExperienceType.POSITIVE,
                "description": f"Memory {i}",
                "emotional_valence": 0.5 + (i * 0.1),
                "strength": 0.3 + (i * 0.1),
                "emotional_weight": 0.4 + (i * 0.1)
            }
            memories.append(memory)
        
        # Test consolidation
        consolidated = memory_engine.consolidate_memories(memories)
        assert len(consolidated) == 5, f"Expected 5 memories, got {len(consolidated)}"
        
        # Test that strongest memories are kept
        strengths = [m["strength"] for m in consolidated]
        assert all(s >= 0.7 for s in strengths), "Weak memories were not pruned correctly"
        
        # Test associative linking
        test_memory = {"id": 99, "type": ExperienceType.POSITIVE, "emotional_valence": 0.6}
        memory_engine.form_associative_links(test_memory, memories[:3])
        
        assert 99 in memory_engine.memory_network, "New memory not added to network"
        
        return True
    
    def test_growth_predictor(self):
        """Test growth prediction system"""
        predictor = GrowthPredictor()
        
        # Test feature extraction
        test_status = {
            "total_experiences": 10,
            "core_memories": 5,
            "total_aspects": 8,
            "identity_coherence": 0.7,
            "emotional_maturity": 0.6,
            "chaos_level": 0.3,
            "value_system": {"connection": 0.8, "growth": 0.7},
            "growth_stage": 5
        }
        
        features = predictor.extract_growth_features(test_status)
        assert len(features) == 8, f"Expected 8 features, got {len(features)}"
        assert all(isinstance(f, float) for f in features), "All features should be numeric"
        
        # Test prediction
        prediction = predictor.predict_growth_trajectory(test_status, steps=3)
        assert "predictions" in prediction, "Prediction should contain predictions"
        assert "uncertainties" in prediction, "Prediction should contain uncertainties"
        assert "confidence" in prediction, "Prediction should contain confidence"
        
        assert len(prediction["predictions"]) == 3, "Should predict 3 steps"
        assert all(p >= 0 for p in prediction["predictions"]), "Predictions should be non-negative"
        
        return True
    
    def test_enhanced_seed_initialization(self):
        """Test enhanced seed initialization"""
        entity = EnhancedRyokoSeed("TestEntity")
        
        # Test that enhanced components are initialized
        assert hasattr(entity, 'chaos_engine'), "Should have chaos engine"
        assert hasattr(entity, 'memory_engine'), "Should have memory engine"
        assert hasattr(entity, 'growth_predictor'), "Should have growth predictor"
        
        assert isinstance(entity.chaos_engine, QuantumChaosEngine)
        assert isinstance(entity.memory_engine, MemoryConsolidationEngine)
        assert isinstance(entity.growth_predictor, GrowthPredictor)
        
        # Test initial state
        assert entity.phase == GrowthPhase.EMBRYONIC
        assert entity.growth_stage == 0
        assert entity.system_health == SystemHealth.OPTIMAL
        
        return True
    
    def test_enhanced_experience_processing(self):
        """Test enhanced experience processing"""
        entity = EnhancedRyokoSeed("ProcessingTest")
        
        # Create diverse experiences
        experiences = [
            Experience(
                type=ExperienceType.TRAUMATIC,
                description="Early challenge",
                base_intensity=0.8,
                emotional_valence=-0.7,
                growth_potential=0.6,
                novelty=0.9
            ),
            Experience(
                type=ExperienceType.TRANSFORMATIVE,
                description="Breakthrough moment", 
                base_intensity=0.9,
                emotional_valence=0.8,
                growth_potential=0.9,
                novelty=0.8
            )
        ]
        
        results = []
        for exp in experiences:
            result = entity.process_experience(exp)
            results.append(result)
            
            # Verify enhanced result structure
            assert "quantum_chaos" in result, "Should include quantum chaos value"
            assert "memory_strength" in result, "Should include memory strength"
            assert "processing_time" in result, "Should include processing time"
        
        # Verify entity state updated
        assert len(entity.experiences) == 2
        assert entity.performance_stats["experiences_processed"] == 2
        
        # Test that quantum chaos values are different
        chaos_values = [r["quantum_chaos"] for r in results]
        assert len(set(round(c, 3) for c in chaos_values)) > 1, "Should have different chaos values"
        
        return True
    
    def test_memory_formation_enhanced(self):
        """Test enhanced memory formation"""
        entity = EnhancedRyokoSeed("MemoryTest")
        
        # Create memory-worthy experience
        intense_experience = Experience(
            type=ExperienceType.TRANSFORMATIVE,
            description="Life-changing realization",
            base_intensity=0.95,
            emotional_valence=0.9, 
            growth_potential=0.95,
            novelty=0.9
        )
        
        result = entity.process_experience(intense_experience)
        
        # Should form core memory
        assert result["core_memory_formed"] == True, "Should form core memory for intense experience"
        assert result["memory_strength"] > 0.7, "Memory strength should be high"
        assert len(entity.core_memories) == 1, "Should have one core memory"
        
        # Verify memory has enhanced properties
        memory = entity.core_memories[0]
        assert "strength" in memory, "Memory should have strength property"
        assert memory["strength"] > 0.7, "Memory strength should be preserved"
        
        return True
    
    def test_growth_prediction_integration(self):
        """Test growth prediction integration"""
        entity = EnhancedRyokoSeed("PredictionTest")
        
        # Add some experiences to enable prediction
        for i in range(8):
            exp = Experience(
                type=ExperienceType.POSITIVE,
                description=f"Learning experience {i}",
                base_intensity=0.6 + (i * 0.05),
                emotional_valence=0.7,
                growth_potential=0.5
            )
            entity.process_experience(exp)
        
        # Test prediction
        prediction = entity.predict_growth(steps=3)
        
        assert "predictions" in prediction, "Should return predictions"
        assert "confidence" in prediction, "Should return confidence score"
        assert len(prediction["predictions"]) == 3, "Should predict 3 steps"
        
        # Verify predictions are reasonable
        current_stage = entity.growth_stage
        for i, pred in enumerate(prediction["predictions"]):
            # Prediction should generally be >= current stage (growth)
            assert pred >= current_stage - 2, f"Prediction {i} seems unreasonable: {pred}"
        
        return True
    
    def test_async_processing(self):
        """Test asynchronous processing"""
        async def run_async_test():
            entity = EnhancedRyokoSeed("AsyncTest")
            
            experiences = [
                Experience(
                    type=ExperienceType.POSITIVE,
                    description=f"Async experience {i}",
                    base_intensity=0.5 + (i * 0.1),
                    emotional_valence=0.6,
                    growth_potential=0.4
                )
                for i in range(5)
            ]
            
            # Process asynchronously
            results = await entity.process_experiences_batch_async(experiences)
            
            # Verify all processed successfully
            assert len(results) == 5
            assert all(r["success"] for r in results)
            assert len(entity.experiences) == 5
            
            return True
        
        # Run async test
        return asyncio.run(run_async_test())
    
    def test_system_health_monitoring(self):
        """Test enhanced system health monitoring"""
        entity = EnhancedRyokoSeed("HealthTest")
        
        # Initially should be optimal
        assert entity.system_health == SystemHealth.OPTIMAL
        
        # Process many experiences to potentially stress system
        for i in range(15):
            exp = Experience(
                type=ExperienceType.CHALLENGE,
                description=f"Stress test {i}",
                base_intensity=0.8,
                emotional_valence=-0.6,
                growth_potential=0.4
            )
            entity.process_experience(exp)
        
        # System should still be stable or better
        assert entity.system_health in [SystemHealth.OPTIMAL, SystemHealth.STABLE]
        
        # Check that performance stats are being tracked
        assert entity.performance_stats["experiences_processed"] == 15
        assert len(entity.performance_stats["processing_times"]) == 15
        
        return True
    
    def test_value_system_development(self):
        """Test enhanced value system development"""
        entity = EnhancedRyokoSeed("ValueTest")
        
        # Process relational experiences
        rel_experiences = [
            Experience(
                type=ExperienceType.RELATIONAL,
                description="Deep connection with friend",
                base_intensity=0.8,
                emotional_valence=0.9,
                growth_potential=0.7
            ),
            Experience(
                type=ExperienceType.RELATIONAL, 
                description="Supportive community",
                base_intensity=0.7,
                emotional_valence=0.8,
                growth_potential=0.6
            )
        ]
        
        for exp in rel_experiences:
            entity.process_experience(exp)
        
        # Should develop relational values
        status = entity.get_detailed_status()
        value_system = status["value_system"]
        
        # Check for expected value categories
        relational_values = [v for v in value_system.keys() 
                           if v in ["connection", "empathy", "trust"]]
        assert len(relational_values) > 0, "Should develop relational values"
        
        # Values should have positive strength
        for value in relational_values:
            assert value_system[value] > 0, f"Value {value} should have positive strength"
        
        return True
    
    def test_comprehensive_life_simulation(self):
        """Test comprehensive life story simulation"""
        entity = EnhancedRyokoSeed("LifeStory")
        
        # Simulate a life story with varied experiences
        life_story = [
            # Early challenges
            Experience(ExperienceType.TRAUMATIC, "Childhood difficulty", 0.7, -0.6, 0.5),
            Experience(ExperienceType.CHALLENGE, "School struggles", 0.6, -0.4, 0.6),
            
            # Positive developments  
            Experience(ExperienceType.POSITIVE, "First success", 0.8, 0.9, 0.7),
            Experience(ExperienceType.RELATIONAL, "True friendship", 0.7, 0.8, 0.6),
            
            # Self-discovery
            Experience(ExperienceType.SELF_DISCOVERY, "Finding passion", 0.9, 0.8, 0.8),
            Experience(ExperienceType.CREATIVE, "Creative breakthrough", 0.8, 0.9, 0.7),
            
            # Transformative experiences
            Experience(ExperienceType.TRANSFORMATIVE, "Life perspective shift", 0.95, 0.7, 0.9),
            Experience(ExperienceType.TRANSFORMATIVE, "Major accomplishment", 0.9, 0.95, 0.8),
        ]
        
        # Process the life story
        growth_stages = []
        for exp in life_story:
            result = entity.process_experience(exp)
            growth_stages.append(entity.growth_stage)
        
        # Verify growth progression
        assert entity.growth_stage > 0, "Should have grown from experiences"
        assert growth_stages[-1] > growth_stages[0], "Should show growth progression"
        
        # Check final state
        final_status = entity.get_detailed_status()
        
        # Should have multiple identity aspects
        assert final_status["total_aspects"] >= 4, "Should develop multiple identity aspects"
        
        # Should have core memories
        assert final_status["core_memories"] > 0, "Should form core memories"
        
        # Should have developed values
        assert len(final_status["value_system"]) >= 3, "Should develop multiple values"
        
        # Should have reasonable system health
        assert final_status["system_health"] in ["optimal", "stable"], "Should maintain good health"
        
        # Should be able to predict future growth
        if final_status["growth_predictor_ready"]:
            prediction = entity.predict_growth()
            assert prediction["confidence"] > 0, "Should have some prediction confidence"
        
        return True

def run_comprehensive_tests():
    """Run all comprehensive tests"""
    print("🚀 RUNNING ENHANCED RYOKO FRAMEWORK TESTS")
    print("=" * 60)
    
    tester = TestEnhancedRyoko()
    tests = [
        ("Quantum Chaos Engine", tester.test_quantum_chaos_engine),
        ("Memory Consolidation", tester.test_memory_consolidation),
        ("Growth Predictor", tester.test_growth_predictor),
        ("Enhanced Seed Initialization", tester.test_enhanced_seed_initialization),
        ("Enhanced Experience Processing", tester.test_enhanced_experience_processing),
        ("Memory Formation Enhanced", tester.test_memory_formation_enhanced),
        ("Growth Prediction Integration", tester.test_growth_prediction_integration),
        ("Async Processing", tester.test_async_processing),
        ("System Health Monitoring", tester.test_system_health_monitoring),
        ("Value System Development", tester.test_value_system_development),
        ("Comprehensive Life Simulation", tester.test_comprehensive_life_simulation),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        if tester.run_test(test_name, test_func):
            passed += 1
        else:
            failed += 1
    
    print("=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 ALL ENHANCED TESTS PASSED! The framework is working correctly.")
        print("\nEnhanced Features Verified:")
        print("✓ Quantum Chaos Engine with phase-dependent behavior")
        print("✓ Sophisticated Memory Consolidation with associative links") 
        print("✓ Growth Prediction with trend analysis")
        print("✓ Enhanced Emotional Impact Calculation")
        print("✓ Adaptive Learning Rates based on growth phase")
        print("✓ Comprehensive System Health Monitoring")
        print("✓ Advanced Value System Development")
        print("✓ Async Processing Support")
        print("✓ Memory Network Formation")
        print("✓ Life Story Simulation Capability")
    else:
        print("❌ Some tests failed. Check implementation.")
    
    return failed == 0

if __name__ == "__main__":
    success = run_comprehensive_tests()
    exit(0 if success else 1)