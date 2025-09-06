# 🤖 Agentic AI Project (agentic_ai_proj)

An agent-based AI project using the **ADK Framework**, demonstrating how intelligent agents can work autonomously with real-world data and tasks.

This project showcases two agent systems:

---

## 🧑‍💼 1. HRIS Agentic System

An AI-powered Human Resources Information System (HRIS) built with a modular agent architecture and backed by an SQLite3 database.

### Features:
- 📋 **Employee Management** (Add, edit, query employees)
- 🗓️ **Leave Management** (Submit, approve, track leave requests)
- 💬 **Performance Tracking** (Store and review employee performance)
- 🚀 **Onboarding Workflow** (Assign and track onboarding tasks)

### Agents:
- `HRManagerAgent` (root agent)
  - `EmployeeRecordsAgent`
  - `LeaveManagementAgent`
  - `PerformanceTrackerAgent`
  - `OnboardingAgent`
  - `QueryAgent`

### Database:
Uses SQLite (`hris.db`) with the following schema:
- `employees`
- `leave_requests`
- `performance_reviews`
- `onboarding_tasks`

---

## 🎲 2. Sample Trivia Agent

A simple demonstration agent that fetches and responds with trivia facts.

### Agent:
- `sample_agent`
  - Replies to user messages with random trivia responses
  - Used to demonstrate basic agent behavior using ADK

---

## 🛠 How to Use

1. **Navigate to the backend folder**:
   ```bash
   cd backend
