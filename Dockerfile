# Use a lightweight Python 3.13 image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code and assets
COPY landing.py .
COPY noback.png .
COPY akt.png .
COPY .streamlit .
COPY banner.png .
COPY aktlogo.png .
# Expose Streamlit's default port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "landing.py", "--server.port", "8501", "--server.address", "0.0.0.0"]