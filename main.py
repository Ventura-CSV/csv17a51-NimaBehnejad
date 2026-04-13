from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    return set(mapping.keys())


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    return set(mapping.values())


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    # could also do:
    # all(v in target...)
    for v in mapping.values():
        if (v not in target):
            return False
    return True

def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
    # if there are no duplicate outputs, then its injective
    return len(mapping.values()) == len(set(mapping.values()))


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
    range = set(mapping.values()) # remove duplicates by making it a set
    return range == target

def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    return is_injective(mapping) & is_surjective(mapping, target)
