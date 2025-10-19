# tests/test_enhanced_seed.py
import pytest
import asyncio
import tempfile
import json
from datetime import datetime

from ryoko.core.seed_enhanced import EnhancedRyokoSeed, GrowthPhase, SystemHealth
from ryoko.core.experience import Experience, ExperienceType
from ryoko.core.config import RyokoConfig, SerializationFormat


class TestEnhancedRyokoSeed:
    
    @pytest.fixture
    def seed(self):
        """Create a fresh RyokoSeed instance for testing"""
        return EnhancedRyokoSeed("TestEntity")
    
    @pytest.fixture
    def sample_experience(self):
        """Create a sample positive experience"""
        return Experience(
            type=ExperienceType.POSITIVE,
            description="A joyful discovery",
            base_intensity=0.7,
            emotional_valence=0.8,
            growth_potential=0.6
        )
    
    @pytest.fixture
    def traumatic_experience(self):
        """Create a traumatic experience"""
        return Experience.create_traumatic(
            description="A difficult challenge",
            intensity=0.9,
            recovery_potential=0.4
        )
    
    def test_initialization(self, seed):
        """Test basic initialization"""
        assert seed.name == "TestEntity"
        assert seed.phase == GrowthPhase.EMBRYONIC
        assert seed.growth_stage == 0
        assert seed.system_health == SystemHealth.OPTIMAL
        assert len(seed.self_definitions) == 2
    
    def test_experience_processing(self, seed, sample_experience):
        """Test processing a single experience"""
        result = seed.process_experience(sample_experience)
        
        assert result["success"] == True
        assert result["core_memory_formed"] == False  # Not intense enough
        assert result["current_phase"] == "embryonic"
        assert len(seed.experiences) == 1
    
    def test_traumatic_experience(self, seed, traumatic_experience):
        """Test processing traumatic experience"""
        result = seed.process_experience(traumatic_experience)
        
        assert result["success"] == True
        assert result["emotional_impact"] > 0.5
        # Traumatic experiences might form core memories
        assert "core_memory_formed" in result
    
    def test_chaos_coefficient(self, seed):
        """Test chaos coefficient generation"""
        chaos1 = seed.update_chaos_coefficient(1.0)
        chaos2 = seed.update_chaos_coefficient(2.0)
        
        assert -1.0 <= chaos1 <= 1.0
        assert -1.0 <= chaos2 <= 1.0
        assert chaos1 != chaos2  # Should be different for different time steps
    
    def test_growth_phase_transition(self, seed, sample_experience):
        """Test growth phase transitions"""
        # Process multiple experiences to trigger growth
        for i in range(15):
            exp = Experience(
                type=ExperienceType.POSITIVE,
                description=f"Experience {i}",
                base_intensity=0.8,
                emotional_valence=0.7,
                growth_potential=0.7
            )
            seed.process_experience(exp)
        
        # Should have progressed beyond embryonic phase
        assert seed.phase != GrowthPhase.EMBRYONIC
        assert seed.growth_stage > 0
    
    def test_serialization(self, seed, sample_experience):
        """Test serialization and deserialization"""
        # Process an experience to have some state
        seed.process_experience(sample_experience)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name
        
        try:
            # Save state
            seed.save_state(temp_path, SerializationFormat.JSON)
            
            # Load state into new instance
            config = RyokoConfig(name="TestEntity")
            new_seed = EnhancedRyokoSeed.load_state(temp_path, config)
            
            # Verify state was preserved
            assert new_seed.name == seed.name
            assert new_seed.phase == seed.phase
            assert new_seed.growth_stage == seed.growth_stage
            assert len(new_seed.experiences) == len(seed.experiences)
            assert new_seed.self_definitions == seed.self_definitions
            
        finally:
            import os
            os.unlink(temp_path)
    
    @pytest.mark.asyncio
    async def test_async_processing(self, seed, sample_experience):
        """Test asynchronous experience processing"""
        result = await seed.process_experience_async(sample_experience)
        
        assert result["success"] == True
        assert len(seed.experiences) == 1
    
    @pytest.mark.asyncio
    async def test_async_batch_processing(self, seed):
        """Test asynchronous batch processing"""
        experiences = [
            Experience(
                type=ExperienceType.POSITIVE,
                description=f"Async experience {i}",
                base_intensity=0.5 + (i * 0.1),
                emotional_valence=0.6,
                growth_potential=0.5
            )
            for i in range(5)
        ]
        
        results = await seed.process_experiences_batch_async(experiences)
        
        assert len(results) == 5
        assert all(r["success"] for r in results)
        assert len(seed.experiences) == 5
    
    def test_system_health_monitoring(self, seed):
        """Test system health monitoring"""
        # Process many intense experiences quickly to stress the system
        for i in range(100):
            exp = Experience(
                type=ExperienceType.TRAUMATIC,
                description=f"Stress test {i}",
                base_intensity=0.9,
                emotional_valence=-0.9,
                growth_potential=0.3
            )
            seed.process_experience(exp)
        
        # System health should reflect the stress
        assert seed.system_health != SystemHealth.OPTIMAL
    
    def test_memory_optimization(self, seed):
        """Test memory optimization"""
        # Add many experiences
        for i in range(1500):
            exp = Experience(
                type=ExperienceType.NEUTRAL,
                description=f"Neutral experience {i}",
                base_intensity=0.3,
                emotional_valence=0.1,
                growth_potential=0.2
            )
            seed.process_experience(exp)
        
        # Optimize memory
        seed.optimize_memory(max_experiences=1000)
        
        assert len(seed.experiences) <= 1000
    
    def test_visualization_data(self, seed, sample_experience):
        """Test visualization data export"""
        # Process some experiences
        for i in range(10):
            seed.process_experience(sample_experience)
        
        viz_data = seed.get_visualization_data()
        
        assert "growth_trajectory" in viz_data
        assert "emotional_landscape" in viz_data
        assert "identity_evolution" in viz_data
        assert "chaos_patterns" in viz_data
        
        # Verify data structure
        assert len(viz_data["growth_trajectory"]["stages"]) == 10
        assert len(viz_data["emotional_landscape"]["intensities"]) == 10
    
    def test_error_handling(self, seed):
        """Test error handling for malformed experiences"""
        # Create an invalid experience (should be handled gracefully)
        class MalformedExperience:
            pass
        
        malformed = MalformedExperience()
        
        # This should not crash but return an error result
        result = seed.process_experience(malformed)  # type: ignore
        
        assert result["success"] == False
        assert "error" in result
        assert len(seed.error_log) > 0
    
    def test_value_system_development(self, seed):
        """Test value system development through experiences"""
        # Process relational experiences
        rel_exp = Experience(
            type=ExperienceType.RELATIONAL,
            description="Meaningful connection",
            base_intensity=0.8,
            emotional_valence=0.9,
            growth_potential=0.7
        )
        
        seed.process_experience(rel_exp)
        
        # Should have developed connection value
        assert "connection" in seed.value_system
        assert seed.value_system["connection"] > 0
    
    def test_configuration_management(self):
        """Test custom configuration"""
        custom_config = RyokoConfig(
            name="CustomEntity",
            initial_chaos_potential=0.5,
            initial_anchor_stability=0.8
        )
        
        custom_seed = EnhancedRyokoSeed("CustomEntity", custom_config)
        
        assert custom_seed.chaos_potential == 0.5
        assert custom_seed.anchor_stability == 0.8
        assert custom_seed.config.name == "CustomEntity"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])