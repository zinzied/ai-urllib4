import sys
import os
import asyncio
from typing import Any

# Ensure we can import ai_urllib4
sys.path.insert(0, os.path.abspath("src"))

try:
    import ai_urllib4
    print("✅ ai_urllib4 imported successfully")
    print(f"Version: {ai_urllib4.__version__}")
except ImportError as e:
    print(f"❌ Failed to import ai_urllib4: {e}")
    sys.exit(1)

# 1. Verify HTTP/2 Imports
try:
    from ai_urllib4.http2 import (
        ConnectionProfile,
        FlowControlStrategy,
        HTTP2Connection, 
        inject_into_ai_urllib4 # Note: In init file might still say urllib5 or needs update, let's verify
    )
    print("✅ HTTP/2 modules imported successfully")
except ImportError as e:
    print(f"❌ Failed to import HTTP/2 modules: {e}")

# 2. Verify WebSocket Imports
try:
    from ai_urllib4.websocket import (
        WebSocketConnection,
        WebSocketFrame,
        WebSocketMessage
    )
    print("✅ WebSocket modules imported successfully")
except ImportError as e:
    print(f"❌ Failed to import WebSocket modules: {e}")

# 3. Verify Security Imports
try:
    from ai_urllib4.util.cert_verification import (
        CertificateTransparencyPolicy,
        SPKIPinningVerifier
    )
    print("✅ Security modules imported successfully")
except ImportError as e:
    print(f"❌ Failed to import Security modules: {e}")

# 4. Verify AI Feature (New)
try:
    from ai_urllib4.ai import AISmartConfig, optimize_params_for
    timeout = AISmartConfig.suggest_timeout("https://api.example.com/v1/data")
    print(f"✅ AI Config imported. Suggested timeout for API: {timeout}s")
except ImportError as e:
    print(f"❌ Failed to import AI modules: {e}")


# 5. Verify Async Support
async def verify_async():
    print("\nTesting Async Capability...")
    try:
        from ai_urllib4.async_connectionpool import connection_from_url
        pool = connection_from_url("http://example.com")
        response = await pool.urlopen("GET", "/")
        print(f"✅ Async request successful: {response}")
        print("✅ AsyncConnectionPool verified")
    except Exception as e:
        print(f"❌ Async verification failed: {e}")

if __name__ == "__main__":
    # Check for installed extras
    print("\nChecking dependencies:")
    try:
        import h2
        print("   - h2: Installed")
    except ImportError:
        print("   - h2: Not Installed (HTTP/2 features might fail at runtime)")

    try:
        import cryptography
        print("   - cryptography: Installed")
    except ImportError:
        print("   - cryptography: Not Installed (Security features might fail at runtime)")

    # Run Async Test
    try:
        asyncio.run(verify_async())
    except Exception as e:
        print(f"❌ Async loop failed: {e}")
