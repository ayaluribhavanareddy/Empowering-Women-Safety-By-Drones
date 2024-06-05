# Empowering-Women-Safety-By-Drones
This project addresses the safety concerns in red alert areas where women face numerous risks, including physical violence, sexual assault, trafficking, and harassment. Our solution deploys autonomous drones equipped with sophisticated sensors and alert mechanisms to detect suspicious activities and assist in traffic management.
Features
Safety Monitoring
Autonomous Drones: Equipped with cameras and motion sensors.
Threat Detection: Utilizes machine learning models trained on datasets of suspicious activities to identify potential threats.
Alert Mechanism: Upon detecting a threat, the drone activates an alert system, emitting a beep sound to nearby police stations. It captures and sends the GPS location and a photo of the suspect vehicle to the authorities.
Traffic Management
Traffic Density Measurement: Drones capture real-time data on vehicle flow on roads or highways using sensors and cameras.
Data Analysis: Helps in managing and mitigating traffic congestion.
Dataset
The system uses a combination of publicly available datasets and custom-collected data to train the machine learning models. These datasets include:

Suspicious Activities Dataset: Contains images and video clips of various suspicious activities.
Traffic Flow Dataset: Includes traffic density and flow data collected from urban areas.
Code Structure
1. Data Collection
data_collection/: Scripts for collecting and preprocessing the datasets.
2. Model Training
model_training/: Code for training the machine learning models to detect suspicious activities and analyze traffic density.
3. Drone Control
drone_control/: Scripts to control drone operations, including real-time data processing, threat detection, and alert system activation.
4. Alert System
alert_system/: Code to handle the alert mechanisms, including sending GPS locations and photos to police stations.
Installation
To set up the project locally, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/drone-patrolling-system.git
Navigate to the project directory:
bash
Copy code
cd drone-patrolling-system
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Collect Data: Run the data collection scripts to gather the necessary datasets.
Train Models: Use the training scripts to build the machine learning models.
Deploy Drones: Set up the drones with the control scripts for real-time monitoring.
Activate Alert System: Ensure the alert system is operational for immediate response.
