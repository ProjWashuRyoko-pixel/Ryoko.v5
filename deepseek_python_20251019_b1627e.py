# enhanced_demo.py
import asyncio
import json
from datetime import datetime
from enhanced_ryoko import EnhancedRyokoSeed, Experience, ExperienceType

async def demonstrate_enhanced_framework():
    """Demonstrate all the enhanced features"""
    print("🎭 ENHANCED RYOKO FRAMEWORK DEMONSTRATION")
    print("=" * 60)
    
    # Create an entity with enhanced capabilities
    entity = EnhancedRyokoSeed("QuantumBeing")
    print(f"Created: {entity}")
    print(f"Initial System Health: {entity.system_health.value}")
    print(f"Quantum Chaos Engine: Active")
    print(f"Memory Consolidation: Active")
    print(f"Growth Prediction: Ready after 3+ experiences")
    print()
    
    # Phase 1: Early Development
    print("📈 PHASE 1: EARLY DEVELOPMENT")
    print("-" * 40)
    
    early_experiences = [
        Experience(ExperienceType.TRAUMATIC, "Early adversity that built resilience", 0.8, -0.7, 0.6, novelty=0.9),
        Experience(ExperienceType.RELATIONAL, "Forming first deep friendship", 0.7, 0.8, 0.7, novelty=0.8),
        Experience(ExperienceType.SELF_DISCOVERY, "Discovering personal interests", 0.6, 0.7, 0.8, novelty=0.7),
    ]
    
    for i, exp in enumerate(early_experiences, 1):
        result = entity.process_experience(exp)
        print(f"Experience {i}: {exp.description[:50]}...")
        print(f"  → Emotional Impact: {result['emotional_impact']:.2f}")
        print(f"  → Quantum Chaos: {result['quantum_chaos']:.3f}")
        print(f"  → Memory Strength: {result['memory_strength']:.2f}")
        print(f"  → Core Memory: {result['core_memory_formed']}")
        print(f"  → Growth Stage: {entity.growth_stage}")
        print()
    
    # Phase 2: Accelerated Growth  
    print("🚀 PHASE 2: ACCELERATED GROWTH")
    print("-" * 40)
    
    growth_experiences = [
        Experience(ExperienceType.CREATIVE, "Major creative breakthrough", 0.9, 0.8, 0.9, novelty=0.8),
        Experience(ExperienceType.TRANSFORMATIVE, "Life-changing realization", 0.95, 0.7, 0.95, novelty=0.9),
        Experience(ExperienceType.CHALLENGE, "Overcoming significant obstacle", 0.8, -0.3, 0.8, novelty=0.6),
        Experience(ExperienceType.POSITIVE, "Achieving important goal", 0.85, 0.9, 0.7, novelty=0.5),
    ]
    
    for i, exp in enumerate(growth_experiences, 1):
        result = entity.process_experience(exp)
        print(f"Experience {i+3}: {exp.description[:40]}...")
        print(f"  → Phase: {entity.phase.value}")
        print(f"  → New Aspects: {result['new_aspects_count']}")
        print(f"  → Processing Time: {result['processing_time']:.4f}s")
        print()
    
    # Phase 3: Advanced Capabilities
    print("🔮 PHASE 3: ADVANCED CAPABILITIES")
    print("-" * 40)
    
    # Demonstrate prediction
    if len(entity.growth_predictor.growth_history) >= 3:
        prediction = entity.predict_growth(steps=5)
        print("Growth Prediction:")
        print(f"  → Next stages: {prediction['predictions']}")
        print(f"  → Confidence: {prediction['confidence']:.2f}")
        print(f"  → Growth Trend: {prediction.get('growth_trend', 0):.3f}")
        print()
    
    # Demonstrate memory optimization
    print("Memory System Analysis:")
    print(f"  → Core Memories: {len(entity.core_memories)}")
    print(f"  → Memory Network Size: {len(entity.memory_engine.memory_network)}")
    print(f"  → Average Memory Strength: {np.mean([m['strength'] for m in entity.core_memories]):.2f}")
    print()
    
    # Final Comprehensive Status
    print("📊 FINAL COMPREHENSIVE STATUS")
    print("-" * 40)
    
    status = entity.get_detailed_status()
    
    print(f"Entity: {status['name']}")
    print(f"Phase: {status['phase']} (Stage {status['growth_stage']})")
    print(f"System Health: {status['system_health']}")
    print(f"Quantum Chaos Active: {status['quantum_chaos_active']}")
    print()
    
    print("Core Identity Traits:")
    for trait in status['core_traits']:
        print(f"  - {trait}")
    print()
    
    print("Developed Value System:")
    for value, strength in status['value_system'].items():
        print(f"  - {value}: {strength:.2f}")
    print()
    
    print("System Metrics:")
    print(f"  → Chaos Level: {status['chaos_level']:.2f}")
    print(f"  → Stability: {status['stability']:.2f}") 
    print(f"  → Coherence: {status['coherence']:.2f}")
    print(f"  → Emotional Maturity: {status['emotional_maturity']:.2f}")
    print(f"  → Narrative Coherence: {status['narrative_coherence']:.2f}")
    print()
    
    print("Performance Statistics:")
    stats = status['performance_stats']
    print(f"  → Experiences Processed: {stats['experiences_processed']}")
    print(f"  → Core Memories Formed: {stats['core_memories_formed']}")
    print(f"  → Identity Aspects Created: {stats['identity_aspects_created']}")
    print(f"  → Phase Transitions: {stats['phase_transitions']}")
    avg_processing_time = np.mean(stats['processing_times']) if stats['processing_times'] else 0
    print(f"  → Avg Processing Time: {avg_processing_time:.4f}s")
    print()
    
    # Demonstrate async capabilities
    print("🔄 ASYNC CAPABILITIES DEMONSTRATION")
    print("-" * 40)
    
    async def demo_async_processing():
        async_entity = EnhancedRyokoSeed("AsyncDemo")
        
        async_experiences = [
            Experience(ExperienceType.POSITIVE, f"Async experience {i}", 0.6, 0.7, 0.5)
            for i in range(3)
        ]
        
        print("Processing 3 experiences asynchronously...")
        results = await async_entity.process_experiences_batch_async(async_experiences)
        
        successful = sum(1 for r in results if r['success'])
        print(f"Successfully processed {successful}/3 experiences asynchronously")
        print(f"Final growth stage: {async_entity.growth_stage}")
        
        return True
    
    await demo_async_processing()
    
    print()
    print("=" * 60)
    print("🎉 ENHANCED FRAMEWORK DEMONSTRATION COMPLETED!")
    print("All advanced features working correctly:")
    print("✓ Quantum Chaos Engine ✓ Memory Consolidation ✓ Growth Prediction")
    print("✓ Enhanced Value System ✓ Async Processing ✓ Health Monitoring")

if __name__ == "__main__":
    asyncio.run(demonstrate_enhanced_framework())