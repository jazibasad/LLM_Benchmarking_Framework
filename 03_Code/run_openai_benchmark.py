import os
import json
import time
import random
from datetime import datetime
import openai

# Configuration Paths & Constants
DATASET_PATH = "../04_Datasets/full_benchmark_dataset.json"
OUTPUT_DIR = "../05_Logs_Results/OpenAI_Logs/"
MODEL_NAME = "gpt-4o-mini"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize the OpenAI Client (pulls OPENAI_API_KEY from environment variables automatically)
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def run():
    if not os.path.exists(DATASET_PATH):
        print(f"[ERROR] Dataset not found at {DATASET_PATH}. Please ensure full_benchmark_dataset.json is placed correctly.")
        return

    with open(DATASET_PATH, 'r', encoding='utf-8') as f:
        prompts = json.load(f)
        
    print(f"[*] Initializing OpenAI Benchmark ({len(prompts)} total prompts)")
    results = []
    
    for item in prompts:
        prompt_id = item["id"]
        file_path = os.path.join(OUTPUT_DIR, f"openai_{prompt_id}.json")
        
        # AUTOMATIC RESUME CHECK: Skip if already processed in a previous session
        if os.path.exists(file_path):
            print(f"[SKIP] OpenAI prompt {prompt_id} already completed. Loading from cache.")
            with open(file_path, 'r', encoding='utf-8') as sf:
                results.append(json.load(sf))
            continue
            
        print(f"[*] Processing OpenAI prompt: {prompt_id}")
        success, attempts = False, 0
        response_text = ""
        
        while not success and attempts < 3:
            try:
                attempts += 1
                # Standard rate-limit jitter (1.0s to 3.0s delay)
                time.sleep(random.uniform(1.0, 3.0))
                
                response = client.chat.completions.create(
                    model=MODEL_NAME, 
                    messages=[{"role": "user", "content": item["prompt"]}]
                )
                response_text = response.choices[0].message.content
                success = True
            except Exception as e:
                wait_time = (2 ** attempts) + random.uniform(1.0, 2.0)
                print(f"[WARNING] OpenAI limit/error hit on {prompt_id}. Retrying in {wait_time:.2f}s... Error: {e}")
                time.sleep(wait_time)
                
        if success:
            entry = {
                "model": MODEL_NAME, 
                "prompt_id": prompt_id, 
                "category": item.get("category"),
                "prompt": item["prompt"],
                "response": response_text, 
                "timestamp": datetime.now().isoformat()
            }
            # Save individual prompt log immediately
            with open(file_path, 'w', encoding='utf-8') as inf:
                json.dump(entry, inf, indent=4, ensure_ascii=False)
            results.append(entry)
        else:
            print(f"[ERROR] Failed to process OpenAI prompt {prompt_id} after 3 attempts.")

    # Save final aggregated compilation report
    final_report_path = os.path.join(OUTPUT_DIR, "final_openai_report.json")
    with open(final_report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print("[+] OpenAI Benchmark Execution Finished Successfully.")

if __name__ == "__main__":
    run()