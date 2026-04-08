# Advanced RAG (Retrieval-Augmented Generation)

An intelligent retrieval-augmented generation system built with LangChain and LangGraph that combines document retrieval, relevance grading, hallucination detection, and web search to provide accurate, grounded answers.

## Features

- **Intelligent Routing**: Routes queries to either vectorstore (RAG) or web search based on query type
- **Document Retrieval**: Retrieves relevant documents from a vector store
- **Relevance Grading**: Automatically grades retrieved documents for relevance to the question
- **Hallucination Detection**: Verifies that generated answers are grounded in retrieved documents
- **Answer Validation**: Checks that generated answers actually address the original question
- **Web Search Fallback**: Automatically performs web search when documents are insufficient
- **Iterative Refinement**: Regenerates answers if they don't meet quality standards
- **State Management**: Maintains conversation state throughout the reasoning process

## Project Structure

```
.
├── main.py                    # Entry point for the RAG system
├── ingestion.py              # Document loading and vector store setup
├── pyproject.toml            # Project configuration and dependencies
├── graph/
│   ├── graph.py             # LangGraph workflow definition
│   ├── state.py             # State schema for the graph
│   ├── consts.py            # Constants for graph nodes
│   ├── nodes/               # Graph node implementations
│   │   ├── retrieve.py      # Document retrieval node
│   │   ├── grade_documents.py # Document grading node
│   │   ├── generate.py      # Answer generation node
│   │   └── web_search.py    # Web search node
│   └── chains/              # LLM chains for specific tasks
│       ├── router.py        # Query routing chain
│       ├── retrieval_grader.py  # Document relevance grader
│       ├── hallucination_grader.py  # Hallucination detection
│       ├── answer_grader.py # Answer validation
│       └── generation.py    # Answer generation chain
```

## Workflow

The system follows this decision flow:

1. **Route Question**: Determines if the query should go to vectorstore RAG or web search
2. **Retrieve**: If RAG, retrieves relevant documents from the vector store
3. **Grade Documents**: Evaluates document relevance; flags for web search if needed
4. **Decide**: Determines whether to proceed with generation or switch to web search
5. **Generate**: Uses an LLM to generate an answer
6. **Check Hallucinations**: Verifies the answer is grounded in retrieved documents
7. **Validate Answer**: Confirms the answer addresses the original question
8. **Iterate**: Regenerates if needed, or searches web as fallback

## Setup

### Prerequisites

- Python 3.11+
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd advanced-rag
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # Windows PowerShell
   # or
   source .venv/bin/activate  # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Set up environment variables:
   Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_key
   TAVILY_API_KEY=your_tavily_key
   GOOGLE_API_KEY=your_google_key
   ```

## Usage

### Prepare Vector Store

First, ingest documents into the vector store:

```bash
python ingestion.py
```

This loads URLs from `ingestion.py`, splits them into chunks, and creates embeddings using HuggingFace models.

### Run the RAG System

```bash
python main.py
```

The default example asks "agent memory?" and prints the workflow's reasoning and final answer.

### Custom Queries

Modify `main.py` to ask different questions:

```python
from graph.graph import app

result = app.invoke(input={"question": "Your question here?"})
print(result)
```

## Dependencies

Key packages:
- **LangChain**: LLM framework
- **LangGraph**: Graph-based workflow orchestration
- **Chroma**: Vector store for documents
- **Tavily**: Web search API
- **HuggingFace Transformers**: Embeddings and language models
- **BeautifulSoup4**: Web scraping
- **Tiktoken**: Token counting

See `pyproject.toml` for the complete list.

## Configuration

- **Vector Store**: Uses Chroma client (can be modified in `ingestion.py`)
- **Embeddings**: HuggingFace "all-MiniLM-L6-v2" model
- **LLM**: Configured in individual chain files (supports OpenAI, Google, HuggingFace)
- **Chunk Size**: 250 tokens with no overlap (configurable in `ingestion.py`)

## Testing

Run tests with:

```bash
pytest graph/chains/tests/
```

## Development

- **Code Formatting**: Uses Black
- **Import Sorting**: Uses isort
- **Type Hints**: Leverages Python type hints for better IDE support

Reformat code:
```bash
black .
isort .
```

## Troubleshooting

### Import Errors
If you encounter `ImportError: cannot import name 'grade_documents'`:
- Check that all dependencies in `chains/` are properly installed
- Ensure there are no circular imports in the codebase
- Verify the `.env` file has required API keys

### Vector Store Issues
- Ensure the `.chroma` directory exists or run `ingestion.py` to create it
- Check that HuggingFace embeddings are downloaded




