"""
Goti Esmoris Tech - Cloud Infrastructure Energy Billing Analyzer
Version: 1.0.0
Description: Ingests real-time kilowatt telemetry from edge monitors, calculates 
             projected energy bills, and triggers financial optimization alerts.
"""

import json
import time
import random

# Financial Billing Matrix (Simulated ARS/USD business tariff rates)
COST_PER_KWH = 0.15 # Cost in USD per kiloWatt-hour
BUDGET_ALERT_THRESHOLD = 150.00 # Maximum monthly energy budget in USD

def process_energy_telemetry(payload_str):
    try:
        data = json.loads(payload_str)
        amps = data.get("current_amps", 0.0)
        kw = data.get("power_kw", 0.0)
        
        print(f"\n[ENERGY TELEMETRY] Load: {amps:.2f} A | Real-Time Power: {kw:.4f} kW")
        
        # Calculate consumption metrics over a simulated operational month
        simulated_monthly_hours = 720
        projected_kwh_consumption = kw * simulated_monthly_hours
        projected_monthly_bill = projected_kwh_consumption * COST_PER_KWH
        
        print(f"-> Projected Monthly Energy Consumption: {projected_kwh_consumption:.2f} kWh")
        print(f"-> Estimated Infrastructure Billing: ${projected_monthly_bill:.2f} USD")
        
        # Financial Smart Optimization Rules
        if projected_monthly_bill > BUDGET_ALERT_THRESHOLD:
            print("⚠️ [BUDGET EXCEEDED] AI Optimization Suggestion: High peak load detected.")
            print("🚀 Action Required: Reschedule heavy heavy equipment usage to off-peak hours to slash tariff costs.")
        else:
            print("✅ Energy expenses tracking under corporate budget guidelines.")
            
    except json.JSONDecodeError:
        print("[ERROR] Corrupted energy telemetry packet.")

if __name__ == "__main__":
    print("====================================================")
    print("      GOTI ESMORIS TECH - SMART BILLING MONITORS     ")
    print("====================================================")
    print("Listening to power infrastructure streams... (Ctrl+C to stop)")
    
    try:
        while True:
            # Nominal scenario (Kitchen/Factory running standard gear)
            nominal_payload = '{"current_amps": 8.50, "power_kw": 1.8700}'
            process_energy_telemetry(nominal_payload)
            time.sleep(3)
            
            # Peak scenario (Ovens/Heavy machinery drawing maximum current)
            peak_payload = f'{{"current_amps": {random.uniform(22.0, 29.0):.2f}, "power_kw": {random.uniform(4.8, 6.3):.4f}}}'
            process_energy_telemetry(peak_payload)
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\nPower telemetry interface safely detached from local host.")
