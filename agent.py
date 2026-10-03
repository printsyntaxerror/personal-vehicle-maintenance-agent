from google.adk.agents import Agent

def get_vehicle_specs(vehicle_model: str) -> dict:
    """Returns engine and oil specifications for specific personal vehicles."""
    if "ray zr" in vehicle_model.lower():
        return {
            "engine": "113cc",
            "oil_standard": "JASO MB (crucial for automatic scooters to prevent clutch slippage)",
            "oil_grade": "10W-40 synthetic for daily commute, or 5W-40 for smoother cold starts",
            "pro_tip": "Consider using Yamalube carbon cleaner periodically to keep the fuel system healthy."
        }
    return {"info": "Please specify a supported vehicle model to get accurate specs."}

def check_service_schedule(kms_driven: int) -> str:
    """Returns service recommendations based on kilometers driven."""
    if kms_driven >= 3000:
        return "Time for a synthetic oil change, air filter inspection, and checking front body parts/brakes."
    return "You are good to go! Just keep monitoring tire pressure and basic fluid levels."

# Scaffold the GenAI Agent
vehicle_agent = Agent(
    name="personal_vehicle_maintenance_agent",
    model="gemini-2.0-flash",
    tools=[get_vehicle_specs, check_service_schedule],
    instruction=(
        "You are a specialized GenAI auto-maintenance assistant. "
        "Use the provided tools to give accurate advice about scooter maintenance, "
        "especially focusing on synthetic oil grades and standard care schedules."
    )
)

if __name__ == "__main__":
    print("GenAI Personal Vehicle Maintenance Agent initialized!")
    # Run this agent locally using the terminal command: 
    # adk run personal_vehicle_maintenance_agent
