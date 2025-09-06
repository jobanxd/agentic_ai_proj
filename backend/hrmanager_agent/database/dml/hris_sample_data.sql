-- HRIS Sample Data (DML - Data Manipulation Language)
-- Run this after creating the schema to populate with sample data

-- Sample Employees
INSERT INTO employees (name, email, position, department, date_joined) VALUES
('Alice Johnson', 'alice.johnson@example.com', 'Software Engineer', 'Engineering', '2023-06-01'),
('Bob Smith', 'bob.smith@example.com', 'HR Manager', 'Human Resources', '2022-03-15'),
('Charlie Lee', 'charlie.lee@example.com', 'Data Analyst', 'Data Science', '2023-01-10'),
('Diana Martinez', 'diana.martinez@example.com', 'Product Manager', 'Product', '2022-08-20'),
('Eva Chen', 'eva.chen@example.com', 'Senior Developer', 'Engineering', '2021-11-05'),
('Frank Wilson', 'frank.wilson@example.com', 'Marketing Specialist', 'Marketing', '2023-09-12'),
('Grace Kim', 'grace.kim@example.com', 'UX Designer', 'Design', '2023-04-18'),
('Henry Brown', 'henry.brown@example.com', 'DevOps Engineer', 'Engineering', '2022-12-01');

-- Sample Leave Requests
INSERT INTO leave_requests (employee_id, start_date, end_date, reason, status) VALUES
(1, '2025-09-10', '2025-09-12', 'Family Event', 'Pending'),
(2, '2025-08-01', '2025-08-05', 'Medical', 'Approved'),
(3, '2025-07-15', '2025-07-18', 'Personal vacation', 'Approved'),
(4, '2025-10-20', '2025-10-22', 'Conference attendance', 'Pending'),
(5, '2025-06-28', '2025-07-02', 'Summer break', 'Rejected'),
(6, '2025-11-05', '2025-11-07', 'Wedding ceremony', 'Pending'),
(7, '2025-09-25', '2025-09-26', 'Sick leave', 'Approved');

-- Sample Performance Reviews
INSERT INTO performance_reviews (employee_id, review_date, reviewer, rating, comments) VALUES
(1, '2025-06-30', 'Bob Smith', 4, 'Great progress, needs to collaborate more.'),
(3, '2025-07-15', 'Alice Johnson', 5, 'Excellent data reporting and analysis.'),
(4, '2025-06-20', 'Eva Chen', 3, 'Good product insights but needs better stakeholder communication.'),
(5, '2025-07-05', 'Bob Smith', 5, 'Outstanding technical leadership and mentoring skills.'),
(6, '2025-06-25', 'Diana Martinez', 4, 'Creative campaigns with strong engagement metrics.'),
(7, '2025-07-10', 'Eva Chen', 4, 'Excellent design thinking and user research capabilities.'),
(8, '2025-06-18', 'Alice Johnson', 3, 'Solid infrastructure work, needs to improve documentation.');

-- Sample Onboarding Tasks
INSERT INTO onboarding_tasks (employee_id, task, due_date, completed) VALUES
(1, 'Complete Security Training', '2023-06-05', 1),
(3, 'Meet Team Lead', '2023-01-12', 0),
(6, 'Setup Development Environment', '2023-09-15', 1),
(6, 'Complete HR Orientation', '2023-09-14', 1),
(6, 'Review Marketing Guidelines', '2023-09-20', 0),
(7, 'Complete Design System Training', '2023-04-22', 1),
(7, 'Meet Design Team', '2023-04-20', 1),
(7, 'Setup Design Tools Access', '2023-04-25', 0),
(8, 'Infrastructure Security Briefing', '2022-12-05', 1),
(8, 'Docker & Kubernetes Training', '2022-12-15', 0),
(1, 'Code Review Process Training', '2023-06-10', 1),
(4, 'Product Strategy Workshop', '2022-08-25', 1);