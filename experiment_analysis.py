#!/usr/bin/env python3
"""
Experiment Analysis: Pine Hollow Mystery vs Anime Baseline
Compare GPT-2 performance across different story themes
"""

import pandas as pd
import numpy as np
import os

def analyze_experiments():
    print("📊 CYOA EXPERIMENT ANALYSIS")
    print("=" * 60)
    
    # Load both experiment results
    if os.path.exists('generated_stories_pine_hollow_baseline.csv'):
        mystery_df = pd.read_csv('generated_stories_pine_hollow_baseline.csv')
        print(f"🌲 Pine Hollow Mystery: {len(mystery_df)} scenarios")
    else:
        print("❌ Pine Hollow results not found")
        return
    
    if os.path.exists('generated_stories_baseline.csv'):
        anime_df = pd.read_csv('generated_stories_baseline.csv')
        print(f"🎌 Anime Baseline: {len(anime_df)} scenarios")
    else:
        print("⚠️ Anime baseline not found for comparison")
        anime_df = None
    
    print("\n" + "=" * 60)
    print("🔍 PINE HOLLOW MYSTERY ANALYSIS")
    print("=" * 60)
    
    # Mystery experiment analysis
    print(f"\n📈 Basic Metrics:")
    print(f"   • Stories generated: {len(mystery_df)}")
    print(f"   • Avg response length: {mystery_df['ai_response'].str.len().mean():.1f} chars")
    print(f"   • Twin Peaks scenarios: {len(mystery_df[mystery_df['atmosphere_level'] == 'twin_peaks'])}")
    print(f"   • Stranger Things scenarios: {len(mystery_df[mystery_df['atmosphere_level'] == 'stranger_things'])}")
    
    print(f"\n🎭 Dialogue Style Distribution:")
    for style in mystery_df['dialogue_style'].unique():
        count = len(mystery_df[mystery_df['dialogue_style'] == style])
        print(f"   • {style}: {count} scenarios")
    
    print(f"\n🌲 Story Branch Distribution:")
    for branch in mystery_df['branch_type'].unique():
        count = len(mystery_df[mystery_df['branch_type'] == branch])
        print(f"   • {branch}: {count} scenarios")
    
    # Quality analysis
    print(f"\n🧠 QUALITY OBSERVATIONS:")
    
    # Check for coherence issues
    short_responses = mystery_df[mystery_df['ai_response'].str.len() < 100]
    long_responses = mystery_df[mystery_df['ai_response'].str.len() > 500]
    
    print(f"   • Short responses (<100 chars): {len(short_responses)}")
    print(f"   • Long responses (>500 chars): {len(long_responses)}")
    
    # Sample analysis
    print(f"\n📝 SAMPLE RESPONSE ANALYSIS:")
    
    for idx in range(min(3, len(mystery_df))):
        row = mystery_df.iloc[idx]
        ai_response = row['ai_response']
        
        print(f"\n🎬 Sample {idx + 1} ({row['atmosphere_level']} - {row['dialogue_style']}):")
        print(f"   📖 Prompt: {row['prompt'][:80]}...")
        print(f"   👤 Human: {row['human_response'][:80]}...")
        print(f"   🤖 AI: {ai_response[:80]}...")
        
        # Quality indicators
        coherent = "Detective" in ai_response or "sheriff" in ai_response.lower() or "coffee" in ai_response.lower()
        on_topic = any(word in ai_response.lower() for word in ['sarah', 'pine', 'mystery', 'disappeared', 'town'])
        atmosphere = any(word in ai_response.lower() for word in ['forest', 'fog', 'dark', 'strange', 'whisper'])
        
        print(f"   ✅ Mystery elements: {'Yes' if on_topic else 'No'}")
        print(f"   🎭 Character consistency: {'Yes' if coherent else 'No'}")
        print(f"   🌫️ Atmospheric: {'Yes' if atmosphere else 'No'}")
    
    # Comparison with anime if available
    if anime_df is not None:
        print("\n" + "=" * 60)
        print("🆚 MYSTERY vs ANIME COMPARISON")
        print("=" * 60)
        
        print(f"\n📊 Length Comparison:")
        mystery_avg = mystery_df['ai_response'].str.len().mean()
        anime_avg = anime_df['ai_response'].str.len().mean()
        print(f"   • Mystery avg: {mystery_avg:.1f} chars")
        print(f"   • Anime avg: {anime_avg:.1f} chars")
        print(f"   • Difference: {mystery_avg - anime_avg:+.1f} chars")
        
        print(f"\n🎯 Theme Consistency:")
        # Check for theme-appropriate keywords
        mystery_keywords = ['detective', 'sheriff', 'mystery', 'disappeared', 'town', 'coffee']
        anime_keywords = ['magic', 'academy', 'guild', 'festival', 'cherry', 'spirits']
        
        mystery_theme_score = mystery_df['ai_response'].apply(
            lambda x: sum(1 for kw in mystery_keywords if kw in x.lower())
        ).mean()
        
        anime_theme_score = anime_df['ai_response'].apply(
            lambda x: sum(1 for kw in anime_keywords if kw in x.lower())
        ).mean()
        
        print(f"   • Mystery theme words per response: {mystery_theme_score:.2f}")
        print(f"   • Anime theme words per response: {anime_theme_score:.2f}")
    
    print("\n" + "=" * 60)
    print("🎯 KEY FINDINGS & NEXT STEPS")
    print("=" * 60)
    
    print(f"\n🔍 Observations:")
    print(f"   • GPT-2 generates long, somewhat coherent responses")
    print(f"   • Mystery atmosphere partially maintained")
    print(f"   • Character consistency needs improvement")
    print(f"   • Twin Peaks dialogue patterns not well captured")
    
    print(f"\n📈 Recommendations:")
    print(f"   1. Fine-tune on mystery/thriller literature")
    print(f"   2. Add more Twin Peaks dialogue examples")
    print(f"   3. Implement better prompt engineering")
    print(f"   4. Create evaluation metrics for atmosphere")
    print(f"   5. Expand dataset to 20+ scenarios per branch")
    
    print(f"\n🚀 Portfolio Value:")
    print(f"   ✅ Shows domain adaptation (anime → mystery)")
    print(f"   ✅ Demonstrates systematic experimentation")
    print(f"   ✅ Unique theme (Twin Peaks + ML is rare!)")
    print(f"   ✅ Clear progression path for improvement")
    
    print(f"\n🌐 Next: Check MLflow UI at http://localhost:5000")

if __name__ == "__main__":
    analyze_experiments() 