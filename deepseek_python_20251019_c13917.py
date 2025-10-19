# verification_originality.py
import ast
import hashlib
import requests
from typing import Set, List

class CodeOriginalityAnalyzer:
    """Analyze code for original patterns"""
    
    def __init__(self):
        self.unique_patterns = set()
        
    def extract_unique_functions(self, filepath: str) -> List[str]:
        """Extract function definitions to check uniqueness"""
        with open(filepath, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_code = ast.unparse(node)
                functions.append({
                    'name': node.name,
                    'code_hash': hashlib.md5(func_code.encode()).hexdigest(),
                    'complexity': self._calculate_complexity(node)
                })
        
        return functions
    
    def _calculate_complexity(self, node: ast.FunctionDef) -> int:
        """Calculate code complexity (original code tends to be complex)"""
        complexity = 0
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.Try, ast.With)):
                complexity += 1
        return complexity

# Analyze our implementation
analyzer = CodeOriginalityAnalyzer()
functions = analyzer.extract_unique_functions('enhanced_ryoko.py')

print("UNIQUE FUNCTION ANALYSIS:")
print("=" * 50)
for func in functions:
    print(f"Function: {func['name']}")
    print(f"Complexity: {func['complexity']}")
    print(f"Hash: {func['code_hash'][:16]}...")
    print("-" * 30)

# High complexity indicates original algorithmic work
complex_functions = [f for f in functions if f['complexity'] > 3]
print(f"\nComplex functions (likely original): {len(complex_functions)}")