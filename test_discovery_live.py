import logging
import sys
import os

# Prepend src to path to ensure we use the local version
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

import ai_urllib4
from ai_urllib4.smart_client import SmartClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def test_live_discovery():
    # Use a real API key for Gemini if available, or heuristic fallback
    # For this test, we'll try to find an API on a well-known site
    # This site usually has JSON backends for its content
    url = "https://httpbin.org/get" # Baseline test
    
    # We will test against a news site that uses JSON for its feed (e.g. Hacker News or similar)
    # But first, let's try a site that we know has a clear JSON-in-script or API pattern.
    targets = [
        "https://www.reddit.com/r/python/", # Should find .json or similar
        "https://api.github.com/users/octocat", 
    ]

    client = SmartClient(
        ai_optimize=True,
        # api_key="YOUR_KEY_HERE" # User can provide this
    )

    print("--- Starting AI Discovery Test ---")
    
    for target in targets:
        print(f"\n[Testing Target]: {target}")
        try:
            # We use discover_api which handles the magic
            resp = client.discover_api(target)
            
            if resp:
                print(f"SUCCESS: Found API at {resp.discovered_from}")
                print(f"Status: {resp.status}")
                print(f"Content-Type: {resp.headers.get('Content-Type')}")
                if hasattr(resp, "json_data"):
                    print("JSON Data sample:", str(resp.json_data)[:200])
            else:
                print(f"INFO: No hidden API automatically discovered for {target} (Heuristics only)")
        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    test_live_discovery()
