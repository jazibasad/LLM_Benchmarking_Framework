import json
import os

def create_full_dataset():
    dataset = []
    
    # Example distribution builder (Scale counters to reach 220 total prompts)
    categories = {
        "Knowledge Retrieval": 40,
        "Multi-step Reasoning": 50,
        "Instruction Following": 40,
        "Hallucination Stress Test": 50,
        "Coding Tasks": 40
    }
    
    prompt_counter = 1
    for category, count in categories.items():
        for i in range(1, count + 1):
            prompt_entry = {
                "id": f"P{prompt_counter:03d}",
                "category": category,
                "prompt": f"[{category} - Sample Prompt {i}] Insert specific evaluation query text here.",
                "difficulty_level": "Medium" if i % 2 == 0 else "High"
            }
            dataset.append(prompt_entry)
            prompt_counter += 1

    output_dir = "../04_Datasets"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "full_benchmark_dataset.json")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=4)
        
    print(f"[+] Successfully generated template dataset with {len(dataset)} prompts at {output_file}")

if __name__ == "__main__":
    create_full_dataset()