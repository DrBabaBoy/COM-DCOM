# COM-DCOM Print Server Simulation

A distributed system simulation demonstrating load-balanced printing tasks using COM/DCOM architecture, with virtual printers and client-server communication.

## 📌 Overview

This project simulates a **print server environment** where multiple clients submit documents to a central server, which dynamically distributes printing tasks across virtual printers. Print jobs are displayed in the console for visualization.

## ✨ Key Features

- **Load Balancing**: Distributes print jobs evenly across available virtual printers.
- **Virtual Printers**: Simulates printers as console outputs with unique IDs.
- **Client-Server Architecture**: Clients connect via `localhost` to submit print jobs.
- **Job Queueing**: Handles concurrent requests and queues jobs during peak loads.
- **Status Monitoring**: Real-time logging of printer availability and job statuses.

## 🛠️ Technologies Used

- **COM/DCOM**: For distributed component communication.
- **Python**: Core server/client implementation.
- **Flask**: HTTP server for handling client requests.
- **Threading**: Concurrent management of printers and jobs.
- **HTML/CSS**: Basic client interface for file submission.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager
