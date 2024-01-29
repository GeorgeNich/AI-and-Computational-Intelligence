# Fuzzy Car Control Guide

This guide provides a structured overview of the Fuzzy Car Control project, outlining key components and resources for understanding and using the system.

## Table of Contents

1. [Introduction](#introduction)
2. [Repository Structure](#repository-structure)
3. [Implementation Details](#implementation-details)
4. [Design of the Fuzzy Inference System](#design-of-the-fuzzy-inference-system)
5. [Control Space Visualization](#control-space-visualization)
6. [Interactive Widget for Testing](#interactive-widget-for-testing)
7. [Simulation and Analysis](#simulation-and-analysis)
8. [Limitations and Future Improvements](#limitations-and-future-improvements)
9. [Contributions](#contributions)
10. [References](#references)

## Introduction

The Fuzzy Car Control project is focused on creating an Automatic Braking System using a Fuzzy Logic Controller. This system enhances safety by adjusting braking force based on the vehicle's speed and distance from obstacles. This guide provides an organized structure to explore and understand the project's components and resources.

## Repository Structure

- **[PBL1_Fuzzy_Logic_Automatic_Braking_Controller.ipynb](PBL1_Fuzzy_Logic_Automatic_Braking_Controller.ipynb)**: The Jupyter Notebook containing the Python code for the Fuzzy Logic Controller implementation and simulations.

- **[README_FuzzyLogic_Introduction.md](README_FuzzyLogic_Introduction.md)**: The introductory Markdown file that provides an overview of the project and its components (you are currently reading this).

- **[SIT215_PBL1_Fuzzy_Car_Control_Report.pdf](SIT215_PBL1_Fuzzy_Car_Control_Report.pdf)**: A comprehensive report detailing the project's design, implementation, and analysis.

## Implementation Details

- [Defining Fuzzy Sets and Membership Functions](#defining-fuzzy-sets-and-membership-functions)
- [Establishing Rules for Fuzzy Logic Control](#establishing-rules-for-fuzzy-logic-control)
- [Visualizations of Membership Functions](#visualizations-of-membership-functions)
- [Interactive Widget for Testing](#interactive-widget-for-testing)

## Design of the Fuzzy Inference System

The Fuzzy Inference System processes two primary inputs: distance and speed. These inputs are fuzzified into linguistic variables and processed through a set of predefined rules. The rules determine the appropriate brake force output based on the current values of distance and speed.

### Defining Fuzzy Sets and Membership Functions

- Linguistic variables include "very_close," "close," "far," "very_slow," "slow," "medium," "fast," "very_fast," "hard," "soft," "reduce," and "nil."

### Establishing Rules for Fuzzy Logic Control

- [Rule 1](#rule-1): If distance is close and speed is slow or medium, then apply soft braking.
- [Rule 2](#rule-2): If distance is far and speed is very_slow or slow, then apply reduced braking.
- [Rule 3](#rule-3): If distance is far and speed is medium, fast, or very_fast, do not apply brake.
- [Rule 4](#rule-4): If distance is very_close, apply hard braking.

### Visualizations of Membership Functions

- [Membership Functions for Distance, Speed, and Brake](#membership-functions-for-distance-speed-and-brake)
- [Control Space Visualization](#control-space-visualization)

### Interactive Widget for Testing

- [Interactive Testing Widget](#interactive-widget-for-testing)

## Simulation and Analysis

- [Simulation of Fuzzy Logic Controller](#simulation-of-fuzzy-logic-controller)
- [Analysis of Controller Performance](#analysis-of-controller-performance)

## Limitations and Future Improvements

- [Addressing Physical Constraints](#addressing-physical-constraints)
- [Surface Recognition](#surface-recognition)
- [Exploring Deep Learning Approaches](#exploring-deep-learning-approaches)

## Contributions

- [Team Collaboration](#team-collaboration)
- [Roles and Contributions](#roles-and-contributions)

## References

- [Research and Resources](#research-and-resources)

Explore each section of this guide to gain a deeper understanding of the Fuzzy Car Control project and its components.
