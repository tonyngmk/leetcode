# Dataclasses Hands-On Learning Plan

## Overview
Dataclasses are a built-in Python feature (3.7+) that simplify creating classes primarily to store data. They automatically generate `__init__`, `__repr__`, `__eq__`, and other methods.

---

## Phase 1: Basics (Exercises 1-5)

### 1.1 Your First Dataclass
- Create a basic dataclass with a few fields
- Understand auto-generated `__repr__` and `__eq__`
- Compare with regular class

### 1.2 Field Types and Defaults
- Define field types (int, str, float, bool)
- Use default values
- Understand mutable defaults issue (list as default)

### 1.3 Field Options
- `field()` with `default`, `default_factory`
- `field()` with `repr`, `compare`, `init`
- Understanding `__init__` order with defaults

---

## Phase 2: Intermediate (Exercises 6-12)

### 2.1 Class Variables and Init Variables
- Difference between class variables and instance fields
- Using `__init_var__`

### 2.2 Post-Init Processing
- Using `__post_init__` to add validation
- Setting derived fields

### 2.3 Immutability
- Creating frozen dataclasses
- Handling nested mutables

### 2.4 Inheritance
- Extending dataclasses
- Overriding fields in subclasses
- Order of field resolution

### 2.5 Comparison and Ordering
- `eq`, `order`, `frozen` parameters
- Using `__lt__`, `__le__`, `__gt__`, `__ge__`
- Sorting dataclass instances

### 2.6 Pattern Matching
- Using dataclasses with match/case
- Destructuring in case blocks

---

## Phase 3: Advanced (Exercises 13-18)

### 3.1 Slots
- Adding `__slots__` to dataclasses
- Memory optimization benefits

### 3.2 Customizing Representation
- Custom `__repr__` with `repr=False`
- Using `field(repr=False)` for sensitive data

### 3.3 Validation
- Property-based validation in `__post_init__`
- Using descriptors with dataclasses
- Pydantic comparison (optional)

### 3.4 Dataclasses with Collections
- Nested dataclasses
- Lists of dataclasses
- Dictionaries with dataclass values

### 3.5 Working with Functions
- Passing dataclass instances to functions
- Returning dataclasses from functions
- Type hints with dataclasses

### 3.6 Serialization
- Converting to dict/JSON
- Converting from dict/JSON
- Custom serialization methods

---

## Phase 4: Real-World Examples (Exercises 19-25)

### 4.1 Data Transfer Objects (DTOs)
- API response models
- Database row models

### 4.2 Configuration Objects
- App settings dataclass
- Environment-based config

### 4.3 Event/Message Models
- Event sourcing models
- Message queue payloads

### 4.4 Game Models
- Player, Enemy, Item classes
- Inventory system

### 4.5 State Management
- FSM (Finite State Machine) states
- Transaction states

### 4.6 Geometry/Math
- Point, Vector, Rectangle
- Operations on geometric objects

### 4.7 Testing
- Test fixtures with dataclasses
- Mock objects with dataclasses

---

## Best Practices

1. **Use frozen=True for immutable data** - Prevents accidental modification
2. **Use default_factory for mutable defaults** - Avoids shared state bugs
3. **Add __post_init__ for validation** - Catches errors early
4. **Use field(repr=False) for sensitive data** - Security consideration
5. **Prefer dataclasses over regular classes for data** - Less boilerplate
6. **Use type hints everywhere** - Better IDE support and documentation

---

## Quick Reference

```python
from dataclasses import dataclass, field, fields
from typing import Optional, List
from datetime import datetime
import json

@dataclass
class Person:
    name: str
    age: int = 0
    email: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'tags': self.tags
        }

# Usage
p = Person("Alice", 30, tags=["developer", "python"])
print(p)
print(p.to_dict())
```
