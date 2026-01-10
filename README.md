# Harmful Gas Emissions Tracker

It's a web-based application that estimates a household’s or a person's monthly emissions for three harmful gases: Carbon from electricity,gas,etc., Methane from unrecycled waste, and Nitrogen Oxides from car exhausts. All gases are converted into CO₂e to give an easy to understand footprint.

---

## Features

- Tracks monthly electricity and gas usage  
- Considers house area for context  
- Calculates emissions from different vehicles  
- Gets methane from unrecycled waste  
- Calculates nitrogen oxides from transport    
- Displays a clear breakdown of each gas separately
- Balloons!!!

---

## User Inputs

| Category | Input |
|---------|-------|
| Energy | Monthly electricity usage (kWh) |
| Gas | Monthly gas usage (kWh or m³) |
| Housing | House/apartment area (m²) |
| Transport | Distance traveled by car, bus, etc. |
| Recycling | Percentage of waste recycled |

---

## Emission Model

- Carbon: from electricity, gas, and vehicle fuel combustion  
- Methane: from unrecycled waste
- Nitrogen Oxides: from car exhaust  
---

## Tech Stack

- Python  
- Streamlit
