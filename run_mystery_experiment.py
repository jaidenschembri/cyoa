#!/usr/bin/env python3
"""
Quick Pine Hollow Mystery Experiment
Test GPT-2 on Twin Peaks-inspired mystery scenarios
"""

import pandas as pd
import mlflow
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
import torch
import warnings
warnings.filterwarnings('ignore')

def main():
    print("🌲 Starting Pine Hollow Mystery Experiment")
    print(f"⚡ Using device: {'GPU' if torch.cuda.is_available() else 'CPU'}")
    
    # Load our enhanced mystery dataset
    mystery_df = pd.read_csv('data/pine_hollow_enhanced_v2.csv')
    print(f"📚 Loaded {len(mystery_df)} mystery scenarios")
    print(f"🎬 Atmosphere progression: {mystery_df['atmosphere_level'].value_counts().to_dict()}")
    print(f"🎭 Dialogue styles: {mystery_df['dialogue_style'].nunique()} unique styles")
    
    # Load GPT-2 model
    print("\n🤖 Loading GPT-2 model...")
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    
    generator = pipeline('text-generation', 
                        model=model, 
                        tokenizer=tokenizer,
                        device=0 if torch.cuda.is_available() else -1)
    print("✅ GPT-2 model loaded")
    
    # Generate mystery story responses
    print("\n🌫️ Generating mystery story responses...")
    generated_stories = []
    
    for idx, row in mystery_df.iterrows():
        prompt = f"Mystery Story: {row['prompt']} {row['response']}"
        
        # Generate AI response
        ai_response = generator(
            prompt,
            max_length=len(prompt.split()) + 40,
            temperature=0.8,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            num_return_sequences=1
        )[0]['generated_text']
        
        # Extract generated part
        ai_continuation = ai_response[len(prompt):].strip()
        
        generated_stories.append({
            'prompt': row['prompt'],
            'human_response': row['response'],
            'ai_response': ai_continuation,
            'branch_type': row['branch_type'],
            'atmosphere_level': row['atmosphere_level'],
            'dialogue_style': row['dialogue_style'],
            'choice_a': row['choice_a'],
            'choice_b': row['choice_b']
        })
        
        print(f"📝 Generated story {idx + 1}/{len(mystery_df)} - {row['atmosphere_level']} atmosphere")
    
    results_df = pd.DataFrame(generated_stories)
    
    # Display sample results
    print("\n🌲 PINE HOLLOW MYSTERY RESULTS (Sample)")
    print("=" * 80)
    
    for idx in range(min(3, len(results_df))):
        row = results_df.iloc[idx]
        print(f"\n🎬 SCENARIO {idx + 1}: {row['branch_type']} ({row['atmosphere_level']})")
        print(f"📖 PROMPT: {row['prompt'][:100]}...")
        print(f"👤 HUMAN: {row['human_response'][:150]}...")
        print(f"🤖 AI: {row['ai_response'][:150]}...")
        print(f"🎭 Style: {row['dialogue_style']}")
    
    # Save results
    results_df.to_csv('generated_stories_pine_hollow_baseline.csv', index=False)
    
    # Log to MLflow
    print("\n📊 Logging to MLflow...")
    mlflow.set_experiment("cyoa_model_experiments")
    
    with mlflow.start_run(run_name="pine_hollow_mystery_baseline"):
        # Parameters
        mlflow.log_param("model_name", model_name)
        mlflow.log_param("story_theme", "pine_hollow_mystery")
        mlflow.log_param("data_source", "twin_peaks_inspired")
        mlflow.log_param("num_scenarios", len(mystery_df))
        mlflow.log_param("atmosphere_progression", "twin_peaks_to_stranger_things")
        
        # Metrics
        mlflow.log_metric("stories_generated", len(results_df))
        mlflow.log_metric("avg_response_length", results_df['ai_response'].str.len().mean())
        mlflow.log_metric("twin_peaks_stories", len(results_df[results_df['atmosphere_level'] == 'twin_peaks']))
        mlflow.log_metric("stranger_things_stories", len(results_df[results_df['atmosphere_level'] == 'stranger_things']))
        
        # Artifacts
        mlflow.log_artifact('generated_stories_pine_hollow_baseline.csv')
        mlflow.log_artifact('data/pine_hollow_enhanced_v2.csv')
        
        print("✅ Experiment logged to MLflow")
    
    print(f"\n🎯 EXPERIMENT COMPLETE!")
    print(f"📁 Results: generated_stories_pine_hollow_baseline.csv")
    print(f"🌐 MLflow UI: http://localhost:5000")
    print(f"📊 Compare with anime baseline to see the difference!")

if __name__ == "__main__":
    main() 