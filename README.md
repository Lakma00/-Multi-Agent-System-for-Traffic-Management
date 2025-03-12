# -Multi-Agent-System-for-Traffic-Management


Traffic Management System
Overview
This project is a Traffic Management System that utilizes an ontology-based approach to simulate and manage traffic lights at multiple intersections. The system dynamically adjusts traffic light durations based on real-time traffic density, helping to reduce congestion and improve traffic flow efficiency.
Features
•	Ontology-Based Traffic Simulation: Uses OWL ontology (TrafficSystem.owl) to store and update traffic-related data.
•	Dynamic Traffic Light Control: Adjusts green light duration based on real-time traffic density.
•	Traffic Congestion Detection: Identifies high-traffic scenarios and enables coordination between adjacent traffic lights.
•	Graphical User Interface (GUI): Visual representation of traffic light operations (traffic_interface.py).
•	Automated Simulation: Runs multiple traffic cycles for testing (traffic_simulation1.py).
File Descriptions
•	TrafficSystem.owl: Ontology file containing traffic system data.
•	traffic_interface.py: A GUI-based system for visualizing traffic light behavior and simulation results.
•	traffic_simulation1.py: A command-line simulation that automates traffic updates and coordination among intersections.
Requirements
To run this project, install the following dependencies:
pip install owlready2 tkinter
How to Run
GUI Simulation
Run the following command to launch the graphical interface:
python traffic_interface.py
Automated Traffic Simulation
To run a command-line simulation of traffic behavior, use:
python traffic_simulation1.py
How It Works
1.	Ontology Loading: The system loads the ontology file (TrafficSystem.owl).
2.	Traffic Light Agents: Each intersection has an agent managing its traffic light based on the ontology data.
3.	Traffic Sensing: Agents randomly generate traffic density values.
4.	Green Time Adjustment: If traffic is high, green light duration increases; if low, it decreases.
5.	Communication Between Intersections: If congestion is detected at adjacent intersections, they coordinate to reduce traffic buildup.
6.	Ontology Updates: The system saves updated traffic conditions in Updated_TrafficSystem.owl.
Future Enhancements
•	Implement machine learning for predictive traffic management.
•	Enhance GUI with real-time traffic visualization.
•	Extend ontology for multi-lane and pedestrian considerations.

