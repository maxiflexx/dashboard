# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /home/workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the port Streamlit will run on
EXPOSE 3333

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
# CMD tail -f /dev/null
