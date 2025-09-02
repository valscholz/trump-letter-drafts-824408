# Trump-Style Letter Generator (Safety-Compliant)

Users want to generate persuasive, high-energy letters inspired by the rhetorical style often associated with Donald Trump for a user-provided topic. The agent must produce content that captures high-level stylistic characteristics while avoiding direct impersonation, exact pastiche, or policy-violating political persuasion, ensuring clarity, safety, and usefulness in a single interaction.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

## Usage

```bash
python run.py "Your input message here"
```

## Development

This agent is built using the OpenAI Agents SDK and follows canonical patterns from the official documentation.

### Files
- `agent.py` - Main agent implementation
- `run.py` - Command-line interface
- `requirements.txt` - Dependencies
- `.env.example` - Environment configuration template
