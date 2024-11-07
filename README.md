# cc-wwf-nlmap

## Prerequisites

- A GEE account
- Python (v3.12.7) installed
- `make` utility installed
- OpenAI API key

## Setup

### 1. Create a Virtual Environment

To keep dependencies isolated, create a virtual environment:

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

On Linux/MacOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install Required Packages

With the virtual environment activated, install the necessary packages:

```bash
pip install -r requirements.txt
```

## Usage

Start the Server
You can start the server by running:

```bash
make run
```

This will initialize the server and make it accessible as configured.

## Deployment - How to

See here [https://docs.streamlit.io/deploy/tutorials](https://docs.streamlit.io/deploy/tutorials)
