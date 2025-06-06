# UTILS

### Document Converter
The document converter is designed to make the LLM's knowledge base easier to configure. Ideally, the user should be able to upload/place their relevant documents (PDF, DOCX, etc.) into the knowledge/ folder, run a command in the terminal, and convert their documents into LLM-friendly formats such as JSON or YAML.

The converter will parse typical document formats into machine-readable structured data including fields like: name, professional summary, skills, experience, and education, which can then be used as static input for generating personalised cover letters. This makes it easier to reuse existing resumes or portfolios without needing to manually write a structured profile.

**Supported formats:**

- .pdf

- .docx

- .txt (optional/fallback)

**Output:**

.yaml or .json file placed into the `knowledge/` folder

This tool enables faster onboarding for new users and ensures consistent input formatting for high-quality LLM outputs.