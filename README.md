# 🔋 Battery Charging Protocols using PyBaMM

## 📌 Overview
This repository contains implementations of various lithium-ion battery charging protocols using **PyBaMM**.

The objective of this project is to **recreate, simulate, and analyze different charging strategies** and understand their impact on battery behavior.

---

## ⚙️ Implemented Charging Protocols

The following charging strategies have been implemented:

- 🔹 **CCCV (Constant Current Constant Voltage)**
- 🔹 **Multistage Constant Current (MSCC)**
- 🔹 **Pulse Charging (PC)**
- 🔹 **CC + Pulse Charging (CCPC)**
- 🔹 **Boost Charging (BC)**

All protocols are implemented using **PyBaMM’s `Experiment` API**.

---

## 📁 Project Structure


---

## 📊 Results

### Charging Protocol Outputs

| Protocol | Output |
|---------|--------|
| CCCV | ![](plots/CCCV.png) |
| Multistage CC | ![](plots/MultistageCC.png) |
| Pulse Charging | ![](plots/PulseC.png) |
| CC + Pulse Charging | ![](plots/CC_PulseC.png) |
| Boost Charging | ![](plots/BoostCharging.png) |

---

## 🧪 Methodology

- Charging protocols are implemented using **PyBaMM simulations**
- The `Experiment` class is used to define time-dependent current profiles
- Simulations track key battery variables such as:
  - Voltage
  - Current
  - State of Charge (SOC)

The implementations aim to **closely replicate real-world charging strategies** described in literature.

---

## 📚 Reference

This project is based on the study:

Keil, P., & Jossen, A. (2016)  
*Charging protocols for lithium-ion batteries and their impact on cycle life—An experimental study with different 18650 high-power cells.*  
Journal of Energy Storage, 6, 125–141.

In this work, I have attempted to recreate and simulate the key charging protocols described in the paper using PyBaMM. The goal is to bridge theoretical research with computational modeling and gain practical insight into battery charging strategies.

---

## 🎯 Objectives

- Recreate real-world battery charging protocols  
- Understand differences between charging strategies  
- Analyze their impact on voltage behavior and charging dynamics  
- Gain hands-on experience with battery modeling using PyBaMM  

---

## 🚀 Future Work

- Incorporate battery degradation and cycle life models  
- Compare efficiency and charging time across protocols  
- Extend simulations to different battery chemistries  
- Perform quantitative comparisons between protocols  

---

## 👨‍💻 Author

This project was developed as part of self-learning and exploration in battery modeling and simulation.
