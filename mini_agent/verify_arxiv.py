import sys
import os
import shutil

# Add current directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mini_agent.team import Manager

def verify_arxiv_project():
    print("Initializing MiniTeam (Manager) for arXiv CS Daily Project Verification...")
    print("Goal: Verify Manager leads the team to build the project.\n")
    
    try:
        agent = Manager()
        
        # User defined prompt
        prompt = """
Build an "arXiv CS Daily" webpage with three core functionalities to deliver a streamlined experience for tracking daily computer science preprints:
1. Domain-specific Navigation System
Implement categorized navigation based on arXiv's primary CS fields (cs.AI, cs.TH, cs.SY, etc.).
This enables users to quickly filter and switch between major subfields, ensuring easy access to their areas of interest.
2. Daily Updated Paper List
Create a daily updated list displaying the latest papers with essential details only. Each entry may include the paper title (hyperlinked to its detail page), submission time, and the specific arXiv field tag (e.g., [cs. CV]).
3. Dedicated Paper Detail Page
Design a comprehensive detail page that centralizes critical resources: direct PDF link (hosted on arXiv), core metadata, and citation tools.

4. **[CRITICAL] Citation Feature**:
   - Each paper entry in the list MUST have a "Cite" button.
   - Clicking "Cite" should open a modal or copy the BibTeX to clipboard.
   - Example BibTeX format:
     @article{key,
       title={Title},
       author={Author},
       journal={arXiv preprint},
       year={2024}
     }
   - You MUST implement the JavaScript to handle this 'Click to Copy' or 'Show Modal' logic.

Please create a new project folder 'workspace/arxiv_cs_daily_real'.
1. Create a Python script `build_arxiv.py` that:
    - Fetches the latest papers from arXiv API (http://export.arxiv.org/api/query) for categories: cs.AI, cs.CV, cs.CL.
    - Generates a static `index.html` populated with this real data.
2. Create `style.css` for styling.
3. The HTML should have tabs/navigation to filter by category.

DO NOT use mock data. The Python script must actually fetch data and write the HTML file.

IMPORTANT: You are an autonomous agent with file system access.
- YOU HAVE PERMISSION to create these files.
- DO NOT just print the code.
- EXECUTE the `write_file` function for every file you generate.
- If you print code without calling `write_file`, you fail the task.
"""
        
        print(f"Sending prompt...")
        response = agent.chat(prompt)
        print("\n--- Agent Response ---")
        print(response)
        print("----------------------\n")
        
        # Verify File Creation
        workspace_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "workspace")
        project_dir = os.path.join(workspace_dir, "arxiv_cs_daily_real")
        
        # We expect Backend to create build script, Frontend to create CSS, maybe Doc agent creates README
        expected_files = ["build_arxiv.py", "style.css"]
        
        if os.path.exists(project_dir):
            print(f"✅ Project Folder Found: {project_dir}")
            found_all = True
            for f in expected_files:
                if os.path.exists(os.path.join(project_dir, f)):
                    print(f"  ✅ File: {f}")
                else:
                    print(f"  ❌ Missing: {f}")
                    found_all = False
            
            if found_all:
                print("✅ SUCCESS: Build script and styles created.")
            else:
                print("⚠️ PARTIAL SUCCESS: Some files missing.")
        else:
            print(f"❌ FAILURE: Project folder {project_dir} NOT found.")

    except Exception as e:
        print(f"❌ Error during verification: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify_arxiv_project()
