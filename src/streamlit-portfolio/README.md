# Streamlit Portfolio

This project is a Streamlit-based portfolio application designed to showcase individual or organizational work, skills, and contact information. 

## Project Structure

The project consists of the following files and directories:

- **app.py**: The main entry point of the Streamlit application, setting up the layout and navigation.
- **pages/**: Contains individual pages for the portfolio:
  - **about.py**: Information about the individual or organization.
  - **projects.py**: A showcase of various projects with descriptions and links.
  - **skills.py**: Details of skills and expertise.
  - **contact.py**: Contact information and a form for inquiries.
  
- **components/**: Reusable components for the portfolio:
  - **header.py**: The header component with title and navigation links.
  - **footer.py**: The footer component with copyright and additional links.
  - **project_card.py**: A component to display individual project details.

- **utils/**: Utility functions for data processing and rendering:
  - **helpers.py**: Functions that assist throughout the application.

- **data/**: Contains JSON files for project and skill data:
  - **projects.json**: Project data including titles, descriptions, and links.
  - **skills.json**: Skill data detailing skills and proficiency levels.

- **styles/**: Custom CSS styles for the portfolio:
  - **main.css**: Styles to enhance the visual appearance.

- **config.yaml**: Configuration settings for the application, such as theme or layout preferences.

- **requirements.txt**: Lists the Python dependencies required for the project.

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the application with:
   ```
   streamlit run app.py
   ```

## Usage

Once the application is running, you can navigate through the various pages to view the portfolio, including the About, Projects, Skills, and Contact sections. Each section is designed to provide a comprehensive overview of the individual or organization.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.