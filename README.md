# Industrial Equipment Environmental Monitoring System

## Project Overview

This project is a web-based Industrial IoT monitoring system designed to collect, store, and visualize environmental data from sensitive industrial equipment.

The system focuses on monitoring temperature and humidity around industrial assets such as electrical panels, electric motors, compressors, control rooms, and production lines. These environmental factors can directly affect equipment reliability, maintenance cost, and production continuity.

## Business Problem

In industrial environments, many sensitive devices must operate within acceptable temperature and humidity ranges. Lack of continuous environmental monitoring can lead to:

- Reduced equipment lifetime
- Unexpected component failures
- Unplanned production downtime
- Increased maintenance and repair costs

## Proposed Solution

The proposed solution is an IoT-based monitoring system that collects environmental data from equipment locations, stores the data in a database, and displays the current and historical status through a web dashboard.

## MVP Scope

The first version of the system focuses only on the essential monitoring workflow:

- Register industrial devices
- Receive temperature data
- Receive humidity data
- Store sensor data in a database
- Provide backend API endpoints
- Display latest sensor values in a web dashboard
- Show simple temperature and humidity charts
- Run the project using Docker Compose

## Target Users

- Factory operators
- Maintenance managers
- Industrial equipment monitoring teams

## Initial System Architecture

```text
IoT Device / Simulator
        |
        | HTTP POST /sensor-data
        v
FastAPI Backend
        |
        v
PostgreSQL Database
        |
        v
Web Dashboard
