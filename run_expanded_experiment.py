#!/usr/bin/env python3
"""
Expanded Pine Hollow Mystery Experiment
Test GPT-2 on our complete story arc with atmospheric progression
"""

import pandas as pd
import mlflow
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
import torch
import warnings
warnings.filterwarnings('ignore')

def main():
    print("🌲 Starting EXPANDED Pine Hollow Mystery Experiment")
    print("=" * 60)
    print(f"⚡ Using device: {'GPU' if torch.cuda.is_available() else 'CPU'}")
    
    # Load our expanded mystery dataset
    expanded_df = pd.read_csv('data/pine_hollow_expanded.csv')
    print(f"📚 Loaded {len(expanded_df)} mystery scenarios")
    
    # Show story progression analysis
    print(f"\n🎭 Story Arc Distribution:")
    arc_counts = expanded_df['story_arc'].value_counts()
    for arc, count in arc_counts.items():
        print(f"   • {arc}: {count} scenarios")
    
    print(f"\n🌫️ Atmosphere Progression:")
    atmo_counts = expanded_df['atmosphere_level'].value_counts()
    for atmo, count in atmo_counts.items():
        print(f"   • {atmo}: {count} scenarios")
    
    print(f"\n🎬 Story Branches:")
    branch_counts = expanded_df['branch_type'].value_counts()
    for branch, count in branch_counts.items():
        print(f"   • {branch}: {count} scenarios")
    
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
    
    # Generate responses for key story moments
    print("\n🌫️ Generating mystery story responses...")
    generated_stories = []
    
    # Test specific story moments for quality
    key_scenarios = [0, 3, 5, 8, 10, 13, 15]  # Opening, revelation, escalation, climax, resolution
    
    for idx in key_scenarios:
        if idx < len(expanded_df):
            row = expanded_df.iloc[idx]
            prompt = f"Mystery Story: {row['prompt']} {row['response']}"
            
            # Generate AI response
            ai_response = generator(
                prompt,
                max_length=len(prompt.split()) + 50,
                temperature=0.7,  # Slightly more focused for mystery
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                num_return_sequences=1
            )[0]['generated_text']
            
            # Extract generated part
            ai_continuation = ai_response[len(prompt):].strip()
            
            generated_stories.append({
                'scenario_id': idx,
                'prompt': row['prompt'],
                'human_response': row['response'],
                'ai_response': ai_continuation,
                'branch_type': row['branch_type'],
                'atmosphere_level': row['atmosphere_level'],
                'dialogue_style': row['dialogue_style'],
                'story_arc': row['story_arc'],
                'choice_a': row['choice_a'],
                'choice_b': row['choice_b']
            })
            
            print(f"📝 Generated story {idx + 1} - {row['story_arc']} ({row['atmosphere_level']})")
    
    results_df = pd.DataFrame(generated_stories)
    
    # Display key results
    print("\n🌲 PINE HOLLOW EXPANDED RESULTS")
    print("=" * 60)
    
    for idx, row in results_df.iterrows():
        print(f"\n🎬 {row['story_arc'].upper()} - {row['branch_type']} ({row['atmosphere_level']})")
        print(f"📖 PROMPT: {row['prompt'][:100]}...")
        print(f"👤 HUMAN: {row['human_response'][:120]}...")
        print(f"🤖 AI: {row['ai_response'][:120]}...")
        
        # Quality analysis
        mystery_words = ['detective', 'sheriff', 'sarah', 'pine', 'mystery']
        atmosphere_words = ['fog', 'dark', 'strange', 'alien', 'entity', 'consciousness']
        
        mystery_score = sum(1 for word in mystery_words if word in row['ai_response'].lower())
        atmosphere_score = sum(1 for word in atmosphere_words if word in row['ai_response'].lower())
        
        print(f"   🔍 Mystery elements: {mystery_score}/5")
        print(f"   🌫️ Atmosphere words: {atmosphere_score}/6")
        print("-" * 60)
    
    # Save results
    results_df.to_csv('generated_stories_expanded_pine_hollow.csv', index=False)
    
    # Log to MLflow
    print("\n📊 Logging to MLflow...")
    mlflow.set_experiment("cyoa_model_experiments")
    
    with mlflow.start_run(run_name="pine_hollow_expanded_experiment"):
        # Parameters
        mlflow.log_param("model_name", model_name)
        mlflow.log_param("story_theme", "pine_hollow_expanded")
        mlflow.log_param("data_source", "twin_peaks_to_stranger_things")
        mlflow.log_param("total_scenarios", len(expanded_df))
        mlflow.log_param("tested_scenarios", len(results_df))
        mlflow.log_param("story_arcs", list(expanded_df['story_arc'].unique()))
        
        # Metrics
        mlflow.log_metric("stories_generated", len(results_df))
        mlflow.log_metric("avg_response_length", results_df['ai_response'].str.len().mean())
        mlflow.log_metric("opening_scenarios", len(expanded_df[expanded_df['story_arc'] == 'opening']))
        mlflow.log_metric("climax_scenarios", len(expanded_df[expanded_df['story_arc'] == 'climax']))
        mlflow.log_metric("twin_peaks_scenarios", len(expanded_df[expanded_df['atmosphere_level'] == 'twin_peaks']))
        mlflow.log_metric("stranger_things_scenarios", len(expanded_df[expanded_df['atmosphere_level'] == 'stranger_things']))
        
        # Artifacts
        mlflow.log_artifact('generated_stories_expanded_pine_hollow.csv')
        mlflow.log_artifact('data/pine_hollow_expanded.csv')
        
        print("✅ Experiment logged to MLflow")
    
    # Analysis summary
    print(f"\n🎯 EXPANDED EXPERIMENT COMPLETE!")
    print(f"📁 Results: generated_stories_expanded_pine_hollow.csv")
    print(f"📊 Total dataset: {len(expanded_df)} scenarios")
    print(f"🧪 Tested scenarios: {len(results_df)} key moments")
    print(f"🌐 MLflow UI: http://localhost:5000")
    
    print(f"\n🚀 NEXT STEPS:")
    print(f"   1. Analyze atmospheric progression quality")
    print(f"   2. Fine-tune model on mystery literature")
    print(f"   3. Create evaluation metrics for story coherence")
    print(f"   4. Build interactive story interface")

if __name__ == "__main__":
    main() 