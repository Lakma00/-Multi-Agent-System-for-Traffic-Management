import random
import time
from owlready2 import *

# Load the ontology
onto = get_ontology("TrafficSystem.owl").load()

class TrafficLightAgent:
    def __init__(self, intersection_id, ontology_instance):
        self.id = intersection_id
        self.ontology_instance = ontology_instance
        
        # Initialize trafficDensity and greenTime from ontology
        self.traffic_density = (
            ontology_instance.trafficDensity[0]
            if hasattr(ontology_instance, "trafficDensity") and ontology_instance.trafficDensity
            else random.randint(5, 20)  # Default value
        )
        self.green_time = (
            ontology_instance.greenTime[0]
            if hasattr(ontology_instance, "greenTime") and ontology_instance.greenTime
            else 30  # Default value
        )

    def sense_traffic(self):
        """Simulate sensing traffic density."""
        self.traffic_density = random.randint(5, 50)  # Simulated dynamic traffic density

        # Update the ontology
        if hasattr(self.ontology_instance, "trafficDensity"):
            if self.ontology_instance.trafficDensity:
                # Update existing value
                self.ontology_instance.trafficDensity[0] = self.traffic_density
            else:
                # Initialize the property if it's empty
                self.ontology_instance.trafficDensity.append(self.traffic_density)
        else:
            print(f"Warning: trafficDensity property not found for {self.ontology_instance.name}")

    def adjust_green_time(self):
        """Adjust green light duration based on traffic density."""
        if self.traffic_density > 30:
            self.green_time = min(60, self.green_time + 5)  # Increase green time
        elif self.traffic_density < 10:
            self.green_time = max(15, self.green_time - 5)  # Decrease green time

        if hasattr(self.ontology_instance, "greenTime"):
            if self.ontology_instance.greenTime:
                # Update existing value
                self.ontology_instance.greenTime[0] = self.green_time
            else:
                # Initialize the property if it's empty
                self.ontology_instance.greenTime.append(self.green_time)
        else:
            print(f"Warning: greenTime property not found for {self.ontology_instance.name}")

    def communicate(self, neighbor_agent):
        """Share traffic density with a neighboring agent."""
        if self.traffic_density > 30 and neighbor_agent.traffic_density > 30:
            print(f"Intersection {self.id} coordinating with {neighbor_agent.id} to avoid congestion.")

    def operate(self):
        """Simulate the traffic light operation."""
        print(f"Intersection {self.id}: Green light for {self.green_time} seconds (Traffic: {self.traffic_density} vehicles).")
        time.sleep(1)  # Simulate real-time operation

# Create traffic light agents from ontology instances
traffic_lights = []
for i, instance in enumerate(onto.individuals()):
    if "TrafficLight" in instance.is_a[0].name:  # Adjust class name as per your ontology
        traffic_lights.append(TrafficLightAgent(i + 1, instance))

# Simulation loop
for _ in range(10):  # Simulate 10 cycles
    for i, agent in enumerate(traffic_lights):
        agent.sense_traffic()
        agent.adjust_green_time()

        # Communicate with the next agent (if exists)
        if i < len(traffic_lights) - 1:
            agent.communicate(traffic_lights[i + 1])

        # Operate the traffic light
        agent.operate()

# Save updated ontology
onto.save(file="Updated_TrafficSystem.owl")
print("Updated ontology saved as 'Updated_TrafficSystem.owl'.")
