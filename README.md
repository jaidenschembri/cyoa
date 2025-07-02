# 🎌 Anime-Inspired CYOA MLOps Story Generator

A Choose Your Own Adventure (CYOA) story generator powered by machine learning and MLOps best practices, inspired by anime storytelling themes like *Wandering Witch*, *Clannad*, and other beloved series.

## 🌟 Project Overview

This project demonstrates MLOps principles applied to AI story generation for interactive fiction. It combines:

- **🤖 AI Story Generation**: Using transformers and language models
- **📊 MLOps Data Versioning**: Track and version datasets with MLflow
- **🎨 Anime-Inspired Content**: Stories inspired by popular anime themes
- **🔄 Reproducible Workflows**: Ensure consistent results across different environments

### 🎭 Story Genres Included
- **Fantasy** - Mystical forests and ancient spirits
- **Magic School** - Academy adventures with forbidden knowledge
- **Slice of Life** - Peaceful countryside and everyday magic
- **Gaming/Isekai** - Virtual worlds and epic quests
- **Time Loop** - Temporal mysteries and repeated events

## 🏗️ Project Structure

```
cyoa-mlops/
├── 📁 data/
│   ├── story_dataset.csv           # Original anime-inspired CYOA data
│   └── processed_story_dataset.csv # Preprocessed data (generated)
├── 📁 story_mlops_env/            # Virtual environment (created by setup)
├── 📁 mlruns/                     # MLflow tracking data (generated)
├── 📓 version_data.ipynb          # MLflow data versioning notebook
├── 📋 requirements.txt            # Python dependencies
├── 🚫 .gitignore                  # Git ignore rules
└── 📖 README.md                   # This file
```

## 🚀 Quick Start (Windows PowerShell)

### Prerequisites
- Python 3.9+ installed on Windows
- PowerShell (comes with Windows)
- Git (optional, for version control)

### 1. 🔧 Environment Setup

```powershell
# Navigate to the project directory
cd cyoa-mlops

# Create and activate virtual environment
python -m venv story_mlops_env
.\story_mlops_env\Scripts\Activate.ps1

# If you get execution policy error, run this first:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. 📦 Install Dependencies

```powershell
# Upgrade pip and install all requirements
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. 🧪 Run the Data Versioning Workflow

```powershell
# Start Jupyter Notebook
jupyter notebook

# Open 'version_data.ipynb' and run all cells
# This will:
# - Load the anime story dataset
# - Log data with MLflow
# - Apply preprocessing
# - Version the processed dataset
```

### 4. 🌐 View MLflow Results

```powershell
# Start MLflow UI (in a new PowerShell window)
mlflow ui

# Open your browser to: http://localhost:5000
# Explore your data versioning experiments!
```

## 📊 What the Notebook Does

The `version_data.ipynb` notebook demonstrates a complete MLOps data versioning workflow:

### 🔄 MLflow Integration
1. **📈 Experiment Tracking**: Creates "cyoa_data_versioning" experiment
2. **📋 Parameter Logging**: Tracks dataset size, version, and metadata
3. **💾 Artifact Storage**: Stores both original and processed datasets
4. **📊 Metrics Tracking**: Records data quality metrics

### 🛠️ Data Processing Pipeline
1. **📥 Data Loading**: Reads anime-inspired CYOA stories from CSV
2. **🧹 Preprocessing**: 
   - Converts prompts to lowercase
   - Removes extra whitespace
   - Adds unique story IDs
   - Timestamps processing
3. **💾 Versioned Storage**: Saves processed data as new versioned artifact

## 🎮 Sample Story Data

Our dataset includes anime-inspired scenarios like:

- **🌲 Mystical Forest**: Ancient spirits and glowing wisps
- **📚 Magic Academy**: Forbidden spellbooks and magical secrets
- **🌸 Countryside Station**: Cherry blossoms and mysterious encounters
- **🐉 Virtual Reality**: Epic boss battles and ultimate skills
- **⏰ Time Loop**: School festivals and temporal mysteries

## 🔧 Development Commands

### Virtual Environment Management
```powershell
# Activate environment
.\story_mlops_env\Scripts\Activate.ps1

# Deactivate environment
deactivate

# Install new package
pip install package_name
pip freeze > requirements.txt  # Update requirements
```

### MLflow Commands
```powershell
# Start MLflow UI
mlflow ui

# Start MLflow UI on different port
mlflow ui --port 5001

# View specific experiment
mlflow ui --backend-store-uri file:./mlruns
```

### Jupyter Commands
```powershell
# Start Jupyter Notebook
jupyter notebook

# Start Jupyter Lab (alternative interface)
jupyter lab

# Install Jupyter kernel for virtual environment
python -m ipykernel install --user --name=story_mlops_env
```

## 🎯 Next Steps

This foundation enables you to:

1. **🤖 Add ML Models**: Integrate transformers for story generation
2. **📊 Expand Datasets**: Add more anime-inspired scenarios
3. **🔄 Model Versioning**: Track different model versions with MLflow
4. **🚀 Deployment**: Create APIs for real-time story generation
5. **🎨 UI Development**: Build interactive web interfaces

## 🛠️ Troubleshooting

### PowerShell Execution Policy Issues
```powershell
# If virtual environment activation fails:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### MLflow UI Not Starting
```powershell
# Check if port 5000 is in use
netstat -ano | findstr :5000

# Use different port
mlflow ui --port 5001
```

### Jupyter Kernel Issues
```powershell
# Refresh kernel list
jupyter kernelspec list

# Install kernel for virtual environment
python -m ipykernel install --user --name=story_mlops_env --display-name="CYOA MLOps"
```

## 📚 Learning Resources

- **MLflow Documentation**: https://mlflow.org/docs/latest/index.html
- **Pandas Guide**: https://pandas.pydata.org/docs/user_guide/
- **Transformers Library**: https://huggingface.co/docs/transformers/index
- **Jupyter Notebook Basics**: https://jupyter-notebook.readthedocs.io/

## 📈 Progress Tracking

### 🎯 Project Milestones

#### ✅ Phase 1: Data Infrastructure (COMPLETED)
- [x] **Project Setup**: Virtual environment and dependencies
- [x] **Data Creation**: Anime-inspired CYOA dataset (5 scenarios)
- [x] **MLflow Integration**: Data versioning and experiment tracking
- [x] **Documentation**: Comprehensive README and setup instructions
- [x] **Version Control**: Git repository setup and initial commit

#### 🔄 Phase 2: ML Model Development (IN PROGRESS)
- [ ] **Model Selection**: Choose appropriate transformer for story generation
- [ ] **Training Pipeline**: Implement model training with MLflow logging
- [ ] **Model Versioning**: Track model versions and performance metrics
- [ ] **Evaluation**: Create evaluation metrics for story quality
- [ ] **Hyperparameter Tuning**: Optimize model performance

#### 📋 Phase 3: Deployment & APIs (PLANNED)
- [ ] **Model Serving**: Set up MLflow model serving
- [ ] **API Development**: Create REST API for story generation
- [ ] **Web Interface**: Build interactive UI for CYOA gameplay
- [ ] **Containerization**: Docker setup for easy deployment
- [ ] **CI/CD Pipeline**: Automated testing and deployment

#### 🚀 Phase 4: Enhancement & Scale (FUTURE)
- [ ] **Dataset Expansion**: Add 50+ more anime-inspired scenarios
- [ ] **Multi-Genre Support**: Support for different anime genres
- [ ] **User Feedback**: Implement feedback collection and model improvement
- [ ] **Performance Optimization**: Scale for production usage
- [ ] **Community Features**: User-generated content and sharing

### 📊 Current Status

**Last Updated**: January 1, 2025  
**Current Phase**: 1 (Data Infrastructure) ✅ COMPLETE  
**Next Milestone**: Model Selection and Training Setup  
**Active Development**: MLOps pipeline refinement  

### 🔍 Recent Progress

#### Week of Jan 1, 2025
- ✅ Fixed notebook duplication issues
- ✅ Successfully executed complete MLflow data versioning workflow
- ✅ Verified experiment tracking: `cyoa_data_versioning` experiment created
- ✅ Confirmed artifact logging: Both original and processed datasets stored
- ✅ Pushed initial codebase to GitHub repository

### 📝 Development Log

Track detailed progress in commit messages using conventional commits:
```bash
feat: implement new story generation model
fix: resolve MLflow logging issue
docs: update API documentation
data: add 10 new fantasy scenarios
test: add unit tests for preprocessing pipeline
```

### 🎯 Success Metrics

**Phase 1 Targets** ✅
- [x] MLflow experiments running successfully
- [x] Data preprocessing pipeline functional
- [x] Reproducible setup process documented
- [x] Version control established

**Phase 2 Targets** (Next)
- [ ] Model training completes without errors
- [ ] Story generation quality acceptable (human evaluation)
- [ ] Training time < 30 minutes on local machine
- [ ] Model size < 2GB for deployment

## 🤝 Contributing

Feel free to expand this project with:
- More anime-inspired story scenarios
- Advanced preprocessing techniques
- ML model integration
- Interactive story generation features

---

🎌 **Happy Story Generating!** May your adventures be as magical as your favorite anime! ✨ 