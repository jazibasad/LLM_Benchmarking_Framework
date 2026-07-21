import os
import json
import time
import random
import logging
from datetime import datetime

# Configure logging for experiment tracking
logging.basicConfig(
    filename='../05_Logs_Results/experiment_execution.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LLMBenchmarkRunner:
    def __init__(self, dataset_path, output_dir):
        self.dataset_path = dataset_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def load_dataset(self):
        """Loads the 220-prompt benchmarking dataset."""
        if not os.path.exists(self.dataset_path):
            logging.error(f"Dataset not found at {self.dataset_path}")
            raise FileNotFoundError(f"Dataset missing: {self.dataset_path}")
        
        with open(self.dataset_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logging.info(f"Successfully loaded {len(data)} prompts from dataset.")
        return data

    def simulate_model_inference(self, prompt, model_name):
        """
        Simulates API interaction with built-in exponential backoff 
        and jitter to safely manage free-tier rate limits.
        """
        max_retries = 3
        backoff_factor = 2

        for attempt in range(max_retries):
            try:
                # Placeholder for actual API client call (e.g., OpenAI/Gemini/Ollama)
                # Adding randomized jitter to prevent rate-limit collisions
                jitter = random.uniform(0.1, 0.5)
                time.sleep(1 + jitter)
                
                # Mock response structure for framework validation
                response_text = f"Simulated response for: '{prompt[:30]}...' using {model_name}"
                return response_text

            except Exception as e:
                wait_time = (backoff_factor ** attempt) + random.uniform(0, 1)
                logging.warning(f"Rate limit or network error on {model_name}. Retrying in {wait_time:.2f}s... Error: {e}")
                time.sleep(wait_time)
        
        logging.error(f"Failed to fetch response for model {model_name} after {max_retries} retries.")
        return None

    def execute_benchmark(self, model_names):
        """Runs the complete evaluation loop across all models and prompts."""
        prompts = self.load_dataset()
        results = []

        for model in model_names:
            print(f"[*] Starting benchmark run for model: {model}")
            for item in prompts:
                prompt_id = item.get("id")
                prompt_text = item.get("prompt")
                category = item.get("category")

                # Fetch response with throttling safety
                response = self.simulate_model_inference(prompt_text, model)

                result_entry = {
                    "timestamp": datetime.now().isoformat(),
                    "model": model,
                    "prompt_id": prompt_id,
                    "category": category,
                    "prompt": prompt_text,
                    "response": response,
                    "status": "Success" if response else "Failed"
                }
                results.append(result_entry)

        # Save raw results to JSON for subsequent analysis
        output_file = os.path.join(self.output_dir, f"raw_experiment_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4)
        
        print(f"[+] Benchmark execution complete. Results saved to {output_file}")
        logging.info(f"Benchmark execution complete. Results saved to {output_file}")

if __name__ == "__main__":
    # Example execution configuration
    DATASET = "../04_Datasets/sample_prompts.json"
    OUTPUT = "../05_Logs_Results/"
    MODELS = ["free-tier-model-a", "free-tier-model-b"]

    # runner = LLMBenchmarkRunner(DATASET, OUTPUT)
    # runner.execute_benchmark(MODELS)
    print("Framework pipeline initialized successfully.")