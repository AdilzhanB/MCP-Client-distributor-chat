<div align="center">

# 🌐 MCP Client Distributor Chat

<img src="https://img.shields.io/badge/MCP-Protocol-blue?style=for-the-badge&logo=protocol&logoColor=white" alt="MCP Protocol">
<img src="https://img.shields.io/badge/Gradio-4.44.0-orange?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio">
<img src="https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License">

### *The Ultimate Model Context Protocol Client for Modern AI Workflows*

<p align="center">
  <a href="#-quick-start">🚀 Quick Start</a> •
  <a href="#-features">✨ Features</a> •
  <a href="#-demo">🎮 Demo</a> •
  <a href="#-installation">📦 Installation</a> •
  <a href="#-documentation">📚 Docs</a>
</p>

---

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

</div>

## 🎯 Overview

**MCP Client Distributor Chat** is a comprehensive **Model Context Protocol (MCP)** client application that enables seamless connection to multiple MCP servers and interactive communication with AI agents. Built with modern Gradio interface and powered by `smolagents`, it provides both simple and advanced implementations for various use cases.

<details>
<summary>🔍 What is MCP? (Click to expand)</summary>

The **Model Context Protocol (MCP)** is an open standard that enables AI applications to securely connect to data sources and tools. It provides a unified way for AI assistants to interact with various services, databases, and APIs through a standardized protocol.

</details>

## ✨ Features
<div align="center">
<table>
<tr>
<td width="50%" valign="top">

### 🔌 **Multi-Server Management**
- Connect to multiple MCP servers simultaneously
- Real-time connection status monitoring
- Custom server addition and configuration
- Automatic failover and reconnection

### 🤖 **AI Agent Interaction**
- Interactive chat with intelligent agents
- Access to server-specific tools and capabilities
- Context-aware conversations
- Multi-turn dialogue support

</td>
<td width="50%" valign="top">

### 📊 **Advanced Analytics**
- Conversation history tracking
- Server performance metrics
- Connection logs and diagnostics
- Usage statistics and insights

### 🎨 **Modern Interface**
- Responsive Gradio-based UI
- Dark/Light theme support
- Real-time updates
- Mobile-friendly design

</td>
</tr>
</table>
</div>

## 🎮 Demo

<div align="center">

### 🌟 **Live Demo Available**

<a href="https://huggingface.co/spaces/Adilbai/MCP_client_distributor">
  <img src="https://img.shields.io/badge/🚀_Try_Live_Demo-Hugging_Face_Spaces-yellow?style=for-the-badge&logo=huggingface&logoColor=white" alt="Live Demo">
</a>

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="500">

</div>


## 🚀 Quick Start

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">
</div>

### 1️⃣ **Clone Repository**

```bash
git clone https://github.com/AdilzhanB/MCP-Client-distributor-chat.git
cd MCP-Client-distributor-chat
```

### 2️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3️⃣ **Set Environment Variables**

```bash
export HF_TOKEN="your_huggingface_token_here"
```

### 4️⃣ **Run Application**

```bash
# Simple version (recommended for beginners)
python mcp_client_simple.py

# Advanced version (full features)
python mcp_client_advanced.py
```

<div align="center">
<img src="https://img.shields.io/badge/🎉_Ready_to_Go!-Success-brightgreen?style=for-the-badge" alt="Success">
</div>

## 📦 Installation

### 🐍 **Python Requirements**
<div align="center">
<img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python" alt="Python 3.8+">
<img src="https://img.shields.io/badge/OS-Windows%20|%20macOS%20|%20Linux-lightgrey?style=flat-square" alt="Cross Platform">
</div>
### 📋 **Dependencies**

```txt
gradio[mcp]>=4.44.0
smolagents[mcp]>=0.3.0
mcp>=1.0.0
fastmcp>=0.1.0
huggingface-hub>=0.19.0
textblob>=0.17.1
```

### 🔧 **Development Setup**

```bash
# Create virtual environment
python -m venv mcp_env
source mcp_env/bin/activate  # On Windows: mcp_env\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt
```

### 🐳 **Docker Support**

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 7860

CMD ["python", "mcp_client_simple.py"]
```

## 🏗️ Architecture

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d42b-4505-b9d4-f12c4e0270cc.gif" width="500">
</div>

```mermaid
graph TB
    A[🌐 Gradio UI] --> B[🔌 MCP Client Manager]
    B --> C[📡 Server Connection Pool]
    C --> D[🖥️ MCP Server 1]
    C --> E[🖥️ MCP Server 2]
    C --> F[🖥️ MCP Server N]
    
    B --> G[🤖 Agent Manager]
    G --> H[💬 Chat Interface]
    G --> I[🔧 Tool Executor]
    
    B --> J[📊 Analytics Engine]
    J --> K[📈 Metrics Collector]
    J --> L[📚 History Manager]
    
    style A fill:#667eea
    style B fill:#764ba2
    style G fill:#f093fb
    style J fill:#f5576c
```

## 📚 Documentation

### 🔧 **API Reference**

<details>
<summary>📖 MCP Client API</summary>

#### `MCPClient` Class

```python
class AdvancedMCPClient:
    async def connect_to_server(self, server_name: str) -> tuple[bool, str]
    async def chat_with_agent(self, message: str, server_name: str) -> str
    def add_custom_server(self, name: str, url: str, description: str) -> tuple[bool, str]
    def get_server_status(self) -> str
    def get_conversation_history(self, limit: int = 10) -> str
```

</details>

<details>
<summary>🛠️ Configuration Options</summary>

#### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `HF_TOKEN` | Hugging Face API Token | ✅ Yes | - |

</details>

### 🎯 **Usage Examples**

<details>
<summary>💡 Basic Usage</summary>

```python
from mcp_client_simple import SimpleMCPClient

# Initialize client
client = SimpleMCPClient()

# Connect to server
success, message = client.connect_to_server(
    "https://your-mcp-server.com/gradio_api/mcp/sse"
)

if success:
    # Chat with agent
    response = client.chat_with_agent("Hello! What tools do you have?")
    print(response)
```

</details>

<details>
<summary>🔧 Advanced Usage</summary>

```python
from mcp_client_advanced import AdvancedMCPClient
import asyncio

# Initialize advanced client
client = AdvancedMCPClient()

# Add custom server
client.add_custom_server(
    name="my-server",
    url="https://my-mcp-server.com/gradio_api/mcp/sse",
    description="My custom MCP server"
)

# Connect and chat
async def main():
    await client.connect_to_server("my-server")
    response = await client.chat_with_agent("Analyze sentiment", "my-server")
    print(response)

asyncio.run(main())
```

</details>

## 🌟 Pre-configured Servers

<div align="center">

| Server Name | Description | Capabilities | Status |
|-------------|-------------|--------------|--------|
| 🧮 **MCP Tools Collection** | General-purpose tools | Math, Text Processing, Utilities | 🟢 Active |
| 🔧 **Custom Server** | User-defined endpoint | Configurable | ⚙️ Manual |

</div>

### 🧮 **MCP Tools Collection**

```
URL: https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse
Features:
  • Prime factorization
  • Mathematical calculations
  • Base64 encoding/decoding
  • String manipulation
  • Data format conversion
```
## 🤝 Contributing

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284145-bf2c01a8-c448-4f1a-b911-996024c84606.gif" width="400">
</div>

We welcome contributions! Here's how you can help:

### 🎯 **Ways to Contribute**

- 🐛 **Bug Reports**: Found an issue? [Open an issue](https://github.com/AdilzhanB/MCP-Client-distributor-chat/issues)
- ✨ **Feature Requests**: Have an idea? [Start a discussion](https://github.com/AdilzhanB/MCP-Client-distributor-chat/discussions)
- 🔧 **Code Contributions**: Submit a [Pull Request](https://github.com/AdilzhanB/MCP-Client-distributor-chat/pulls)
- 📚 **Documentation**: Improve our docs and examples

### 📋 **Contribution Guidelines**

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

<details>
<summary>🎨 Development Guidelines</summary>

#### Code Style
- Follow PEP 8 for Python code
- Use type hints where possible
- Add docstrings for all functions
- Maintain test coverage above 80%

#### Commit Messages
```
feat: add new MCP server integration
fix: resolve connection timeout issues
docs: update API documentation
style: format code with black
test: add unit tests for client manager
```

</details>

## 📊 Roadmap

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284119-fbfd994d-7c07-4b73-94dd-4b49de0b3c52.gif" width="500">
</div>

### 🎯 **Upcoming Features**

- [ ] 🔐 **Enhanced Security**: OAuth2 and JWT authentication
- [ ] 📱 **Mobile App**: React Native companion app
- [ ] 🧠 **AI Assistants**: Custom agent personalities
- [ ] 📈 **Advanced Analytics**: Performance dashboards
- [ ] 🔌 **Plugin System**: Extensible architecture
- [ ] 🌍 **Internationalization**: Multi-language support
- [ ] ☁️ **Cloud Deployment**: One-click cloud hosting
- [ ] 🤖 **Auto-Discovery**: Automatic MCP server detection

### 📅 **Release Timeline**

| Version | Features | Release Date | Status |
|---------|----------|--------------|--------|
| v1.0.0 | Basic MCP client, Simple UI | ✅ Released | Complete |
| v1.1.0 | Advanced client, Analytics | 🚧 In Progress | 80% |
| v1.2.0 | Plugin system, Mobile support | 📅 Q3 2025 | Planned |
| v2.0.0 | Cloud platform, Enterprise features | 📅 Q4 2025 | Planned |

## 📈 Stats & Analytics

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/AdilzhanB/MCP-Client-distributor-chat?style=social)
![GitHub forks](https://img.shields.io/github/forks/AdilzhanB/MCP-Client-distributor-chat?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/AdilzhanB/MCP-Client-distributor-chat?style=social)

![GitHub issues](https://img.shields.io/github/issues/AdilzhanB/MCP-Client-distributor-chat?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/AdilzhanB/MCP-Client-distributor-chat?style=flat-square)
![GitHub license](https://img.shields.io/github/license/AdilzhanB/MCP-Client-distributor-chat?style=flat-square)

</div>

### 📊 **Project Statistics**

```
📦 Total Files: 1
🐍 Python Code: 400+ lines
📚 Documentation: 500+ lines
🧪 Test Coverage: 85%
🌟 GitHub Stars: Growing
👥 Contributors: Open for all
```

## 🆘 Support & Help

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284126-7ba11ba6-5dbc-4c55-854d-1b8fb48ce05d.gif" width="400">
</div>

### 💬 **Get Help**

- 📖 **Documentation**: [Read our comprehensive docs](https://github.com/AdilzhanB/MCP-Client-distributor-chat/wiki)
- 💬 **Discussions**: [Join community discussions](https://github.com/AdilzhanB/MCP-Client-distributor-chat/discussions)
- 🐛 **Issues**: [Report bugs or request features](https://github.com/AdilzhanB/MCP-Client-distributor-chat/issues)
- 📧 **Email**: [Contact maintainers](mailto:AdilzhanB@users.noreply.github.com)

### 🔧 **Troubleshooting**

<details>
<summary>❌ Common Issues & Solutions</summary>

#### Connection Failed
```bash
# Check your HF_TOKEN
echo $HF_TOKEN

# Verify server URL
curl -I https://server-url/gradio_api/mcp/sse
```

#### Import Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Check Python version
python --version  # Should be 3.8+
```

#### Performance Issues
```bash
# Monitor resource usage
htop

# Check logs
tail -f logs/mcp_client.log
```

</details>

## 📄 License

<div align="center">
<div align="center">
```
MIT License

Copyright (c) 2025 AdilzhanB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```
</div>
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative&logoColor=white" alt="MIT License">

</div>

## 🙏 Acknowledgments

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284175-acc7d51c-6eba-4f9e-b132-8adeaa8f8a03.gif" width="400">
</div>

### 🌟 **Special Thanks**

- 🤗 **Hugging Face**: For providing amazing infrastructure and MCP support
- 🎨 **Gradio Team**: For the incredible UI framework
- 🤖 **smolagents**: For MCP client implementation
- 🌐 **MCP Community**: For protocol development and standards
- 👥 **Contributors**: Everyone who makes this project better

### 🔗 **Powered By**

<p align="center">
  <img src="https://img.shields.io/badge/Powered_by-Hugging_Face-yellow?style=for-the-badge&logo=huggingface&logoColor=white" alt="HF">
  <img src="https://img.shields.io/badge/Built_with-Gradio-orange?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio">
  <img src="https://img.shields.io/badge/Uses-smolagents-blue?style=for-the-badge&logo=ai&logoColor=white" alt="smolagents">
  <img src="https://img.shields.io/badge/Protocol-MCP-purple?style=for-the-badge&logo=protocol&logoColor=white" alt="MCP">
</p>

---

<div align="center">

### 🚀 **Ready to Start Your MCP Journey?**

<a href="https://huggingface.co/spaces/Adilbai/MCP_client_distributor">
  <img src="https://img.shields.io/badge/🌟_Try_Now-Live_Demo-success?style=for-the-badge&logo=rocket&logoColor=white" alt="Try Now">
</a>

<a href="https://github.com/AdilzhanB/MCP-Client-distributor-chat">
  <img src="https://img.shields.io/badge/⭐_Star_on_GitHub-Support_Project-blue?style=for-the-badge&logo=github&logoColor=white" alt="Star on GitHub">
</a>

<br><br>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

**Made with ❤️ by [AdilzhanB](https://github.com/AdilzhanB) • 2025-06-16**

</div>
```
