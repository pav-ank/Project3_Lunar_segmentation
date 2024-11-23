# Lunar Segmentation Project with FastAPI and Streamlit 🌛
* This project implements lunar image segmentation using a deep learning model and serves the results through a FastAPI backend. The project also includes a front-end interface using Streamlit for easy interaction with the model.

## Prerequisites 
Prerequisites
Before running the project locally, make sure you have the following installed on your system:

Python 3.7+
pip (Python package installer)
Git (to clone the repository)
If you don't have Python installed, you can download it from [Python.org](https://www.python.org/)

## Project Setup
### 1. Clone the Repository
First, clone the repository to your local system.
```
git clone https://github.com/your-username/lunar-segmentation-project.git
cd lunar-segmentation-project
```

### 2. Create a Virtual Environment (optional but recommended)
To keep dependencies isolated, it's a good idea to create a virtual environment:
```
python3 -m venv venv
```
Activate the virtual environment:
* On Windows
```
venv\Scripts\activate
```

### 3. Install Dependencies
Install the required packages from `requirements.txt.`
```
pip install -r requirements.txt
```
This will install the necessary libraries such as FastAPI, Streamlit, and others needed for the lunar segmentation model.


4. Set Up Environment Variables (if needed)
Some projects require environment variables for configuration (e.g., API keys, paths). If your project needs this:

Create a .env file in the root of the project.
Add necessary environment variables (for example, database URLs, API tokens, etc.).
Example .env file:
```
MODEL_PATH=/path/to/your/trained/model
```

### 5. Run the FastAPI Backend
FastAPI will serve the model for making predictions. To start the FastAPI server, run the following command:
```
uvicorn app.main:app --reload
```
`app.main` refers to the main FastAPI application in the app folder.
The `--reload` flag enables automatic reloading during development.
The FastAPI server will run locally at `http://127.0.0.1:8000.`

### 6. Run the Streamlit Frontend
Streamlit will provide the user interface for the project. To run the Streamlit app:
```
streamlit run app/streamlit_app.py
```
This will start a local Streamlit server and open the UI in your web browser. The interface will allow you to upload lunar images and see the segmentation results.

### 7. Test the End-to-End Process
* Upload Image in Streamlit: Once the Streamlit app is running, go to http://localhost:8501 in your web browser.
* Make Predictions: Upload a lunar image and submit it. The backend (FastAPI) will process the image using the trained segmentation model, and the result will be displayed on the Streamlit front-end.

### File Structure
Here is the basic structure of the project:
```
lunar-segmentation-project/
│
├── app/
│   ├── main.py          # FastAPI app for serving model predictions
│   ├── model.py         # Lunar segmentation model code
│   └── streamlit_app.py # Streamlit front-end app
│
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (if needed)
└── README.md            # Project documentation
```

### Troubleshooting
If you run into issues, consider the following:

* FastAPI server not starting: Ensure all dependencies are installed, and you have activated the virtual environment.
* Streamlit UI not loading: Make sure Streamlit is installed `(pip install streamlit)` and try running the command `streamlit run app/streamlit_app.py` again.
* Model loading errors: Verify that the model file path in the `.env` file is correct and points to the right location.
