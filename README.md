# Gym Trainer

A Django web application for learning proper gym exercise techniques.

## Features
- **Homepage**: Welcome message with navigation to core features.
- **Add Exercise**: Form to input exercise details (name, description, muscles) and upload media (GIF/JPG/PNG).
- **Add Comment**: Form to add comments to specific exercises.
- **Exercise List**: Table of all exercises with muscle filtering, links to flashcards, and media upload.
- **Flashcards**: Interactive cards displaying exercise details, comments (with scrollable section), and media, navigable via "Previous"/"Next" buttons.
- **Input Validation**: Ensures non-empty fields and minimum description length (10 characters).
- **Frontend**: Bootstrap 5.3 for responsive design, custom CSS for card animations and fixed-height flashcards.
- **Media Support**: Upload and display GIFs or images for exercises.

## Setup
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd gym_trainer
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Open `http://localhost:8000` in your browser.

## Technologies
- **Backend**: Django, SQLite
- **Frontend**: Bootstrap 5.3 (via CDN), custom CSS, JavaScript for flashcard navigation
- **Tools**: Git, pylint (code quality), Zoom (demo recording)

## Project Structure
- `exercises/`: Main app with models, views, forms, templates, and static files.
- `gym_trainer/`: Project settings and main URLs.
- `media/`: Stores uploaded media files (GIFs, images).
- `static/`: Custom CSS for styling.

## Notes
- The project meets all requirements: 5 pages, input/output pages, validation, templates, frontend, and Git usage.
- Code is linted with pylint, targeting a score of ≥8/10.
- Demo video (3–5 minutes) showcases all features and is uploaded to Google Drive.