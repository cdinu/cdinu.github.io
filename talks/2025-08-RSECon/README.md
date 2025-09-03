# 2025-07-ARC-Festival

## Conversational Interfaces for Research

This repository contains materials for the presentation "Conversational Interfaces for Research: Transforming Data Interaction with LLMs and MCP" by Cristian Dinu at the ARC Festival, July 2025.

### Contents

- **Presentation Files**: Quarto files (`index.qmd`, `narative.qmd`) for slides and narrative.
- **Images**: Visual assets used in the presentation.
- **Extensions**: MCP-related extensions and tools.
- **Intensity MCP**: Python implementation of a Model Context Protocol server for carbon intensity data.

### Prerequisites for running the MCP server

- **Node.js**: Required for running MCP inspector.
- **uv**: Python project manager for MCP server setup.

### Installation

To set up the Intensity MCP server:

```bash
uv init intensity_mcp
cd intensity_mcp
uv add "mcp[cli]" requests
```

### License

This work is licensed under the Creative Commons Attribution 4.0 International License (CC-BY). You are free to share and adapt the material as long as appropriate credit is given.

### Author

Cristian Dinu  
Research Software Engineer at ARC  
Specializing in high-resolution energy monitoring, appliance-level energy insights, and natural language interfaces.

### Links

- [Model Context Protocol (MCP), Official website](https://modelcontextprotocol.io/)
- [VSCode MCP](https://code.visualstudio.com/mcp)
- [Debbie O'Brien - Build Your First MCP Server: Tutorial for Beginners](https://www.youtube.com/watch?v=egVm_z1nnnQ&t=163s)
- [Sofware Is Changing Again](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again)
- [MCPs: Value Creation, Capture, and Destruction—Lessons from the API Era](https://leonisnewsletter.substack.com/p/mcps-value-creation-capture-and-destructionlesso)
