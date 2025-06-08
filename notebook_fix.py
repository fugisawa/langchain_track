# Add this cell at the very beginning of your notebook (before any other imports)

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the Hugging Face token
hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
if hf_token:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token
    print("✅ Hugging Face token loaded successfully")
else:
    print("❌ Warning: HUGGINGFACE_API_TOKEN not found in environment variables")

# Now you can continue with your existing notebook code...

# ============================================================================
# Replace your existing cell 3 with this corrected version:
# ============================================================================

from langchain_huggingface.chat_models.huggingface import ChatHuggingFace
from langchain_huggingface.llms.huggingface_endpoint import HuggingFaceEndpoint

# ============================================================================
# Replace your existing cell 4 with this corrected version:
# ============================================================================

# Use a simpler model that's more likely to work
modelo = 'microsoft/DialoGPT-medium'  # Instead of Mixtral

llm = HuggingFaceEndpoint(
    repo_id=modelo,
    huggingfacehub_api_token=hf_token,  # Explicit token
    max_new_tokens=50,
    temperature=0.7
)
chat = ChatHuggingFace(llm=llm)

# Alternative: If you want to try Mixtral, you might need a PRO subscription.
# modelo = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
