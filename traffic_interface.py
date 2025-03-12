from tkinter import *
from owlready2 import *
import random

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
        if hasattr(self.ontology_instance, "trafficDensity"):
            if self.ontology_instance.trafficDensity:
                self.ontology_instance.trafficDensity[0] = self.traffic_density
            else:
                self.ontology_instance.trafficDensity.append(self.traffic_density)

    def adjust_green_time(self):
        """Adjust green light duration based on traffic density."""
        if self.traffic_density > 30:
            self.green_time = min(60, self.green_time + 5)  # Increase green time
        elif self.traffic_density < 10:
            self.green_time = max(15, self.green_time - 5)  # Decrease green time

        if hasattr(self.ontology_instance, "greenTime"):
            if self.ontology_instance.greenTime:
                self.ontology_instance.greenTime[0] = self.green_time
            else:
                self.ontology_instance.greenTime.append(self.green_time)

# Create traffic light agents from ontology instances
traffic_lights = []
for i, instance in enumerate(onto.individuals()):
    if "TrafficLight" in instance.is_a[0].name:  # Adjust class name as per your ontology
        traffic_lights.append(TrafficLightAgent(i + 1, instance))

# GUI Functions
def display_agents():
    """Display traffic light data."""
    result = ""
    for agent in traffic_lights:
        result += f"Intersection {agent.id} - Traffic Density: {agent.traffic_density}, Green Time: {agent.green_time} seconds\n"
    output_text.delete(1.0, END)
    output_text.insert(END, result)

def simulate_updates():
    """Simulate traffic updates and decision-making."""
    status_label.config(text="Simulation in progress...", fg="#F39C12")
    output = ""  # Initialize the output string for displaying simulation results
    congestion_alerts = ""  # Initialize the string for congestion alerts
    congestion_detected = False  # Flag to track if congestion occurs

    # Loop through each agent to simulate traffic updates and light changes
    for i, agent in enumerate(traffic_lights):
        # Sense traffic and adjust green time
        agent.sense_traffic()
        agent.adjust_green_time()

        # Create output for each intersection's green light and traffic status
        output += f"Intersection {agent.id}: Green light for {agent.green_time} seconds (Traffic: {agent.traffic_density} vehicles).\n"
        
        # Apply color-coding to green light
        if agent.green_time > 50:
            output += f"\n!!! HIGH TRAFFIC ALERT at Intersection {agent.id} !!!\n"

        # If this agent has a neighboring agent, simulate communication to avoid congestion
        if i < len(traffic_lights) - 1:
            neighbor_agent = traffic_lights[i + 1]
            if agent.traffic_density > 30 and neighbor_agent.traffic_density > 30:
                congestion_alerts += f"\n!!! CONGESTION ALERT: Intersection {agent.id} coordinating with {neighbor_agent.id} to avoid congestion !!!\n"
                congestion_detected = True

    # Display the output in the GUI text box
    output_text.delete(1.0, END)
    output_text.insert(END, output)

    # Display congestion alerts in a separate box with color highlight
    congestion_alert_text.delete(1.0, END)
    if congestion_alerts:
        congestion_alert_text.insert(END, congestion_alerts)
        congestion_alert_text.config(state=NORMAL, fg="red", bg="#F9EB8B")
    else:
        congestion_alert_text.config(state=NORMAL, fg="#2C3E50", bg="#ecf0f1")

    # Save the updated ontology
    onto.save(file="Updated_TrafficSystem.owl")  # Save changes
    status_label.config(text="Simulation complete and ontology updated.", fg="#2ECC71")

# Create the GUI window
root = Tk()
root.title("Traffic Management System")
root.geometry("800x700")  # Set window size
root.configure(bg="#ecf0f1")  # Background color

# Title Label
Label(root, text="Traffic Management System", font=("Helvetica", 20, "bold"), fg="#2980b9", bg="#ecf0f1").pack(pady=20)

# Buttons for actions with icons
Button(root, text="Display Traffic Lights", command=display_agents, font=("Helvetica", 14), bg="#3498DB", fg="white", relief=RAISED, width=20).pack(pady=10)
Button(root, text="Simulate Traffic Updates", command=simulate_updates, font=("Helvetica", 14), bg="#2ECC71", fg="white", relief=RAISED, width=20).pack(pady=10)

# Output Text area with Scrollbar for regular output
output_frame = Frame(root, bg="#ecf0f1")
output_frame.pack(pady=10)

output_text = Text(output_frame, height=15, width=80, font=("Courier", 12), wrap=WORD, bg="#F7F9F9", fg="#2C3E50", insertbackground="black")
output_text.pack(side=LEFT, fill=BOTH, padx=10)
scrollbar = Scrollbar(output_frame, command=output_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
output_text.config(yscrollcommand=scrollbar.set)

# Congestion Alerts Frame
congestion_frame = Frame(root, bg="#ecf0f1")
congestion_frame.pack(pady=10)

congestion_alert_text = Text(congestion_frame, height=5, width=80, font=("Courier", 12), wrap=WORD, bg="#ecf0f1", fg="#2C3E50", insertbackground="black", state=DISABLED)
congestion_alert_text.pack(side=LEFT, fill=BOTH, padx=10)

# Status Label for simulation
status_label = Label(root, text="", font=("Helvetica", 14), fg="#2C3E50", bg="#ecf0f1")
status_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
