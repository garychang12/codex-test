"""Utilities for estimating PCB copper thickness from 4-wire resistance measurements."""

from __future__ import annotations

from dataclasses import dataclass

COPPER_RESISTIVITY_20C = 1.724e-8  # ohm-meter
COPPER_TEMP_COEFF = 0.0039  # per °C


@dataclass(frozen=True)
class Measurement:
    resistance_ohm: float
    length_m: float
    width_m: float
    temperature_c: float = 20.0
    current_a: float | None = None


def resistance_to_20c(resistance_ohm: float, temperature_c: float) -> float:
    """Convert measured resistance at temperature_c to equivalent 20°C resistance."""
    if resistance_ohm <= 0:
        raise ValueError("resistance_ohm must be > 0")
    factor = 1 + COPPER_TEMP_COEFF * (temperature_c - 20.0)
    if factor <= 0:
        raise ValueError("temperature compensation factor must be > 0")
    return resistance_ohm / factor


def thickness_from_measurement(measurement: Measurement) -> float:
    """Return copper thickness in meters."""
    if measurement.length_m <= 0:
        raise ValueError("length_m must be > 0")
    if measurement.width_m <= 0:
        raise ValueError("width_m must be > 0")

    r20 = resistance_to_20c(measurement.resistance_ohm, measurement.temperature_c)
    return COPPER_RESISTIVITY_20C * measurement.length_m / (r20 * measurement.width_m)


def meters_to_micrometers(value_m: float) -> float:
    return value_m * 1_000_000


def micrometers_to_oz(value_um: float) -> float:
    """Approximate conversion: 1 oz copper ~= 34.79 µm."""
    return value_um / 34.79
