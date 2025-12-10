# Butter Launch Toolkit

Generate a research-backed launch plan for the **Butter** organic lip balm brand.

## Features
- Pulls reference content from URLs you provide (e.g., sustainability reports, ingredient research, category roundups).
- Extracts quick summaries and lightweight keywords from the fetched content.
- Produces a Markdown launch blueprint covering positioning, messaging, campaign ideas, and a reference bibliography.

> This environment does not have internet access. Run the tool locally with connectivity to populate real data.

## Getting Started
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Populate a YAML list of sources to research:
   ```yaml
   - https://example.com/organic-lip-balm-trends
   - https://example.com/sustainable-packaging
   ```
4. Run the CLI to generate the launch plan:
   ```bash
   python -m butter_balm.cli --sources sources.yaml --brand "Butter" --output butter_plan.md
   ```

Use `--verbose` for debug logs or `--timeout` to adjust network timeouts.
