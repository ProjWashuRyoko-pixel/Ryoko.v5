# examples/comprehensive_usage.py
"""
Comprehensive usage examples for Enhanced Ryoko Framework
"""
import asyncio
import json
from datetime import datetime
from ryoko.core.seed_enhanced import EnhancedRyokoSeed
from ryoko.core.experience import Experience, ExperienceType
from ryoko.core.config import RyokoConfig, SerializationFormat

def demo_basic_usage():
    """Demonstrate basic usage of the enhanced framework"""
    print("=== Enhanced Ryoko Framework Demo ===\n")
    
    # Create a configured entity
    config = RyokoConfig(
        name="Aurora",
        initial_chaos_potential=0.3,
        initial_emotional_maturity=0.4
    )
    
    entity = EnhancedRyokoSeed("Aurora", config)
    print(f"Created: {entity}")
    
    # Create diverse experiences
    experiences = [
        Experience.create_traumatic(
            description="Early life challenge",
            intensity=0.8,
            recovery_potential=0.6
        ),
        Experience(
            type=ExperienceType.RELATIONAL,
            description="First meaningful friendship",
            base_intensity=0.7,
            emotional_valence=0.9,
            growth_potential=0.8
        ),
        Experience.create_breakthrough(
            description="Discovering personal passion",
            insight_level=0.9
        )
    ]
    
    # Process experiences
    for exp in experiences:
        result = entity.process_experience(exp)
        print(f"Processed: {exp.description}")
        print(f"  → Emotional impact: {result['emotional_impact']:.2f}")
        print(f"  → Core memory: {result['core_memory_formed']}")
        print(f"  → New aspects: {result['new_aspects_count']}")
        print()
    
    # Show comprehensive status
    status = entity.get_detailed_status()
    print("=== Final Status ===")
    print(f"Phase: {status['phase']} (Stage {status['growth_stage']})")
    print(f"System Health: {status['system_health']}")
    print(f"Core Traits: {', '.join(status['core_traits'])}")
    print(f"Value System: {status['value_system']}")
    print(f"Chaos Level: {status['chaos_level']:.2f}")
    print(f"Stability: {status['stability']:.2f}")
    print(f"Coherence: {status['coherence']:.2f}")

async def demo_async_usage():
    """Demonstrate asynchronous usage"""
    print("\n=== Async Processing Demo ===")
    
    entity = EnhancedRyokoSeed("AsyncEntity")
    
    # Create batch of experiences
    experiences = [
        Experience(
            type=ExperienceType.POSITIVE,
            description=f"Async experience {i}",
            base_intensity=0.5 + (i * 0.1),
            emotional_valence=0.6 + (i * 0.05),
            growth_potential=0.4 + (i * 0.1)
        )
        for i in range(10)
    ]
    
    # Process asynchronously
    results = await entity.process_experiences_batch_async(experiences)
    
    successful = sum(1 for r in results if r['success'])
    print(f"Successfully processed {successful}/{len(experiences)} experiences asynchronously")

def demo_persistence():
    """Demonstrate state persistence"""
    print("\n=== Persistence Demo ===")
    
    # Create and develop an entity
    entity = EnhancedRyokoSeed("PersistentEntity")
    
    for i in range(5):
        exp = Experience(
            type=ExperienceType.SELF_DISCOVERY,
            description=f"Learning experience {i}",
            base_intensity=0.6,
            emotional_valence=0.7,
            growth_potential=0.5
        )
        entity.process_experience(exp)
    
    original_status = entity.get_detailed_status()
    
    # Save state
    entity.save_state("demo_entity_state.json", SerializationFormat.JSON)
    print("Saved entity state to demo_entity_state.json")
    
    # Load into new instance
    loaded_entity = EnhancedRyokoSeed.load_state("demo_entity_state.json")
    loaded_status = loaded_entity.get_detailed_status()
    
    # Verify state preservation
    assert original_status['phase'] == loaded_status['phase']
    assert original_status['growth_stage'] == loaded_status['growth_stage']
    assert original_status['total_aspects'] == loaded_status['total_aspects']
    
    print("State successfully saved and loaded!")
    print(f"Loaded entity: {loaded_entity}")

def demo_visualization_data():
    """Demonstrate visualization data export"""
    print("\n=== Visualization Data Demo ===")
    
    entity = EnhancedRyokoSeed("VizEntity")
    
    # Generate some growth data
    for i in range(20):
        exp = Experience(
            type=ExperienceType.POSITIVE if i % 2 == 0 else ExperienceType.CHALLENGE,
            description=f"Growth experience {i}",
            base_intensity=0.4 + (i * 0.03),
            emotional_valence=0.6 if i % 2 == 0 else -0.3,
            growth_potential=0.5 + (i * 0.02)
        )
        entity.process_experience(exp)
    
    viz_data = entity.get_visualization_data()
    
    print("Available visualization datasets:")
    for key, value in viz_data.items():
        if isinstance(value, dict) and 'timestamps' in value:
            print(f"  {key}: {len(value['timestamps'])} data points")
        elif isinstance(value, list):
            print(f"  {key}: {len(value)} items")
        else:
            print(f"  {key}: {type(value).__name__}")

def demo_system_health():
    """Demonstrate system health monitoring"""
    print("\n=== System Health Monitoring Demo ===")
    
    entity = EnhancedRyokoSeed("HealthMonitor")
    
    print(f"Initial health: {entity.system_health.value}")
    
    # Stress the system with intense experiences
    for i in range(50):
        exp = Experience(
            type=ExperienceType.TRAUMATIC,
            description=f"Stress test {i}",
            base_intensity=0.9,
            emotional_valence=-0.8,
            growth_potential=0.2
        )
        entity.process_experience(exp)
    
    print(f"After stress: {entity.system_health.value}")
    print(f"Error count: {len(entity.error_log)}")
    print(f"Performance stats: {entity.performance_stats}")

async def main():
    """Run all demos"""
    demo_basic_usage()
    await demo_async_usage()
    demo_persistence()
    demo_visualization_data()
    demo_system_health()

if __name__ == "__main__":
    asyncio.run(main())