# CorefUD Scorer - Installation and Usage Guide

## Package Installation

The CorefUD scorer can now be installed as a Python package using pip or uv.

### Installation Steps

#### Using pip

```bash
# Install from the repository (for development)
pip install -e .

# Or install from a specific location
pip install /path/to/corefud-scorer

# Or install from GitHub (once published)
pip install git+https://github.com/ufal/corefud-scorer.git
```

#### Using uv (recommended for faster installation)

```bash
# Install from the repository (for development)
uv pip install -e .

# Or install from a specific location
uv pip install /path/to/corefud-scorer
```

### Virtual Environment Setup

It's recommended to use a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows

# Install the package
pip install -e .
```

## Command-Line Interface

After installation, two CLI commands are available:

### 1. CorefUD Scorer

```bash
corefud_scorer [OPTIONS] KEY_FILE SYS_FILE
```

**Options:**
- `-m, --metrics`: Select specific metrics (default: `all`)
  - Choices: `all`, `lea`, `muc`, `bcub`, `ceafe`, `ceafm`, `blanc`, `mor`, `zero`
- `-s, --keep-singletons`: Evaluate also singletons
- `-a, --match`: Select mention matching method (default: `head`)
  - Choices: `exact`, `partial`, `head`
- `-x, --exact-match`: Shortcut for exact matching
- `-z, --zero-match-method`: Zero mention matching method (default: `dependent`)
  - Choices: `linear`, `dependent`

**Example:**
```bash
corefud_scorer -m muc bcub ceafe -s key.conllu sys.conllu
```

### 2. Universal Anaphora Scorer

```bash
ua_scorer [OPTIONS] KEY_FILE SYS_FILE
```

**Options:**
- `-f, --format`: Input format (default: `ua`)
  - Choices: `ua`, `corefud`, `conll`
- `-m, --metrics`: Metrics to evaluate (default: `conll`)
  - Choices: `all`, `conll`, `muc`, `bcub`, `ceafe`, `ceafm`, `blanc`, `lea`, `mention`, `zero`, `non-referring`, `bridging`
- `-a, --match`: Mention matching type (default: `exact`)
  - Choices: `exact`, `partial-corefud`, `partial-craft`, `head`
- `-s, --keep-singletons`: Evaluate also singletons
- `-l, --keep-split-antecedents`: Evaluate also split-antecedents
- `-z, --keep-zeros`: Evaluate also zeros
- `--zero-match-method`: Zero anaphora matching method
  - Choices: `linear`, `dependent`
- `-d, --evaluate-discourse-deixis`: Evaluate discourse deixis
- `-t, --shared-task`: Use specific shared task settings
  - Choices: `conll12`, `crac18`, `craft19`, `crac22`, `codicrac22ar`, `codicrac22br`, `codicrac22dd`, `crac23`, `crac24`

**Example:**
```bash
ua_scorer -f corefud -m muc bcub ceafe -a head key.conllu sys.conllu
```

## Backward Compatibility

The original Python scripts are still available for backward compatibility:

```bash
python corefud-scorer.py [OPTIONS] KEY_FILE SYS_FILE
python ua-scorer.py [OPTIONS] KEY_FILE SYS_FILE
```

These scripts now internally call the CLI commands provided by the package.

## Development

For development with automatic updates when code changes:

```bash
# Install in editable mode
pip install -e .

# Or with uv
uv pip install -e .
```

## Running Tests

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/
```

## Package Structure

```
corefud-scorer/
├── scorer/              # Main package
│   ├── __init__.py
│   ├── cli.py          # CLI entry points
│   ├── base/           # Base classes
│   ├── conll/          # CoNLL format support
│   ├── corefud/        # CorefUD format support
│   ├── eval/           # Evaluation metrics
│   └── ua/             # Universal Anaphora scorer
├── tests/              # Test suite
├── pyproject.toml      # Package metadata and dependencies
├── .gitignore          # Git ignore rules
├── README.md           # Main documentation
└── INSTALL.md          # This file
```

## Troubleshooting

### Command not found after installation

Make sure the virtual environment is activated and the package is installed:

```bash
source venv/bin/activate
pip list | grep corefud-scorer
```

If not installed, run:
```bash
pip install -e .
```

### Import errors

Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

Or reinstall the package:
```bash
pip install -e . --force-reinstall
```
