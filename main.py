import os
import sys

# Add the current directory to sys.path for streamlit to find modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    os.system("streamlit run ui/app.py")
