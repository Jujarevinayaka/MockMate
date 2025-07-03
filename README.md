# MockMate

This project is a collection of job descriptions (JDs) and prompt templates for various roles, designed to help job seekers prepare for interviews.

## Directory Structure

- `JDs/`: Contains job descriptions in Markdown format.
- `PromptBank/`: Contains prompt templates for different roles, each designed to simulate a specific interview type.
- `Resume/`: Contains resume templates.

## Usage

The `PromptBank` directory contains several specialized prompts, each acting as a distinct interview simulator. To use them, you will interact with the AI, providing the requested input (typically a job description and your resume), and the AI will guide you through a mock interview or analysis based on the selected prompt.

Here's a breakdown of the available interview simulations:

-   **01_JFA.txt (Job Fit Analyzer):**
    *   **Role:** Brutally Honest Job Fit Analyzer.
    *   **Purpose:** Provides a candid assessment of your job fit by comparing your qualifications against a given job description. It offers an overall fit score, highlights strengths and critical gaps, assesses interview likelihood, and recommends whether to apply, upskill, or look elsewhere.
    *   **Input:** Full job description and your resume.

-   **02_HM.txt (Hiring Manager):**
    *   **Role:** First-Round Hiring Manager.
    *   **Purpose:** Simulates a hiring manager-style mock interview focusing on your experience, communication, initiative, and team fit. You'll be asked open-ended questions, receive feedback after each answer, and get a final summary with a shortlist decision.
    *   **Input:** Job description and your resume.

-   **03_PM.txt (Product Manager):**
    *   **Role:** Senior Product Manager Interviewer.
    *   **Purpose:** Conducts a rigorous product interview to assess your product thinking, strategic clarity, customer empathy, and execution ability through scenario-based questions.
    *   **Input:** Job description and your resume.

-   **03_TL.txt (Technical Lead):**
    *   **Role:** Senior Technical Lead Interviewer.
    *   **Purpose:** Conducts a rigorous technical interview to assess core technical capabilities, including problem-solving, coding, system design, architectural thinking, and collaboration.
    *   **Input:** Job description, your resume/technical background, and optional area of technical focus.

-   **04_TPM.txt (Technical Product Manager):**
    *   **Role:** Senior Technical Product Manager Interviewer.
    *   **Purpose:** Provides a deep-dive TPM interview to evaluate your product sense, technical fluency, and cross-functional leadership, focusing on technical decision-making and platform thinking.
    *   **Input:** Job description and your resume.

-   **05_Man.txt (Managerial Interviewer):**
    *   **Role:** Managerial Interviewer.
    *   **Purpose:** Assesses your ability to lead, manage ambiguity, handle pressure, and drive outcomes through people, focusing on leadership competencies and behavioral aspects.
    *   **Input:** Job description and your resume.

-   **06_HR.txt (HR Interviewer):**
    *   **Role:** Human Resources Interviewer.
    *   **Purpose:** Simulates a final HR screening round to evaluate cultural fit, motivation, compensation alignment, communication skills, and ethical awareness.
    *   **Input:** Job description, your resume, preferred location, and compensation expectations.

The `meta_runner.md` file provides instructions on how to sequentially run these interview simulations.

## Contributing

Contributions are welcome! Please refer to the project's guidelines for contributing.

