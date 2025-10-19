# simple_test.py
"""
Simple test to verify Ryoko core functionality without dependencies
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

class SimpleRyokoTest:
    """Minimal test implementation"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
    
    def run_test(self, test_name, test_func):
        """Run a single test"""
        try:
            result = test_func()
            if result:
                print(f"✅ {test_name}")
                self.passed += 1
            else:
                print(f"❌ {test_name}")
                self.failed += 1
        except Exception as e:
            print(f"💥 {test_name} - Exception: {e}")
            self.failed += 1
    
    def test_basic_creation(self):
        """Test basic object creation"""
        # We'll test with our minimal implementation
        from test_ryoko_framework import EnhancedRyokoSeed, Experience, ExperienceType
        
        entity = EnhancedRyokoSeed("TestEntity")
        return entity.name == "TestEntity"
    
    def test_experience_processing(self):
        """Test experience processing"""
        from test_ryoko_framework import EnhancedRyokoSeed, Experience, ExperienceType
        
        entity = EnhancedRyokoSeed("TestEntity")
        exp = Experience(
            type=ExperienceType.POSITIVE,
            description="Test experience",
            base_intensity=0.5,
            emotional_valence=0.6,
            growth_potential=0.4
        )
        
        result = entity.process_experience(exp)
        return result["success"] and len(entity.experiences) == 1
    
    def test_growth_progression(self):
        """Test that entities grow with experiences"""
        from test_ryoko_framework import EnhancedRyokoSeed, Experience, ExperienceType
        
        entity = EnhancedRyokoSeed("GrowthTest")
        
        # Add multiple experiences
        for i in range(3):
            exp = Experience(
                type=ExperienceType.POSITIVE,
                description=f"Experience {i}",
                base_intensity=0.6,
                emotional_valence=0.7,
                growth_potential=0.5
            )
            entity.process_experience(exp)
        
        return len(entity.experiences) == 3 and entity.performance_stats["experiences_processed"] == 3
    
    def test_status_reporting(self):
        """Test status reporting functionality"""
        from test_ryoko_framework import EnhancedRyokoSeed
        
        entity = EnhancedRyokoSeed("StatusTest")
        status = entity.get_status()
        
        required_fields = ["name", "phase", "growth_stage", "core_traits"]
        return all(field in status for field in required_fields)
    
    def run_all_tests(self):
        """Run all simple tests"""
        print("Running Simple Ryoko Framework Tests...")
        print("=" * 50)
        
        tests = [
            ("Basic Entity Creation", self.test_basic_creation),
            ("Experience Processing", self.test_experience_processing),
            ("Growth Progression", self.test_growth_progression),
            ("Status Reporting", self.test_status_reporting),
        ]
        
        for test_name, test_func in tests:
            self.run_test(test_name, test_func)
        
        print("=" * 50)
        print(f"Results: {self.passed} passed, {self.failed} failed")
        
        return self.failed == 0

if __name__ == "__main__":
    test_runner = SimpleRyokoTest()
    success = test_runner.run_all_tests()
    sys.exit(0 if success else 1)