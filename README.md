# LLM-Benchmarking-Framework

A scientific, reproducible framework for evaluating the performance and reliability of freely accessible Large Language Models (LLMs).

## Project Overview
This repository contains a comprehensive benchmarking suite designed to evaluate free-tier LLMs across multiple dimensions, including multi-step knowledge retrieval, reasoning depth, instruction adherence, and hallucination robustness. To mitigate contamination, tests are conducted using an original 220-prompt library.

## Repository Directory Structure
- `01_Proposal/`: Contains the formal project proposal and research scope submitted for supervisor approval (`project_proposal.docx`).
- `02_Reports/`: Weekly progress reports tracking development milestones using structured status updates (`progress_report_w1.docx`, `progress_report_w2.docx`, `progress_report_w3.docx`).
- `03_Code/`: Core Python scripts, including batch execution engines and manual logging assistants (`benchmark_runner.py`).
- `04_Datasets/`: Original prompt datasets and testing subsets, including the complete 220-prompt library (`full_benchmark_dataset.json`).
- `05_Logs_Results/`: Raw experiment data outputs, serialized JSON logs, and execution traces.
- `06_Final_Report/`: The evolving research paper, methodology documentation, and statistical findings (`main_research_paper.docx`).

## Methodology & Hypotheses
The project evaluates models using a granular 0–5 scoring rubric across five core categories:
1. Knowledge Retrieval
2. Multi-step Reasoning
3. Instruction Following
4. Hallucination Stress Testing
5. Coding Tasks

The framework is specifically engineered to test three core hypotheses regarding reasoning efficiency scaling, non-linear hallucination sensitivity under complex premises, and constraint-following robustness.

## Current Project Status
- **Week 1:** Completed repository setup, project proposal approval, evaluation rubric design, and research hypotheses formulation.
- **Week 2:** Developed the core Python execution and logging runner (`benchmark_runner.py`) with structured schema integration.
- **Week 3:** Completed full dataset curation, successfully establishing the comprehensive 220-prompt library (`full_benchmark_dataset.json`) across all five specialized testing categories.
- **Week 4 (Upcoming):** Initiating manual test runs of the benchmarking prompts across targeted free-tier model chat interfaces and serializing logs.

## Author & Supervision
- **Researcher:** Jazib Asad
- **Supervisor:** Mr. Uzair, NESCOM (CENTech)