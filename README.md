Multi-Agent System for Traffic Management

🚦 Project Overview

This project is a Traffic Management System that uses an ontology-based multi-agent approach to simulate and manage traffic lights across multiple intersections. The system dynamically adjusts green light durations based on real-time traffic density, aiming to reduce congestion and improve traffic flow efficiency.


✨ Key Features

* Ontology-Based Traffic Simulation
  Uses `TrafficSystem.owl` (OWL ontology) to store and update traffic-related data.

* Dynamic Traffic Light Control
  Automatically adjusts green light duration based on real-time traffic density.

* Traffic Congestion Detection & Coordination
  Identifies high-traffic scenarios and enables communication between adjacent intersections for coordinated traffic management.

* Graphical User Interface (GUI)
  Visual representation of intersection traffic light operations (`traffic_interface.py`).

* Automated Traffic Simulation
  Runs multiple simulation cycles via command line for testing and analysis (`traffic_simulation1.py`).

 📁 File Descriptions
 
`TrafficSystem.owl`      - Ontology file containing the traffic system data.                      
`traffic_interface.py`   - GUI for visualizing and interacting with traffic light behavior.        
`traffic_simulation1.py` - Command-line simulation for automated traffic control and coordination. 

🧰 Requirements

Install the required Python libraries:

pip install owlready2 tkinter

 🚀 How to Run

GUI Simulation

Launch the graphical user interface:

python traffic_interface.py

Automated Simulation (Command-Line)

Run the traffic light simulation in the terminal:

python traffic_simulation1.py


⚙️ How It Works

1. Ontology Loading
   The system loads `TrafficSystem.owl` using the `owlready2` library.

2. Traffic Light Agents
   Each intersection is managed by an autonomous agent that controls its traffic light based on ontology data.

3. Traffic Sensing
   Agents simulate real-time traffic density using random values.

4. Green Light Adjustment

   * High traffic density → longer green light duration
   * Low traffic density → shorter green light duration

5. Inter-Agent Communication
   Neighboring intersections communicate when congestion is detected to synchronize signals and prevent buildup.

6. Ontology Updates
   After each cycle, updated conditions are saved in `Updated_TrafficSystem.owl`.


🔮 Future Enhancements

* Integrate machine learning models for predictive traffic management.
* Add real-time traffic visualization to the GUI.
* Extend the ontology to support multi-lane roads, pedestrian crossings, and emergency vehicle priority.




