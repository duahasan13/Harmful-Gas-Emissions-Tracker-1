# Harmful Gas Emissions Tracker

A web-based application that estimates a user’s **monthly environmental impact** by calculating harmful greenhouse gases:  
**Carbon Dioxide (CO₂), Methane (CH₄) from unrecycled waste, and Nitrogen Oxides (NOₓ) from vehicle exhausts**.  

The app converts all gases into **CO₂-equivalent (CO₂e)** to give an easy-to-understand footprint for households and individuals.

---

## Features

- Tracks monthly electricity and gas usage  
- Considers house area for context  
- Country-specific emission factors  
- Calculates emissions from different vehicles  
- Models methane from unrecycled waste  
- Calculates nitrogen oxides (NOₓ) from transport  
- Aggregates into total CO₂e footprint  
- Displays a clear breakdown of contributions  
- Runs as a browser-based web app (no Python IDLE required)

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

- **CO₂**: from electricity, gas, and vehicle fuel combustion  
- **Methane (CH₄)**: from unrecycled organic waste
