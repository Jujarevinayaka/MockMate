# MockMate

MockMate is your personal AI interview coach. It transforms your command-line assistant into a suite of expert interviewers, from hiring managers to technical leads, allowing you to practice for specific job roles. Get realistic, role-specific practice sessions and actionable feedback tailored to your resume and the job you want, helping you build the confidence to ace your next interview.

## Directory Structure

- `JDs/`: **Add your target job description here.**
- `PromptBank/`: Contains prompt templates for different roles, each designed to simulate a specific interview type.
- `Resume/`: **Add your resume here.**

## How to Use MockMate

MockMate helps you prepare for interviews by simulating various interview scenarios with an AI.

### Steps to Get Started:

1.  **Add Your Job Description:** Place the job description you are targeting into the `JDs/` folder. You can replace the existing `Google.md` file or add a new one.
2.  **Add Your Resume:** Add your own resume to the `Resume/` folder. You can replace the existing `Resume.md` file.
3.  **Run the Simulations:**
    *   Paste the path `PromptBank/meta_runner.txt` into a large Gemini CLI. This prompt acts as a controller, guiding the AI through the different interview simulations.
    *   The AI will start with the first simulation, the **Job Fit Analyzer**, and will ask for the job description and your resume.
    *   Follow the on-screen instructions. After each simulation, you can say "Next Prompt" to proceed to the next interview type.

### Available Interview Simulations:

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

## Contributing

Contributions are welcome! Please refer to the project's guidelines for contributing.
