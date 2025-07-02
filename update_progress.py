#!/usr/bin/env python3
"""
Simple script to update progress tracking for CYOA MLOps project.
Usage: python update_progress.py
"""

import os
import datetime
from typing import List

def get_user_input() -> dict:
    """Get progress update information from user."""
    print("🎯 CYOA MLOps Progress Update Tool")
    print("=" * 40)
    
    # Get basic info
    accomplishment = input("\n✅ What did you accomplish? (brief description): ")
    time_spent = input("⏰ Time spent (e.g., '30 min', '2 hours'): ")
    
    # Get technical details
    print("\n🔧 Technical details (optional, press Enter to skip):")
    technical_details = []
    while True:
        detail = input("  - ")
        if not detail:
            break
        technical_details.append(detail)
    
    # Get issues/notes
    issues = input("\n🚧 Any issues encountered? (optional): ")
    notes = input("📝 Additional notes? (optional): ")
    
    return {
        'accomplishment': accomplishment,
        'time_spent': time_spent,
        'technical_details': technical_details,
        'issues': issues,
        'notes': notes,
        'timestamp': datetime.datetime.now()
    }

def update_progress_file(data: dict) -> None:
    """Update the PROGRESS.md file with new entry."""
    
    # Read existing file
    if os.path.exists('PROGRESS.md'):
        with open('PROGRESS.md', 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        print("❌ PROGRESS.md not found!")
        return
    
    # Format new entry
    date_str = data['timestamp'].strftime("%B %d, %Y")
    time_str = data['timestamp'].strftime("%I:%M %p")
    
    new_entry = f"""
#### ✅ {time_str} - {data['accomplishment']}
**Duration**: {data['time_spent']}
"""
    
    if data['technical_details']:
        new_entry += "\n**Technical Details**:\n"
        for detail in data['technical_details']:
            new_entry += f"- {detail}\n"
    
    if data['issues']:
        new_entry += f"\n**Issues**: {data['issues']}\n"
    
    if data['notes']:
        new_entry += f"\n**Notes**: {data['notes']}\n"
    
    # Find insertion point (after "### 🗓️ [current date]" section)
    today_header = f"### 🗓️ {date_str}"
    
    if today_header in content:
        # Add to existing day section
        insert_pos = content.find(today_header)
        next_day_pos = content.find("### 🗓️", insert_pos + len(today_header))
        
        if next_day_pos == -1:
            # This is the latest day, append before next major section
            next_section_pos = content.find("## 🎯 Current Sprint Goals")
            if next_section_pos != -1:
                content = content[:next_section_pos] + new_entry + "\n" + content[next_section_pos:]
            else:
                content = content + new_entry
        else:
            # Insert before next day
            content = content[:next_day_pos] + new_entry + "\n" + content[next_day_pos:]
    else:
        # Create new day section
        new_day_section = f"""
{today_header}
{new_entry}
"""
        # Insert after the last existing day
        last_day_pos = content.rfind("### 🗓️")
        if last_day_pos != -1:
            next_section_pos = content.find("## 🎯 Current Sprint Goals", last_day_pos)
            if next_section_pos != -1:
                content = content[:next_section_pos] + new_day_section + "\n" + content[next_section_pos:]
            else:
                content = content + new_day_section
        else:
            # No existing days, add after detailed log header
            log_header_pos = content.find("## 📅 Detailed Progress Log")
            if log_header_pos != -1:
                insert_pos = content.find("\n", log_header_pos) + 1
                content = content[:insert_pos] + new_day_section + content[insert_pos:]
    
    # Update last updated timestamp
    content = content.replace(
        f"**Last Updated**: January 1, 2025, 10:30 PM",
        f"**Last Updated**: {data['timestamp'].strftime('%B %d, %Y, %I:%M %p')}"
    )
    
    # Write back to file
    with open('PROGRESS.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Progress updated in PROGRESS.md!")

def suggest_commit_message(data: dict) -> str:
    """Suggest a git commit message based on the accomplishment."""
    accomplishment = data['accomplishment'].lower()
    
    # Simple categorization
    if any(word in accomplishment for word in ['fix', 'bug', 'error', 'issue']):
        prefix = "fix"
    elif any(word in accomplishment for word in ['add', 'new', 'create', 'implement']):
        prefix = "feat"
    elif any(word in accomplishment for word in ['doc', 'readme', 'comment']):
        prefix = "docs"
    elif any(word in accomplishment for word in ['test', 'testing']):
        prefix = "test"
    elif any(word in accomplishment for word in ['refactor', 'clean', 'organize']):
        prefix = "refactor"
    else:
        prefix = "chore"
    
    return f"{prefix}: {data['accomplishment']}"

def main():
    """Main function."""
    try:
        # Get progress data
        data = get_user_input()
        
        # Update progress file
        update_progress_file(data)
        
        # Suggest commit message
        commit_msg = suggest_commit_message(data)
        print(f"\n📝 Suggested commit message:")
        print(f"   {commit_msg}")
        
        # Ask if user wants to commit
        if input("\n🔄 Auto-commit these changes? (y/n): ").lower().startswith('y'):
            os.system('git add .')
            os.system(f'git commit -m "{commit_msg}"')
            print("✅ Changes committed!")
            
            if input("📤 Push to GitHub? (y/n): ").lower().startswith('y'):
                os.system('git push')
                print("✅ Changes pushed to GitHub!")
        
        print("\n🎉 Progress tracking updated successfully!")
        print("📊 Check PROGRESS.md for the full log")
        print("🌐 View on GitHub: https://github.com/jaidenschembri/cyoa")
        
    except KeyboardInterrupt:
        print("\n\n👋 Progress update cancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main() 