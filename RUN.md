# RUN Guide - GitHub Copilot Custom Agent

This guide explains how to run and use this GitHub Copilot Custom Agent template repository.

## Overview

This repository contains a template for creating a custom GitHub Copilot agent. Custom agents allow you to extend GitHub Copilot's capabilities with specialized knowledge and behaviors tailored to your specific needs.

## Prerequisites

Before you begin, ensure you have:

- A GitHub account with access to GitHub Copilot
- Access to this repository
- Basic knowledge of Markdown
- Git installed on your local machine (for local testing)

## Quick Start

### 1. Configure Your Custom Agent

Edit the agent configuration file located at `.github/agents/my-agent.agent.md`:

```markdown
---
name: YourAgentName
description: A brief description of what your agent does
---

# Your Agent Name

Describe what your agent does here...
```

**Required fields:**
- `name`: A unique name for your agent (alphanumeric, hyphens, and underscores)
- `description`: A short description (1-2 sentences) of your agent's purpose

### 2. Deploy Your Agent

To make your agent available in GitHub Copilot:

1. **Commit your changes:**
   ```bash
   git add .github/agents/my-agent.agent.md
   git commit -m "Configure custom agent"
   ```

2. **Push to the default branch:**
   ```bash
   git push origin main
   ```

3. **Verify deployment:**
   - Once merged into the default branch, your agent will be available in GitHub Copilot
   - It may take a few minutes for the agent to become active

### 3. Test Your Agent Locally (Optional)

You can test your custom agent locally using the Copilot CLI:

1. **Install the Copilot CLI:**
   ```bash
   gh extension install github/gh-copilot
   ```

2. **Test your agent:**
   ```bash
   gh copilot --agent my-agent "Your test query here"
   ```

For more details on local testing, visit the GitHub Copilot documentation: https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line

## Configuration Details

### Agent File Structure

The agent configuration file uses YAML frontmatter followed by Markdown content:

```markdown
---
name: agent-name
description: Short description
---

# Agent Title

Extended documentation about what the agent does, how to use it,
and any special instructions or knowledge it should have.
```

### Best Practices

1. **Choose a descriptive name:** Make it clear what your agent does
2. **Write clear documentation:** Explain the agent's capabilities and use cases
3. **Test thoroughly:** Use the Copilot CLI to test before deploying
4. **Keep it focused:** Agents work best when they have a specific purpose
5. **Update regularly:** Keep your agent's knowledge current

## Usage

Once deployed, you can use your custom agent in:

- **GitHub Copilot Chat:** Reference your agent by name
- **Pull Request reviews:** Agents can help review code changes
- **Issue triage:** Use agents to help categorize and prioritize issues
- **Code generation:** Get specialized code suggestions

## Troubleshooting

### Agent not appearing after deployment
- Verify the file is in `.github/agents/` directory
- Ensure the file has `.agent.md` extension
- Check that YAML frontmatter is properly formatted
- Wait a few minutes for the agent to become active

### Configuration errors
- Validate YAML syntax in the frontmatter
- Ensure all required fields (name, description) are present
- Check for special characters in the name field

### Local testing issues
- Ensure Copilot CLI is properly installed
- Verify you're authenticated with GitHub
- Check that you have access to the repository

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Using GitHub Copilot in the Command Line](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)
- [GitHub Copilot Features](https://docs.github.com/en/copilot/using-github-copilot)

## Next Steps

1. Customize your agent configuration
2. Test locally using the Copilot CLI
3. Deploy to the default branch
4. Start using your custom agent in GitHub Copilot

---

For questions or issues, please open an issue in this repository.
