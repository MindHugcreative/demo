from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'mindhug_demo_secret_key'  # Required for session

# Define the steps in our flow
STEPS = [
    'welcome',
    'challenges',
    'resources',
    'learning_plan',
    'progress',
    'modules',
    'summary'
]

@app.route('/')
def index():
    # Reset session and start from beginning
    session['current_step'] = 0
    return redirect(url_for('welcome'))

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    session['current_step'] = 0
    
    if request.method == 'POST':
        # Store any form data from this step
        session['notes'] = request.form.get('notes', '')
        return redirect(url_for('challenges'))
    
    return render_template('welcome.html')

@app.route('/challenges', methods=['GET', 'POST'])
def challenges():
    session['current_step'] = 1
    
    if request.method == 'POST':
        # Store selected challenge
        session['selected_challenge'] = request.form.get('challenge', '')
        return redirect(url_for('resources'))
    
    return render_template('challenges.html')

@app.route('/resources', methods=['GET', 'POST'])
def resources():
    session['current_step'] = 2
    
    # Get the selected challenge from the previous step
    selected_challenge = session.get('selected_challenge', 'safety')
    
    if request.method == 'POST':
        # Store selected module if coming from resources page
        if 'selected_module' in request.form:
            session['selected_module'] = request.form.get('selected_module')
            return redirect(url_for('learning_plan'))
        
        # Store selected resources if they're changing filters
        session['resource_category'] = request.form.get('category', '')
        session['resource_type'] = request.form.get('type', '')
        session['resource_level'] = request.form.get('level', '')
        return redirect(url_for('learning_plan'))
    
    # For the demo, we'll only implement detailed resources for "safety"
    # In a real app, you'd have different resources for each challenge
    return render_template('resources.html', selected_challenge=selected_challenge)

@app.route('/learning-plan', methods=['GET', 'POST'])
def learning_plan():
    session['current_step'] = 3
    
    if request.method == 'POST':
        # If there's a module selection, store it
        selected_module = request.form.get('selected_module')
        if selected_module:
            session['selected_module'] = selected_module
        
        # If they click "Start learning module now"
        if 'start_module' in request.form:
            return redirect(url_for('learning_modules'))
        
        # If they click "Save for later" (in a real app, you'd save this to a database)
        if 'save_later' in request.form:
            # Just stay on the same page for demo purposes
            pass
    
    # Get the selected module name for display
    module_name = "Building Psychological safety"  # Default for the demo
    
    return render_template('learning_plan.html', module_name=module_name)

@app.route('/learning-modules', methods=['GET', 'POST'])
def learning_modules():
    session['current_step'] = 4
    
    if request.method == 'POST':
        # Handle module completion
        if 'complete_module' in request.form:
            # In a real app, you would mark this module as completed
            # and redirect to the next module or summary page
            return redirect(url_for('module_complete'))
    
    # In a real app, you'd load the specific module content based on progress
    module = {
        'title': 'Creating a Safe Environment',
        'number': 1,
        'total': 3,
        'takeaways': [
            'Validate feelings before moving to solutions',
            'Watch for non-verbal clues'
        ],
        'resources': [
            'Safety Assessment Worksheet',
            'Psychological safety discussion questionnaire'
        ]
    }
    
    return render_template('learning_modules.html', module=module)

@app.route('/module-complete', methods=['GET', 'POST'])
def module_complete():
    # Redirect to completed modules page
    return redirect(url_for('completed_modules'))

@app.route('/completed-modules')
def completed_modules():
    # Show the completed modules page
    return render_template('completed_modules.html')

@app.route('/create-action-plan', methods=['POST'])
def create_action_plan():
    # Get the selected client ID
    client_id = request.form.get('selected_client', '')
    
    # Store in session for use in the action plan page
    session['selected_client'] = client_id
    
    # Redirect to action plan page
    return render_template('action_plan.html', client_id=client_id)

@app.route('/save-action-plan', methods=['POST'])
def save_action_plan():
    # Get form data (in a real app, you'd save this to a database)
    technique = request.form.get('technique', '')
    adaptation = request.form.get('adaptation', '')
    implementation = request.form.get('implementation', '')
    
    # Store in session for demo purposes
    session['action_plan'] = {
        'technique': technique,
        'adaptation': adaptation,
        'implementation': implementation
    }
    
    # Redirect to session complete page
    return redirect(url_for('session_complete'))

@app.route('/session-complete')
def session_complete():
    # Show completed session notification
    return render_template('welcome.html', show_completed=True)

@app.route('/progress', methods=['GET', 'POST'])
def progress():
    session['current_step'] = 4
    
    if request.method == 'POST':
        # Store progress information
        session['progress_percentage'] = 30  # Example value
        return redirect(url_for('modules'))
    
    return render_template('progress.html')

@app.route('/modules', methods=['GET', 'POST'])
def modules():
    session['current_step'] = 5
    
    # Mock data for learning modules
    modules = [
        {'id': 1, 'title': 'Module 1', 'completed': True},
        {'id': 2, 'title': 'Module 2', 'completed': True},
        {'id': 3, 'title': 'Module 3', 'completed': False},
        {'id': 4, 'title': 'Module 4', 'completed': False}
    ]
    
    if request.method == 'POST':
        # Store module selection or completion
        selected_module = request.form.get('module', '')
        if selected_module:
            session['selected_module'] = selected_module
        return redirect(url_for('summary'))
    
    return render_template('modules.html', modules=modules)

@app.route('/summary')
def summary():
    session['current_step'] = 6
    return render_template('summary.html')

if __name__ == '__main__':
    app.run(debug=True)
