# ============================================
# Stage 1: Build dependencies and virtual env
# ============================================
FROM python:3.10-slim AS builder

# Set working directory
WORKDIR /app

# Install system dependencies for building packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies in a virtual environment
COPY requirements.txt .
RUN python -m venv /venv && \
    . /venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# ============================================
# Stage 2: Final lightweight image
# ============================================
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy virtual environment from builder stage
COPY --from=builder /venv /venv

# Set environment variables to use the virtual environment
ENV PATH="/venv/bin:$PATH"

# Copy application files
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "port.py", "--server.port=8501", "--server.address=0.0.0.0"]