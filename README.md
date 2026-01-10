# Harmful Gas Emissions Tracker

A web-based application that estimates a user’s monthly environmental impact by calculating harmful gases: Carbon from electricity,gas,etc., Methane from unrecycled waste, and Nitrogen Oxides from car exhausts. The app converts all gases into CO₂-equivalent to give an easy to understand footprint for households and individuals.

---

## Features

- Tracks monthly electricity and gas usage  
- Considers house area for context  
- Country-specific emission factors  
- Calculates emissions from different vehicles  
- Models methane from unrecycled waste  
- Calculates nitrogen oxides (NOₓ) from transport  
- Gathers into total CO₂e footprint  
- Displays a clear breakdown of contributions

---

## User Inputs

| Category | Input |
|---------|-------|
| Energy | Monthly electricity usage (kWh) |
| Gas | Monthly gas usage (kWh or m³) |
| Location | Country of residence |
| Housing | House/apartment area (m²) |
| Transport | Distance traveled by car, bus, etc. |
| Recycling | Percentage of waste recycled |

---

## Emission Model

- Carbon: from electricity, gas, and vehicle fuel combustion  
- Methane: from unrecycled waste
- Nitrogen Oxides: from car exhaust
