# LLM-Benchmarking-Framework

A scientific, reproducible framework for evaluating the performance and reliability of freely accessible Large Language Models (LLMs).

## Project Overview
This repository contains a comprehensive benchmarking suite designed to evaluate free-tier LLMs across multiple dimensions, including multi-step knowledge retrieval, reasoning depth, instruction adherence, and hallucination robustness. To mitigate contamination, tests are conducted using an original 220-prompt library processed through an automated, resumable multi-model execution architecture.

## Repository Directory Structure
- `01_Proposal/`: Contains the formal project proposal and research scope submitted for supervisor approval (`project_proposal.docx`).
- `02_Reports/`: Weekly progress reports tracking development milestones using structured status updates (`progress_report_w1.docx`, `progress_report_w2.docx`, `progress_report_w3.docx`).
- `03_Code/`: Independent automated benchmark runners for multi-model evaluation (`run_gemini_benchmark.py`, `run_openai_benchmark.py`, `run_groq_benchmark.py`).
- `04_Datasets/`: Original prompt datasets and testing subsets, including the complete 220-prompt library (`full_benchmark_dataset.json`).
- `05_Logs_Results/`: Isolated experiment data outputs and serialized JSON prompt logs partitioned by provider:
  - `Gemini_Logs/`: Individual response JSONs and consolidated reports for Google Gemini (`gemini-2.5-flash`).
  - `OpenAI_Logs/`: Individual response JSONs and consolidated reports for OpenAI GPT (`gpt-4o-mini`).
  - `Groq_Logs/`: Individual response JSONs and consolidated reports for Groq Llama (`llama-3.3-70b-versatile`).
- `06_Final_Report/`: The evolving research paper, methodology documentation, and statistical findings (`main_research_paper.docx`).

## Methodology & Hypotheses
The project evaluates models using a granular 0–5 scoring rubric across five core categories:
1. Knowledge Retrieval
2. Multi-step Reasoning
3. Instruction Following
4. Hallucination Stress Testing
5. Coding Tasks

The framework is engineered with provider-specific rate-limit jitter (`random.uniform`), exponential backoff retry algorithms, and automated state-persistence checks (`os.path.exists`) to enable fault-tolerant, resumable daily data collection across free cloud API tiers without quota waste or data loss.

## Current Project Status
- **Week 1:** Completed repository setup, project proposal approval, evaluation rubric design, and research hypotheses formulation.
- **Week 2:** Developed the core Python execution and logging runner (`benchmark_runner.py`) with structured schema integration and dataset validation.
- **Week 3:** Decoupled the monolithic pipeline into three specialized runner modules (`run_gemini_benchmark.py`, `run_openai_benchmark.py`, `run_groq_benchmark.py`) with automated session resumption, isolated logging partitions, and rate-limit engineering.
- **Week 4 (Current):** Executing automated data collection across the 220-prompt dataset for all three target models and initiating comparative log analysis.

## Author & Supervision
- **Researcher:** Jazib Asad
- **Supervisor:** Mr. Uzair, NESCOM (CENTech)