import asyncio
import sys
import os

sys.path.insert(0, os.path.abspath("src"))

from urllib5.async_connectionpool import connection_from_url

async def test_real_website():
    print("🌐 Connecting to http://example.com...")
    try:
        pool = connection_from_url("http://example.com")
        # Ensure port is set (connection_from_url might default it, but let's be safe in our test usage)
        if pool.port is None:
            pool.port = 80
            
        response = await pool.urlopen("GET", "/")
        
        print("\n✅ Response Received!")
        print("-" * 40)
        # Print first 200 chars
        print(response[:200]) 
        print("-" * 40)
        
        if "Example Domain" in response:
             print("\n✅ Verification Successful: 'Example Domain' found in response.")
        else:
             print("\n⚠️ Verification Warning: 'Example Domain' NOT found. Check content.")
             
    except Exception as e:
        print(f"\n❌ Test Failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_real_website())
