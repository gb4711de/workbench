# Workbench

General-purpose compute workbench for experimentation and verification.

## Automated Workflows

### Run Code
Execute arbitrary Python scripts via GitHub Actions:
```bash
# Encode your script
SCRIPT=$(base64 -w0 your_script.py)

# Trigger workflow
gh workflow run run-code.yml \
  -f script="$SCRIPT" \
  -f dependencies="gymnasium stable-baselines3" \
  -f timeout="60"
```

### Tests
Runs pytest on push or manually:
```bash
gh workflow run tests.yml -f test_path="tests/test_rl.py"
```

## Topics

Create topic-specific directories:
- `vision/` - Computer Vision, ViT, CNNs
- `rl/` - Reinforcement Learning
- `nlp/` - Natural Language Processing
- `dl/` - Deep Learning fundamentals

Each topic can have its own tests in `tests/`.
