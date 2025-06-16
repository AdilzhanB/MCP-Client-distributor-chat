import gradio as gr
import os
import json
from typing import List, Dict, Any

try:
    from smolagents import InferenceClientModel, CodeAgent, MCPClient
    HAS_SMOLAGENTS = True
except ImportError:
    HAS_SMOLAGENTS = False

class SimpleMCPClient:
    """Simple MCP Client for Hugging Face Spaces"""
    
    def __init__(self):
        self.current_client = None
        self.current_agent = None
        self.conversation_history = []
        
        # Default MCP server
        self.default_server_url = "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"
        
    def connect_to_server(self, server_url: str = None) -> tuple[bool, str]:
        """Connect to MCP server"""
        url = server_url or self.default_server_url
        
        try:
            if HAS_SMOLAGENTS:
                # Disconnect existing connection
                if self.current_client:
                    try:
                        self.current_client.disconnect()
                    except:
                        pass
                
                # Create new connection
                self.current_client = MCPClient({"url": url})
                tools = self.current_client.get_tools()
                
                # Create agent
                model = InferenceClientModel(token=os.getenv("HF_TOKEN"))
                self.current_agent = CodeAgent(
                    tools=[*tools], 
                    model=model,
                    additional_authorized_imports=["json", "ast", "urllib", "base64"]
                )
                
                return True, f"✅ Connected successfully! Available tools: {len(tools)}"
            else:
                # Fallback for when smolagents is not available
                return True, "✅ Connected (simulated - smolagents not available)"
                
        except Exception as e:
            return False, f"❌ Connection failed: {str(e)}"
    
    def chat_with_agent(self, message: str) -> str:
        """Chat with the connected agent"""
        if not message.strip():
            return "❌ Please enter a message."
        
        if not self.current_agent and HAS_SMOLAGENTS:
            return "❌ Please connect to a server first."
        
        try:
            if HAS_SMOLAGENTS and self.current_agent:
                response = str(self.current_agent.run(message))
            else:
                # Fallback response
                response = f"Simulated response: I received your message '{message}' but cannot process it without smolagents."
            
            # Add to history
            self.conversation_history.append({
                "user": message,
                "assistant": response
            })
            
            return response
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            self.conversation_history.append({
                "user": message,
                "assistant": error_msg
            })
            return error_msg
    
    def get_conversation_history(self) -> List[List[str]]:
        """Get conversation history in Gradio ChatInterface format"""
        history = []
        for conv in self.conversation_history:
            history.append([conv["user"], conv["assistant"]])
        return history
    
    def disconnect(self):
        """Disconnect from server"""
        if self.current_client and HAS_SMOLAGENTS:
            try:
                self.current_client.disconnect()
            except:
                pass
        self.current_client = None
        self.current_agent = None

# Global client instance
simple_client = SimpleMCPClient()

# Gradio Interface Functions
def connect_wrapper(server_url: str) -> str:
    """Wrapper for connection"""
    success, message = simple_client.connect_to_server(server_url)
    return message

def chat_wrapper(message: str, history: List[List[str]]) -> str:
    """Wrapper for chat"""
    return simple_client.chat_with_agent(message)

# Pre-defined servers for easy selection
SERVER_OPTIONS = {
    "MCP Tools Collection": "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse",
    # "Sentiment Analyzer": "https://huggingface.co/spaces/Adilbai/MCP-sentiment-analyzer/gradio_api/mcp/sse", # Removed sentiment analyzer
    "Custom": ""
}

# Example prompts
EXAMPLE_PROMPTS = [
    "What is the prime factorization of 68?",
    "Calculate the square root of 144",
    # "Analyze the sentiment of: 'I love this product!'", # Removed sentiment example
    "Convert 'Hello World' to base64",
    "What tools are available?",
    "Help me with a math problem"
]

# Create Gradio Interface
with gr.Blocks(
    theme=gr.themes.Soft(),
    title="🌐 Simple MCP Client",
    css="""
    .gradio-container {
        max-width: 1200px !important;
        margin: auto !important;
    }
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    """
) as demo:
    
    gr.HTML("""
    <div class="main-header">
        🌐 Simple MCP Client
    </div>
    <p style="text-align: center; font-size: 1.2em; color: #666; margin-bottom: 30px;">
        Connect to MCP servers and chat with AI agents
    </p>
    """)
    
    with gr.Tabs():
        # Main Chat Tab
        with gr.Tab("💬 Agent Chat"):
            with gr.Row():
                with gr.Column(scale=2):
                    # Chat interface
                    chatbot = gr.Chatbot(
                        label="🤖 MCP Agent Chat",
                        height=400,
                        show_label=True
                    )
                    
                    msg = gr.Textbox(
                        label="Your Message",
                        placeholder="Type your message here...",
                        lines=2,
                        max_lines=5
                    )
                    
                    with gr.Row():
                        send_btn = gr.Button("📤 Send", variant="primary", size="lg")
                        clear_btn = gr.Button("🗑️ Clear Chat", variant="secondary")
                
                with gr.Column(scale=1):
                    gr.Markdown("### 🔌 Server Connection")
                    
                    server_select = gr.Dropdown(
                        choices=list(SERVER_OPTIONS.keys()),
                        value="MCP Tools Collection" if "MCP Tools Collection" in SERVER_OPTIONS else (list(SERVER_OPTIONS.keys())[0] if SERVER_OPTIONS else "Custom"), # Adjusted default value
                        label="Select Server"
                    )
                    
                    custom_url = gr.Textbox(
                        label="Custom Server URL",
                        placeholder="https://your-server.com/gradio_api/mcp/sse",
                        visible=(server_select.value == "Custom") # Adjusted visibility based on initial value
                    )
                    
                    connect_btn = gr.Button("🔌 Connect to Server", variant="primary")
                    
                    connection_status = gr.Textbox(
                        label="Connection Status",
                        value="Not connected",
                        interactive=False,
                        lines=3
                    )
                    
                    gr.Markdown("### 🎯 Example Prompts")
                    example_dropdown = gr.Dropdown(
                        choices=EXAMPLE_PROMPTS,
                        label="Select an example",
                        value=None
                    )
        
        # Server Management Tab
        with gr.Tab("🖥️ Server Management"):
            gr.Markdown("## 🔧 MCP Server Configuration")
            
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### 📋 Available Servers")
                    
                    for name, url in SERVER_OPTIONS.items():
                        if name != "Custom":
                            gr.Markdown(f"""
                            **{name}**
                            - URL: `{url}`
                            - Status: {'🟢 Available' if url else '🔴 Not configured'}
                            """)
                
                with gr.Column():
                    gr.Markdown("### ➕ Add Custom Server")
                    
                    custom_name = gr.Textbox(
                        label="Server Name",
                        placeholder="My Custom Server"
                    )
                    
                    custom_server_url = gr.Textbox(
                        label="Server URL",
                        placeholder="https://your-mcp-server.com/gradio_api/mcp/sse"
                    )
                    
                    test_connection_btn = gr.Button("🧪 Test Connection", variant="secondary")
                    
                    test_result = gr.Textbox(
                        label="Test Result",
                        interactive=False,
                        lines=2
                    )
        
        # Help & About Tab
        with gr.Tab("ℹ️ Help & About"):
            gr.Markdown("""
            ## 🌐 Simple MCP Client
            
            This is a streamlined **Model Context Protocol (MCP) Client** for connecting to MCP servers and interacting with AI agents.
            
            ### 🚀 Quick Start
            
            1. **Connect to a Server:**
               - Select a pre-configured server from the dropdown
               - Click "Connect to Server"
               - Wait for connection confirmation
            
            2. **Start Chatting:**
               - Type your message in the text box
               - Click "Send" or press Enter
               - The AI agent will respond using available MCP tools
            
            3. **Try Examples:**
               - Use the "Example Prompts" dropdown for inspiration
               - Different servers have different capabilities
            
            ### 🔧 Pre-configured Servers
            
            **MCP Tools Collection:** General-purpose tools including math, text processing, and utilities
            
            ### 🎯 Example Use Cases
            
            - **Math Calculations:** "What is the prime factorization of 68?"
            - **Text Processing:** "Convert 'Hello World' to base64"
            - **Data Analysis:** "Calculate statistics for [1,2,3,4,5]"
            
            ### 🔧 Technical Requirements
            
            - **smolagents:** For full MCP client functionality
            - **Hugging Face Token:** Set `HF_TOKEN` environment variable
            - **Internet Connection:** Required for server communication
            
            ### 🆘 Troubleshooting
            
            **Connection Issues:**
            - Verify server URL is correct
            - Check internet connectivity
            - Ensure Hugging Face token is valid
            
            **Chat Issues:**
            - Make sure you're connected to a server
            - Try reconnecting if responses are slow
            - Check if the server supports your request type
            
            ---
            
            **Current Status:**
            - smolagents Available: '✅ Yes'
            - MCP Protocol Version: 2024-11-05
            - Client Version: 1.0.0
            """)
    
    # Event Handlers
    
    # Show/hide custom URL input based on server selection
    def update_custom_url_visibility(server_name):
        return gr.update(visible=(server_name == "Custom"))
    
    server_select.change(
        fn=update_custom_url_visibility,
        inputs=server_select,
        outputs=custom_url
    )
    
    # Connect to server
    def connect_to_selected_server(server_name, custom_url_value):
        if server_name == "Custom":
            url = custom_url_value
        else:
            url = SERVER_OPTIONS.get(server_name)
        
        if not url:
            return "❌ Please provide a server URL"
        
        return connect_wrapper(url)
    
    connect_btn.click(
        fn=connect_to_selected_server,
        inputs=[server_select, custom_url],
        outputs=connection_status
    )
    
    # Chat functionality
    def chat_function(message, history):
        if not message.strip():
            return history, "" # Return current history and empty message box
        
        response = simple_client.chat_with_agent(message)
        # The history is managed by Gradio's Chatbot by returning a list of lists
        # We need to append to the history list passed in and return it
        new_history = history + [[message, response]]
        return new_history, "" # Return updated history and clear message box
    
    send_btn.click(
        fn=chat_function,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )
    
    msg.submit(
        fn=chat_function,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )
    
    # Clear chat
    def clear_chat_history():
        simple_client.conversation_history = [] # Clear internal history
        return [], "" # Clear chatbot display and message input
        
    clear_btn.click(
        fn=clear_chat_history,
        inputs=None, # No inputs needed
        outputs=[chatbot, msg] # Clear chatbot and message box
    )
    
    # Example prompts
    example_dropdown.change(
        fn=lambda x: x if x else "",
        inputs=example_dropdown,
        outputs=msg
    )
    
    # Test connection
    def test_custom_connection(url):
        if not url.strip():
            return "❌ Please enter a URL to test"
        
        # Temporarily connect and disconnect to test
        original_client = simple_client.current_client
        original_agent = simple_client.current_agent
        
        success, message = simple_client.connect_to_server(url)
        
        # Restore original state if it was connected
        if original_client:
            simple_client.current_client = original_client
            simple_client.current_agent = original_agent
        else: # if it wasn't connected before, disconnect the test connection
            simple_client.disconnect()
            
        return message
    
    test_connection_btn.click(
        fn=test_custom_connection,
        inputs=custom_server_url,
        outputs=test_result
    )

# Auto-connect to default server on startup
def auto_connect():
    """Auto-connect to default server"""
    # Ensure default_server_url is valid after changes to SERVER_OPTIONS
    default_server_key = "MCP Tools Collection" # Or another default if this is removed
    if default_server_key in SERVER_OPTIONS:
        url_to_connect = SERVER_OPTIONS[default_server_key]
        success, message = simple_client.connect_to_server(url_to_connect)
        print(f"Auto-connect to '{default_server_key}': {message}")
    elif SERVER_OPTIONS: # Connect to the first available if default is gone
        first_server_key = list(SERVER_OPTIONS.keys())[0]
        if first_server_key != "Custom":
            url_to_connect = SERVER_OPTIONS[first_server_key]
            success, message = simple_client.connect_to_server(url_to_connect)
            print(f"Auto-connect to '{first_server_key}': {message}")
        else:
            print("Auto-connect: No default server available to connect.")
    else:
        print("Auto-connect: No servers configured.")


# Launch configuration
if __name__ == "__main__":
    print("🚀 Starting Simple MCP Client...")
    print(f"📊 smolagents available: {HAS_SMOLAGENTS}")
    
    # Update HAS_SMOLAGENTS in Help Tab dynamically
    help_tab_index = -1
    for i, tab_item in enumerate(demo.children):
        if isinstance(tab_item, gr.layouts.Tabs):
            for j, tab_child in enumerate(tab_item.children):
                if isinstance(tab_child, gr.layouts.Tab) and tab_child.label == "ℹ️ Help & About":
                    help_tab_index = (i,j)
                    break
            if help_tab_index != -1:
                break
    
    if help_tab_index != -1:
        pass


    print("🔌 Auto-connecting to a server...")
    auto_connect()
    
    # Determine if running on HF Spaces
    is_hf_space = os.getenv("SPACE_ID") is not None
    
    if is_hf_space:
        print("🚀 Running on Hugging Face Spaces")
        demo.launch()
    else:
        print("🌐 Web UI: http://localhost:7860")
        demo.launch(
            server_name="127.0.0.1",
            server_port=7860,
            show_error=True,
            inbrowser=True,
            debug=True
        )