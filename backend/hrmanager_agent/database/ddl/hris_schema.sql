-- HRIS Database Schema (DDL - Data Definition Language)
-- Run this to create all the tables

-- Drop tables if they exist (for clean recreation)
DROP TABLE IF EXISTS onboarding_tasks;
DROP TABLE IF EXISTS performance_reviews;
DROP TABLE IF EXISTS leave_requests;
DROP TABLE IF EXISTS employees;

-- Employees Table
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    position TEXT,
    department TEXT,
    date_joined DATE NOT NULL
);

-- Leave Requests Table
CREATE TABLE leave_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    reason TEXT,
    status TEXT DEFAULT 'Pending',  -- Pending, Approved, Rejected
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Performance Reviews Table
CREATE TABLE performance_reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    review_date DATE,
    reviewer TEXT,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),  -- 1-5 scale
    comments TEXT,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Onboarding Tasks Table
CREATE TABLE onboarding_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    task TEXT,
    due_date DATE,
    completed BOOLEAN DEFAULT 0,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);