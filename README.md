# MindHug Demo - Coaching Platform

A comprehensive platform for coaches to build psychological safety, manage learning modules, and create personalized coaching plans for clients.

## Getting Started

Follow these instructions to get the MindHug Demo application running on your local machine.

### Prerequisites

- Python 3.7+ installed
- pip (Python package manager)
- Git (optional)

### Installation

1. **Clone the repository** (or download and unzip)
   ```bash
   git clone https://github.com/MindHugcreative/demo.git
   cd demo
   ```

2. **Create a virtual environment**
   ```bash
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask application**
   ```bash
   # On macOS/Linux
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run
   
   # On Windows
   set FLASK_APP=app.py
   set FLASK_ENV=development
   flask run
   ```

2. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:5000/`

## Features

- **Psychological Safety Assessment**: Tools for evaluating and building client safety
- **Learning Modules**: Structured content for coach education and development
- **Coaching Challenges**: Address specific client struggles with targeted resources
- **Action Plans**: Create and manage personalized client intervention plans
- **Resource Library**: Access to worksheets, questionnaires, and techniques

## Project Structure

- `app.py`: Main application file
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript, images)
- `data/`: Data files (JSON, CSV)
- `utils/`: Utility functions
- `requirements.txt`: List of dependencies

## Contributing

1. Fork the repository      
2. Create a new branch
3. Make your changes and commit them
4. Push to your fork
5. Create a pull request

## License

This project is licensed under the MIT License. See the LICENSE file for details.